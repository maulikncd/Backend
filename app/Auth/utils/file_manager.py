"""
File Manager Utilities for Project File Operations
Handles saving blueprints, code, and website files to project folders
"""

import json
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime

from sqlalchemy import text
from app.Auth.db.session import SessionLocal

from app.Auth.core.config import get_settings


def _resolve_sqlite_path(database_url: str) -> str:
    """Convert sqlite database URL to filesystem path."""
    """Convert sqlite database URL to filesystem path."""
    if not database_url.startswith("sqlite"):
        return None

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

# Backend path for relative path resolution
BACKEND_PATH = Path(__file__).parent.parent.parent.parent
PROJECTS_FOLDER = BACKEND_PATH / "projects"


def get_project_from_session(session_id: str, user_id: int, db=None) -> Optional[Dict[str, Any]]:
    """
    Get project information from session_id and user_id.
    
    Looks up the metadata table to find associated project_id,
    then fetches full project details from projects table.
    """
    try:
        user_id_int = int(user_id) if isinstance(user_id, str) else user_id
        
        # Use provided db session or create a new one
        should_close = False
        if db is None:
            db = SessionLocal()
            should_close = True
            
        try:
            # First, find project_id from metadata table using session_id
            # Using raw SQL since Metadata model might not be available
            metadata_query = text("""
                SELECT project_id FROM metadata 
                WHERE session_id = :session_id AND user_id = :user_id
                ORDER BY created_at DESC LIMIT 1
            """)
            result = db.execute(metadata_query, {"session_id": session_id, "user_id": user_id_int})
            metadata_row = result.fetchone()
            
            if not metadata_row:
                print(f"[file_manager] No metadata found for session {session_id}")
                return None
            
            project_id = metadata_row[0]
            
            # Now fetch project details
            project_query = text("""
                SELECT project_id, user_id, project_name, folder_path, created_at
                FROM projects
                WHERE project_id = :project_id AND user_id = :user_id
            """)
            result = db.execute(project_query, {"project_id": project_id, "user_id": user_id_int})
            project_row = result.fetchone()
            
            if not project_row:
                print(f"[file_manager] Project {project_id} not found")
                return None
            
            # Unpack based on query order
            # project_id, user_id, project_name, folder_path, created_at
            p_id, owner_id, p_name, f_path, c_at = project_row
            
            # Determine folder path
            if f_path:
                project_folder = Path(f_path)
            else:
                project_folder = PROJECTS_FOLDER / f"{owner_id}_{p_id}_{p_name}"
            
            return {
                "project_id": p_id,
                "user_id": owner_id,
                "project_name": p_name,
                "folder_path": str(project_folder),
                "created_at": c_at
            }
            
        finally:
            if should_close:
                db.close()
            
    except Exception as e:
        print(f"[file_manager] Error getting project: {e}")
        return None


def save_blueprint_to_file(project: Dict[str, Any], blueprint: Dict[str, Any], create_backup: bool = True) -> Dict[str, Any]:
    """
    Save blueprint JSON to project's Blueprint folder.
    
    Args:
        project: Project dict with folder_path
        blueprint: Blueprint JSON data
        create_backup: If True, creates timestamped backup (default True)
        
    Returns:
        Dict with save status and file path
    """
    try:
        project_folder = Path(project["folder_path"])
        blueprint_folder = project_folder / "Blueprint"
        blueprint_folder.mkdir(parents=True, exist_ok=True)
        
        # Always save as latest.json for easy access
        latest_file = blueprint_folder / "latest.json"
        with open(latest_file, 'w', encoding='utf-8') as f:
            json.dump(blueprint, f, indent=2, ensure_ascii=False)
        
        blueprint_file = latest_file  # Default to latest
        
        # Only create timestamped backup if requested
        if create_backup:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            blueprint_file = blueprint_folder / f"blueprint_{timestamp}.json"
            
            with open(blueprint_file, 'w', encoding='utf-8') as f:
                json.dump(blueprint, f, indent=2, ensure_ascii=False)
            
            print(f"[file_manager] 💾 Blueprint saved to {blueprint_file}")
            
            # Cleanup: Keep only last 5 timestamped backups
            _cleanup_old_blueprints(blueprint_folder, keep_count=5)
        
        return {
            "success": True,
            "file_path": str(blueprint_file),
            "latest_path": str(latest_file),
            "blueprint_folder": str(blueprint_folder)
        }
        
    except Exception as e:
        print(f"[file_manager] Error saving blueprint: {e}")
        return {
            "success": False,
            "error": str(e)
        }


def _cleanup_old_blueprints(blueprint_folder: Path, keep_count: int = 5):
    """
    Remove old blueprint backup files, keeping only the most recent ones.
    
    Args:
        blueprint_folder: Path to Blueprint folder
        keep_count: Number of recent backups to keep
    """
    try:
        # Find all timestamped blueprint files (not latest.json)
        backup_files = sorted(
            [f for f in blueprint_folder.glob("blueprint_*.json")],
            key=lambda x: x.stat().st_mtime,
            reverse=True  # Newest first
        )
        
        # Delete files beyond keep_count
        files_to_delete = backup_files[keep_count:]
        for old_file in files_to_delete:
            old_file.unlink()
            print(f"[file_manager] 🗑️ Deleted old backup: {old_file.name}")
            
    except Exception as e:
        print(f"[file_manager] Error cleaning up old blueprints: {e}")


def save_website_files(project: Dict[str, Any], pages: Dict[str, str]) -> Dict[str, Any]:
    """
    Save generated HTML files to project's Code folder.
    
    Args:
        project: Project dict with folder_path
        pages: Dict of filename -> HTML content (e.g., {"index.html": "<html>..."})
        
    Returns:
        Dict with save status, code_folder, and list of saved files
    """
    try:
        project_folder = Path(project["folder_path"])
        code_folder = project_folder / "Code"
        code_folder.mkdir(parents=True, exist_ok=True)
        
        saved_files = []
        
        for filename, html_content in pages.items():
            # Ensure filename has .html extension
            if not filename.endswith('.html'):
                filename = f"{filename}.html"
            
            file_path = code_folder / filename
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            saved_files.append(str(file_path))
            print(f"[file_manager] 📄 Saved {filename}")
        
        print(f"[file_manager] ✅ Saved {len(saved_files)} files to {code_folder}")
        
        return {
            "success": True,
            "code_folder": str(code_folder),
            "saved_files": saved_files,
            "saved_count": len(saved_files)
        }
        
    except Exception as e:
        print(f"[file_manager] Error saving website files: {e}")
        return {
            "success": False,
            "code_folder": None,
            "saved_files": [],
            "saved_count": 0,
            "error": str(e)
        }


def get_latest_blueprint(project: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Get latest blueprint from project's Blueprint folder.
    
    Args:
        project: Project dict with folder_path
        
    Returns:
        Blueprint JSON or None
    """
    try:
        project_folder = Path(project["folder_path"])
        latest_file = project_folder / "Blueprint" / "latest.json"
        
        if latest_file.exists():
            with open(latest_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return None
        
    except Exception as e:
        print(f"[file_manager] Error reading blueprint: {e}")
        return None


def get_website_files(project: Dict[str, Any]) -> Dict[str, str]:
    """
    Get all HTML files from project's Code folder.
    
    Args:
        project: Project dict with folder_path
        
    Returns:
        Dict of filename -> HTML content
    """
    try:
        project_folder = Path(project["folder_path"])
        code_folder = project_folder / "Code"
        
        if not code_folder.exists():
            return {}
        
        pages = {}
        for html_file in code_folder.glob("*.html"):
            with open(html_file, 'r', encoding='utf-8') as f:
                pages[html_file.name] = f.read()
        
        return pages
        
    except Exception as e:
        print(f"[file_manager] Error reading website files: {e}")
        return {}


def ensure_project_folders(project: Dict[str, Any]) -> bool:
    """
    Ensure all required project folders exist.
    
    Creates: Metadata/, Blueprint/, Code/, Assets/
    
    Args:
        project: Project dict with folder_path
        
    Returns:
        True if successful
    """
    try:
        project_folder = Path(project["folder_path"])
        
        folders = ["Metadata", "Blueprint", "Code", "Assets"]
        for folder in folders:
            (project_folder / folder).mkdir(parents=True, exist_ok=True)
        
        print(f"[file_manager] 📁 Ensured project folders exist")
        return True
        
    except Exception as e:
        print(f"[file_manager] Error creating folders: {e}")
        return False


def save_asset(project: Dict[str, Any], asset_name: str, asset_data: bytes) -> Optional[str]:
    """
    Save an asset (image, css, js) to project's Assets folder.
    
    Args:
        project: Project dict with folder_path
        asset_name: Filename for the asset
        asset_data: Binary data of the asset
        
    Returns:
        Path to saved asset or None
    """
    try:
        project_folder = Path(project["folder_path"])
        assets_folder = project_folder / "Assets"
        assets_folder.mkdir(parents=True, exist_ok=True)
        
        asset_path = assets_folder / asset_name
        
        with open(asset_path, 'wb') as f:
            f.write(asset_data)
        
        return str(asset_path)
        
    except Exception as e:
        print(f"[file_manager] Error saving asset: {e}")
        return None
