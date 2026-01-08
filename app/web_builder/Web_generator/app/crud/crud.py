"""
CRUD operations for Web_generator module
# added by web_generator
"""

import redis
import json
import sqlite3
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

# Import settings to get database URL
from app.Auth.core.config import get_settings

# Redis connection for session management (optional - will work without Redis)
redis_available = False
redis_client = None

try:
    redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    redis_client.ping()  # Test connection
    redis_available = True
    print("[CRUD] ✅ Redis connection established")
    
    # Fix for Windows Redis "MISCONF" error
    try:
        redis_client.config_set('stop-writes-on-bgsave-error', 'no')
    except Exception:
        pass
except Exception as e:
    print(f"[CRUD] ⚠️ Redis not available, using file-based sessions: {e}")

def _resolve_sqlite_path(database_url: str) -> str:
    """
    Convert a sqlite database URL (sqlite:///...) into a filesystem path
    so we can connect with sqlite3 and share the same file as SQLAlchemy.
    """
    if not database_url.startswith("sqlite"):
        raise ValueError("Metadata persistence currently supports sqlite only")

    # Support sqlite:///absolute_or_relative and sqlite:///<drive>/<path>
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

# Get database path from settings
settings = get_settings()
AUTH_DB_PATH = _resolve_sqlite_path(settings.database_url)

def _init_web_generator_tables():
    """Ensure the web generator tables exist."""
    if AUTH_DB_PATH != ":memory:":
        Path(AUTH_DB_PATH).parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(AUTH_DB_PATH) as conn:
        # Create blueprint table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS blueprint (
                blueprint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                blueprint TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES metadata (session_id)
            )
            """
        )
        
        # Create code table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS code (
                code_id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                code TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES metadata (session_id)
            )
            """
        )
        
        # Create chat-history table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS chat_history (
                conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                uid INTEGER NOT NULL,
                session_id TEXT NOT NULL,
                chat_id TEXT NOT NULL,
                conversion_id INTEGER NOT NULL,
                user_input TEXT NOT NULL,
                AI_response TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES metadata (session_id)
            )
            """
        )

# Initialize the tables
_init_web_generator_tables()

def get_session(session_id: str) -> Optional[Dict[str, Any]]:
    """Get session data from Redis first, fallback to database metadata.
    Tries multiple key formats for compatibility with different modules.
    
    🆕 Also handles proj_X format for legacy projects.
    🆕 Works without Redis - uses file-based fallbacks."""
    try:
        # Try Redis only if available
        if redis_available and redis_client:
            try:
                # Try Redis with 'session:' prefix first (Web_generator format)
                session_data = redis_client.get(f"session:{session_id}")
                if session_data:
                    print(f"[CRUD] Found session in Redis with 'session:' prefix")
                    return json.loads(session_data)
                
                # Try Redis without prefix (Recommendation format)
                session_data = redis_client.get(session_id)
                if session_data:
                    print(f"[CRUD] Found session in Redis without prefix")
                    return json.loads(session_data)
            except Exception as e:
                print(f"[CRUD] Redis error, falling back to database: {e}")
        
        # If not in Redis (or Redis unavailable), try to get from database metadata table
        print(f"[CRUD] Checking database for session...")
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT path FROM metadata WHERE session_id = ? ORDER BY created_at DESC LIMIT 1",
                (session_id,)
            )
            result = cursor.fetchone()
            if result:
                # Path is stored relative to backend folder, read the JSON file
                metadata_path = result[0]
                backend_path = Path(__file__).parent.parent.parent.parent.parent.parent
                full_path = backend_path / metadata_path
                
                if full_path.exists():
                    with open(full_path, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    print(f"[CRUD] Found session in database metadata file: {full_path}")
                    return metadata
                else:
                    print(f"[CRUD] Metadata file not found at path: {full_path}")
        
        # 🆕 Handle proj_X format - create virtual session from project folder
        if session_id.startswith("proj_"):
            try:
                project_id = session_id.replace("proj_", "")
                backend_path = Path(__file__).parent.parent.parent.parent.parent.parent
                projects_folder = backend_path / "projects"
                
                if projects_folder.exists():
                    # Find project folder matching the project_id
                    for folder in projects_folder.iterdir():
                        if folder.is_dir():
                            parts = folder.name.split("_", 2)
                            if len(parts) >= 2 and parts[1] == project_id:
                                # Found project folder - create virtual session
                                metadata_file = folder / "metadata" / "project.json"
                                if metadata_file.exists():
                                    with open(metadata_file, 'r', encoding='utf-8') as f:
                                        project_meta = json.load(f)
                                        # Create session-like structure
                                        virtual_session = {
                                            "session_id": session_id,
                                            "user_id": project_meta.get("user_id"),
                                            "project_id": project_id,
                                            "project_name": project_meta.get("project_name"),
                                            "folder_path": str(folder),
                                            "_is_synthetic": True
                                        }
                                        print(f"[CRUD] Created virtual session from project folder: {folder}")
                                        return virtual_session
                                else:
                                    # No metadata file, but folder exists - create minimal session
                                    virtual_session = {
                                        "session_id": session_id,
                                        "project_id": project_id,
                                        "folder_path": str(folder),
                                        "_is_synthetic": True
                                    }
                                    print(f"[CRUD] Created minimal virtual session from project folder: {folder}")
                                    return virtual_session
            except Exception as e:
                print(f"[CRUD] Error creating virtual session: {e}")
        
        print(f"[CRUD] Session not found anywhere for session_id: {session_id}")
        return None
    except Exception as e:
        print(f"Error getting session: {e}")
        return None

def save_session(session_id: str, session_data: Dict[str, Any]) -> bool:
    """Save session data to Redis (if available)"""
    if not redis_available or not redis_client:
        print(f"[CRUD] ⚠️ Redis not available, session not saved")
        return False
    try:
        redis_client.set(f"session:{session_id}", json.dumps(session_data))
        return True
    except Exception as e:
        print(f"Error saving session: {e}")
        return False

def get_project_metadata(session_id: str) -> Optional[Dict[str, Any]]:
    """Get project metadata from session"""
    session = get_session(session_id)
    if session and "metadata" in session:
        return session["metadata"]
    return None

def save_project_state(session_id: str, state: Dict[str, Any]) -> bool:
    """Save project state to session"""
    session = get_session(session_id)
    if session:
        session["project_state"] = state
        return save_session(session_id, session)
    return False

def get_project_state(session_id: str) -> Optional[Dict[str, Any]]:
    """Get project state from session"""
    session = get_session(session_id)
    if session and "project_state" in session:
        return session["project_state"]
    return {}

def save_action_history(session_id: str, action: Dict[str, Any]) -> bool:
    """Save action to history for undo/redo functionality"""
    session = get_session(session_id)
    if session:
        if "action_history" not in session:
            session["action_history"] = []
        
        session["action_history"].append({
            **action,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 50 actions
        if len(session["action_history"]) > 50:
            session["action_history"] = session["action_history"][-50:]
        
        return save_session(session_id, session)
    return False

def get_action_history(session_id: str) -> List[Dict[str, Any]]:
    """Get action history from session"""
    session = get_session(session_id)
    if session and "action_history" in session:
        return session["action_history"]
    return []

def save_chat_history_to_session(session_id: str, messages: List[Dict[str, Any]]) -> bool:
    """Save chat history to session"""
    session = get_session(session_id)
    if session:
        session["chat_history"] = messages
        return save_session(session_id, session)
    return False

def get_chat_history_from_session(session_id: str) -> List[Dict[str, Any]]:
    """Get chat history from database (updated for new structure)"""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT user_input, AI_response, created_at FROM chat_history WHERE session_id = ? ORDER BY created_at",
                (session_id,)
            )
            results = cursor.fetchall()
            
            history = []
            for user_input, ai_response, created_at in results:
                history.extend([
                    {
                        "role": "user",
                        "message": user_input,
                        "timestamp": created_at
                    },
                    {
                        "role": "assistant",
                        "message": ai_response,
                        "timestamp": created_at
                    }
                ])
            return history
    except Exception as e:
        print(f"Error getting chat history: {e}")
        return []

def save_blueprint_to_db(session_id: str, blueprint: Dict[str, Any]) -> int:
    """Save blueprint to database and optionally to project folder.
    
    🆕 For proj_X format sessions, also saves to project's blue/ folder.
    """
    try:
        # 1. Save to database
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO blueprint (session_id, blueprint) VALUES (?, ?)",
                (session_id, json.dumps(blueprint))
            )
            conn.commit()
            blueprint_id = cursor.lastrowid
        
        # 2. For proj_X format, also save to project folder
        if session_id.startswith("proj_"):
            try:
                project_id = session_id.replace("proj_", "")
                backend_path = Path(__file__).parent.parent.parent.parent.parent.parent
                projects_folder = backend_path / "projects"
                
                for folder in projects_folder.iterdir():
                    if folder.is_dir():
                        parts = folder.name.split("_", 2)
                        if len(parts) >= 2 and parts[1] == project_id:
                            blue_folder = folder / "blue"
                            blue_folder.mkdir(parents=True, exist_ok=True)
                            
                            blueprint_path = blue_folder / "latest.json"
                            with open(blueprint_path, 'w', encoding='utf-8') as f:
                                json.dump(blueprint, f, indent=2)
                            print(f"[CRUD] Saved blueprint to project folder: {blueprint_path}")
                            break
            except Exception as e:
                print(f"[CRUD] Error saving blueprint to project folder: {e}")
        
        return blueprint_id
    except Exception as e:
        print(f"Error saving blueprint: {e}")
        return -1

def get_blueprint_from_db(session_id: str) -> Optional[Dict[str, Any]]:
    """Get latest blueprint from database or project folder.
    
    🆕 Supports proj_X format for legacy projects without original session_id.
    """
    try:
        # 1. First try database
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT blueprint FROM blueprint WHERE session_id = ? ORDER BY created_at DESC LIMIT 1",
                (session_id,)
            )
            result = cursor.fetchone()
            if result:
                return json.loads(result[0])
        
        # 2. Handle proj_X format - load from project folder
        if session_id.startswith("proj_"):
            try:
                project_id = session_id.replace("proj_", "")
                backend_path = Path(__file__).parent.parent.parent.parent.parent.parent
                projects_folder = backend_path / "projects"
                
                # Find project folder matching the project_id
                for folder in projects_folder.iterdir():
                    if folder.is_dir():
                        # Folder format: {user_id}_{project_id}_{project_name}
                        parts = folder.name.split("_", 2)
                        if len(parts) >= 2 and parts[1] == project_id:
                            # Found the project folder
                            blueprint_path = folder / "blue" / "latest.json"
                            if blueprint_path.exists():
                                with open(blueprint_path, 'r', encoding='utf-8') as f:
                                    print(f"[CRUD] Loaded blueprint from project folder: {blueprint_path}")
                                    return json.load(f)
            except Exception as e:
                print(f"[CRUD] Error loading blueprint from project folder: {e}")
        
        return None
    except Exception as e:
        print(f"Error getting blueprint: {e}")
        return None

def delete_blueprint_from_db(session_id: str) -> bool:
    """Delete all blueprints for a session (for force regeneration)"""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM blueprint WHERE session_id = ?",
                (session_id,)
            )
            conn.commit()
            deleted_count = cursor.rowcount
            print(f"[CRUD] Deleted {deleted_count} blueprint(s) for session {session_id}")
            return deleted_count > 0
    except Exception as e:
        print(f"Error deleting blueprint: {e}")
        return False

def save_code_to_db(session_id: str, code: str) -> int:
    """Save or overwrite generated code to database"""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Check if code already exists for this session
            cursor.execute(
                "SELECT code_id FROM code WHERE session_id = ? ORDER BY created_at DESC LIMIT 1",
                (session_id,)
            )
            existing = cursor.fetchone()
            
            if existing:
                # Update existing code
                cursor.execute(
                    "UPDATE code SET code = ?, created_at = CURRENT_TIMESTAMP WHERE code_id = ?",
                    (code, existing[0])
                )
                code_id = existing[0]
            else:
                # Insert new code
                cursor.execute(
                    "INSERT INTO code (session_id, code) VALUES (?, ?)",
                    (session_id, code)
                )
                code_id = cursor.lastrowid
            
            conn.commit()
            return code_id
    except Exception as e:
        print(f"Error saving code: {e}")
        return -1

def get_code_from_db(session_id: str) -> Optional[Dict[str, Any]]:
    """Get latest code from database"""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT code_id, code, created_at FROM code WHERE session_id = ? ORDER BY created_at DESC LIMIT 1",
                (session_id,)
            )
            result = cursor.fetchone()
            if result:
                return {
                    "code_id": result[0],
                    "code": result[1],
                    "created_at": result[2]
                }
        return None
    except Exception as e:
        print(f"Error getting code: {e}")
        return None

def get_user_chat_history(uid: int) -> Dict[str, List[Dict[str, Any]]]:
    """Get all chat history for a user grouped by chat_id"""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT chat_id, conversion_id, user_input, AI_response, created_at 
                FROM chat_history 
                WHERE uid = ? 
                ORDER BY chat_id, conversion_id
                """,
                (uid,)
            )
            results = cursor.fetchall()
            
            # Group by chat_id
            chat_history = {}
            for chat_id, conversion_id, user_input, ai_response, created_at in results:
                if chat_id not in chat_history:
                    chat_history[chat_id] = []
                
                chat_history[chat_id].append({
                    "conversion_id": conversion_id,
                    "user_input": user_input,
                    "AI_response": ai_response,
                    "created_at": created_at
                })
            
            return chat_history
    except Exception as e:
        print(f"Error getting user chat history: {e}")
        return {}

def get_chat_history_by_chat_id(uid: int, chat_id: str) -> List[Dict[str, Any]]:
    """Get specific chat history for a user by chat_id"""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT conversion_id, user_input, AI_response, created_at 
                FROM chat_history 
                WHERE uid = ? AND chat_id = ? 
                ORDER BY conversion_id
                """,
                (uid, chat_id)
            )
            results = cursor.fetchall()
            
            history = []
            for conversion_id, user_input, ai_response, created_at in results:
                history.extend([
                    {
                        "role": "user",
                        "message": user_input,
                        "conversion_id": conversion_id,
                        "timestamp": created_at
                    },
                    {
                        "role": "assistant",
                        "message": ai_response,
                        "conversion_id": conversion_id,
                        "timestamp": created_at
                    }
                ])
            return history
    except Exception as e:
        print(f"Error getting chat history by chat_id: {e}")
        return []

def get_user_chat_list(uid: int) -> List[Dict[str, Any]]:
    """Get list of all chat_ids for a user with last message info"""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT chat_id, MAX(created_at) as last_message_time, 
                       COUNT(*) as message_count
                FROM chat_history 
                WHERE uid = ? 
                GROUP BY chat_id 
                ORDER BY last_message_time DESC
                """,
                (uid,)
            )
            results = cursor.fetchall()
            
            chat_list = []
            for chat_id, last_message_time, message_count in results:
                chat_list.append({
                    "chat_id": chat_id,
                    "last_message_time": last_message_time,
                    "message_count": message_count
                })
            return chat_list
    except Exception as e:
        print(f"Error getting user chat list: {e}")
        return []

def save_chat_to_db(session_id: str, uid: int, chat_id: str, conversion_id: int, user_input: str, ai_response: str) -> int:
    """Save chat conversation to database with new structure"""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO chat_history (uid, session_id, chat_id, conversion_id, user_input, AI_response) VALUES (?, ?, ?, ?, ?, ?)",
                (uid, session_id, chat_id, conversion_id, user_input, ai_response)
            )
            conn.commit()
            return cursor.lastrowid
    except Exception as e:
        print(f"Error saving chat: {e}")
        return -1

def save_action_history_redis(session_id: str, action: Dict[str, Any]) -> bool:
    """Save action to Redis for undo/redo (max 5 actions)"""
    try:
        # Get current actions
        actions_key = f"actions:{session_id}"
        current_actions = redis_client.lrange(actions_key, 0, -1)
        
        # Add new action to the front
        action_data = json.dumps({
            **action,
            "timestamp": datetime.now().isoformat()
        })
        
        redis_client.lpush(actions_key, action_data)
        # Keep only last 5 actions
        redis_client.ltrim(actions_key, 0, 4)
        return True
    except Exception as e:
        print(f"Error saving action history: {e}")
        return False

def get_action_history_redis(session_id: str) -> List[Dict[str, Any]]:
    """Get action history from Redis"""
    try:
        actions_key = f"actions:{session_id}"
        actions_data = redis_client.lrange(actions_key, 0, -1)
        return [json.loads(action) for action in actions_data]
    except Exception as e:
        print(f"Error getting action history: {e}")
        return []

def undo_action_redis(session_id: str) -> Optional[Dict[str, Any]]:
    """Undo last action from Redis"""
    try:
        actions_key = f"actions:{session_id}"
        # Remove and return the first action (most recent)
        action_data = redis_client.lpop(actions_key)
        if action_data:
            return json.loads(action_data)
        return None
    except Exception as e:
        print(f"Error undoing action: {e}")
        return None

def redo_action_redis(session_id: str, action: Dict[str, Any]) -> bool:
    """Redo action by adding it back to Redis"""
    try:
        actions_key = f"actions:{session_id}"
        action_data = json.dumps({
            **action,
            "timestamp": datetime.now().isoformat()
        })
        redis_client.lpush(actions_key, action_data)
        # Keep only last 5 actions
        redis_client.ltrim(actions_key, 0, 4)
        return True
    except Exception as e:
        print(f"Error redoing action: {e}")
        return False
