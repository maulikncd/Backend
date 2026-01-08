"""
SQLAlchemy session/engine factory.
"""

from __future__ import annotations

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.Auth.core.config import get_settings
from app.Auth.db.base import Base
from app.Auth import models  # noqa: F401  # ensure models are registered with SQLAlchemy

settings = get_settings()

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
    if settings.database_url.startswith("sqlite")
    else {},
    future=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)


def get_db() -> Generator:
    """
    FastAPI dependency that yields a DB session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Create database tables if they do not exist.
    """
    Base.metadata.create_all(bind=engine)
