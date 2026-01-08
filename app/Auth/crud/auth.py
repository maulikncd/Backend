"""
CRUD helpers for authentication operations.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.Auth.core.exceptions import ResourceConflictError
from app.Auth.models.user import User


def get_user_by_email(db: Session, email: str, login_method: str | None = None) -> User | None:
    """Get user by email and optionally by login_method.
    
    Args:
        db: Database session
        email: User's email
        login_method: Optional login method to filter by
        
    Returns:
        User object if found, None otherwise
    """
    query = select(User).where(User.email == email)
    if login_method:
        # Check if login_method exists in the comma-separated list
        query = query.where(User.login_method.contains(login_method))
    return db.execute(query).scalar_one_or_none()


def create_user(
    db: Session,
    *,
    username: str,
    email: str,
    hashed_password: str,
    login_method: str,
    device_id: str | None = None,
    device_name: str | None = None,
    location: str | None = None,
    ip_address: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        login_method=login_method,
        device_id=device_id,
        device_name=device_name,
        location=location,
        ip_address=ip_address,
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError as exc:  # pragma: no cover - depends on DB backend
        db.rollback()
        raise ResourceConflictError("Email already registered with this login method") from exc
    db.refresh(user)
    return user
