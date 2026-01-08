"""
Metadata model.
"""
from __future__ import annotations

from datetime import datetime
from sqlalchemy import Integer, String, Column, Text, DateTime, func
from app.Auth.db.base import Base

class Metadata(Base):
    __tablename__ = "metadata"

    metadata_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    session_id = Column(Text, nullable=False)
    project_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    path = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
