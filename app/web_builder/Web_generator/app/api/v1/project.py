from fastapi import APIRouter, Depends, HTTPException, Body
from typing import List, Optional, Dict, Any
from app.web_builder.Web_generator.app.schemas.schema import *
from app.web_builder.Web_generator.app.schemas.blueprint_schema import MetadataInput
from app.Auth.core.dependencies import get_current_user
from app.Auth.models.user import User
from app.Auth.db.session import get_db
from app.web_builder.Web_generator.app.crud.crud import *
from app.web_builder.Web_generator.app.services.project_service import *
from app.web_builder.Web_generator.app.services.blueprint_service import get_blueprint_service
from sqlalchemy.orm import Session

router = APIRouter()


# ============================================================
# 1️⃣ BLUEPRINT GENERATION ENDPOINTS
# ============================================================

@router.post("/generate-blueprint")
def generate_blueprint_from_session(
    data: BlueprintRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Generate AI-powered blueprint from session metadata.
    
    Uses session_id to fetch metadata from database and generates
    a rich, component-wise blueprint using AI.
    
    If force_regenerate=True, deletes old cached blueprint and regenerates fresh.
    """
    session = get_session(data.session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    # Check user authorization
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session access")
    
    # Delete old blueprint if force regenerate is requested
    if data.force_regenerate:
        try:
            delete_blueprint_from_db(data.session_id)
            print(f"[API] 🗑️ Force regenerate: Deleted old blueprint for {data.session_id}")
        except Exception as e:
            print(f"[API] ⚠️ Could not delete old blueprint: {e}")
    
    # Generate blueprint using BlueprintService
    blueprint_service = get_blueprint_service()
    blueprint = blueprint_service.generate_blueprint_from_session(data.session_id)
    
    if "error" in blueprint:
        raise HTTPException(500, blueprint["error"])
    
    return {"blueprint": blueprint, "status": "generated", "force_regenerated": data.force_regenerate}


@router.post("/generate-blueprint-from-metadata")
def generate_blueprint_from_metadata(
    metadata: Dict[str, Any] = Body(...),
    user: User = Depends(get_current_user)
):
    """
    Generate AI-powered blueprint directly from metadata JSON.
    
    Accepts complete metadata from recommendation team and generates
    a rich, component-wise blueprint with AI-generated content.
    
    Expected metadata format:
    {
        "session_id": "...",
        "user_prompt": "...",
        "business_extracted_data": {...},
        "questionnaire": {"questions": [...]},
        "design": {"selected_palette": {...}},
        "features": [...]
    }
    """
    if not metadata:
        raise HTTPException(400, "Metadata is required")
    
    # Generate blueprint using BlueprintService
    blueprint_service = get_blueprint_service()
    blueprint = blueprint_service.generate_blueprint(metadata)
    
    if "error" in blueprint:
        raise HTTPException(500, blueprint["error"])
    
    return {"blueprint": blueprint, "status": "generated"}


# Legacy endpoint (keeping for backward compatibility)
@router.post("/generate_blueprint")
def generate_blueprint_legacy(
    data: BlueprintRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    [LEGACY] Generate blueprint from session metadata using session_id.
    Use /generate-blueprint instead for AI-powered generation.
    """
    session = get_session(data.session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session")
    
    blueprint = generate_project_blueprint(data.session_id, db)
    return {"blueprint": blueprint}


# ============================================================
# 2️⃣ CODE GENERATION ENDPOINTS
# ============================================================

@router.post("/generate-code")
@router.post("/generate_code")
@router.post("/generate-project")
def generate_project(
    data: GenerateRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Generate multi-page website code from blueprint.
    Saves all HTML files to project's code folder.
    
    🆕 Now checks for cached code first (preserves property changes).
    Use force_regenerate=true to bypass cache and regenerate from Blueprint.
    
    Returns:
        - pages: Dict of filename -> HTML content
        - pages_count: Number of pages generated
        - page_names: List of generated page names
        - code_folder: Path where files were saved
        - saved_files: List of saved file paths
        - from_cache: True if returned cached code (preserves property changes)
    """
    result = generate_code(
        data.session_id, 
        data.blueprint, 
        db, 
        force_regenerate=data.force_regenerate or False
    )
    
    # Handle error case
    if isinstance(result, dict) and "error" in result:
        return {"error": result["error"], "status": "failed"}
    
    return {
        "status": "generated",
        "pages": result.get("pages", {}),
        "main_page": result.get("main_page", ""),
        "pages_count": result.get("pages_count", 0),
        "page_names": result.get("page_names", []),
        "code_folder": result.get("code_folder"),
        "saved_files": result.get("saved_files", []),
        "from_cache": result.get("from_cache", False)
    }


# ============================================================
# 2.5️⃣ PROPERTIES PANEL - BLUEPRINT SYNC ENDPOINTS
# ============================================================

@router.post("/update-property")
def update_blueprint_property(
    data: UpdatePropertyRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update a specific property in the Blueprint.
    Called when user changes a property in PropertiesPanel.
    
    This enables real-time sync between UI edits and Blueprint.
    
    Args:
        session_id: Session identifier
        component_id: Component to update (e.g., "hero", "about")
        field: Field to update (e.g., "title", "description")
        value: New value
        element_info: Optional element context for smart matching
    
    Returns:
        - success: Whether update was successful
        - component: Updated component name
        - field: Updated field name
    """
    from app.web_builder.Web_generator.app.services.chatbot.blueprint_editor import BlueprintEditor
    
    # Get current blueprint
    blueprint = get_blueprint_from_db(data.session_id)
    if not blueprint:
        raise HTTPException(404, "Blueprint not found for this session")
    
    # Create editor and find component
    editor = BlueprintEditor()
    
    # Try to find component by ID or name matching
    component_key = None
    component_id_lower = data.component_id.lower().strip()
    
    # Check components in blueprint
    components = blueprint.get("components", {})
    for key, comp in components.items():
        comp_id = comp.get("id", "").lower()
        comp_name = comp.get("name", "").lower()
        key_lower = key.lower().replace("comp-", "")
        
        if (component_id_lower == comp_id or 
            component_id_lower == comp_name or 
            component_id_lower == key_lower or
            component_id_lower in key_lower):
            component_key = key
            break
    
    if not component_key:
        # Try fuzzy match with element info
        if data.element_info and data.element_info.get("classes"):
            classes = data.element_info["classes"].lower()
            for key in components:
                key_clean = key.replace("comp-", "").lower()
                if key_clean in classes:
                    component_key = key
                    break
    
    if not component_key:
        return {
            "success": False,
            "error": f"Could not find component: {data.component_id}",
            "available_components": list(components.keys())
        }
    
    # Update the property
    field_path = f"props.{data.field}" if not data.field.startswith("props.") else data.field
    
    # Handle special fields
    if data.field in ["text", "title", "content", "description"]:
        # Check if it's a title-like field
        if data.element_info and data.element_info.get("tagName", "").lower() == "h1":
            field_path = "props.title"
        elif data.element_info and data.element_info.get("tagName", "").lower() == "h2":
            field_path = "props.subtitle"
        elif data.element_info and data.element_info.get("tagName", "").lower() == "p":
            field_path = "props.description"
    
    # Use blueprint editor to update
    updated_blueprint, success, message = editor.edit_component(
        blueprint, 
        component_key.replace("comp-", ""), 
        field_path, 
        data.value
    )
    
    if success:
        # Save updated blueprint to DB
        save_blueprint_to_db(data.session_id, updated_blueprint)
        
        # Also save to file if project exists
        session = get_session(data.session_id)
        if session and session.get("user_id") and db:
            try:
                from app.Auth.utils.file_manager import get_project_from_session, save_blueprint_to_file
                project = get_project_from_session(data.session_id, session["user_id"], db)
                if project:
                    save_blueprint_to_file(project, updated_blueprint, create_backup=False)
            except Exception as e:
                print(f"[update-property] Warning: Could not save to file: {e}")
        
        return {
            "success": True,
            "component": component_key,
            "field": data.field,
            "message": message
        }
    
    return {
        "success": False,
        "error": message
    }


@router.post("/apply-changes")
def apply_and_regenerate(
    data: ApplyChangesRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Apply all Blueprint changes and regenerate HTML code.
    Called when user clicks "Apply Changes" in PropertiesPanel.
    
    This:
    1. Saves Blueprint to database
    2. Optionally regenerates HTML from Blueprint
    3. Returns the new HTML content
    
    Returns:
        - success: Whether operation was successful
        - html: Regenerated HTML content (if regenerate_code=true)
        - blueprint_saved: Whether Blueprint was saved
    """
    # Get current blueprint
    blueprint = get_blueprint_from_db(data.session_id)
    if not blueprint:
        raise HTTPException(404, "Blueprint not found")
    
    # Blueprint is already saved during update-property calls
    # But save again to ensure consistency
    save_blueprint_to_db(data.session_id, blueprint)
    
    result = {
        "success": True,
        "blueprint_saved": True
    }
    
    # Regenerate HTML if requested
    if data.regenerate_code:
        # Force regenerate from Blueprint (ignore cached code)
        code_result = generate_code(
            data.session_id, 
            blueprint, 
            db, 
            force_regenerate=True  # Ignore cached code, regenerate fresh
        )
        
        if "error" in code_result:
            result["success"] = False
            result["error"] = code_result["error"]
        else:
            result["html"] = code_result.get("main_page", "")
            result["code_regenerated"] = True
    
    return result


# ============================================================
# 3️⃣ CHAT ENDPOINTS
# ============================================================

@router.post("/chat-message")
def chat_message(
    data: ChatMessageRequest,
    user: User = Depends(get_current_user)
):
    """
    Handle chat messages for AI-powered project assistance.
    
    Uses Gemma 3 12B for cost-effective conversational AI.
    Can modify blueprint based on user requests.
    
    Returns:
        - response: AI message to user
        - actions_taken: List of blueprint modifications made
        - blueprint_updated: Whether blueprint was changed
        - suggestions: Optional improvement suggestions
        - intent: Detected user intent (suggestion/edit/add/remove/general)
    """
    result = process_chat_message(data.session_id, data.message, str(user.user_id))
    
    return {
        "response": result.get("response", ""),
        "actions_taken": result.get("actions_taken", []),
        "blueprint_updated": result.get("blueprint_updated", False),
        "suggestions": result.get("suggestions"),
        "intent": result.get("intent", "general")
    }


@router.get("/chat-suggestions/{session_id}")
def get_chat_suggestions(
    session_id: str,
    user: User = Depends(get_current_user)
):
    """
    Get AI-powered improvement suggestions for the blueprint.
    
    Returns:
        List of suggestions with title, description, component, and priority.
    """
    from app.web_builder.Web_generator.app.services.chatbot import get_chatbot_service
    
    session = get_session(session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session access")
    
    chatbot = get_chatbot_service()
    result = chatbot.get_suggestions(session_id)
    
    if "error" in result:
        raise HTTPException(404, result["error"])
    
    return result


@router.post("/chat-history")
def save_chat_history(
    data: ChatHistoryRequest,
    user: User = Depends(get_current_user)
):
    """
    Save chat history for session.
    """
    result = save_chat_history_to_session(data.session_id, data.messages)
    return {"status": "saved", "message_count": len(data.messages)}


@router.get("/get-history")
def get_chat_history(
    session_id: str,
    user: User = Depends(get_current_user)
):
    """
    Get chat history for session.
    """
    session = get_session(session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session")
    
    history = get_chat_history_from_session(session_id)
    return {"chat_history": history}


# ============================================================
# 4️⃣ DRAFT CODE ENDPOINTS
# ============================================================

@router.post("/draft-code")
def draft_code(
    data: DraftCodeRequest,
    user: User = Depends(get_current_user)
):
    """
    Generate draft code for specific components.
    Saves to version control system with undo/redo support.
    """
    result = generate_draft_code(data.session_id, data.component, data.requirements)
    return result


@router.get("/get-latest-code/{session_id}")
def get_latest_code(
    session_id: str,
    user: User = Depends(get_current_user)
):
    """
    Get latest code for a session (draft or saved).
    Used by frontend on page reload.
    
    Returns:
        - code: The latest code
        - source: "draft" or "saved"
        - version: Current version number
        - can_undo: Whether undo is available
        - can_redo: Whether redo is available
    """
    from app.web_builder.Web_generator.app.crud.version_control import get_latest_code as get_code
    
    session = get_session(session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session access")
    
    result = get_code(session_id)
    return result


# ============================================================
# 5️⃣ CODE MANAGEMENT ENDPOINTS
# ============================================================

@router.post("/save-code")
def save_code(
    data: SaveCodeRequest,
    user: User = Depends(get_current_user)
):
    """
    Save generated code to project.
    Clears all draft versions and saves final code.
    """
    result = save_project_code(data.session_id, data.code, data.file_path)
    
    if isinstance(result, dict):
        return result
    
    return {
        "status": "saved", 
        "file_path": data.file_path,
        "drafts_cleared": True
    }


# ============================================================
# 6️⃣ UNDO/REDO ENDPOINTS
# ============================================================

@router.post("/undo")
def undo_action(
    data: UndoRedoRequest,
    user: User = Depends(get_current_user)
):
    """
    Undo last code change.
    Returns the previous version's code.
    
    Returns:
        - code: Previous version code
        - version: Version number
        - can_undo: Can undo further
        - can_redo: Can redo now
    """
    result = undo_project_action(data.session_id)
    
    if result.get("success"):
        return {
            "status": "undone",
            "code": result.get("code", ""),
            "version": result.get("version", 1),
            "can_undo": result.get("can_undo", False),
            "can_redo": result.get("can_redo", True)
        }
    
    raise HTTPException(400, result.get("error", "Cannot undo"))


@router.post("/redo")
def redo_action(
    data: UndoRedoRequest,
    user: User = Depends(get_current_user)
):
    """
    Redo last undone code change.
    Returns the next version's code.
    
    Returns:
        - code: Next version code
        - version: Version number
        - can_undo: Can undo now
        - can_redo: Can redo further
    """
    result = redo_project_action(data.session_id)
    
    if result.get("success"):
        return {
            "status": "redone",
            "code": result.get("code", ""),
            "version": result.get("version", 1),
            "can_undo": result.get("can_undo", True),
            "can_redo": result.get("can_redo", False)
        }
    
    raise HTTPException(400, result.get("error", "Cannot redo"))


# ============================================================
# 7️⃣ UTILITY ENDPOINTS
# ============================================================

@router.get("/blueprint/{session_id}")
def get_blueprint(
    session_id: str,
    user: User = Depends(get_current_user)
):
    """
    Get existing blueprint for a session.
    """
    session = get_session(session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session")
    
    blueprint = get_blueprint_from_db(session_id)
    if not blueprint:
        raise HTTPException(404, "Blueprint not found for this session")
    
    return {"blueprint": blueprint}


@router.post("/generated-code")
@router.post("/generated_code")
def get_generated_code_api(
    data: BlueprintRequest,
    user: User = Depends(get_current_user)
):
    """
    Get generated code for a session.
    """
    return get_code(data.session_id, user)

@router.get("/code/{session_id}")
def get_code(
    session_id: str,
    user: User = Depends(get_current_user)
):
    """
    Get existing generated code for a session.
    """
    session = get_session(session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session")
    
    code_data = get_code_from_db(session_id)
    if not code_data:
        raise HTTPException(404, "Code not found for this session")
    
    return code_data

