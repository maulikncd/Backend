"""
Version Control CRUD operations for Draft Management
Handles undo/redo with max 5 versions
# added by web_generator
"""

import redis
import json
import sqlite3
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path

from app.Auth.core.config import get_settings

# Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Fix for Windows Redis "MISCONF" error
try:
    redis_client.config_set('stop-writes-on-bgsave-error', 'no')
except Exception as e:
    print(f"Warning: Could not set Redis config: {e}")


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


# Get database path
settings = get_settings()
AUTH_DB_PATH = _resolve_sqlite_path(settings.database_url)

# Maximum versions to keep
MAX_VERSIONS = 5


def _init_version_tables():
    """Ensure the draft versions table exists."""
    if AUTH_DB_PATH != ":memory:":
        Path(AUTH_DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    
    with sqlite3.connect(AUTH_DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS draft_versions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                version_number INTEGER NOT NULL,
                code TEXT NOT NULL,
                file_path TEXT,
                change_description TEXT,
                is_current BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(session_id, version_number)
            )
            """
        )
        # Create index for faster lookups
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_draft_session 
            ON draft_versions(session_id, version_number DESC)
            """
        )


# Initialize tables on import
_init_version_tables()


# ============================================================
# REDIS KEY HELPERS
# ============================================================

def _get_versions_key(session_id: str) -> str:
    """Get Redis key for version list."""
    return f"draft:{session_id}:versions"


def _get_index_key(session_id: str) -> str:
    """Get Redis key for current version index."""
    return f"draft:{session_id}:current_index"


def _get_redo_key(session_id: str) -> str:
    """Get Redis key for redo stack."""
    return f"draft:{session_id}:redo_stack"


# ============================================================
# DRAFT VERSION OPERATIONS
# ============================================================

def save_draft_version(
    session_id: str, 
    code: str, 
    change_description: str = "",
    file_path: str = None
) -> Dict[str, Any]:
    """
    Save a new draft version.
    - Clears redo stack (new change invalidates redo)
    - Keeps only last MAX_VERSIONS drafts
    - Saves to both Redis (fast) and SQLite (backup)
    
    Returns:
        Dict with version info and can_undo/can_redo flags
    """
    try:
        versions_key = _get_versions_key(session_id)
        index_key = _get_index_key(session_id)
        redo_key = _get_redo_key(session_id)
        
        # Clear redo stack (new change invalidates redo)
        redis_client.delete(redo_key)
        
        # Get current versions
        current_versions = redis_client.lrange(versions_key, 0, -1)
        
        # Calculate new version number
        if current_versions:
            last_version = json.loads(current_versions[0])
            new_version_num = last_version.get("version_number", 0) + 1
        else:
            new_version_num = 1
        
        # Create version data
        version_data = {
            "version_number": new_version_num,
            "code": code,
            "file_path": file_path,
            "change_description": change_description,
            "timestamp": datetime.now().isoformat()
        }
        
        # Add to Redis (front of list = newest)
        redis_client.lpush(versions_key, json.dumps(version_data))
        
        # Trim to MAX_VERSIONS
        redis_client.ltrim(versions_key, 0, MAX_VERSIONS - 1)
        
        # Set current index to 0 (newest)
        redis_client.set(index_key, "0")
        
        # Backup to SQLite
        _backup_to_sqlite(session_id, version_data)
        
        # Get updated count
        version_count = redis_client.llen(versions_key)
        
        return {
            "success": True,
            "version": new_version_num,
            "can_undo": version_count > 1,
            "can_redo": False,
            "message": f"Draft version {new_version_num} saved"
        }
        
    except Exception as e:
        print(f"[version_control] Error saving draft: {e}")
        return {
            "success": False,
            "error": str(e)
        }


def get_current_draft(session_id: str) -> Dict[str, Any]:
    """
    Get the current draft version (at current index).
    
    Returns:
        Dict with code, version info, and undo/redo flags
    """
    try:
        versions_key = _get_versions_key(session_id)
        index_key = _get_index_key(session_id)
        redo_key = _get_redo_key(session_id)
        
        # Get current index
        current_index = redis_client.get(index_key)
        if current_index is None:
            # No drafts, try to get from saved code
            return _get_saved_code_fallback(session_id)
        
        current_index = int(current_index)
        
        # Get version at current index
        version_data = redis_client.lindex(versions_key, current_index)
        
        if not version_data:
            return _get_saved_code_fallback(session_id)
        
        version = json.loads(version_data)
        version_count = redis_client.llen(versions_key)
        redo_count = redis_client.llen(redo_key)
        
        return {
            "success": True,
            "code": version.get("code", ""),
            "version": version.get("version_number", 1),
            "file_path": version.get("file_path"),
            "change_description": version.get("change_description", ""),
            "source": "draft",
            "can_undo": current_index < version_count - 1,
            "can_redo": redo_count > 0
        }
        
    except Exception as e:
        print(f"[version_control] Error getting current draft: {e}")
        return _get_saved_code_fallback(session_id)


def undo_draft(session_id: str) -> Dict[str, Any]:
    """
    Undo to previous draft version.
    - Moves current version to redo stack
    - Points to previous version
    
    Returns:
        Dict with previous version's code and flags
    """
    try:
        versions_key = _get_versions_key(session_id)
        index_key = _get_index_key(session_id)
        redo_key = _get_redo_key(session_id)
        
        # Get current index
        current_index = redis_client.get(index_key)
        if current_index is None:
            return {"success": False, "error": "No versions to undo"}
        
        current_index = int(current_index)
        version_count = redis_client.llen(versions_key)
        
        # Check if we can undo
        if current_index >= version_count - 1:
            return {"success": False, "error": "Already at oldest version"}
        
        # Get current version before moving
        current_version = redis_client.lindex(versions_key, current_index)
        
        # Push current to redo stack
        if current_version:
            redis_client.lpush(redo_key, current_version)
            # Keep redo stack limited
            redis_client.ltrim(redo_key, 0, MAX_VERSIONS - 1)
        
        # Move index to previous (older) version
        new_index = current_index + 1
        redis_client.set(index_key, str(new_index))
        
        # Get the previous version
        prev_version_data = redis_client.lindex(versions_key, new_index)
        
        if not prev_version_data:
            return {"success": False, "error": "No previous version found"}
        
        prev_version = json.loads(prev_version_data)
        redo_count = redis_client.llen(redo_key)
        
        return {
            "success": True,
            "code": prev_version.get("code", ""),
            "version": prev_version.get("version_number", 1),
            "file_path": prev_version.get("file_path"),
            "can_undo": new_index < version_count - 1,
            "can_redo": redo_count > 0,
            "message": "Undo successful"
        }
        
    except Exception as e:
        print(f"[version_control] Error undoing: {e}")
        return {"success": False, "error": str(e)}


def redo_draft(session_id: str) -> Dict[str, Any]:
    """
    Redo to next (undone) draft version.
    - Pops from redo stack
    - Moves index back to newer version
    
    Returns:
        Dict with redo version's code and flags
    """
    try:
        versions_key = _get_versions_key(session_id)
        index_key = _get_index_key(session_id)
        redo_key = _get_redo_key(session_id)
        
        # Check if redo stack has items
        redo_count = redis_client.llen(redo_key)
        if redo_count == 0:
            return {"success": False, "error": "Nothing to redo"}
        
        # Pop from redo stack
        redo_version = redis_client.lpop(redo_key)
        
        if not redo_version:
            return {"success": False, "error": "Redo stack empty"}
        
        # Get current index and move back
        current_index = redis_client.get(index_key)
        if current_index is None:
            current_index = 0
        else:
            current_index = int(current_index)
        
        # Move index to newer version
        new_index = max(0, current_index - 1)
        redis_client.set(index_key, str(new_index))
        
        version = json.loads(redo_version)
        version_count = redis_client.llen(versions_key)
        new_redo_count = redis_client.llen(redo_key)
        
        return {
            "success": True,
            "code": version.get("code", ""),
            "version": version.get("version_number", 1),
            "file_path": version.get("file_path"),
            "can_undo": new_index < version_count - 1,
            "can_redo": new_redo_count > 0,
            "message": "Redo successful"
        }
        
    except Exception as e:
        print(f"[version_control] Error redoing: {e}")
        return {"success": False, "error": str(e)}


def finalize_and_clear_drafts(session_id: str, final_code: str, file_path: str = None) -> Dict[str, Any]:
    """
    Finalize the code (save to main code table) and clear all drafts.
    Called when user clicks "Save" button.
    
    Returns:
        Dict with save status
    """
    try:
        # Import here to avoid circular import
        from app.web_builder.Web_generator.app.crud.crud import save_code_to_db
        
        # Save final code to main code table
        code_id = save_code_to_db(session_id, final_code)
        
        if code_id == -1:
            return {"success": False, "error": "Failed to save final code"}
        
        # Clear all Redis keys for this session's drafts
        versions_key = _get_versions_key(session_id)
        index_key = _get_index_key(session_id)
        redo_key = _get_redo_key(session_id)
        
        redis_client.delete(versions_key)
        redis_client.delete(index_key)
        redis_client.delete(redo_key)
        
        # Clear SQLite draft versions
        _clear_sqlite_drafts(session_id)
        
        return {
            "success": True,
            "code_id": code_id,
            "file_path": file_path,
            "drafts_cleared": True,
            "message": "Code saved and drafts cleared"
        }
        
    except Exception as e:
        print(f"[version_control] Error finalizing: {e}")
        return {"success": False, "error": str(e)}


def get_latest_code(session_id: str) -> Dict[str, Any]:
    """
    Get the latest code for a session.
    Priority:
    1. Current draft (if exists)
    2. Saved code from database
    
    Used by frontend on page reload.
    """
    # First try to get current draft
    draft = get_current_draft(session_id)
    
    if draft.get("success") and draft.get("source") == "draft":
        return draft
    
    # Fallback to saved code
    return _get_saved_code_fallback(session_id)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def _backup_to_sqlite(session_id: str, version_data: Dict[str, Any]) -> bool:
    """Backup draft version to SQLite for crash recovery."""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Mark all existing as not current
            cursor.execute(
                "UPDATE draft_versions SET is_current = FALSE WHERE session_id = ?",
                (session_id,)
            )
            
            # Insert new version
            cursor.execute(
                """
                INSERT OR REPLACE INTO draft_versions 
                (session_id, version_number, code, file_path, change_description, is_current)
                VALUES (?, ?, ?, ?, ?, TRUE)
                """,
                (
                    session_id,
                    version_data.get("version_number", 1),
                    version_data.get("code", ""),
                    version_data.get("file_path"),
                    version_data.get("change_description", "")
                )
            )
            
            # Keep only last MAX_VERSIONS
            cursor.execute(
                """
                DELETE FROM draft_versions 
                WHERE session_id = ? 
                AND id NOT IN (
                    SELECT id FROM draft_versions 
                    WHERE session_id = ? 
                    ORDER BY version_number DESC 
                    LIMIT ?
                )
                """,
                (session_id, session_id, MAX_VERSIONS)
            )
            
            conn.commit()
            return True
            
    except Exception as e:
        print(f"[version_control] SQLite backup error: {e}")
        return False


def _clear_sqlite_drafts(session_id: str) -> bool:
    """Clear all SQLite draft versions for a session."""
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            conn.execute(
                "DELETE FROM draft_versions WHERE session_id = ?",
                (session_id,)
            )
            conn.commit()
            return True
    except Exception as e:
        print(f"[version_control] Error clearing SQLite drafts: {e}")
        return False


def _get_saved_code_fallback(session_id: str) -> Dict[str, Any]:
    """Get saved code from main code table as fallback."""
    try:
        from app.web_builder.Web_generator.app.crud.crud import get_code_from_db
        
        saved_code = get_code_from_db(session_id)
        
        if saved_code:
            return {
                "success": True,
                "code": saved_code.get("code", ""),
                "version": 1,
                "source": "saved",
                "can_undo": False,
                "can_redo": False
            }
        
        return {
            "success": False,
            "error": "No code found",
            "code": "",
            "source": "none",
            "can_undo": False,
            "can_redo": False
        }
        
    except Exception as e:
        print(f"[version_control] Error getting saved code: {e}")
        return {
            "success": False,
            "error": str(e),
            "code": "",
            "source": "none",
            "can_undo": False,
            "can_redo": False
        }


def restore_from_sqlite(session_id: str) -> bool:
    """
    Restore Redis draft versions from SQLite backup.
    Called on server restart or Redis failure.
    """
    try:
        with sqlite3.connect(AUTH_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT version_number, code, file_path, change_description, created_at
                FROM draft_versions 
                WHERE session_id = ? 
                ORDER BY version_number DESC
                LIMIT ?
                """,
                (session_id, MAX_VERSIONS)
            )
            results = cursor.fetchall()
            
            if not results:
                return False
            
            versions_key = _get_versions_key(session_id)
            index_key = _get_index_key(session_id)
            
            # Clear existing Redis data
            redis_client.delete(versions_key)
            
            # Restore versions
            for version_num, code, file_path, description, created_at in results:
                version_data = {
                    "version_number": version_num,
                    "code": code,
                    "file_path": file_path,
                    "change_description": description,
                    "timestamp": created_at
                }
                redis_client.rpush(versions_key, json.dumps(version_data))
            
            # Set index to newest (0)
            redis_client.set(index_key, "0")
            
            return True
            
    except Exception as e:
        print(f"[version_control] Error restoring from SQLite: {e}")
        return False


# ============================================================
# BLUEPRINT VERSION CONTROL (for chatbot service compatibility)
# ============================================================

def save_blueprint_version(session_id: str, blueprint: Dict[str, Any], change_description: str = "") -> Dict[str, Any]:
    """
    Save a blueprint version (wrapper for chatbot service).
    Stores blueprint as JSON string in the draft system.
    """
    blueprint_json = json.dumps(blueprint)
    return save_draft_version(session_id, blueprint_json, change_description, file_path="blueprint.json")


def get_latest_blueprint_version(session_id: str) -> Optional[Dict[str, Any]]:
    """
    Get latest blueprint version (wrapper for chatbot service).
    """
    result = get_current_draft(session_id)
    
    if result.get("success") and result.get("file_path") == "blueprint.json":
        try:
            return json.loads(result.get("code", "{}"))
        except:
            pass
    
    # Fallback to main blueprint
    try:
        from app.web_builder.Web_generator.app.crud.crud import get_blueprint_from_db
        return get_blueprint_from_db(session_id)
    except:
        return None


def save_auto_draft(session_id: str, code: str, description: str = "Auto-saved draft") -> bool:
    """
    Auto-save draft (for crash recovery).
    Called periodically or on significant changes.
    """
    result = save_draft_version(session_id, code, description)
    return result.get("success", False)
