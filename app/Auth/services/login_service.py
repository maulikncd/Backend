"""
Login service for handling user authentication.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session

from app.Auth.core.config import get_settings
from app.Auth.core.exceptions import ValidationServiceError, ApplicationError
from app.Auth.core.security import verify_password, create_access_token, create_refresh_token, hash_password
from app.Auth.crud.auth import get_user_by_email
from app.Auth.crud.login import create_login_record
from app.Auth.models.login_record import LoginRecord
from app.Auth.models.refresh_token import RefreshToken


class LoginService:
    """Service for handling user login operations."""

    def login(
        self,
        db: Session,
        *,
        email: str,
        password: str,
        login_method: str = "manual",
        device_id: Optional[str] = None,
        device_name: Optional[str] = None,
        location: Optional[str] = None,
        ip_address: Optional[str] = None,
    ) -> dict:
        """
        Authenticate user and create login record with refresh token.
        
        Returns:
            dict: Contains user_id, email, access_token, refresh_token
        """
        # Get user by email
        user = get_user_by_email(db, email=email)
        if not user:
            raise ApplicationError("Invalid email or password", error_code="INVALID_CREDENTIALS")

        # Verify password
        if not verify_password(password, user.hashed_password):
            raise ApplicationError("Invalid email or password", error_code="INVALID_CREDENTIALS")

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

        # Create refresh token
        settings = get_settings()
        refresh_token_exp = settings.refresh_token_exp_minutes
        
        # Create the refresh token
        refresh_token = create_refresh_token(
            subject=str(user.user_id),
            refresh_token_id=login.login_id,
            extra_claims={"email": user.email}
        )
        
        # Log the token creation
        import logging
        logger = logging.getLogger(__name__)
        logger.debug(f"Created refresh token for user_id={user.user_id}, login_id={login.login_id}")
        logger.debug(f"Token (first 50 chars): {refresh_token[:50]}...")

        # Hash the token for storage
        token_hash = hash_password(refresh_token)
        logger.debug(f"Hashed token (first 50 chars): {token_hash[:50]}...")
        logger.debug(f"Hash length: {len(token_hash)}")

        # Store the refresh token
        token_row = RefreshToken(
            user_id=user.user_id,
            token_hash=token_hash,
            expires_at=datetime.utcnow() + timedelta(minutes=refresh_token_exp)
        )
        db.add(token_row)
        db.commit()
        db.refresh(token_row)
        
        logger.debug(f"Stored refresh token with ID: {token_row.refresh_token_id}")

        # Update login record with the refresh token ID
        login.current_refresh_token_id = token_row.refresh_token_id
        db.commit()
        logger.debug(f"Updated login record {login.login_id} with refresh_token_id: {token_row.refresh_token_id}")

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
            "username": user.username,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.access_token_exp_minutes * 60  # in seconds
        }
