"""
Service for handling refresh token operations.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.Auth.core.config import get_settings
from app.Auth.core.exceptions import ApplicationError
from app.Auth.core.security import create_access_token, hash_password
from app.Auth.models.login_record import LoginRecord
from app.Auth.models.refresh_token import RefreshToken

logger = logging.getLogger(__name__)

settings = get_settings()


class RefreshTokenService:
    """Service for handling refresh token operations."""

    @classmethod
    def refresh_token(
        cls,
        db: Session,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """
        Refresh an access token using a valid refresh token.
        
        Args:
            db: Database session
            refresh_token: The refresh token to use for getting a new access token
            
        Returns:
            dict: Contains new access and refresh tokens
            
        Raises:
            ApplicationError: If the token is invalid, expired, or inactive
        """
        # Decode the refresh token
        try:
            logger.debug(f"Attempting to decode refresh token")
            payload = jwt.decode(
                refresh_token,
                settings.refresh_token_secret,
                algorithms=[settings.jwt_algorithm],
            )
            
            logger.debug(f"Decoded token payload: {payload}")
            
            # Validate token type
            if payload.get("type") != "refresh":
                raise ApplicationError("Invalid token type", status_code=400, error_code="INVALID_TOKEN")
                
            user_id = int(payload["sub"])
            refresh_token_id = payload.get("refresh_token_id")
            logger.debug(f"Extracted user_id: {user_id}, refresh_token_id: {refresh_token_id}")
            
            if not refresh_token_id:
                raise ApplicationError("Missing refresh token ID in token", status_code=400, error_code="INVALID_TOKEN")
                
        except JWTError as e:
            if str(e) == "Signature has expired":
                raise ApplicationError("Refresh token has expired", status_code=401, error_code="TOKEN_EXPIRED")
            raise ApplicationError("Invalid refresh token", status_code=400, error_code="INVALID_TOKEN")
            
        # Get the login record using the refresh_token_id (which is actually the login_id)
        logger.debug(f"Looking up login record with login_id: {refresh_token_id}")
        login = db.query(LoginRecord).filter(
            LoginRecord.login_id == refresh_token_id
        ).first()
        
        if not login:
            logger.error(f"Login record not found for login_id: {refresh_token_id}")
            raise ApplicationError("Invalid refresh token - login not found", status_code=400, error_code="INVALID_TOKEN")
            
        logger.debug(f"Found login record: {login.login_id}, current_refresh_token_id: {login.current_refresh_token_id}")
            
        # Get the refresh token record using the current_refresh_token_id from login
        token_row = db.query(RefreshToken).filter(
            RefreshToken.refresh_token_id == login.current_refresh_token_id
        ).first()
        
        if not token_row:
            logger.error(f"Refresh token not found for refresh_token_id: {login.current_refresh_token_id}")
            raise ApplicationError("Invalid refresh token - token not found", status_code=400, error_code="INVALID_TOKEN")
            
        logger.debug(f"Found refresh token: {token_row.refresh_token_id}, is_active: {token_row.is_active}")
            
        if not token_row.is_active:
            logger.warning(f"Refresh token {token_row.refresh_token_id} is not active")
            raise ApplicationError("Refresh token is no longer active", status_code=401, error_code="TOKEN_INACTIVE")
            
        # Verify the token hash matches
        try:
            # First verify the token is valid by decoding it again
            decoded_payload = jwt.decode(
                refresh_token,
                settings.refresh_token_secret,
                algorithms=[settings.jwt_algorithm],
            )
            logger.debug(f"Successfully decoded token. Payload: {decoded_payload}")
            
            # Then verify the hash matches
            stored_hash = token_row.token_hash
            computed_hash = hash_password(refresh_token)
            
            logger.debug(f"Token hash verification:")
            logger.debug(f"- Stored hash (first 10 chars): {stored_hash[:10]}...")
            logger.debug(f"- Computed hash (first 10 chars): {computed_hash[:10]}...")
            logger.debug(f"- Token being verified (first 50 chars): {refresh_token[:50]}...")
            
            if not stored_hash == computed_hash:
                logger.error(f"Token hash mismatch!")
                logger.error(f"- Stored hash length: {len(stored_hash)}")
                logger.error(f"- Computed hash length: {len(computed_hash)}")
                
                # Check if it's a timing attack or just a mismatch
                if len(stored_hash) != len(computed_hash):
                    logger.error("Hash lengths don't match! This suggests different hashing methods were used.")
                
                raise ApplicationError("Invalid refresh token - hash mismatch", status_code=400, error_code="INVALID_TOKEN")
                
            logger.debug("Token hash verification successful")
                
        except JWTError as e:
            if str(e) == "Signature has expired":
                raise ApplicationError("Refresh token has expired", status_code=401, error_code="TOKEN_EXPIRED")
            raise ApplicationError(f"Invalid refresh token - {str(e)}", status_code=400, error_code="INVALID_TOKEN")
            
        # Deactivate the old refresh token
        token_row.is_active = False
        
        # Create a new refresh token
        new_refresh_token = cls._create_refresh_token(
            db=db,
            user_id=user_id,
            login_id=login.login_id,
            email=login.email
        )
        
        # Create new access token
        access_token = create_access_token(
            subject=str(user_id),
            extra_claims={
                "email": login.email,
                "refresh_token_id": login.current_refresh_token_id
            }
        )
        
        db.commit()
        
        return {
            "access_token": access_token,
            "refresh_token": new_refresh_token,
            "token_type": "bearer",
            "expires_in": settings.access_token_exp_minutes * 60
        }
    
    @classmethod
    def _create_refresh_token(
        cls,
        db: Session,
        user_id: int,
        login_id: int,
        email: str
    ) -> str:
        """Helper method to create a new refresh token."""
        # Create new refresh token
        refresh_token_exp = settings.refresh_token_exp_minutes
        refresh_token = jwt.encode(
            {
                "sub": str(user_id),
                "refresh_token_id": login_id,
                "email": email,
                "type": "refresh",
                "exp": datetime.utcnow() + timedelta(minutes=refresh_token_exp)
            },
            settings.refresh_token_secret,
            algorithm=settings.jwt_algorithm
        )
        
        # Store the new refresh token
        token_row = RefreshToken(
            user_id=user_id,
            token_hash=hash_password(refresh_token),
            expires_at=datetime.utcnow() + timedelta(minutes=refresh_token_exp)
        )
        db.add(token_row)
        db.flush()
        
        # Update login record with new refresh token ID
        login = db.query(LoginRecord).filter(
            LoginRecord.login_id == login_id
        ).first()
        
        if login:
            login.current_refresh_token_id = token_row.refresh_token_id
            db.flush()
        
        return refresh_token
