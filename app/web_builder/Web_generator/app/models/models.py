"""
Models for Web_generator module
# added by web_generator
"""

from sqlalchemy import Column, String, Text, DateTime, Dict, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    blueprint = Column(JSON)
    code = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(String, default="created")

class ChatHistory(Base):
    __tablename__ = "chat_history"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    role = Column(String, nullable=False)  # "user" or "assistant"
    timestamp = Column(DateTime, default=datetime.utcnow)

class ProjectAction(Base):
    __tablename__ = "project_actions"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    action_type = Column(String, nullable=False)  # "generate", "save", "undo", etc.
    action_data = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)
