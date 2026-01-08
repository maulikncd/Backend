"""
Login record model for tracking user login sessions.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.Auth.db.base import Base


class LoginRecord(Base):
    """Model for storing user login session records."""

    __tablename__ = "login_records"

    login_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    login_method: Mapped[str] = mapped_column(String(50), nullable=False, default="manual")
    ip_address: Mapped[Optional[str]] = mapped_column(String(45), nullable=True)
    login_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    device_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    device_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    logout_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    current_refresh_token_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("refresh_tokens.refresh_token_id"),
        nullable=True
    )
    
    # Relationship
    refresh_token: Mapped[Optional["RefreshToken"]] = relationship("RefreshToken")
