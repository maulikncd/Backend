"""
Social authentication service.
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
from app.Auth.crud.auth import get_user_by_email, create_user
from app.Auth.crud.login import create_login_record, update_user_login_records
from app.Auth.crud.refresh_token import create_refresh_token as create_refresh_token_db
from app.Auth.core.exceptions import ResourceConflictError
from app.Auth.models.user import User


class SocialService:
    """
    Service for handling social authentication (Google, Facebook, Apple, etc.).
    """

    @staticmethod
    def login(
        db: Session,
        *,
        email: str,
        username: str,
        login_method: str,
        social_id: str,
        picture: str | None = None,
        device_id: str | None = None,
        device_name: str | None = None,
        location: str | None = None,
        ip_address: str | None = None,
    ) -> Dict[str, str]:
        """
        Handle social login - implements email-first, method-second logic.
        
        Args:
            db: Database session
            email: User's email
            username: Username from social provider
            login_method: Social provider (google, facebook, apple, etc.)
            social_id: Social provider user ID
            picture: Profile picture URL from social provider
            device_id: Device identifier
            device_name: Device name
            location: User location
            ip_address: User IP address
            
        Returns:
            Dictionary containing user data and tokens
        """
        # Get user by email (email-first approach)
        existing_user = get_user_by_email(db, email)
        
        if existing_user:
            # User exists - check login method
            existing_methods = existing_user.login_method.split(",") if existing_user.login_method else []
            
            # Always update user information on social login, even if method already exists
            return SocialService._handle_existing_user_login(
                db,
                user=existing_user,
                login_method=login_method,
                social_id=social_id,
                username=username,
                picture=picture,
                device_id=device_id,
                device_name=device_name,
                location=location,
                ip_address=ip_address,
            )
        else:
            # User doesn't exist - create new user with social data
            return SocialService._create_new_social_user(
                db,
                email=email,
                username=username,
                login_method=login_method,
                social_id=social_id,
                picture=picture,
                device_id=device_id,
                device_name=device_name,
                location=location,
                ip_address=ip_address,
            )

    @staticmethod
    def _handle_existing_user_login(
        db: Session,
        *,
        user: User,
        login_method: str,
        social_id: str,
        username: str,
        picture: str | None = None,
        device_id: str | None = None,
        device_name: str | None = None,
        location: str | None = None,
        ip_address: str | None = None,
    ) -> Dict[str, str]:
        """
        Handle social login for existing user (manual signup).
        """
        # Update social ID if missing for the specific provider
        if login_method == "google" and not user.google_social_id:
            user.google_social_id = social_id
        # TODO: Add other social providers (facebook_social_id, apple_social_id, etc.)
        
        # Only update username if it's not from a manual signup
        if 'manual' not in user.login_method:
            user.username = username
        
        # Only update picture if not already set
        if not user.picture and picture:
            user.picture = picture
        
        # Append social provider to login_method if not already present
        login_methods = user.login_method.split(",") if user.login_method else []
        if login_method not in login_methods:
            login_methods.append(login_method)
            user.login_method = ",".join(login_methods)
        
        user.updated_at = datetime.utcnow()
        
        db.commit()
        db.refresh(user)
        
        # Update all previous login records with new username
        update_user_login_records(db, user.user_id, username)
        
        # Create login record and tokens
        return SocialService._create_login_session(
            db,
            user=user,
            login_method=login_method,
            device_id=device_id,
            device_name=device_name,
            location=location,
            ip_address=ip_address,
        )

    @staticmethod
    def _create_new_social_user(
        db: Session,
        *,
        email: str,
        username: str,
        login_method: str,
        social_id: str,
        picture: str | None = None,
        device_id: str | None = None,
        device_name: str | None = None,
        location: str | None = None,
        ip_address: str | None = None,
    ) -> Dict[str, str]:
        """
        Create new user with social data.
        """
        # Create user with social data
        user = User(
            username=username,
            email=email,
            hashed_password="",  # No password for social accounts
            login_method=login_method,
            google_social_id=social_id if login_method == "google" else None,
            # TODO: Add other social providers
            picture=picture,
            device_id=device_id,
            device_name=device_name,
            location=location,
            ip_address=ip_address,
        )
        
        db.add(user)
        try:
            db.commit()
        except Exception as exc:  # pragma: no cover - depends on DB backend
            db.rollback()
            raise ResourceConflictError("Failed to create user") from exc
        db.refresh(user)
        
        # Create login record and tokens
        return SocialService._create_login_session(
            db,
            user=user,
            login_method=login_method,
            device_id=device_id,
            device_name=device_name,
            location=location,
            ip_address=ip_address,
        )

    @staticmethod
    def _create_login_session(
        db: Session,
        *,
        user: User,
        login_method: str,
        device_id: str | None = None,
        device_name: str | None = None,
        location: str | None = None,
        ip_address: str | None = None,
    ) -> Dict[str, str]:
        """
        Create login record and generate tokens.
        """
        # Create login record using CRUD
        login = create_login_record(
            db,
            user_id=user.user_id,
            email=user.email,
            login_method=login_method,
            ip_address=ip_address,
            device_id=device_id,
            device_name=device_name,
            location=location,
        )

        # Create refresh token
        settings = get_settings()
        refresh_token_exp = settings.refresh_token_exp_minutes
        refresh_token = create_refresh_token(
            subject=str(user.user_id),
            refresh_token_id=login.login_id,
            extra_claims={"email": user.email}
        )

        # Store refresh token in DB using CRUD
        token_hash = hash_password(refresh_token)
        expires_at = datetime.utcnow() + timedelta(minutes=refresh_token_exp)
        token_row = create_refresh_token_db(
            db,
            user_id=user.user_id,
            token_hash=token_hash,
            expires_at=expires_at,
        )

        # Update login record with refresh token ID
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
            "username": user.username,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.access_token_exp_minutes * 60  # in seconds
        }


# Backward compatibility alias
GoogleService = SocialService
