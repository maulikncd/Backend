import json
from pathlib import Path

import redis
from sqlalchemy import text
from app.Auth.core.config import get_settings
from app.Auth.db.session import SessionLocal
from app.Auth.models.metadata import Metadata
from app.Auth.models.project import Project

# Redis configuration
settings = get_settings()
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

def get_redis():
    return redis_client


# Removed _resolve_sqlite_path and _init_metadata_db as they are sqlite specific.
# Tables should be created by alembic or main init logic.


def save_session(session_id: str, data: dict):
    """Save session data to Redis"""
    redis_client.set(session_id, json.dumps(data))


def get_session(session_id: str):
    """Get session data from Redis"""
    data = redis_client.get(session_id)
    return json.loads(data) if data else None


def delete_session(session_id: str):
    """Delete a session from Redis."""
    redis_client.delete(session_id)


def save_metadata(metadata: dict, user_id: str, username: str, project_id: int, session_id: str):
    """
    Persist metadata JSON inside the existing project directory for the user.

    Metadata files are stored under an existing project folder (created via the
    project management flow) in a Metadata/ subdirectory. If the project does
    not exist or does not belong to the user, an error is raised.
    """
    backend_path = Path(__file__).parent.parent.parent.parent.parent.parent
    projects_folder = backend_path / "projects"

    try:
        user_id_int = int(user_id)
    except (TypeError, ValueError):
        raise ValueError("Invalid user identifier provided for metadata storage.")

    # Fetch project information to validate ownership and locate folder
    # Fetch project information to validate ownership and locate folder
    db = SessionLocal()
    try:
        project_row = db.execute(
            text("SELECT folder_path, user_id, project_name FROM projects WHERE project_id = :pid"),
            {"pid": project_id}
        ).fetchone()

        if not project_row:
            raise ValueError("Project not found.")

        folder_path, owner_user_id, project_name = project_row
        if owner_user_id != user_id_int:
            raise PermissionError("Project does not belong to the authenticated user.")

        if folder_path:
            project_folder = Path(folder_path)
        else:
            project_folder = projects_folder / f"{owner_user_id}_{project_id}_{project_name}"

        if not project_folder.exists():
            raise FileNotFoundError(f"Project folder not found on disk at {project_folder}")

        metadata_folder = project_folder / "Metadata"
        metadata_folder.mkdir(parents=True, exist_ok=True)

        metadata_filename = f"metadata_{session_id}.json"
        metadata_file_path = metadata_folder / metadata_filename

        with open(metadata_file_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        try:
            relative_path = metadata_file_path.relative_to(backend_path)
        except ValueError:
            relative_path = metadata_file_path

        # Insert metadata record
        new_metadata = Metadata(
            session_id=session_id,
            project_id=project_id,
            user_id=user_id_int,
            path=str(relative_path)
        )
        db.add(new_metadata)
        db.commit()
        db.refresh(new_metadata)
        
        return {
            "metadata_id": new_metadata.metadata_id, 
            "created_at": new_metadata.created_at, 
            "path": new_metadata.path
        }

    finally:
        db.close()


def save_answers(session_id: str, answers: dict):
    """Save user answers to Redis"""
    session = get_session(session_id)
    if session:
        session["answers"] = answers
        save_session(session_id, session)


def save_color_palettes(session_id: str, palettes: list):
    """Save color palettes to Redis"""
    session = get_session(session_id)
    if session:
        session["palettes"] = palettes
        save_session(session_id, session)


def save_selected_palette(session_id: str, selected_palette: dict):
    """Save selected palette to Redis"""
    session = get_session(session_id)
    if session:
        session["selected_palette"] = selected_palette
        save_session(session_id, session)


def save_features(session_id: str, features: list):
    """Save features to Redis"""
    session = get_session(session_id)
    if session:
        session["features"] = features
        save_session(session_id, session)


def save_selected_features(session_id: str, selected_features: list):
    """Save selected features to Redis"""
    session = get_session(session_id)
    if session:
        session["selected_features"] = selected_features
        save_session(session_id, session)
