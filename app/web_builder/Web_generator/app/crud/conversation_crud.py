"""
Conversation CRUD operations for Chatbot & History System
Handles conversation management, message storage, and history fetching
"""

import json
import uuid
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

from sqlalchemy import text
from app.Auth.core.config import get_settings
from app.Auth.db.session import SessionLocal

# Get database path from settings (unused for functionality now)
settings = get_settings()

# _resolve_sqlite_path and _init_conversation_tables removed
# as we support Postgres now.
# Tables conversations and messages are expected to exist in the DB.


# ============================================================
# CONVERSATION CRUD OPERATIONS
# ============================================================

def create_conversation(
    uid: int, 
    session_id: str, 
    title: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new conversation for a user.
    """
    try:
        conversation_id = f"conv_{uuid.uuid4().hex[:12]}"
        default_title = title or "New Conversation"
        now = datetime.now().isoformat()
        
        db = SessionLocal()
        try:
            db.execute(
                text("""
                INSERT INTO conversations (conversation_id, uid, session_id, title, created_at, updated_at)
                VALUES (:cid, :uid, :sid, :title, :created, :updated)
                """),
                {
                    "cid": conversation_id,
                    "uid": uid,
                    "sid": session_id,
                    "title": default_title,
                    "created": now,
                    "updated": now
                }
            )
            db.commit()
        finally:
            db.close()
        
        print(f"[ConversationCRUD] ✅ Created conversation: {conversation_id}")
        
        return {
            "conversation_id": conversation_id,
            "uid": uid,
            "session_id": session_id,
            "title": default_title,
            "created_at": now,
            "updated_at": now
        }
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error creating conversation: {e}")
        return {"error": str(e)}


def get_conversations_by_session(
    session_id: str, 
    uid: int, 
    limit: int = 50
) -> List[Dict[str, Any]]:
    """
    Get all conversations for a session (sidebar history).
    """
    try:
        db = SessionLocal()
        try:
            results = db.execute(
                text("""
                SELECT 
                    c.conversation_id,
                    c.title,
                    c.created_at,
                    c.updated_at,
                    (SELECT content FROM messages m 
                     WHERE m.conversation_id = c.conversation_id 
                     ORDER BY m.created_at DESC LIMIT 1) as last_message,
                    (SELECT COUNT(*) FROM messages m 
                     WHERE m.conversation_id = c.conversation_id) as message_count
                FROM conversations c
                WHERE c.session_id = :sid AND c.uid = :uid
                ORDER BY c.updated_at DESC
                LIMIT :limit
                """),
                {"sid": session_id, "uid": uid, "limit": limit}
            ).fetchall()
            
            conversations = []
            for row in results:
                # row[4] (last_message) might be None
                last_msg = row[4]
                if last_msg and len(last_msg) > 100:
                    last_msg = last_msg[:100] + "..."
                
                conversations.append({
                    "conversation_id": row[0],
                    "title": row[1],
                    "created_at": row[2],
                    "updated_at": row[3],
                    "last_message": last_msg,
                    "message_count": row[5]
                })
            
            return conversations
        finally:
            db.close()
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting conversations: {e}")
        return []


def get_conversation(conversation_id: str, uid: int) -> Optional[Dict[str, Any]]:
    """
    Get a specific conversation by ID.
    """
    try:
        db = SessionLocal()
        try:
            result = db.execute(
                text("""
                SELECT conversation_id, uid, session_id, title, created_at, updated_at
                FROM conversations
                WHERE conversation_id = :cid AND uid = :uid
                """),
                {"cid": conversation_id, "uid": uid}
            ).fetchone()
            
            if result:
                return {
                    "conversation_id": result[0],
                    "uid": result[1],
                    "session_id": result[2],
                    "title": result[3],
                    "created_at": result[4],
                    "updated_at": result[5]
                }
            return None
        finally:
            db.close()
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting conversation: {e}")
        return None


def update_conversation_title(
    conversation_id: str, 
    title: str, 
    uid: int
) -> bool:
    """
    Update conversation title.
    """
    try:
        db = SessionLocal()
        try:
            result = db.execute(
                text("""
                UPDATE conversations 
                SET title = :title, updated_at = :updated
                WHERE conversation_id = :cid AND uid = :uid
                """),
                {
                    "title": title,
                    "updated": datetime.now().isoformat(),
                    "cid": conversation_id,
                    "uid": uid
                }
            )
            db.commit()
            return result.rowcount > 0
        finally:
            db.close()
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error updating title: {e}")
        return False


def delete_conversation(conversation_id: str, uid: int) -> bool:
    """
    Delete a conversation and all its messages.
    """
    try:
        db = SessionLocal()
        try:
            # Verify ownership
            check = db.execute(
                text("SELECT id FROM conversations WHERE conversation_id = :cid AND uid = :uid"),
                {"cid": conversation_id, "uid": uid}
            ).fetchone()
            
            if not check:
                return False
            
            # Delete messages first
            db.execute(
                text("DELETE FROM messages WHERE conversation_id = :cid"),
                {"cid": conversation_id}
            )
            
            # Delete conversation
            db.execute(
                text("DELETE FROM conversations WHERE conversation_id = :cid"),
                {"cid": conversation_id}
            )
            
            db.commit()
            print(f"[ConversationCRUD] ✅ Deleted conversation: {conversation_id}")
            return True
        finally:
            db.close()
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error deleting conversation: {e}")
        return False


# ============================================================
# MESSAGE CRUD OPERATIONS
# ============================================================

def save_message(
    conversation_id: str,
    role: str,
    content: str,
    message_type: str = "text",
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Save a message to a conversation.
    """
    try:
        message_id = f"msg_{uuid.uuid4().hex[:12]}"
        now = datetime.now().isoformat()
        metadata_json = json.dumps(metadata) if metadata else None
        
        db = SessionLocal()
        try:
            # Insert message
            db.execute(
                text("""
                INSERT INTO messages (message_id, conversation_id, role, content, message_type, metadata, created_at)
                VALUES (:mid, :cid, :role, :content, :mtype, :meta, :created)
                """),
                {
                    "mid": message_id,
                    "cid": conversation_id,
                    "role": role,
                    "content": content,
                    "mtype": message_type,
                    "meta": metadata_json,
                    "created": now
                }
            )
            
            # Update conversation's updated_at
            db.execute(
                text("UPDATE conversations SET updated_at = :updated WHERE conversation_id = :cid"),
                {"updated": now, "cid": conversation_id}
            )
            
            db.commit()
        finally:
            db.close()
        
        print(f"[ConversationCRUD] ✅ Saved message {message_id} to {conversation_id} (role: {role})")
        
        return {
            "message_id": message_id,
            "conversation_id": conversation_id,
            "role": role,
            "content": content,
            "message_type": message_type,
            "metadata": metadata,
            "created_at": now
        }
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error saving message: {e}")
        return {"error": str(e)}


def get_messages(
    conversation_id: str, 
    limit: int = 100,
    offset: int = 0
) -> List[Dict[str, Any]]:
    """
    Get all messages for a conversation.
    """
    try:
        db = SessionLocal()
        try:
            results = db.execute(
                text("""
                SELECT message_id, role, content, message_type, metadata, created_at
                FROM messages
                WHERE conversation_id = :cid
                ORDER BY created_at ASC
                LIMIT :limit OFFSET :offset
                """),
                {"cid": conversation_id, "limit": limit, "offset": offset}
            ).fetchall()
            
            messages = []
            for row in results:
                # row: message_id, role, content, message_type, metadata, created_at
                meta = row[4]
                if meta and isinstance(meta, str):
                    try:
                        meta = json.loads(meta)
                    except:
                        meta = None
                
                messages.append({
                    "message_id": row[0],
                    "role": row[1],
                    "content": row[2],
                    "message_type": row[3],
                    "metadata": meta,
                    "created_at": row[5]
                })
            
            return messages
        finally:
            db.close()
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting messages: {e}")
        return []


def get_recent_messages(
    conversation_id: str, 
    count: int = 10
) -> List[Dict[str, Any]]:
    """
    Get recent messages for AI context.
    """
    try:
        db = SessionLocal()
        try:
            results = db.execute(
                text("""
                SELECT role, content, message_type, created_at
                FROM messages
                WHERE conversation_id = :cid
                ORDER BY created_at DESC
                LIMIT :limit
                """),
                {"cid": conversation_id, "limit": count}
            ).fetchall()
            
            # Reverse to get oldest first
            messages = []
            for row in reversed(results):
                messages.append({
                    "role": row[0],
                    "content": row[1],
                    "message_type": row[2],
                    "created_at": row[3]
                })
            
            return messages
        finally:
            db.close()
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting recent messages: {e}")
        return []


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def generate_title_from_message(message: str, max_length: int = 40) -> str:
    """
    Generate a conversation title from the first user message.
    """
    # Clean up message
    title = message.strip()
    
    # Remove common prefixes
    prefixes = ["please ", "can you ", "i want to ", "i need to ", "help me "]
    for prefix in prefixes:
        if title.lower().startswith(prefix):
            title = title[len(prefix):]
            break
    
    # Capitalize first letter
    title = title[0].upper() + title[1:] if title else "New Conversation"
    
    # Truncate if too long
    if len(title) > max_length:
        title = title[:max_length-3] + "..."
    
    return title


def get_or_create_conversation(
    uid: int, 
    session_id: str, 
    conversation_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get existing conversation or create a new one.
    """
    if conversation_id:
        conv = get_conversation(conversation_id, uid)
        if conv:
            return conv
    
    # Create new conversation
    return create_conversation(uid, session_id)


def get_conversation_count(session_id: str, uid: int) -> int:
    """Get total conversation count for a session."""
    try:
        db = SessionLocal()
        try:
            result = db.execute(
                text("SELECT COUNT(*) FROM conversations WHERE session_id = :sid AND uid = :uid"),
                {"sid": session_id, "uid": uid}
            ).fetchone()
            return result[0] if result else 0
        finally:
            db.close()
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting count: {e}")
        return 0
