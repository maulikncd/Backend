"""
Conversation CRUD operations for Chatbot & History System
Handles conversation management, message storage, and history fetching
"""

import sqlite3
import json
import uuid
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

from app.Auth.core.config import get_settings

# Get database path from settings
settings = get_settings()

def _resolve_sqlite_path(database_url: str) -> str:
    """Convert sqlite database URL to filesystem path."""
    if not database_url.startswith("sqlite"):
        raise ValueError("Metadata persistence currently supports sqlite only")
    
    prefix = "sqlite:///"
    alt_prefix = "sqlite://"
    
    if database_url.startswith(prefix):
        raw_path = database_url[len(prefix):]
    elif database_url.startswith(alt_prefix):
        raw_path = database_url[len(alt_prefix):]
    else:
        raw_path = database_url
    
    raw_path = raw_path.strip()
    
    if raw_path in ("", ":memory:"):
        return ":memory:"
    
    return str(Path(raw_path).resolve())

AUTH_DB_PATH = _resolve_sqlite_path(settings.database_url)
print(f"[ConversationCRUD] Using database: {AUTH_DB_PATH}")


def _init_conversation_tables():
    """Initialize conversation and messages tables."""
    if AUTH_DB_PATH != ":memory:":
        Path(AUTH_DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    
    with sqlite3.connect(AUTH_DB_PATH) as conn:
        # Create conversations table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id TEXT UNIQUE NOT NULL,
                uid INTEGER NOT NULL,
                session_id TEXT NOT NULL,
                title TEXT DEFAULT 'New Conversation',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create messages table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id TEXT UNIQUE NOT NULL,
                conversation_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                message_type TEXT DEFAULT 'text',
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations(conversation_id)
            )
        """)
        
        # Create index for faster queries
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_conversations_session 
            ON conversations(session_id, uid)
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_messages_conversation 
            ON messages(conversation_id)
        """)
        
        conn.commit()
        print("[ConversationCRUD] ✅ Tables initialized successfully")


# Initialize tables on module load
_init_conversation_tables()


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
    
    Args:
        uid: User ID
        session_id: Session ID for the project
        title: Optional title (auto-generated if not provided)
    
    Returns:
        Dict with conversation details
    """
    try:
        conversation_id = f"conv_{uuid.uuid4().hex[:12]}"
        default_title = title or "New Conversation"
        now = datetime.now().isoformat()
        
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO conversations (conversation_id, uid, session_id, title, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (conversation_id, uid, session_id, default_title, now, now))
            conn.commit()
        
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
    
    Args:
        session_id: Session ID
        uid: User ID
        limit: Max number of conversations to return
    
    Returns:
        List of conversation dicts with last message preview
    """
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Get conversations with last message
            cursor.execute("""
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
                WHERE c.session_id = ? AND c.uid = ?
                ORDER BY c.updated_at DESC
                LIMIT ?
            """, (session_id, uid, limit))
            
            results = cursor.fetchall()
            
            conversations = []
            for row in results:
                conversations.append({
                    "conversation_id": row[0],
                    "title": row[1],
                    "created_at": row[2],
                    "updated_at": row[3],
                    "last_message": row[4][:100] + "..." if row[4] and len(row[4]) > 100 else row[4],
                    "message_count": row[5]
                })
            
            return conversations
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting conversations: {e}")
        return []


def get_conversation(conversation_id: str, uid: int) -> Optional[Dict[str, Any]]:
    """
    Get a specific conversation by ID.
    
    Args:
        conversation_id: Conversation ID
        uid: User ID (for authorization)
    
    Returns:
        Conversation dict or None
    """
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT conversation_id, uid, session_id, title, created_at, updated_at
                FROM conversations
                WHERE conversation_id = ? AND uid = ?
            """, (conversation_id, uid))
            
            result = cursor.fetchone()
            
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
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting conversation: {e}")
        return None


def update_conversation_title(
    conversation_id: str, 
    title: str, 
    uid: int
) -> bool:
    """
    Update conversation title (auto-generated from first message).
    
    Args:
        conversation_id: Conversation ID
        title: New title
        uid: User ID (for authorization)
    
    Returns:
        True if updated successfully
    """
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE conversations 
                SET title = ?, updated_at = ?
                WHERE conversation_id = ? AND uid = ?
            """, (title, datetime.now().isoformat(), conversation_id, uid))
            conn.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error updating title: {e}")
        return False


def delete_conversation(conversation_id: str, uid: int) -> bool:
    """
    Delete a conversation and all its messages.
    
    Args:
        conversation_id: Conversation ID
        uid: User ID (for authorization)
    
    Returns:
        True if deleted successfully
    """
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Verify ownership
            cursor.execute("""
                SELECT id FROM conversations 
                WHERE conversation_id = ? AND uid = ?
            """, (conversation_id, uid))
            
            if not cursor.fetchone():
                return False
            
            # Delete messages first
            cursor.execute("""
                DELETE FROM messages WHERE conversation_id = ?
            """, (conversation_id,))
            
            # Delete conversation
            cursor.execute("""
                DELETE FROM conversations WHERE conversation_id = ?
            """, (conversation_id,))
            
            conn.commit()
            print(f"[ConversationCRUD] ✅ Deleted conversation: {conversation_id}")
            return True
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
    
    Args:
        conversation_id: Conversation ID
        role: "user" or "assistant"
        content: Message content
        message_type: "text", "suggestion", "code_change", "blueprint_change"
        metadata: Additional data (actions_taken, suggestions, etc.)
    
    Returns:
        Dict with message details
    """
    try:
        message_id = f"msg_{uuid.uuid4().hex[:12]}"
        now = datetime.now().isoformat()
        metadata_json = json.dumps(metadata) if metadata else None
        
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Insert message
            cursor.execute("""
                INSERT INTO messages (message_id, conversation_id, role, content, message_type, metadata, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (message_id, conversation_id, role, content, message_type, metadata_json, now))
            
            # Update conversation's updated_at
            cursor.execute("""
                UPDATE conversations SET updated_at = ? WHERE conversation_id = ?
            """, (now, conversation_id))
            
            conn.commit()
        
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
    
    Args:
        conversation_id: Conversation ID
        limit: Max number of messages
        offset: Pagination offset
    
    Returns:
        List of message dicts
    """
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT message_id, role, content, message_type, metadata, created_at
                FROM messages
                WHERE conversation_id = ?
                ORDER BY created_at ASC
                LIMIT ? OFFSET ?
            """, (conversation_id, limit, offset))
            
            results = cursor.fetchall()
            
            messages = []
            for row in results:
                messages.append({
                    "message_id": row[0],
                    "role": row[1],
                    "content": row[2],
                    "message_type": row[3],
                    "metadata": json.loads(row[4]) if row[4] else None,
                    "created_at": row[5]
                })
            
            return messages
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting messages: {e}")
        return []


def get_recent_messages(
    conversation_id: str, 
    count: int = 10
) -> List[Dict[str, Any]]:
    """
    Get recent messages for AI context.
    
    Args:
        conversation_id: Conversation ID
        count: Number of recent messages
    
    Returns:
        List of recent messages (oldest first)
    """
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT role, content, message_type, created_at
                FROM messages
                WHERE conversation_id = ?
                ORDER BY created_at DESC
                LIMIT ?
            """, (conversation_id, count))
            
            results = cursor.fetchall()
            
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
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting recent messages: {e}")
        return []


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def generate_title_from_message(message: str, max_length: int = 40) -> str:
    """
    Generate a conversation title from the first user message.
    
    Args:
        message: User's first message
        max_length: Maximum title length
    
    Returns:
        Generated title string
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
    
    Args:
        uid: User ID
        session_id: Session ID
        conversation_id: Optional existing conversation ID
    
    Returns:
        Conversation dict
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
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*) FROM conversations
                WHERE session_id = ? AND uid = ?
            """, (session_id, uid))
            result = cursor.fetchone()
            return result[0] if result else 0
    except Exception as e:
        print(f"[ConversationCRUD] ❌ Error getting count: {e}")
        return 0
