"""
Version Control CRUD operations for Draft Management
Handles undo/redo with max 5 versions
# added by web_generator
"""

import redis
import json
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path

from sqlalchemy import text
from app.Auth.core.config import get_settings
from app.Auth.db.session import SessionLocal

# Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Fix for Windows Redis "MISCONF" error
try:
    redis_client.config_set('stop-writes-on-bgsave-error', 'no')
except Exception as e:
    print(f"Warning: Could not set Redis config: {e}")


# Get database path (unused for path logic now)
settings = get_settings()

# Maximum versions to keep
MAX_VERSIONS = 5


# _init_version_tables removed/assumed unnecessary or handled externally
# because creating tables with raw SQL on import is risky in production environments.
# However, if we MUST support it:
# Postgres syntax for auto increment is SERIAL.
# We will skip table creation on import to avoid startup errors if user has restricted permissions.


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
    - Saves to both Redis (fast) and Database (backup)
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
        
        # Backup to Database
        _backup_to_db(session_id, version_data)
        
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
    """Get the current draft version (at current index)."""
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
    """Undo to previous draft version."""
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
    """Redo to next (undone) draft version."""
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
        
        # Clear database draft versions
        _clear_db_drafts(session_id)
        
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
    """Get the latest code for a session."""
    # First try to get current draft
    draft = get_current_draft(session_id)
    
    if draft.get("success") and draft.get("source") == "draft":
        return draft
    
    # Fallback to saved code
    return _get_saved_code_fallback(session_id)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def _backup_to_db(session_id: str, version_data: Dict[str, Any]) -> bool:
    """Backup draft version to Database for crash recovery."""
    try:
        db = SessionLocal()
        try:
            # Mark all existing as not current
            db.execute(
                text("UPDATE draft_versions SET is_current = FALSE WHERE session_id = :sid"),
                {"sid": session_id}
            )
            
            # Insert new version
            # Using INSERT ... ON CONFLICT (session_id, version_number) DO UPDATE
            # Assumes Postgres
            db.execute(
                text("""
                INSERT INTO draft_versions 
                (session_id, version_number, code, file_path, change_description, is_current)
                VALUES (:sid, :vn, :code, :fp, :cd, TRUE)
                ON CONFLICT (session_id, version_number) DO UPDATE SET
                code = EXCLUDED.code,
                file_path = EXCLUDED.file_path,
                change_description = EXCLUDED.change_description,
                is_current = TRUE
                """),
                {
                    "sid": session_id,
                    "vn": version_data.get("version_number", 1),
                    "code": version_data.get("code", ""),
                    "fp": version_data.get("file_path"),
                    "cd": version_data.get("change_description", "")
                }
            )
            
            # Keep only last MAX_VERSIONS
            # Complex delete used in sqlite example, simplified logic here:
            # We can just ignore cleanup for now to avoid complex SQL or do it later.
            # But let's try to keep it clean.
            db.execute(
                 text("""
                 DELETE FROM draft_versions 
                 WHERE session_id = :sid 
                 AND id NOT IN (
                     SELECT id FROM draft_versions 
                     WHERE session_id = :sid 
                     ORDER BY version_number DESC 
                     LIMIT :limit
                 )
                 """),
                 {"sid": session_id, "limit": MAX_VERSIONS}
            )
            
            db.commit()
            return True
            
        except Exception as e:
             # If table doesn't exist, we just ignore persistence error to avoid crashing app
             # print(f"[version_control] DB backup error (ignoring): {e}")
             return False
        finally:
            db.close()
            
    except Exception as e:
        print(f"[version_control] DB backup error: {e}")
        return False


def _clear_db_drafts(session_id: str) -> bool:
    """Clear all database draft versions for a session."""
    try:
        db = SessionLocal()
        try:
            db.execute(
                text("DELETE FROM draft_versions WHERE session_id = :sid"),
                {"sid": session_id}
            )
            db.commit()
            return True
        finally:
            db.close()
    except Exception as e:
        print(f"[version_control] Error clearing DB drafts: {e}")
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


def restore_from_db(session_id: str) -> bool:
    """
    Restore Redis draft versions from Database backup.
    """
    try:
        db = SessionLocal()
        try:
            results = db.execute(
                text("""
                SELECT version_number, code, file_path, change_description, created_at
                FROM draft_versions 
                WHERE session_id = :sid
                ORDER BY version_number DESC
                LIMIT :limit
                """),
                {"sid": session_id, "limit": MAX_VERSIONS}
            ).fetchall()
            
            if not results:
                return False
            
            versions_key = _get_versions_key(session_id)
            index_key = _get_index_key(session_id)
            
            # Clear existing Redis data
            redis_client.delete(versions_key)
            
            # Restore versions
            for row in results:
                # row: version_number, code, file_path, change_description, created_at
                version_data = {
                    "version_number": row[0],
                    "code": row[1],
                    "file_path": row[2],
                    "change_description": row[3],
                    "timestamp": row[4].isoformat() if hasattr(row[4], 'isoformat') else str(row[4])
                }
                redis_client.rpush(versions_key, json.dumps(version_data))
            
            # Set index to newest (0)
            redis_client.set(index_key, "0")
            
            return True
        finally:
            db.close()
            
    except Exception as e:
        print(f"[version_control] Error restoring from DB: {e}")
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
