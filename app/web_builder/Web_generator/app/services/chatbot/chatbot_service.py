"""
Chatbot Service - Main orchestrator for AI-powered blueprint editing
Uses Llama via Groq API for cost-effective conversations
"""

import json
import httpx
from typing import Dict, Any, Optional, List
from datetime import datetime

from app.Auth.core.config import get_settings
from app.web_builder.Web_generator.app.crud.crud import (
    get_blueprint_from_db,
    save_blueprint_to_db,
    get_chat_history_from_session,
    save_chat_to_db,
    get_session
)
from app.web_builder.Web_generator.app.crud.version_control import (
    save_blueprint_version,
    get_latest_blueprint_version,
    save_auto_draft
)
from .blueprint_editor import BlueprintEditor
from .chatbot_prompts import (
    CHATBOT_SYSTEM_PROMPT,
    INTENT_DETECTION_PROMPT,
    SUGGESTION_PROMPT,
    COMPONENT_TEMPLATES
)


class ChatbotService:
    """
    AI-powered chatbot service for blueprint editing.
    Uses Llama via Groq API for cost-effective conversational AI.
    """
    
    # Groq API Configuration (hardcoded for reliability)
    GROQ_BASE_URL = "https://api.groq.com/openai/v1"
    GROQ_CHATBOT_MODEL = "llama-3.1-8b-instant"  # Fast Llama model for chatbot
    
    def __init__(self):
        settings = get_settings()
        self.model = self.GROQ_CHATBOT_MODEL  # Always use Llama
        # Use groq_api_key, fallback to premium_ai_api_key for backward compatibility
        self.api_key = settings.groq_api_key or settings.premium_ai_api_key
        self.base_url = self.GROQ_BASE_URL  # Always use Groq API
        self.timeout = 30.0
        self.blueprint_editor = BlueprintEditor()
        
        print(f"[ChatbotService] Initialized with model: {self.model}, base_url: {self.base_url}")
        
        if not self.api_key:
            print("[ChatbotService] WARNING: GROQ_API_KEY not configured. Chatbot will use fallback responses.")
    
    def _get_headers(self) -> Dict[str, str]:
        """Get headers for API requests."""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def _clean_json_response(self, response_text: str) -> str:
        """Clean AI response to extract valid JSON."""
        text = response_text.strip()
        
        # Remove markdown code blocks
        if "```json" in text:
            text = text.split("```json")[-1].split("```")[0]
        elif "```" in text:
            parts = text.split("```")
            if len(parts) >= 2:
                text = parts[1]
        
        text = text.strip()
        
        # Find JSON boundaries
        start_idx = text.find("{")
        end_idx = text.rfind("}")
        
        if start_idx != -1 and end_idx != -1:
            text = text[start_idx:end_idx + 1]
        
        return text
    
    def _call_ai(
        self, 
        system_prompt: str, 
        user_message: str,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """
        Call the AI API with given prompts.
        
        Args:
            system_prompt: System instructions
            user_message: User message
            temperature: Creativity level
            
        Returns:
            Parsed JSON response or error dict
        """
        if not self.api_key:
            return {"error": "API key not configured"}
        
        try:
            payload = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                "temperature": temperature,
                "max_tokens": 2000,
                "response_format": {"type": "json_object"}  # Force JSON output
            }
            
            print(f"[ChatbotService] Calling AI with model: {self.model}")
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self._get_headers(),
                    json=payload
                )
                
                if response.status_code != 200:
                    print(f"[ChatbotService] API Error: {response.status_code} - {response.text[:200]}")
                    return {"error": f"API Error: {response.status_code}"}
                
                result = response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "{}")
                
                # Debug: Log raw AI response
                print(f"[ChatbotService] Raw AI response (first 500 chars): {content[:500]}")
                
                # Try to parse as JSON
                cleaned = self._clean_json_response(content)
                print(f"[ChatbotService] Cleaned JSON (first 500 chars): {cleaned[:500]}")
                
                try:
                    parsed = json.loads(cleaned)
                    print(f"[ChatbotService] Parsed actions: {parsed.get('actions', [])}")
                    return parsed
                except json.JSONDecodeError as e:
                    print(f"[ChatbotService] JSON parse error: {e}")
                    # Return as plain text response
                    return {
                        "response": content,
                        "intent": "general",
                        "actions": []
                    }
                    
        except httpx.TimeoutException:
            return {"error": "Request timeout"}
        except Exception as e:
            print(f"[ChatbotService] Error: {str(e)}")
            return {"error": str(e)}
    
    def _call_ai_with_history(
        self, 
        system_prompt: str, 
        user_message: str,
        conversation_history: List[Dict[str, str]],
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """Call the AI API with conversation history for context."""
        if not self.api_key:
            return {"error": "API key not configured"}
        
        try:
            # Build messages array with history
            messages = [{"role": "system", "content": system_prompt}]
            
            # Add conversation history
            for msg in conversation_history:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if content:
                    messages.append({"role": role, "content": content})
            
            # Add current user message
            messages.append({"role": "user", "content": user_message})
            
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": 2000,
                "response_format": {"type": "json_object"}
            }
            
            print(f"[ChatbotService] Calling AI with {len(messages)-1} context messages...")
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self._get_headers(),
                    json=payload
                )
                
                if response.status_code != 200:
                    print(f"[ChatbotService] API Error: {response.status_code}")
                    return {"error": f"API Error: {response.status_code}"}
                
                result = response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "{}")
                cleaned = self._clean_json_response(content)
                
                try:
                    return json.loads(cleaned)
                except json.JSONDecodeError:
                    return {"response": content, "intent": "general", "actions": []}
                    
        except Exception as e:
            print(f"[ChatbotService] Error: {str(e)}")
            return {"error": str(e)}
    
    def _format_conversation_history(self, messages: List[Dict[str, str]]) -> str:
        """Format conversation history for the prompt."""
        if not messages:
            return "No previous messages."
        
        lines = []
        for msg in messages:
            role = msg.get("role", "user").capitalize()
            content = msg.get("content", "")[:200]  # Limit length
            lines.append(f"{role}: {content}")
        
        return "\n".join(lines)
    
    def process_message(
        self, 
        session_id: str, 
        message: str, 
        user_id: int,
        conversation_history: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        Process a chat message and generate AI response with potential blueprint modifications.
        
        Args:
            session_id: Current session ID
            message: User's message
            user_id: User ID for history tracking
            conversation_history: Optional list of previous messages for context
            
        Returns:
            Dict with response, actions_taken, blueprint_updated, suggestions
        """
        # Get current blueprint
        blueprint = get_blueprint_from_db(session_id)
        
        if not blueprint:
            return self._fallback_response(
                "I notice you don't have a blueprint yet. Would you like me to help you generate one first? You can use the blueprint generation feature to create your website structure.",
                session_id, user_id, message
            )
        
        # Use provided conversation history or fetch from session
        if conversation_history:
            history_text = self._format_conversation_history(conversation_history[-10:])
        else:
            chat_history = get_chat_history_from_session(session_id)
            history_text = self._format_chat_history(chat_history[-10:])
        
        # Get blueprint summary for context
        blueprint_summary = self.blueprint_editor.get_blueprint_summary(blueprint)
        
        # Build the system prompt with context
        system_prompt = CHATBOT_SYSTEM_PROMPT.format(
            blueprint_context=blueprint_summary,
            chat_history=history_text
        )
        
        # Call AI with conversation history if provided
        if conversation_history:
            ai_response = self._call_ai_with_history(system_prompt, message, conversation_history[-6:])
        else:
            ai_response = self._call_ai(system_prompt, message)
        
        if "error" in ai_response:
            return self._fallback_response(
                f"I'm having trouble connecting right now. Let me help you with a quick response. What would you like to change in your website?",
                session_id, user_id, message
            )
        
        # Process actions if any
        actions_taken = []
        blueprint_updated = False
        
        actions = ai_response.get("actions", [])
        
        # Fallback: If intent is edit but no actions, try to extract from message
        if not actions and ai_response.get("intent") == "edit":
            print(f"[ChatbotService] No actions from AI, attempting fallback parsing...")
            fallback_action = self._extract_action_from_message(message, blueprint)
            if fallback_action:
                actions = [fallback_action]
                print(f"[ChatbotService] Fallback action created: {fallback_action}")
        
        for action in actions:
            action_type = action.get("action_type", "none")
            
            if action_type == "edit":
                print(f"[ChatbotService] Executing edit action: {action}")
                try:
                    result = self._execute_edit(blueprint, action)
                    print(f"[ChatbotService] Edit result: success={result.get('success')}, action_info={result.get('action_info')}")
                    if result.get("success"):
                        blueprint = result["blueprint"]
                        blueprint_updated = True
                        actions_taken.append(result["action_info"])
                except Exception as e:
                    print(f"[ChatbotService] Error executing edit: {e}")
                    
            elif action_type == "add":
                result = self._execute_add(blueprint, action)
                if result.get("success"):
                    blueprint = result["blueprint"]
                    blueprint_updated = True
                    actions_taken.append(result["action_info"])
                    
            elif action_type == "remove":
                result = self._execute_remove(blueprint, action)
                if result.get("success"):
                    blueprint = result["blueprint"]
                    blueprint_updated = True
                    actions_taken.append(result["action_info"])
        
        # Save updated blueprint if modified
        if blueprint_updated:
            save_blueprint_to_db(session_id, blueprint)
            # Also save as draft version for undo/redo
            change_desc = ", ".join([a.get("message", "") for a in actions_taken])
            save_blueprint_version(session_id, blueprint, change_desc)
            
            # Also sync to latest.json file (without creating backup - version control handles history)
            try:
                session = get_session(session_id)
                if session and session.get("user_id"):
                    from app.Auth.utils.file_manager import get_project_from_session, save_blueprint_to_file
                    # Need DB session - create one
                    from app.Auth.db.session import SessionLocal
                    with SessionLocal() as db:
                        project = get_project_from_session(session_id, session["user_id"], db)
                        if project:
                            # create_backup=False - we already have version control in DB
                            save_blueprint_to_file(project, blueprint, create_backup=False)
                            print(f"[ChatbotService] ✅ Synced blueprint to latest.json")
            except Exception as e:
                print(f"[ChatbotService] ⚠️ Could not sync to file: {e}")
        
        # Get response text
        response_text = ai_response.get("response", "I understand. Let me help you with that.")
        
        # Note: Message saving is now handled by conversation API
        # This service only processes the message and returns the result
        
        return {
            "response": response_text,
            "actions_taken": actions_taken,
            "blueprint_updated": blueprint_updated,
            "suggestions": ai_response.get("suggestions"),
            "intent": ai_response.get("intent", "general")
        }
    
    def _execute_edit(self, blueprint: Dict[str, Any], action: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an edit action on the blueprint.
        
        Handles both:
        - Root-level fields (projectName, theme.colorPalette.primary, seo.title)
        - Component fields (comp-home.props.title)
        """
        component_type = action.get("component_type")
        field = action.get("field", "")
        new_value = action.get("new_value")
        
        if new_value is None:
            return {"success": False, "action_info": {"type": "edit", "message": "No value provided"}}
        
        # Root-level fields that are not components
        root_fields = ["projectName", "projectType", "theme", "seo", "navigation", "globalStyles", "designVision"]
        
        # Check if this is a root-level edit
        is_root_edit = False
        field_path = ""
        
        # Case 1: component_type is a root field
        if component_type and any(component_type.lower() == rf.lower() for rf in root_fields):
            is_root_edit = True
            # If field is same as component_type, use just the field
            if field and field.lower() == component_type.lower():
                field_path = field
            elif field and field != component_type:
                field_path = f"{component_type}.{field}"
            else:
                field_path = component_type
        
        # Case 2: component_type starts with root field (e.g., "theme.colorPalette")
        elif component_type and any(component_type.lower().startswith(rf.lower() + ".") for rf in root_fields):
            is_root_edit = True
            if field:
                field_path = f"{component_type}.{field}"
            else:
                field_path = component_type
        
        # Case 3: component_type is None or "root" and field starts with root field
        elif not component_type or component_type.lower() == "root":
            is_root_edit = True
            field_path = field
        
        # Case 4: field itself is a root field (like "projectName")
        elif field and any(field.lower() == rf.lower() for rf in root_fields):
            is_root_edit = True
            field_path = field
        
        print(f"[ChatbotService] _execute_edit: component_type={component_type}, field={field}, is_root_edit={is_root_edit}, field_path={field_path}")
        
        if is_root_edit:
            # Edit root-level field
            modified, success, message = self.blueprint_editor.edit_root_field(
                blueprint, field_path, new_value
            )
            print(f"[ChatbotService] edit_root_field result: success={success}, message={message}")
            return {
                "success": success,
                "blueprint": modified if success else blueprint,
                "action_info": {
                    "type": "edit",
                    "component": "root",
                    "field": field_path,
                    "message": message
                }
            }
        
        # Component-level edit
        if not component_type:
            return {"success": False, "action_info": {"type": "edit", "message": "No component specified"}}
        
        # Try to find the component (handle both "hero" and "comp-home" formats)
        comp_key = component_type
        if component_type not in blueprint.get("components", {}):
            # Try with "comp-" prefix
            for key in blueprint.get("components", {}).keys():
                if component_type.lower() in key.lower():
                    comp_key = key
                    break
        
        modified, success, message = self.blueprint_editor.edit_component(
            blueprint, comp_key, field, new_value
        )
        
        return {
            "success": success,
            "blueprint": modified if success else blueprint,
            "action_info": {
                "type": "edit",
                "component": comp_key,
                "field": field,
                "message": message
            }
        }
    
    def _execute_add(self, blueprint: Dict[str, Any], action: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an add action on the blueprint."""
        component_type = action.get("component_type")
        
        if not component_type:
            return {"success": False}
        
        # Get template for this component type
        template = COMPONENT_TEMPLATES.get(component_type.lower())
        if not template:
            return {"success": False}
        
        # Customize template with project info
        project_name = blueprint.get("projectName", "Your Business")
        component_data = json.loads(json.dumps(template).replace("{business_name}", project_name))
        
        modified, success, message = self.blueprint_editor.add_component(
            blueprint, component_type, component_data
        )
        
        return {
            "success": success,
            "blueprint": modified if success else blueprint,
            "action_info": {
                "type": "add",
                "component": component_type,
                "message": message
            }
        }
    
    def _execute_remove(self, blueprint: Dict[str, Any], action: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a remove action on the blueprint."""
        component_type = action.get("component_type")
        
        if not component_type:
            return {"success": False}
        
        modified, success, message = self.blueprint_editor.remove_component(
            blueprint, component_type
        )
        
        return {
            "success": success,
            "blueprint": modified if success else blueprint,
            "action_info": {
                "type": "remove",
                "component": component_type,
                "message": message
            }
        }
    
    def _extract_action_from_message(self, message: str, blueprint: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Fallback: Extract action from user message when AI doesn't return proper actions.
        Handles common patterns like name changes, headline edits, etc.
        """
        import re
        message_lower = message.lower()
        
        # Check if message contains name change indicators
        name_change_indicators = ['name', 'naam']
        has_name_indicator = any(ind in message_lower for ind in name_change_indicators)
        
        if has_name_indicator:
            # Try to extract the new name - look for the last meaningful words
            # Pattern: anything that looks like a name after common words
            
            # First, try to find quoted name
            quoted = re.search(r'["\']([^"\']+)["\']', message)
            if quoted:
                new_name = quoted.group(1).strip()
            else:
                # Remove common prefixes to find the name
                cleaned = message_lower
                remove_patterns = [
                    r'^.*?name\s*(?:change\s*)?(?:kr(?:ke|o)?|kar(?:ke|o)?|do|to|se)?\s*',
                    r'^.*?(?:is|ye|yeh)\s+(?:website|site)\s+(?:ka|ki)?\s*name\s*(?:change\s*)?(?:kr(?:ke|o)?|kar(?:ke|o)?|do)?\s*',
                ]
                
                for pattern in remove_patterns:
                    cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
                
                # Remove trailing action words
                cleaned = re.sub(r'\s*(kr|kar|karo|do|rakh|de)\s*$', '', cleaned, flags=re.IGNORECASE)
                cleaned = cleaned.strip()
                
                if cleaned:
                    new_name = cleaned
                else:
                    return None
            
            if new_name and len(new_name) > 1:
                # Title case the name
                new_name = ' '.join(word.capitalize() for word in new_name.split())
                print(f"[ChatbotService] Extracted name from message: '{new_name}'")
                return {
                    "action_type": "edit",
                    "component_type": "projectName",
                    "field": "projectName",
                    "new_value": new_name
                }
        
        # Pattern 2: Headline/title change patterns
        headline_indicators = ['headline', 'title', 'heading']
        if any(ind in message_lower for ind in headline_indicators):
            quoted = re.search(r'["\']([^"\']+)["\']', message)
            if quoted:
                new_headline = quoted.group(1).strip()
                if new_headline:
                    return {
                        "action_type": "edit",
                        "component_type": "comp-home",
                        "field": "props.title",
                        "new_value": new_headline
                    }
        
        return None
    
    def _format_chat_history(self, history: List[Dict[str, Any]]) -> str:
        """Format chat history for AI context."""
        if not history:
            return "No previous messages"
        
        formatted = []
        for msg in history:
            role = msg.get("role", "user")
            message = msg.get("message", "")
            formatted.append(f"{role.title()}: {message}")
        
        return "\n".join(formatted)
    
    def _fallback_response(
        self, 
        message: str, 
        session_id: str, 
        user_id: int, 
        user_message: str
    ) -> Dict[str, Any]:
        """Generate a fallback response when AI is unavailable."""
        import uuid
        chat_id = f"chat_{uuid.uuid4().hex[:8]}"
        save_chat_to_db(session_id, user_id, chat_id, 1, user_message, message)
        
        return {
            "response": message,
            "actions_taken": [],
            "blueprint_updated": False,
            "suggestions": None,
            "intent": "general"
        }
    
    def get_suggestions(self, session_id: str) -> Dict[str, Any]:
        """
        Generate improvement suggestions for the current blueprint.
        
        Args:
            session_id: Session ID to get blueprint from
            
        Returns:
            Dict with suggestions list
        """
        blueprint = get_blueprint_from_db(session_id)
        
        if not blueprint:
            return {"error": "No blueprint found", "suggestions": []}
        
        website_type = blueprint.get("websiteType", "business")
        business_name = blueprint.get("projectName", "Your Business")
        
        prompt = SUGGESTION_PROMPT.format(
            blueprint=json.dumps(blueprint, indent=2)[:3000],  # Limit size
            website_type=website_type,
            business_name=business_name
        )
        
        response = self._call_ai(
            "You are a website design expert. Provide specific, actionable suggestions.",
            prompt,
            temperature=0.8
        )
        
        return response


# Singleton instance
_chatbot_service_instance: Optional[ChatbotService] = None


def get_chatbot_service() -> ChatbotService:
    """Get or create chatbot service singleton instance."""
    global _chatbot_service_instance
    if _chatbot_service_instance is None:
        _chatbot_service_instance = ChatbotService()
    return _chatbot_service_instance
