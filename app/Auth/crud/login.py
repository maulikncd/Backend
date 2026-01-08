"""
CRUD operations for login records.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from app.Auth.models.login_record import LoginRecord


def create_login_record(
    db: Session,
    *,
    user_id: int,
    email: str,
    login_method: str = "manual",
    ip_address: Optional[str] = None,
    device_id: Optional[str] = None,
    device_name: Optional[str] = None,
    location: Optional[str] = None,
) -> LoginRecord:
    """Create a new login record."""
    login_record = LoginRecord(
        user_id=user_id,
        email=email,
        login_method=login_method,
        ip_address=ip_address,
        device_id=device_id,
        device_name=device_name,
        location=location,
        login_at=datetime.utcnow(),
        is_active=True,
    )
    db.add(login_record)
    db.commit()
    db.refresh(login_record)
    return login_record


def get_active_login_by_user(db: Session, user_id: int) -> Optional[LoginRecord]:
    """Get the active login record for a user."""
    return (
        db.query(LoginRecord)
        .filter(LoginRecord.user_id == user_id, LoginRecord.is_active == True)
        .first()
    )


def deactivate_login_record(db: Session, login_id: int) -> Optional[LoginRecord]:
    """Deactivate a login record by setting logout_at."""
    login_record = db.query(LoginRecord).filter(LoginRecord.login_id == login_id).first()
    if login_record:
        login_record.is_active = False
        login_record.logout_at = datetime.utcnow()
        db.commit()
        db.refresh(login_record)
    return login_record


def update_user_login_records(db: Session, user_id: int, username: str) -> list[LoginRecord]:
    """Update username for all login records of a user."""
    login_records = (
        db.query(LoginRecord)
        .filter(LoginRecord.user_id == user_id)
        .all()
    )
    for record in login_records:
        record.username = username
    db.commit()
    return login_records


def deactivate_user_logins(db: Session, user_id: int) -> list[LoginRecord]:
    """Deactivate all active login records for a user."""
    login_records = (
        db.query(LoginRecord)
        .filter(LoginRecord.user_id == user_id, LoginRecord.is_active == True)
        .all()
    )
    for record in login_records:
        record.is_active = False
        record.logout_at = datetime.utcnow()
    db.commit()
    return login_records
