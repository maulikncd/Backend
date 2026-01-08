"""
Project services for Web_generator module
# added by web_generator
"""

import os
from typing import Dict, Any, List, Optional
from app.web_builder.Web_generator.app.crud.crud import *
import uuid
from datetime import datetime

def generate_project_blueprint(session_id: str, db=None, force_regenerate: bool = False) -> Dict[str, Any]:
    """
    Generate project blueprint from session metadata using AI.
    Now uses BlueprintService for AI-powered generation.
    
    Args:
        session_id: Session ID to use for generation
        db: Database session (optional)
        force_regenerate: If True, delete old blueprint and regenerate fresh
    """
    # Import here to avoid circular imports
    from app.web_builder.Web_generator.app.services.blueprint_service import get_blueprint_service
    
    # Delete old blueprint if force regenerate is requested
    if force_regenerate:
        try:
            delete_blueprint_from_db(session_id)
            print(f"[project_service] 🗑️ Deleted old blueprint for fresh regeneration")
        except Exception as e:
            print(f"[project_service] ⚠️ Could not delete old blueprint: {e}")
    
    # Use BlueprintService for AI-powered generation
    blueprint_service = get_blueprint_service()
    blueprint = blueprint_service.generate_blueprint_from_session(session_id)
    
    # If there's an error, return it
    if "error" in blueprint:
        return blueprint
    
    # Save blueprint to file system if project exists and db session is provided
    if db:
        session = get_session(session_id)
        if session and "user_id" in session:
            try:
                from app.Auth.utils.file_manager import get_project_from_session, save_blueprint_to_file
                project = get_project_from_session(session_id, session["user_id"], db)
                if project:
                    save_blueprint_to_file(project, blueprint)
            except Exception as e:
                print(f"[project_service] Error saving to file: {e}")
    
    return blueprint

def generate_code(session_id: str, blueprint: Optional[Dict[str, Any]] = None, db=None, force_regenerate: bool = False) -> Dict[str, Any]:
    """
    Generate SINGLE-PAGE website code from blueprint using HTMLGeneratorService.
    All sections (Hero, About, Menu, Contact, etc.) are combined into one index.html.
    Saves the HTML file to project's code folder.
    
    🆕 IMPORTANT: Now checks for existing saved code first!
    If saved code exists (from property panel edits), returns that instead of regenerating.
    This preserves inline style/class changes made via the element editor.
    
    Use force_regenerate=True to ignore saved code and regenerate from Blueprint.
    
    Priority:
    1. If force_regenerate is False, check for existing saved code in database
    2. If saved code exists, return it (preserves property changes)
    3. If no saved code OR force_regenerate, generate from blueprint
    
    Returns:
        Dict containing:
        - pages: Dict of filename -> HTML content
        - main_page: The index.html content (for backward compatibility)
        - code_folder: Path where files were saved
        - saved_files: List of saved file paths
        - from_cache: Whether code was returned from cache (not regenerated)
    """
    from app.web_builder.Web_generator.app.services.html_generator_service import get_html_generator_service
    
    # 🆕 CHECK FOR EXISTING SAVED CODE FIRST (unless force_regenerate)
    if not force_regenerate and session_id:
        existing_code = get_code_from_db(session_id)
        if existing_code and existing_code.get("code"):
            print(f"[project_service] 📦 Found existing saved code, returning cached version (preserves property changes)")
            main_html = existing_code.get("code", "")
            return {
                "pages": {"index.html": main_html},
                "main_page": main_html,
                "pages_count": 1,
                "page_names": ["index.html"],
                "code_folder": None,
                "saved_files": [],
                "from_cache": True,
                "message": "Returned existing code (includes your property changes)"
            }
    
    # Determine if request body has a FULL blueprint (not just simple component list)
    is_full_blueprint = (
        blueprint and 
        isinstance(blueprint, dict) and 
        (blueprint.get("componentOrder") or blueprint.get("projectName") or blueprint.get("theme"))
    )
    
    # If session_id provided and no full blueprint in request, always get from DB
    if session_id and not is_full_blueprint:
        db_blueprint = get_blueprint_from_db(session_id)
        if db_blueprint:
            blueprint = db_blueprint
            print(f"[project_service] 📋 Using blueprint from database")
        elif not blueprint:
            return {"error": "No blueprint found. Please generate blueprint first."}
    
    if not blueprint:
        return {"error": "No blueprint provided and none found in database."}
    
    print(f"[project_service] 🚀 Generating HTML from blueprint...")
    
    # Get HTML generator service
    html_generator = get_html_generator_service()
    
    # Generate SINGLE PAGE website (all sections in one HTML file)
    # Previously: pages = html_generator.generate(blueprint, output_dir=None)
    pages = html_generator.generate_single_page(blueprint, output_dir=None)
    
    # Get main index.html for backward compatibility
    main_html = pages.get("index.html", "")
    
    # Initialize response
    result = {
        "pages": pages,
        "main_page": main_html,
        "pages_count": len(pages),
        "page_names": list(pages.keys()),
        "code_folder": None,
        "saved_files": []
    }
    
    # Save files to project's code folder if db provided
    if db:
        session = get_session(session_id)
        if session and "user_id" in session:
            try:
                from app.Auth.utils.file_manager import get_project_from_session, save_website_files
                project = get_project_from_session(session_id, session["user_id"], db)
                if project:
                    # Save all pages to code folder
                    save_result = save_website_files(project, pages)
                    result["code_folder"] = save_result.get("code_folder")
                    result["saved_files"] = save_result.get("saved_files", [])
                    print(f"[project_service] 💾 Saved {save_result.get('saved_count', 0)} files to {result['code_folder']}")
            except Exception as e:
                print(f"[project_service] Error saving to project folder: {e}")
    
    # Save main code to database
    code_id = save_code_to_db(session_id, main_html)
    
    # Save action to Redis for undo/redo
    save_action_history_redis(session_id, {
        "action": "generate_code",
        "code_id": code_id,
        "blueprint_id": blueprint.get("blueprint_id") if isinstance(blueprint, dict) else None,
        "pages_generated": list(pages.keys())
    })
    
    print(f"[project_service] ✅ Generated {len(pages)} HTML pages!")
    
    return result

def process_chat_message(session_id: str, message: str, user_id: str) -> Dict[str, Any]:
    """
    Process chat message using AI-powered chatbot.
    Uses Gemma 3 12B for cost-effective conversational AI.
    
    Returns:
        Dict containing:
        - response: AI message to user
        - actions_taken: List of blueprint modifications made
        - blueprint_updated: Boolean flag if blueprint was changed
        - suggestions: Optional improvement suggestions
        - intent: Detected user intent
    """
    from app.web_builder.Web_generator.app.services.chatbot import get_chatbot_service
    
    chatbot = get_chatbot_service()
    
    # Convert user_id to int if it's a string
    uid = int(user_id) if isinstance(user_id, str) else user_id
    
    # Process message with AI
    result = chatbot.process_message(session_id, message, uid)
    
    return result

def generate_draft_code(session_id: str, component: str, requirements: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Generate draft code for specific component.
    Saves to version control system for undo/redo support.
    
    Returns:
        Dict with draft code, version info, and undo/redo flags
    """
    from app.web_builder.Web_generator.app.crud.version_control import save_draft_version
    
    component_templates = {
        "header": "<header>\n  <nav>\n    <h1>Your Logo</h1>\n    <ul>\n      <li><a href='#'>Home</a></li>\n      <li><a href='#'>About</a></li>\n      <li><a href='#'>Contact</a></li>\n    </ul>\n  </nav>\n</header>",
        "navbar": "<nav class='navbar'>\n  <div class='logo'>Logo</div>\n  <ul class='nav-links'>\n    <li><a href='#'>Home</a></li>\n    <li><a href='#'>About</a></li>\n    <li><a href='#'>Services</a></li>\n    <li><a href='#'>Contact</a></li>\n  </ul>\n</nav>",
        "footer": "<footer>\n  <p>&copy; 2024 Your Website. All rights reserved.</p>\n</footer>",
        "contact": "<section class='contact'>\n  <h2>Contact Us</h2>\n  <form>\n    <input type='text' placeholder='Name' required>\n    <input type='email' placeholder='Email' required>\n    <textarea placeholder='Message' required></textarea>\n    <button type='submit'>Send</button>\n  </form>\n</section>",
        "about": "<section class='about'>\n  <h2>About Us</h2>\n  <p>We are a company dedicated to providing excellent services.</p>\n</section>",
        "hero": "<section class='hero'>\n  <h1>Welcome to Our Website</h1>\n  <p>Your success is our priority</p>\n  <a href='#' class='btn'>Get Started</a>\n</section>"
    }
    
    draft = component_templates.get(component.lower(), f"<!-- Component '{component}' not found in templates -->")
    
    # Save to version control system
    file_path = f"components/{component.lower()}.html"
    result = save_draft_version(
        session_id, 
        draft, 
        change_description=f"Generated {component} component",
        file_path=file_path
    )
    
    return {
        "draft": draft,
        "version": result.get("version", 1),
        "can_undo": result.get("can_undo", False),
        "can_redo": result.get("can_redo", False),
        "status": "generated"
    }

def save_project_code(session_id: str, code: str, file_path: str) -> Dict[str, Any]:
    """
    Save generated code to project - FINAL SAVE.
    Clears all draft versions and saves final code to database.
    
    Returns:
        Dict with save status and draft cleanup info
    """
    from app.web_builder.Web_generator.app.crud.version_control import finalize_and_clear_drafts
    
    # Finalize code and clear all drafts
    result = finalize_and_clear_drafts(session_id, code, file_path)
    
    if result.get("success"):
        return {
            "success": True,
            "status": "saved",
            "file_path": file_path,
            "code_id": result.get("code_id"),
            "drafts_cleared": True,
            "message": "Code saved and all drafts cleared"
        }
    
    return {
        "success": False,
        "error": result.get("error", "Failed to save code")
    }

def undo_project_action(session_id: str) -> Dict[str, Any]:
    """
    Undo last code change using version control.
    Returns the previous version's code.
    """
    from app.web_builder.Web_generator.app.crud.version_control import undo_draft
    
    result = undo_draft(session_id)
    return result

def redo_project_action(session_id: str) -> Dict[str, Any]:
    """
    Redo last undone code change using version control.
    Returns the next version's code.
    """
    from app.web_builder.Web_generator.app.crud.version_control import redo_draft
    
    result = redo_draft(session_id)
    return result

def extract_components_from_metadata(metadata: Dict[str, Any]) -> List[str]:
    """
    Extract component list from metadata
    """
    components = ["header", "main", "footer"]  # Default components
    
    # Add components based on selected features
    selected_features = metadata.get("selected_features", [])
    if isinstance(selected_features, list):
        for feature in selected_features:
            if isinstance(feature, dict) and "name" in feature:
                if "Authentication" in feature["name"]:
                    components.append("login-form")
                elif "Payments" in feature["name"]:
                    components.append("payment-form")
                elif "Admin" in feature["name"]:
                    components.append("admin-panel")
            elif isinstance(feature, str):
                # Handle case where features are stored as strings
                if "Authentication" in feature:
                    components.append("login-form")
                elif "Payments" in feature:
                    components.append("payment-form")
                elif "Admin" in feature:
                    components.append("admin-panel")
    
    return components

def generate_html_code(blueprint: Dict[str, Any]) -> str:
    """
    Generate HTML code from blueprint
    """
    structure = blueprint.get("structure", {})
    components = structure.get("components", [])
    styling = structure.get("styling", {})
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Website</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        header {{
            background: #333;
            color: white;
            padding: 1rem 0;
        }}
        nav ul {{
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 2rem;
        }}
        nav a {{
            color: white;
            text-decoration: none;
        }}
        main {{
            min-height: 70vh;
            padding: 2rem 0;
        }}
        footer {{
            background: #333;
            color: white;
            text-align: center;
            padding: 1rem 0;
        }}
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="container">
                <h1>Generated Website</h1>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
        </nav>
    </header>
    
    <main>
        <div class="container">
            <section id="home">
                <h2>Welcome to Your Website</h2>
                <p>This is a dynamically generated website based on your requirements.</p>
            </section>
            
            <section id="about">
                <h2>About Us</h2>
                <p>We provide excellent services tailored to your needs.</p>
            </section>
            
            <section id="contact">
                <h2>Contact Us</h2>
                <p>Get in touch with us for more information.</p>
            </section>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2024 Generated Website. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""
    
    return html
