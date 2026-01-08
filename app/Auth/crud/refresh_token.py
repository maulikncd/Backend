"""
CRUD operations for refresh tokens.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session

from app.Auth.core.security import hash_password
from app.Auth.models.refresh_token import RefreshToken


def create_refresh_token(
    db: Session,
    *,
    user_id: int,
    token_hash: str,
    expires_at: datetime,
) -> RefreshToken:
    """Create a new refresh token."""
    refresh_token = RefreshToken(
        user_id=user_id,
        token_hash=token_hash,
        expires_at=expires_at,
        is_active=True,
    )
    db.add(refresh_token)
    db.commit()
    db.refresh(refresh_token)
    return refresh_token


def get_active_refresh_token(db: Session, token_hash: str) -> Optional[RefreshToken]:
    """Get an active refresh token by hash."""
    return (
        db.query(RefreshToken)
        .filter(
            RefreshToken.token_hash == token_hash,
            RefreshToken.is_active == True,
            RefreshToken.expires_at > datetime.utcnow(),
        )
        .first()
    )


def revoke_refresh_token(db: Session, token_id: int) -> Optional[RefreshToken]:
    """Revoke a refresh token by setting is_active to False."""
    refresh_token = db.query(RefreshToken).filter(RefreshToken.refresh_token_id == token_id).first()
    if refresh_token:
        refresh_token.is_active = False
        db.commit()
        db.refresh(refresh_token)
    return refresh_token


def revoke_user_refresh_tokens(db: Session, user_id: int) -> list[RefreshToken]:
    """Revoke all active refresh tokens for a user."""
    refresh_tokens = (
        db.query(RefreshToken)
        .filter(RefreshToken.user_id == user_id, RefreshToken.is_active == True)
        .all()
    )
    for token in refresh_tokens:
        token.is_active = False
    db.commit()
    return refresh_tokens


def cleanup_expired_tokens(db: Session) -> int:
    """Delete expired refresh tokens and return count of deleted tokens."""
    expired_tokens = (
        db.query(RefreshToken)
        .filter(RefreshToken.expires_at <= datetime.utcnow())
        .all()
    )
    count = len(expired_tokens)
    for token in expired_tokens:
        db.delete(token)
    db.commit()
    return count
