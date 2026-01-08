
import json
import sqlite3
from pathlib import Path

import redis
from app.Auth.core.config import get_settings

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


AUTH_DB_PATH = _resolve_sqlite_path(settings.database_url)


def _init_metadata_db():
    """Ensure the SQLite database and metadata table exist."""
    if AUTH_DB_PATH != ":memory:":
        Path(AUTH_DB_PATH).parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(AUTH_DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS metadata (
                metadata_id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                project_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                path TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


_init_metadata_db()


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
    with sqlite3.connect(AUTH_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT folder_path, user_id, project_name
            FROM projects
            WHERE project_id = ?
            """,
            (project_id,),
        )
        project_row = cursor.fetchone()

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
        raise FileNotFoundError("Project folder not found on disk.")

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

    with sqlite3.connect(AUTH_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO metadata (session_id, project_id, user_id, path)
            VALUES (?, ?, ?, ?)
            """,
            (session_id, project_id, user_id_int, str(relative_path)),
        )
        conn.commit()
        metadata_id = cursor.lastrowid
        cursor.execute(
            """
            SELECT metadata_id, created_at
            FROM metadata
            WHERE metadata_id = ?
            """,
            (metadata_id,),
        )
        result = cursor.fetchone()

    return {"metadata_id": result[0], "created_at": result[1], "path": str(relative_path)}


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
