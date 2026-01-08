"""
Blueprint model.
"""
from __future__ import annotations

from sqlalchemy import Integer, Text, Column
from sqlalchemy.dialects.postgresql import JSON
from app.Auth.db.base import Base

class Blueprint(Base):
    __tablename__ = "blueprint"

    blueprint_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Text, nullable=False)
    blueprint = Column(JSON, nullable=True) 
