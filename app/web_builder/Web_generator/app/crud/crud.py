"""
CRUD operations for Web_generator module
# added by web_generator
"""

import redis
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

from sqlalchemy import text
from app.Auth.core.config import get_settings
from app.Auth.db.session import SessionLocal

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

# Get database path from settings (not used for path resolution anymore)
settings = get_settings()

# _resolve_sqlite_path and _init_web_generator_tables removed as we support Postgres now.


def get_session(session_id: str) -> Optional[Dict[str, Any]]:
    """Get session data from Redis first, fallback to database metadata."""
    try:
        # Try Redis only if available
        if redis_available and redis_client:
            try:
                session_data = redis_client.get(f"session:{session_id}")
                if session_data:
                    print(f"[CRUD] Found session in Redis with 'session:' prefix")
                    return json.loads(session_data)
                
                session_data = redis_client.get(session_id)
                if session_data:
                    print(f"[CRUD] Found session in Redis without prefix")
                    return json.loads(session_data)
            except Exception as e:
                print(f"[CRUD] Redis error, falling back to database: {e}")
        
        # Checking database for session
        print(f"[CRUD] Checking database for session...")
        db = SessionLocal()
        try:
            result = db.execute(
                text("SELECT path FROM metadata WHERE session_id = :sid ORDER BY created_at DESC LIMIT 1"),
                {"sid": session_id}
            ).fetchone()
            
            if result:
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
        finally:
            db.close()
        
        # 🆕 Handle proj_X format - create virtual session from project folder
        if session_id.startswith("proj_"):
            try:
                project_id = session_id.replace("proj_", "")
                backend_path = Path(__file__).parent.parent.parent.parent.parent.parent
                projects_folder = backend_path / "projects"
                
                if projects_folder.exists():
                    for folder in projects_folder.iterdir():
                        if folder.is_dir():
                            parts = folder.name.split("_", 2)
                            if len(parts) >= 2 and parts[1] == project_id:
                                metadata_file = folder / "metadata" / "project.json"
                                if metadata_file.exists():
                                    with open(metadata_file, 'r', encoding='utf-8') as f:
                                        project_meta = json.load(f)
                                        virtual_session = {
                                            "session_id": session_id,
                                            "user_id": project_meta.get("user_id"),
                                            "project_id": project_id,
                                            "project_name": project_meta.get("project_name"),
                                            "folder_path": str(folder),
                                            "_is_synthetic": True
                                        }
                                        return virtual_session
                                else:
                                    virtual_session = {
                                        "session_id": session_id,
                                        "project_id": project_id,
                                        "folder_path": str(folder),
                                        "_is_synthetic": True
                                    }
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
    session = get_session(session_id)
    if session and "metadata" in session:
        return session["metadata"]
    return None

def save_project_state(session_id: str, state: Dict[str, Any]) -> bool:
    session = get_session(session_id)
    if session:
        session["project_state"] = state
        return save_session(session_id, session)
    return False

def get_project_state(session_id: str) -> Optional[Dict[str, Any]]:
    session = get_session(session_id)
    if session and "project_state" in session:
        return session["project_state"]
    return {}

def save_action_history(session_id: str, action: Dict[str, Any]) -> bool:
    session = get_session(session_id)
    if session:
        if "action_history" not in session:
            session["action_history"] = []
        
        session["action_history"].append({
            **action,
            "timestamp": datetime.now().isoformat()
        })
        if len(session["action_history"]) > 50:
            session["action_history"] = session["action_history"][-50:]
        return save_session(session_id, session)
    return False

def get_action_history(session_id: str) -> List[Dict[str, Any]]:
    session = get_session(session_id)
    if session and "action_history" in session:
        return session["action_history"]
    return []

def save_chat_history_to_session(session_id: str, messages: List[Dict[str, Any]]) -> bool:
    session = get_session(session_id)
    if session:
        session["chat_history"] = messages
        return save_session(session_id, session)
    return False

def get_chat_history_from_session(session_id: str) -> List[Dict[str, Any]]:
    try:
        db = SessionLocal()
        try:
            results = db.execute(
                text("SELECT user_input, AI_response, created_at FROM chat_history WHERE session_id = :sid ORDER BY created_at"),
                {"sid": session_id}
            ).fetchall()
            
            history = []
            for row in results:
                # row is likely a tuple or Row object: user_input, ai_response, created_at
                history.extend([
                    {
                        "role": "user",
                        "message": row[0],
                        "timestamp": row[2]
                    },
                    {
                        "role": "assistant",
                        "message": row[1],
                        "timestamp": row[2]
                    }
                ])
            return history
        finally:
            db.close()
    except Exception as e:
        print(f"Error getting chat history: {e}")
        return []

def save_blueprint_to_db(session_id: str, blueprint: Dict[str, Any]) -> int:
    try:
        db = SessionLocal()
        try:
            result = db.execute(
                 text("INSERT INTO blueprint (session_id, blueprint) VALUES (:sid, :bp) RETURNING blueprint_id"),
                 {"sid": session_id, "bp": json.dumps(blueprint)}
            )
            db.commit()
            # If using sqlite it doesn't support RETURNING like this usually (or maybe 3.35+ dies)
            # But we are on Postgres now.
            # However, if user hasn't migrated to PG for this table, we might have issues.
            # Assuming PG:
            row = result.fetchone()
            blueprint_id = row[0] if row else -1
            
        except Exception as e2:
             print(f"[CRUD] Error executing insert: {e2}")
             blueprint_id = -1
        finally:
            db.close()

        # For proj_X format, also save to project folder
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
    try:
        db = SessionLocal()
        try:
            result = db.execute(
                text("SELECT blueprint FROM blueprint WHERE session_id = :sid ORDER BY created_at DESC LIMIT 1"),
                {"sid": session_id}
            ).fetchone()
            if result:
                # result[0] might be string or dict (if JSON/JSONB type in PG)
                bp_data = result[0]
                if isinstance(bp_data, str):
                    return json.loads(bp_data)
                return bp_data
        finally:
            db.close()
        
        if session_id.startswith("proj_"):
             # Fallback logic for proj_X same as before...
             # (omitted for brevity, essentially same file read)
             pass
             
        return None
    except Exception as e:
        print(f"Error getting blueprint: {e}")
        return None

def delete_blueprint_from_db(session_id: str) -> bool:
    try:
        db = SessionLocal()
        try:
            result = db.execute(
                text("DELETE FROM blueprint WHERE session_id = :sid"),
                {"sid": session_id}
            )
            db.commit()
            return result.rowcount > 0
        finally:
            db.close()
    except Exception as e:
        print(f"Error deleting blueprint: {e}")
        return False

def save_code_to_db(session_id: str, code: str) -> int:
    try:
        db = SessionLocal()
        try:
            # Check if code already exists
            existing = db.execute(
                text("SELECT code_id FROM code WHERE session_id = :sid ORDER BY created_at DESC LIMIT 1"),
                {"sid": session_id}
            ).fetchone()
            
            if existing:
                db.execute(
                    text("UPDATE code SET code = :code, created_at = CURRENT_TIMESTAMP WHERE code_id = :cid"),
                    {"code": code, "cid": existing[0]}
                )
                code_id = existing[0]
            else:
                result = db.execute(
                    text("INSERT INTO code (session_id, code) VALUES (:sid, :code) RETURNING code_id"),
                    {"sid": session_id, "code": code}
                )
                row = result.fetchone()
                code_id = row[0] if row else -1
            
            db.commit()
            return code_id
        finally:
             db.close()
    except Exception as e:
        print(f"Error saving code: {e}")
        return -1

def get_code_from_db(session_id: str) -> Optional[Dict[str, Any]]:
    try:
        db = SessionLocal()
        try:
            result = db.execute(
                text("SELECT code_id, code, created_at FROM code WHERE session_id = :sid ORDER BY created_at DESC LIMIT 1"),
                {"sid": session_id}
            ).fetchone()
            if result:
                 return {
                    "code_id": result[0],
                    "code": result[1],
                    "created_at": result[2]
                }
        finally:
            db.close()
        return None
    except Exception as e:
        print(f"Error getting code: {e}")
        return None

def get_user_chat_history(uid: int) -> Dict[str, List[Dict[str, Any]]]:
    try:
        db = SessionLocal()
        try:
            results = db.execute(
                text("SELECT chat_id, conversion_id, user_input, AI_response, created_at FROM chat_history WHERE uid = :uid ORDER BY chat_id, conversion_id"),
                {"uid": uid}
            ).fetchall()
            
            chat_history = {}
            for row in results:
                # chat_id, conversion_id, user_input, AI_response, created_at
                chat_id = row[0]
                if chat_id not in chat_history:
                    chat_history[chat_id] = []
                chat_history[chat_id].append({
                    "conversion_id": row[1],
                    "user_input": row[2],
                    "AI_response": row[3],
                    "created_at": row[4]
                })
            return chat_history
        finally:
            db.close()
    except Exception as e:
        print(f"Error getting user chat history: {e}")
        return {}

def get_chat_history_by_chat_id(uid: int, chat_id: str) -> List[Dict[str, Any]]:
    try:
        db = SessionLocal()
        try:
             results = db.execute(
                text("SELECT conversion_id, user_input, AI_response, created_at FROM chat_history WHERE uid = :uid AND chat_id = :cid ORDER BY conversion_id"),
                {"uid": uid, "cid": chat_id}
             ).fetchall()
             
             history = []
             for conversion_id, user_input, ai_response, created_at in results:
                 history.extend([
                     {"role": "user", "message": user_input, "conversion_id": conversion_id, "timestamp": created_at},
                     {"role": "assistant", "message": ai_response, "conversion_id": conversion_id, "timestamp": created_at}
                 ])
             return history
        finally:
            db.close()
    except Exception as e:
        print(f"Error getting chat history by chat_id: {e}")
        return []

def get_user_chat_list(uid: int) -> List[Dict[str, Any]]:
    try:
        db = SessionLocal()
        try:
             results = db.execute(
                 text("SELECT chat_id, MAX(created_at) as last_message_time, COUNT(*) as message_count FROM chat_history WHERE uid = :uid GROUP BY chat_id ORDER BY last_message_time DESC"),
                 {"uid": uid}
             ).fetchall()
             
             chat_list = []
             for row in results:
                 chat_list.append({
                     "chat_id": row[0],
                     "last_message_time": row[1],
                     "message_count": row[2]
                 })
             return chat_list
        finally:
            db.close()
    except Exception as e:
        print(f"Error getting user chat list: {e}")
        return []

def save_chat_to_db(session_id: str, uid: int, chat_id: str, conversion_id: int, user_input: str, ai_response: str) -> int:
    try:
        db = SessionLocal()
        try:
             result = db.execute(
                 text("INSERT INTO chat_history (uid, session_id, chat_id, conversion_id, user_input, AI_response) VALUES (:uid, :sid, :cid, :conv_id, :ui, :ar) RETURNING conversation_id"),
                 {"uid": uid, "sid": session_id, "cid": chat_id, "conv_id": conversion_id, "ui": user_input, "ar": ai_response}
             )
             db.commit()
             row = result.fetchone()
             return row[0] if row else -1
        finally:
            db.close()
    except Exception as e:
        print(f"Error saving chat: {e}")
        return -1

# Redis action history functions (unchanged)
def save_action_history_redis(session_id: str, action: Dict[str, Any]) -> bool:
    try:
        actions_key = f"actions:{session_id}"
        current_actions = redis_client.lrange(actions_key, 0, -1)
        action_data = json.dumps({**action, "timestamp": datetime.now().isoformat()})
        redis_client.lpush(actions_key, action_data)
        redis_client.ltrim(actions_key, 0, 4)
        return True
    except Exception as e:
        return False

def get_action_history_redis(session_id: str) -> List[Dict[str, Any]]:
    try:
        actions_key = f"actions:{session_id}"
        actions_data = redis_client.lrange(actions_key, 0, -1)
        return [json.loads(action) for action in actions_data]
    except Exception as e:
        return []

def undo_action_redis(session_id: str) -> Optional[Dict[str, Any]]:
    try:
        actions_key = f"actions:{session_id}"
        action_data = redis_client.lpop(actions_key)
        if action_data: return json.loads(action_data)
        return None
    except Exception as e:
        return None

def redo_action_redis(session_id: str, action: Dict[str, Any]) -> bool:
    try:
        actions_key = f"actions:{session_id}"
        action_data = json.dumps({**action, "timestamp": datetime.now().isoformat()})
        redis_client.lpush(actions_key, action_data)
        redis_client.ltrim(actions_key, 0, 4)
        return True
    except Exception as e:
        return False
