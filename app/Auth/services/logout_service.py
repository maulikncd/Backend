"""
Logout service for handling user logout operations.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

from jose import jwt
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.Auth.core.config import get_settings
from app.Auth.core.exceptions import ApplicationError
from app.Auth.models.login_record import LoginRecord
from app.Auth.models.refresh_token import RefreshToken

logger = logging.getLogger(__name__)
settings = get_settings()


class LogoutService:
    """Service for handling user logout operations."""

    @classmethod
    def logout(
        cls,
        db: Session,
        *,
        refresh_token: str,
        access_token: Optional[str] = None,
        ip_address: Optional[str] = None,
    ) -> dict:
        """
        Logout user by deactivating the refresh token, blacklisting access token, and updating login record.
        
        Args:
            db: Database session
            refresh_token: The refresh token to invalidate
            access_token: Optional access token to blacklist
            ip_address: Optional IP address of the logout request
            
        Returns:
            dict: Contains logout success message
            
        Raises:
            ApplicationError: If the token is invalid or already logged out
        """
        # Decode the refresh token to get the login_id
        try:
            logger.debug(f"Attempting to logout with refresh token")
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
                
        except jwt.JWTError as e:
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
        
        # Check if already logged out
        if login.logout_at:
            logger.warning(f"Login record {login.login_id} already logged out at {login.logout_at}")
            raise ApplicationError("Already logged out", status_code=400, error_code="ALREADY_LOGGED_OUT")
            
        # Get the refresh token record using the current_refresh_token_id from login
        token_row = db.query(RefreshToken).filter(
            RefreshToken.refresh_token_id == login.current_refresh_token_id
        ).first()
        
        if not token_row:
            logger.error(f"Refresh token not found for refresh_token_id: {login.current_refresh_token_id}")
            raise ApplicationError("Invalid refresh token - token not found", status_code=400, error_code="INVALID_TOKEN")
            
        logger.debug(f"Found refresh token: {token_row.refresh_token_id}, is_active: {token_row.is_active}")
        
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
            from app.Auth.core.security import hash_password
            computed_hash = hash_password(refresh_token)
            
            logger.debug(f"Token hash verification:")
            logger.debug(f"- Stored hash (first 10 chars): {stored_hash[:10]}...")
            logger.debug(f"- Computed hash (first 10 chars): {computed_hash[:10]}...")
            
            if not stored_hash == computed_hash:
                logger.error("Token hash mismatch")
                raise ApplicationError("Invalid refresh token - hash mismatch", status_code=400, error_code="INVALID_TOKEN")
                
            logger.debug("Token hash verification successful")
                
        except jwt.JWTError as e:
            if str(e) == "Signature has expired":
                raise ApplicationError("Refresh token has expired", status_code=401, error_code="TOKEN_EXPIRED")
            raise ApplicationError(f"Invalid refresh token - {str(e)}", status_code=400, error_code="INVALID_TOKEN")
        
        # Deactivate the refresh token
        token_row.is_active = False
        logger.debug(f"Deactivated refresh token {token_row.refresh_token_id}")
        
        # Update login record with logout time and deactivate it
        login.logout_at = func.now()
        login.is_active = False  # Deactivate the login record
        login.ip_address = ip_address or login.ip_address  # Update IP if provided
        logger.debug(f"Updated login record {login.login_id} with logout time and deactivated it")
        
        # Commit changes
        db.commit()
        
        # Blacklist access token if provided
        if access_token:
            try:
                logger.info("Attempting to blacklist access token")
                # Decode access token to get jti and expiry
                payload = jwt.decode(
                    access_token,
                    settings.access_token_secret,
                    algorithms=[settings.jwt_algorithm],
                )
                jti = payload.get("jti")
                exp = payload.get("exp")
                
                logger.info(f"Access token decoded - jti: {jti}, exp: {exp}")
                
                if jti and exp:
                    # Calculate remaining TTL
                    now = datetime.now().timestamp()
                    ttl = int(exp - now)
                    
                    # Apply production-level TTL bounds
                    min_ttl = settings.blacklist_min_ttl_seconds
                    max_ttl = settings.blacklist_max_ttl_seconds
                    
                    if ttl < min_ttl:
                        ttl = min_ttl
                        logger.info(f"Applied minimum TTL: {ttl} seconds")
                    elif ttl > max_ttl:
                        ttl = max_ttl
                        logger.info(f"Applied maximum TTL: {ttl} seconds")
                    else:
                        logger.info(f"Using calculated TTL: {ttl} seconds")
                    
                    if ttl > 0:
                        # Store in Redis with TTL using synchronous client
                        import redis
                        redis_client = redis.from_url(settings.redis_url, decode_responses=True)
                        key = f"blacklist_access:{jti}"
                        redis_client.setex(key, ttl, "1")
                        redis_client.close()
                        logger.info(f"Successfully blacklisted access token jti: {jti} with TTL: {ttl}s")
                    else:
                        logger.warning("Calculated TTL is 0 or negative, skipping blacklist")
                else:
                    logger.warning(f"Access token missing jti or exp claim - jti: {jti}, exp: {exp}")
                    
            except jwt.JWTError as e:
                logger.warning(f"Failed to decode access token for blacklisting: {str(e)}")
            except Exception as e:
                logger.warning(f"Failed to blacklist access token: {str(e)}")
        else:
            logger.info("No access token provided for blacklisting")
        
        logger.info(f"Successfully logged out user {user_id} from login {login.login_id}")
        
        return {
            "message": "Logged out successfully",
            "logged_out_at": datetime.utcnow().isoformat(),
            "login_id": login.login_id
        }
