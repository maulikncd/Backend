"""
Reusable FastAPI dependencies.
"""

from __future__ import annotations

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from sqlalchemy.orm import Session

from app.Auth.core.config import Settings, get_settings
from app.Auth.db.session import get_db
from app.Auth.models.user import User

security = HTTPBearer()


def get_app_settings() -> Settings:
    """
    Expose settings via dependency injection.
    """
    return get_settings()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency to get current authenticated user from JWT access token.
    Includes token blacklist checking for proper logout functionality.
Storage.
    """
    settings = get_settings()
    
    try:
        # Decode JWT token
        payload = jwt.decode(
            credentials.credentials,
            settings.access_token_secret,
            algorithms=[settings.jwt_algorithm]
        )
        
        user_id = int(payload.get("sub"))
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"X-Error-Code": "INVALID_TOKEN"}
            )
        
        # Check if access token is blacklisted in Redis
        jti = payload.get("jti")
        if jti:
            import logging
            logger = logging.getLogger(__name__)
            logger.info(f"Checking blacklist for jti: {jti}")
            
            try:
                import redis
                redis_client = redis.from_url(settings.redis_url, decode_responses=True)
                key = f"blacklist_access:{jti}"
                blacklisted = redis_client.get(key)
                redis_client.close()
                
                logger.info(f"Blacklist check result for {jti}: {blacklisted}")
                
                if blacklisted:
                    logger.warning(f"Token {jti} is blacklisted - rejecting request")
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Token has been revoked",
                        headers={"X-Error-Code": "TOKEN_REVOKED"}
                    )
                else:
                    logger.info(f"Token {jti} is not blacklisted")
                    
            except HTTPException:
                # Re-raise HTTPException (like token revoked)
                raise
            except Exception as e:
                # Log error but don't fail authentication if Redis is unavailable
                logger.warning(f"Failed to check token blacklist: {str(e)}")
        else:
            logger.warning("No jti found in access token payload")
        
        # Get user from database
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"X-Error-Code": "USER_NOT_FOUND"}
            )
        
        return user
        
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"X-Error-Code": "INVALID_TOKEN"}
        )
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"X-Error-Code": "INVALID_TOKEN"}
        )

