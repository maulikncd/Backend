"""
Security helpers for hashing passwords and generating JWT tokens.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict

from jose import jwt
from passlib.context import CryptContext

from app.Auth.core.config import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()


def hash_password(plain_password: str) -> str:
    """Hash a password or token.
    
    Args:
        plain_password: The plain text password or token to hash
        
    Returns:
        str: The hashed password/token
    """
    # For tokens, we'll use a simpler hash since they're already cryptographically random
    if len(plain_password) > 50:  # Likely a JWT token
        import hashlib
        return hashlib.sha256(plain_password.encode()).hexdigest()
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password or token against a hash.
    
    Args:
        plain_password: The plain text password or token to verify
        hashed_password: The hashed password or token to verify against
        
    Returns:
        bool: True if the password/token matches the hash, False otherwise
    """
    # For tokens, we'll use a simpler hash comparison
    if len(plain_password) > 50:  # Likely a JWT token
        import hashlib
        return hashed_password == hashlib.sha256(plain_password.encode()).hexdigest()
    return pwd_context.verify(plain_password, hashed_password)


def _create_token(subject: str, expires_delta: timedelta, extra_claims: Dict[str, Any]) -> str:
    expire = datetime.now(tz=timezone.utc) + expires_delta
    payload = {"sub": subject, "exp": expire, **extra_claims}
    return jwt.encode(payload, settings.access_token_secret, algorithm=settings.jwt_algorithm)


def create_access_token(subject: str, extra_claims: Dict[str, Any] | None = None) -> str:
    expires = timedelta(minutes=settings.access_token_exp_minutes)
    claims = extra_claims or {}
    # Add jti claim for unique token identification
    import uuid
    claims["jti"] = str(uuid.uuid4())
    return _create_token(subject, expires, claims)


def create_refresh_token(
    subject: str,
    refresh_token_id: int,
    extra_claims: Dict[str, Any] | None = None,
) -> str:
    expire = timedelta(minutes=settings.refresh_token_exp_minutes)
    payload_exp = datetime.now(tz=timezone.utc) + expire

    payload = {
        "sub": subject,
        "refresh_token_id": refresh_token_id,  # 👈 IMPORTANT
        "exp": payload_exp,
        "type": "refresh",
    }

    if extra_claims:
        payload.update(extra_claims)

    return jwt.encode(
        payload,
        settings.refresh_token_secret,
        algorithm=settings.jwt_algorithm,
    )
