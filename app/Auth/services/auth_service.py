"""
Auth service containing business logic for user signup.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Dict

from sqlalchemy.orm import Session

from app.Auth.core.config import get_settings
from app.Auth.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
)
from app.Auth.crud.auth import create_user, get_user_by_email
from app.Auth.crud.login import create_login_record
from app.Auth.core.exceptions import ResourceConflictError, ValidationServiceError
from app.Auth.models.login_record import LoginRecord
from app.Auth.models.refresh_token import RefreshToken
from app.Auth.utils.otp_service import OTPService


class AuthService:
    """
    Domain service encapsulating signup workflow.
    """

    @staticmethod
    def signup(
        db: Session,
        *,
        username: str,
        email: str,
        password: str,
        confirm_password: str,
        login_method: str,
        device_id: str | None = None,
        device_name: str | None = None,
        location: str | None = None,
        ip_address: str | None = None,
    ) -> Dict[str, str]:
        if password != confirm_password:
            raise ValidationServiceError("Passwords do not match")

        # Get user by email (email-first approach)
        existing_user = get_user_by_email(db, email)
        
        if existing_user:
            # User exists - check login method
            existing_methods = existing_user.login_method.split(",") if existing_user.login_method else []
            
            if login_method in existing_methods:
                # Same method twice - return 409 conflict
                raise ResourceConflictError(f"Account already exists with {login_method} login method")
            else:
                # Different method - update user to allow both methods
                existing_methods.append(login_method)
                existing_user.login_method = ",".join(existing_methods)
                existing_user.updated_at = datetime.utcnow()
                
                # Update password if this is manual signup and user doesn't have password
                if login_method == "manual" and not existing_user.hashed_password:
                    existing_user.hashed_password = hash_password(password)
                
                db.commit()
                db.refresh(existing_user)
                user = existing_user
        else:
            # User doesn't exist - create new user
            hashed = hash_password(password)
            user = create_user(
                db,
                username=username,
                email=email,
                hashed_password=hashed,
                login_method=login_method,
                device_id=device_id,
                device_name=device_name,
                location=location,
                ip_address=ip_address,
            )

        # (A) Create login record
        login = LoginRecord(
            user_id=user.user_id,
            email=user.email,
            login_method=login_method,
            ip_address=ip_address,
            device_id=device_id,
            device_name=device_name,
            location=location,
        )
        db.add(login)
        db.commit()
        db.refresh(login)

        # (B) Create refresh token
        settings = get_settings()
        refresh_token_exp = settings.refresh_token_exp_minutes
        refresh_token = create_refresh_token(
            subject=str(user.user_id),
            refresh_token_id=login.login_id,  # Using login_id as refresh_token_id
            extra_claims={"email": user.email}
        )

        # (C) Store refresh token in DB
        token_row = RefreshToken(
            user_id=user.user_id,
            token_hash=hash_password(refresh_token),
            expires_at=datetime.utcnow() + timedelta(minutes=refresh_token_exp)
        )
        db.add(token_row)
        db.commit()
        db.refresh(token_row)

        # (D) Update login record with refresh token ID
        login.current_refresh_token_id = token_row.refresh_token_id
        db.commit()

        # Create access token
        access_token = create_access_token(
            subject=str(user.user_id),
            extra_claims={
                "email": user.email,
                "refresh_token_id": token_row.refresh_token_id
            }
        )

        return {
            "user_id": user.user_id,
            "email": user.email,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.access_token_exp_minutes * 60  # in seconds
        }

    @staticmethod
    async def send_signup_otp(
        db: Session,
        *,
        email: str,
        username: str = None,
        password: str = None,
        confirm_password: str = None,
        login_method: str = "manual",
        device_id: str | None = None,
        device_name: str | None = None,
        location: str | None = None,
    ) -> Dict[str, str]:
        """Send OTP for email verification during signup and store user data."""
        # Check if user already exists with same login method
        existing_user = get_user_by_email(db, email)
        if existing_user:
            existing_methods = existing_user.login_method.split(",") if existing_user.login_method else []
            if login_method in existing_methods:
                raise ResourceConflictError(f"Account already exists with {login_method} login method")

        # Generate OTP
        otp = OTPService.generate_otp()
        
        # Store OTP in Redis
        otp_stored = await OTPService.store_otp(email, otp)
        if not otp_stored:
            raise ValidationServiceError("OTP already sent, please wait", error_code="OTP_ALREADY_SENT")
        
        # Store user data in Redis for retrieval during OTP verification
        user_data = {
            "username": username,
            "password": password,
            "confirm_password": confirm_password,
            "login_method": login_method,
            "device_id": device_id,
            "device_name": device_name,
            "location": location,
        }
        await OTPService.store_user_data(email, user_data)
        
        # Send OTP via email
        email_sent = await OTPService.send_otp_email(email, otp)
        if not email_sent:
            raise ValidationServiceError("Failed to send OTP email", error_code="OTP_SEND_FAILED")
        
        return {"message": "OTP sent successfully"}

    @staticmethod
    async def verify_otp_only(
        db: Session,
        *,
        email: str,
        otp: str,
        ip_address: str | None = None,
    ) -> Dict[str, str]:
        """Verify OTP and create user account using stored user data."""
        # Verify OTP
        otp_valid = await OTPService.verify_otp(email, otp)
        if not otp_valid:
            raise ValidationServiceError("Invalid or expired OTP", error_code="OTP_INVALID_OR_EXPIRED")

        # Retrieve stored user data
        user_data = await OTPService.get_user_data(email)
        if not user_data:
            raise ValidationServiceError("User data not found. Please restart signup process.", error_code="USER_DATA_NOT_FOUND")

        # Extract user data
        username = user_data.get("username")
        password = user_data.get("password")
        confirm_password = user_data.get("confirm_password")
        login_method = user_data.get("login_method", "manual")
        device_id = user_data.get("device_id")
        device_name = user_data.get("device_name")
        location = user_data.get("location")

        # Validate required fields
        if not all([username, password, confirm_password]):
            raise ValidationServiceError("Missing required user data. Please restart signup process.", error_code="MISSING_USER_DATA")

        if password != confirm_password:
            raise ValidationServiceError("Passwords do not match", error_code="PASSWORDS_DO_NOT_MATCH")

        # Get user by email (email-first approach)
        existing_user = get_user_by_email(db, email)
        
        if existing_user:
            # User exists - check login method
            existing_methods = existing_user.login_method.split(",") if existing_user.login_method else []
            
            if login_method in existing_methods:
                # Same method twice - return 409 conflict
                raise ResourceConflictError(f"Account already exists with {login_method} login method")
            else:
                # Different method - update user to allow both methods
                existing_methods.append(login_method)
                existing_user.login_method = ",".join(existing_methods)
                existing_user.updated_at = datetime.utcnow()
                
                # Update password if this is manual signup and user doesn't have password
                if login_method == "manual" and not existing_user.hashed_password:
                    existing_user.hashed_password = hash_password(password)
                
                # Update username if this is manual signup (manual username takes priority)
                if login_method == "manual":
                    existing_user.username = username
                
                db.commit()
                db.refresh(existing_user)
                user = existing_user
        else:
            # User doesn't exist - create new user
            hashed = hash_password(password)
            user = create_user(
                db,
                username=username,
                email=email,
                hashed_password=hashed,
                login_method=login_method,
                device_id=device_id,
                device_name=device_name,
                location=location,
                ip_address=ip_address,
            )

        # (A) Create login record
        login = LoginRecord(
            user_id=user.user_id,
            email=user.email,
            login_method=login_method,
            ip_address=ip_address,
            device_id=device_id,
            device_name=device_name,
            location=location,
        )
        db.add(login)
        db.commit()
        db.refresh(login)

        # (B) Create refresh token
        settings = get_settings()
        refresh_token_exp = settings.refresh_token_exp_minutes
        refresh_token = create_refresh_token(
            subject=str(user.user_id),
            refresh_token_id=login.login_id,  # Using login_id as refresh_token_id
            extra_claims={"email": user.email}
        )

        # (C) Store refresh token in DB
        token_row = RefreshToken(
            user_id=user.user_id,
            token_hash=hash_password(refresh_token),
            expires_at=datetime.utcnow() + timedelta(minutes=refresh_token_exp)
        )
        db.add(token_row)
        db.commit()
        db.refresh(token_row)

        # (D) Update login record with refresh token ID
        login.current_refresh_token_id = token_row.refresh_token_id
        db.commit()

        # Create access token
        access_token = create_access_token(
            subject=str(user.user_id),
            extra_claims={
                "email": user.email,
                "refresh_token_id": token_row.refresh_token_id
            }
        )

        # Clean up stored user data from Redis
        await OTPService.delete_user_data(email)

        return {
            "user_id": user.user_id,
            "email": user.email,
            "username": user.username,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.access_token_exp_minutes * 60  # in seconds
        }

    @staticmethod
    async def verify_signup_otp(
        db: Session,
        *,
        email: str,
        otp: str,
        username: str,
        password: str,
        confirm_password: str,
        login_method: str = "manual",
        device_id: str | None = None,
        device_name: str | None = None,
        location: str | None = None,
        ip_address: str | None = None,
    ) -> Dict[str, str]:
        """Verify OTP and create user account."""
        if password != confirm_password:
            raise ValidationServiceError("Passwords do not match")

        # Verify OTP
        otp_valid = await OTPService.verify_otp(email, otp)
        if not otp_valid:
            raise ValidationServiceError("Invalid or expired OTP")

        # Get user by email (email-first approach)
        existing_user = get_user_by_email(db, email)
        
        if existing_user:
            # User exists - check login method
            existing_methods = existing_user.login_method.split(",") if existing_user.login_method else []
            
            if login_method in existing_methods:
                # Same method twice - return 409 conflict
                raise ResourceConflictError(f"Account already exists with {login_method} login method")
            else:
                # Different method - update user to allow both methods
                existing_methods.append(login_method)
                existing_user.login_method = ",".join(existing_methods)
                existing_user.updated_at = datetime.utcnow()
                
                # Update password if this is manual signup and user doesn't have password
                if login_method == "manual" and not existing_user.hashed_password:
                    existing_user.hashed_password = hash_password(password)
                
                db.commit()
                db.refresh(existing_user)
                user = existing_user
        else:
            # User doesn't exist - create new user
            hashed = hash_password(password)
            user = create_user(
                db,
                username=username,
                email=email,
                hashed_password=hashed,
                login_method=login_method,
                device_id=device_id,
                device_name=device_name,
                location=location,
                ip_address=ip_address,
            )

        # (A) Create login record
        login = LoginRecord(
            user_id=user.user_id,
            email=user.email,
            login_method=login_method,
            ip_address=ip_address,
            device_id=device_id,
            device_name=device_name,
            location=location,
        )
        db.add(login)
        db.commit()
        db.refresh(login)

        # (B) Create refresh token
        settings = get_settings()
        refresh_token_exp = settings.refresh_token_exp_minutes
        refresh_token = create_refresh_token(
            subject=str(user.user_id),
            refresh_token_id=login.login_id,  # Using login_id as refresh_token_id
            extra_claims={"email": user.email}
        )

        # (C) Store refresh token in DB
        token_row = RefreshToken(
            user_id=user.user_id,
            token_hash=hash_password(refresh_token),
            expires_at=datetime.utcnow() + timedelta(minutes=refresh_token_exp)
        )
        db.add(token_row)
        db.commit()
        db.refresh(token_row)

        # (D) Update login record with refresh token ID
        login.current_refresh_token_id = token_row.refresh_token_id
        db.commit()

        # Create access token
        access_token = create_access_token(
            subject=str(user.user_id),
            extra_claims={
                "email": user.email,
                "refresh_token_id": token_row.refresh_token_id
            }
        )

        return {
            "user_id": user.user_id,
            "email": user.email,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.access_token_exp_minutes * 60  # in seconds
        }
