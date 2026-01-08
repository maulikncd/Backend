"""
Enhanced Chatbot Service - Handles both Blueprint and Element-level edits
Combines conversation AI with direct HTML manipulation
"""

import json
import httpx
import re
from typing import Dict, Any, Optional, List
from datetime import datetime

from app.Auth.core.config import get_settings
from app.web_builder.Web_generator.app.crud.crud import (
    get_blueprint_from_db,
    save_blueprint_to_db,
    get_session
)
from app.web_builder.Web_generator.app.crud.version_control import (
    save_blueprint_version
)
from .blueprint_editor import BlueprintEditor
from .element_editor import ElementEditor, get_element_editor
from .enhanced_chatbot_prompts import ENHANCED_CHATBOT_PROMPT, ELEMENT_INTENT_PROMPT
from .chatbot_prompts import COMPONENT_TEMPLATES


class EnhancedChatbotService:
    """
    Enhanced AI-powered chatbot service that handles:
    1. Blueprint modifications (global website changes)
    2. Direct element modifications (text, color, style changes)
    3. Natural conversation and suggestions
    """
    
    # Groq API Configuration
    GROQ_BASE_URL = "https://api.groq.com/openai/v1"
    GROQ_MODEL = "llama-3.1-8b-instant"
    
    def __init__(self):
        settings = get_settings()
        self.model = self.GROQ_MODEL
        self.api_key = settings.groq_api_key or settings.premium_ai_api_key
        self.base_url = self.GROQ_BASE_URL
        self.timeout = 60.0
        self.blueprint_editor = BlueprintEditor()
        self.element_editor = get_element_editor()
        
        print(f"[EnhancedChatbotService] Initialized with model: {self.model}")
        
        if not self.api_key:
            print("[EnhancedChatbotService] WARNING: API key not configured")
    
    def _get_headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def _clean_json_response(self, response_text: str) -> str:
        """Clean AI response to extract valid JSON."""
        text = response_text.strip()
        
        if "```json" in text:
            text = text.split("```json")[-1].split("```")[0]
        elif "```" in text:
            parts = text.split("```")
            if len(parts) >= 2:
                text = parts[1]
        
        text = text.strip()
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
        """Call the AI API."""
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
                "response_format": {"type": "json_object"}
            }
            
            print(f"[EnhancedChatbotService] Calling AI...")
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self._get_headers(),
                    json=payload
                )
                
                if response.status_code != 200:
                    print(f"[EnhancedChatbotService] API Error: {response.status_code}")
                    return {"error": f"API Error: {response.status_code}"}
                
                result = response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "{}")
                
                cleaned = self._clean_json_response(content)
                
                try:
                    return json.loads(cleaned)
                except json.JSONDecodeError as e:
                    print(f"[EnhancedChatbotService] JSON parse error: {e}")
                    return {
                        "response": content,
                        "intent": "general",
                        "mode": "conversation",
                        "actions": []
                    }
                    
        except httpx.TimeoutException:
            return {"error": "Request timeout"}
        except Exception as e:
            print(f"[EnhancedChatbotService] Error: {str(e)}")
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
        
        # Retry configuration
        max_retries = 3
        base_delay = 1
        
        last_error = None
        
        for attempt in range(max_retries):
            try:
                # Build messages array with history
                messages = [{"role": "system", "content": system_prompt}]
                
                # Add conversation history (use more context as we fetch 30 now)
                for msg in conversation_history[-20:]:
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
                
                if attempt > 0:
                    print(f"[EnhancedChatbotService] 🔄 Retry attempt {attempt+1}/{max_retries}...")
                else:
                    print(f"[EnhancedChatbotService] Calling AI with {len(messages)-1} context messages...")
                
                with httpx.Client(timeout=self.timeout) as client:
                    response = client.post(
                        f"{self.base_url}/chat/completions",
                        headers=self._get_headers(),
                        json=payload
                    )
                    
                    if response.status_code != 200:
                        print(f"[EnhancedChatbotService] API Error: {response.status_code} - {response.text}")
                        # If rate limit (429) or server error (5xx), retry
                        if response.status_code == 429 or response.status_code >= 500:
                            import time
                            time.sleep(base_delay * (2 ** attempt)) # Exponential backoff
                            last_error = f"API Error: {response.status_code}"
                            continue
                        
                        return {"error": f"API Error: {response.status_code}"}
                    
                    result = response.json()
                    content = result.get("choices", [{}])[0].get("message", {}).get("content", "{}")
                    
                    cleaned = self._clean_json_response(content)
                    
                    try:
                        return json.loads(cleaned)
                    except json.JSONDecodeError as e:
                        print(f"[EnhancedChatbotService] JSON parse error: {e}")
                        # Fallback to general text response
                        return {
                            "response": content,
                            "intent": "general",
                            "mode": "conversation",
                            "actions": []
                        }
                        
            except httpx.TimeoutException:
                print(f"[EnhancedChatbotService] ⏱️ API Timeout after {self.timeout}s (Attempt {attempt+1})")
                last_error = "Request timeout"
                if attempt < max_retries - 1:
                    continue
            except Exception as e:
                print(f"[EnhancedChatbotService] ❌ Unexpected Error: {str(e)}")
                import traceback
                traceback.print_exc()
                last_error = str(e)
                if attempt < max_retries - 1:
                    import time
                    time.sleep(1)
                    continue
        
        return {"error": f"Failed after {max_retries} attempts. Last error: {last_error}"}

    def process_message(
        self,
        session_id: str,
        message: str,
        user_id: int,
        selected_element: Optional[Dict[str, Any]] = None,
        html_content: Optional[str] = None,
        conversation_history: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        Process a chat message with optional element context.
        """
        # Get current blueprint for context
        blueprint = get_blueprint_from_db(session_id)
        
        # Determine mode
        has_element = selected_element is not None and bool(selected_element)
        
        # Build context info
        context_info = self._build_context_info(blueprint, session_id)
        element_info = self._build_element_info_enhanced(selected_element) if has_element else "No element selected"
        
        # DEBUG: Log element info being sent to AI
        print(f"[EnhancedChatbotService] 📋 Element Info for AI:")
        print(f"  - has_element: {has_element}")
        if selected_element:
            print(f"  - tagName: {selected_element.get('tagName')}")
            elem_text = selected_element.get('text') or ''
            print(f"  - text: {elem_text[:100] if elem_text else '(empty)'}")
        
        # 🆕 Detect if this is a question about the element (no action needed)
        is_question = self._is_question_about_element(message)
        
        # Build system prompt
        system_prompt = ENHANCED_CHATBOT_PROMPT.format(
            context_info=context_info,
            element_info=element_info
        )
        
        # 🆕 Add conversation context summary to user message for better understanding
        enriched_message = self._enrich_message_with_context(message, selected_element, conversation_history or [])
        
        # Call AI with conversation history
        ai_response = self._call_ai_with_history(system_prompt, enriched_message, conversation_history or [])
        
        if "error" in ai_response:
            # 🆕 Return specific error message for debugging
            error_msg = ai_response["error"]
            print(f"[EnhancedChatbotService] ⚠️ Returning error to user: {error_msg}")
            return self._fallback_response(
                f"I encountered an error: {error_msg}. Please try again.",
                has_element
            )
        
        # Process actions
        actions_taken = []
        html_updated = False
        blueprint_updated = False
        updated_html = html_content
        
        mode = ai_response.get("mode", "conversation")
        actions = ai_response.get("actions", [])
        
        # Fallback action extraction for element edits
        if has_element and not actions and ai_response.get("intent") in ["element_edit", "edit"]:
            fallback_action = self._extract_element_action(message, selected_element)
            if fallback_action:
                actions = [fallback_action]
                print(f"[EnhancedChatbotService] Fallback element action: {fallback_action}")
        
        # 🆕 NEW: When no element selected but AI wants to edit, try to infer from message
        if not has_element and html_content and not actions and ai_response.get("intent") in ["element_edit", "edit", "general"]:
            # Try to extract action from message (for common patterns like "button ka text")
            inferred_element = self._infer_element_from_context(message, blueprint, html_content)
            if inferred_element:
                fallback_action = self._extract_element_action(message, inferred_element)
                if fallback_action:
                    # Switch to element mode with inferred element
                    selected_element = inferred_element
                    has_element = True
                    actions = [fallback_action]
                    print(f"[EnhancedChatbotService] 🎯 Inferred element + action: {inferred_element.get('tagName')} → {fallback_action}")
        
        # Debug: Log what we have
        print(f"[EnhancedChatbotService] 📊 Processing actions:")
        print(f"  - has_element: {has_element}")
        print(f"  - html_content length: {len(html_content) if html_content else 0}")
        print(f"  - actions count: {len(actions)}")
        
        for action in actions:
            action_type = action.get("action_type", "")
            target = action.get("target", "")
            details = action.get("details", {})
            
            print(f"[EnhancedChatbotService] 🎬 Action: {action_type}, Target: {target}")
            print(f"  - details: {details}")
            
            # 🆕 Normalize target - treat element type names as "element"
            element_targets = ["element", "button", "heading", "text", "link", "image", "div", "section", "nav", "footer", "header", "h1", "h2", "h3", "p", "a", "img", "span"]
            is_element_action = target.lower() in element_targets or action_type.startswith("edit_")
            print(f"  - is_element_action: {is_element_action} (target='{target}', action_type='{action_type}')")
            
            # Element-level edits - with explicit element selected
            if is_element_action and has_element and html_content:
                print(f"[EnhancedChatbotService] ✅ Element edit with selection")
                result = self._execute_element_action(
                    action_type, 
                    selected_element, 
                    details, 
                    updated_html or html_content
                )
                print(f"[EnhancedChatbotService] 📝 Element action result: success={result.get('success')}, msg={result.get('message')}")
                if result.get("success"):
                    updated_html = result.get("html")
                    html_updated = True
                    actions_taken.append({
                        "type": action_type,
                        "target": "element",
                        "message": result.get("message")
                    })
                    print(f"[EnhancedChatbotService] ✨ HTML updated! Length: {len(updated_html) if updated_html else 0}")
            
            # 🆕 Element edit WITHOUT explicit selection - try to infer element
            elif is_element_action and html_content and not has_element:
                print(f"[EnhancedChatbotService] 🔍 Element action without selection - inferring element")
                print(f"  - is_element_action: {is_element_action}")
                print(f"  - has_element: {has_element}")
                print(f"  - html_content exists: {bool(html_content)}")
                
                # Try to infer which element to edit from message context
                inferred_element = self._infer_element_from_context(message, blueprint, html_content)
                
                if inferred_element:
                    print(f"[EnhancedChatbotService] 🎯 Inferred element: {inferred_element.get('tagName')}")
                    result = self._execute_element_action(
                        action_type, 
                        inferred_element, 
                        details, 
                        updated_html or html_content
                    )
                    if result.get("success"):
                        updated_html = result.get("html")
                        html_updated = True
                        actions_taken.append({
                            "type": action_type,
                            "target": "element",
                            "message": result.get("message") + " (auto-detected)"
                        })
                        print(f"[EnhancedChatbotService] ✨ HTML updated via auto-detection! Length: {len(updated_html) if updated_html else 0}")
                    else:
                        print(f"[EnhancedChatbotService] ⚠️ Inferred element action failed: {result.get('message')}")
                else:
                    # 🆕 Direct HTML text replacement fallback
                    new_text = details.get("new_text")
                    old_text = details.get("old_text") or details.get("target_text")
                    
                    # 🔍 DEBUG: Log what we have
                    print(f"[EnhancedChatbotService] 🔍 Direct replacement check:")
                    print(f"  - action_type: {action_type}")
                    print(f"  - new_text: {new_text}")
                    print(f"  - old_text: {old_text}")
                    print(f"  - has html_content: {bool(html_content)}")
                    
                    if action_type == "edit_text" and new_text and html_content:
                        print(f"[EnhancedChatbotService] 🔍 Attempting direct HTML text replacement")
                        print(f"  - old_text: {old_text}")
                        print(f"  - new_text: {new_text}")
                        
                        direct_result = self._direct_html_text_replace(
                            updated_html or html_content, 
                            old_text, 
                            new_text,
                            message
                        )
                        
                        if direct_result.get("success"):
                            updated_html = direct_result.get("html")
                            html_updated = True
                            actions_taken.append({
                                "type": "edit_text",
                                "target": "element",
                                "message": direct_result.get("message", "Text updated directly in HTML")
                            })
                            print(f"[EnhancedChatbotService] ✨ Direct HTML replacement successful!")
                        else:
                            print(f"[EnhancedChatbotService] ⚠️ Direct HTML replacement failed: {direct_result.get('message')}")
                            
                            # Try blueprint CTA update as last resort
                            if blueprint:
                                print(f"[EnhancedChatbotService] 🔍 Attempting blueprint CTA fallback for '{new_text}'")
                                updated_cta = False
                                components = blueprint.get("components", {}) if blueprint else {}
                                
                                for c_name, comp in components.items():
                                    props = comp.get("props", {}) if comp else {}
                                    for prop_key in ["cta", "buttonText", "btnText", "actionText"]:
                                        if prop_key in props:
                                            print(f"[EnhancedChatbotService] 🎯 Fallback: updating {c_name}.props.{prop_key} to '{new_text}'")
                                            res_bp, res_success, res_msg = self.blueprint_editor.edit_component(
                                                blueprint, c_name, f"props.{prop_key}", new_text
                                            )
                                            if res_success:
                                                blueprint = res_bp
                                                blueprint_updated = True
                                                actions_taken.append({
                                                    "type": "blueprint_edit",
                                                    "target": "blueprint",
                                                    "message": f"Updated {c_name} button text (Fallback)"
                                                })
                                                updated_cta = True
                                            break
                                    if updated_cta:
                                        break
                            else:
                                print(f"[EnhancedChatbotService] ⚠️ No blueprint available for fallback")
            
            # Blueprint-level edits
            elif target == "blueprint" or action_type.startswith("blueprint_"):
                result = self._execute_blueprint_action(
                    action_type, 
                    blueprint, 
                    details, 
                    session_id
                )
                if result.get("success"):
                    blueprint = result.get("blueprint")
                    blueprint_updated = True
                    actions_taken.append({
                        "type": action_type,
                        "target": "blueprint",
                        "message": result.get("message")
                    })
        
        # Save updated blueprint if modified
        if blueprint_updated:
            save_blueprint_to_db(session_id, blueprint)
            change_desc = ", ".join([a.get("message", "") for a in actions_taken])
            save_blueprint_version(session_id, blueprint, change_desc)
        
        # Response
        response_text = ai_response.get("response", "Done!")
        
        # Debug: Log what we're returning
        print(f"[EnhancedChatbotService] 🔚 Final result:")
        print(f"  - html_updated: {html_updated}")
        print(f"  - updated_html length: {len(updated_html) if updated_html else 0}")
        print(f"  - blueprint_updated: {blueprint_updated}")
        print(f"  - actions_taken: {len(actions_taken)}")
        
        return {
            "response": response_text,
            "actions_taken": actions_taken,
            "blueprint_updated": blueprint_updated,
            "html_updated": html_updated,
            "updated_html": updated_html if html_updated else None,
            "suggestions": ai_response.get("suggestions"),
            "intent": ai_response.get("intent", "general"),
            "mode": mode
        }
    
    def _execute_element_action(
        self,
        action_type: str,
        element: Dict[str, Any],
        details: Dict[str, Any],
        html: str
    ) -> Dict[str, Any]:
        """Execute an element-level action."""
        selector = {
            'id': element.get('id'),
            'classes': element.get('classes') or element.get('className'),
            'tagName': element.get('tagName'),
            'text': element.get('text', '')[:100]
        }
        
        print(f"[EnhancedChatbotService] Executing {action_type} on element: {selector}")
        
        try:
            if action_type == "edit_text":
                new_text = details.get("new_text", "")
                modified, success, msg = self.element_editor.edit_text(html, selector, new_text)
                return {"success": success, "html": modified, "message": msg}
            
            elif action_type == "edit_color":
                color_type = details.get("color_type", "text")
                color_value = details.get("color_value", "")
                modified, success, msg = self.element_editor.edit_color(html, selector, color_type, color_value)
                return {"success": success, "html": modified, "message": msg}
            
            elif action_type == "edit_style":
                prop = details.get("style_property", "")
                value = details.get("style_value", "")
                modified, success, msg = self.element_editor.edit_style(html, selector, prop, value)
                return {"success": success, "html": modified, "message": msg}
            
            elif action_type == "add_class":
                classes = details.get("classes", "")
                modified, success, msg = self.element_editor.edit_class(html, selector, "add", classes)
                return {"success": success, "html": modified, "message": msg}
            
            elif action_type == "remove_class":
                classes = details.get("classes", "")
                modified, success, msg = self.element_editor.edit_class(html, selector, "remove", classes)
                return {"success": success, "html": modified, "message": msg}
            
            elif action_type == "remove_element":
                modified, success, msg = self.element_editor.remove_element(html, selector)
                return {"success": success, "html": modified, "message": msg}
            
            elif action_type == "replace_element":
                new_html = details.get("new_html", "")
                modified, success, msg = self.element_editor.replace_element(html, selector, new_html)
                return {"success": success, "html": modified, "message": msg}
            
            # 🆕 Handle add_element - Map to edit_text if we have text content
            elif action_type == "add_element":
                # If adding text/emoji to existing element, treat as edit_text
                new_text = details.get("text") or details.get("new_text") or details.get("content", "")
                if new_text and element.get("text"):
                    # Append to existing text
                    combined_text = element.get("text") + " " + new_text
                    modified, success, msg = self.element_editor.edit_text(html, selector, combined_text)
                    return {"success": success, "html": modified, "message": f"Added '{new_text}' to element"}
                elif new_text:
                    modified, success, msg = self.element_editor.edit_text(html, selector, new_text)
                    return {"success": success, "html": modified, "message": msg}
                else:
                    return {"success": False, "message": "No text content to add"}
            
            # 🆕 Handle append_text - Add to existing text (for emojis, etc.)
            elif action_type == "append_text":
                append_text = details.get("text") or details.get("append", "") or details.get("new_text", "")
                current_text = element.get("text", "")
                position = details.get("position", "end")  # "start" or "end"
                
                if position == "start":
                    combined_text = append_text + " " + current_text
                else:
                    combined_text = current_text + " " + append_text
                
                modified, success, msg = self.element_editor.edit_text(html, selector, combined_text.strip())
                return {"success": success, "html": modified, "message": f"Appended '{append_text}'"}
            
            # 🆕 Handle edit_content as alias for edit_text
            elif action_type in ["edit_content", "change_text", "update_text", "set_text"]:
                new_text = details.get("new_text") or details.get("text") or details.get("content", "")
                modified, success, msg = self.element_editor.edit_text(html, selector, new_text)
                return {"success": success, "html": modified, "message": msg}
            
            else:
                # 🆕 Last resort: if there's new_text in details, try edit_text anyway
                new_text = details.get("new_text") or details.get("text")
                if new_text:
                    print(f"[EnhancedChatbotService] Unknown action '{action_type}' but has text - trying edit_text")
                    modified, success, msg = self.element_editor.edit_text(html, selector, new_text)
                    return {"success": success, "html": modified, "message": msg}
                return {"success": False, "message": f"Unknown action type: {action_type}"}
                
        except Exception as e:
            print(f"[EnhancedChatbotService] Element action error: {e}")
            return {"success": False, "message": str(e)}
    
    def _execute_blueprint_action(
        self,
        action_type: str,
        blueprint: Dict[str, Any],
        details: Dict[str, Any],
        session_id: str
    ) -> Dict[str, Any]:
        """Execute a blueprint-level action."""
        try:
            if action_type in ["edit", "blueprint_edit"]:
                component_type = details.get("component_type")
                field = details.get("field", "")
                new_value = details.get("new_value")
                
                # Root-level fields
                root_fields = ["projectName", "theme", "seo", "navigation", "globalStyles"]
                
                if component_type in root_fields or not component_type or component_type == "root":
                    field_path = field if field else component_type
                    modified, success, msg = self.blueprint_editor.edit_root_field(
                        blueprint, field_path, new_value
                    )
                else:
                    modified, success, msg = self.blueprint_editor.edit_component(
                        blueprint, component_type, field, new_value
                    )
                
                return {"success": success, "blueprint": modified, "message": msg}
            
            elif action_type in ["add", "blueprint_add"]:
                component_type = details.get("component_type")
                template = COMPONENT_TEMPLATES.get(component_type.lower(), {})
                
                if template:
                    project_name = blueprint.get("projectName", "Your Business")
                    component_data = json.loads(
                        json.dumps(template).replace("{business_name}", project_name)
                    )
                    modified, success, msg = self.blueprint_editor.add_component(
                        blueprint, component_type, component_data
                    )
                    return {"success": success, "blueprint": modified, "message": msg}
                
                return {"success": False, "message": f"Unknown component type: {component_type}"}
            
            elif action_type in ["remove", "blueprint_remove"]:
                component_type = details.get("component_type")
                modified, success, msg = self.blueprint_editor.remove_component(
                    blueprint, component_type
                )
                return {"success": success, "blueprint": modified, "message": msg}
            
            else:
                return {"success": False, "message": f"Unknown blueprint action: {action_type}"}
                
        except Exception as e:
            print(f"[EnhancedChatbotService] Blueprint action error: {e}")
            return {"success": False, "message": str(e)}
    
    def _extract_element_action(
        self, 
        message: str, 
        element: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """🆕 Enhanced fallback: Extract action from message when AI doesn't return proper actions."""
        message_lower = message.lower().strip()
        
        # 🆕 First check if this is a QUESTION - if so, return None (no action needed)
        if self._is_question_about_element(message):
            print(f"[EnhancedChatbotService] ❓ Detected question, not extracting action")
            return None
        
        # Text change patterns - improved for Hindi/Hinglish
        text_patterns = [
            # Direct quotes
            r"['\"]([^'\"]+)['\"]\s*(?:karo|kar\s*do|kardo|likhdo|likho|likh\s*do|change\s*karo|set\s*karo)",
            r"(?:change|set|update)\s*(?:to|karo?)\s*['\"]?([^'\"]+)['\"]?",
            r"(?:text|content)\s*(?:ko?|change|karo|kardo|to|se)\s*['\"]?([^'\"]+)['\"]?",
            r"isko?\s*['\"]([^'\"]+)['\"]\s*(?:karo|kardo|likhdo)",
            r"['\"]([^'\"]+)['\"]\s*(?:likh|likho|likhdo)",
            # Without quotes
            r"(?:text|heading|title)\s+(.+?)\s*(?:karo|kardo|set|change)$",
        ]
        
        for pattern in text_patterns:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                new_text = match.group(1).strip()
                # Clean up common suffixes
                new_text = re.sub(r'\s*(karo|kardo|kar\s*do|likhdo|set)\s*$', '', new_text, flags=re.IGNORECASE).strip()
                if len(new_text) > 1:
                    print(f"[EnhancedChatbotService] ✏️ Extracted text change: '{new_text}'")
                    return {
                        "action_type": "edit_text",
                        "target": "element",
                        "details": {"new_text": new_text}
                    }
        
        # Color patterns - expanded for Hindi colors
        color_map = {
            # English
            'red': '#ef4444', 'blue': '#3b82f6', 'green': '#22c55e', 
            'yellow': '#eab308', 'purple': '#a855f7', 'pink': '#ec4899', 
            'orange': '#f97316', 'white': '#ffffff', 'black': '#000000', 
            'gray': '#6b7280', 'grey': '#6b7280', 'cyan': '#06b6d4', 
            'teal': '#14b8a6', 'indigo': '#6366f1', 'violet': '#8b5cf6', 
            'gold': '#fbbf24',
            # Hindi
            'lal': '#ef4444', 'neela': '#3b82f6', 'hara': '#22c55e', 
            'peela': '#eab308', 'safed': '#ffffff', 'kala': '#000000',
            'gulabi': '#ec4899', 'narangi': '#f97316'
        }
        
        for color_name, color_value in color_map.items():
            if color_name in message_lower:
                # Determine color type from context
                color_type = "text"
                tag = element.get('tagName', '').lower()
                
                # Background indicators
                if any(word in message_lower for word in ['background', 'bg', 'button ka', 'card ka', 'box ka']):
                    color_type = "background"
                # Border indicators  
                elif any(word in message_lower for word in ['border', 'outline']):
                    color_type = "border"
                # Element-based defaults
                elif tag in ['button', 'a']:
                    color_type = "background"
                # Text color indicators
                elif any(word in message_lower for word in ['text', 'font', 'color']):
                    color_type = "text"
                
                print(f"[EnhancedChatbotService] 🎨 Extracted color change: {color_type}={color_value}")
                return {
                    "action_type": "edit_color",
                    "target": "element",
                    "details": {
                        "color_type": color_type,
                        "color_value": color_value
                    }
                }
        
        # Size patterns - expanded
        if any(word in message_lower for word in ['bigger', 'larger', 'bada', 'badi', 'bada karo', 'increase size', 'thoda bada']):
            print(f"[EnhancedChatbotService] 📐 Extracted size increase")
            return {
                "action_type": "edit_style",
                "target": "element",
                "details": {
                    "style_property": "font-size",
                    "style_value": "1.5em"
                }
            }
        
        if any(word in message_lower for word in ['smaller', 'chhota', 'chhoti', 'chhota karo', 'decrease size', 'thoda chhota']):
            print(f"[EnhancedChatbotService] 📐 Extracted size decrease")
            return {
                "action_type": "edit_style",
                "target": "element",
                "details": {
                    "style_property": "font-size",
                    "style_value": "0.8em"
                }
            }
        
        # Style patterns - shadow, rounded, etc.
        if any(word in message_lower for word in ['shadow', 'shadow add', 'shadow karo']):
            return {
                "action_type": "add_class",
                "target": "element",
                "details": {"classes": "shadow-lg"}
            }
        
        if any(word in message_lower for word in ['rounded', 'round', 'gol', 'corner']):
            return {
                "action_type": "add_class",
                "target": "element",
                "details": {"classes": "rounded-xl"}
            }
        
        # Remove patterns - expanded
        if any(word in message_lower for word in ['remove', 'delete', 'hatao', 'hata do', 'hatana', 'remove karo', 'delete karo', 'nikal do']):
            print(f"[EnhancedChatbotService] 🗑️ Extracted remove action")
            return {
                "action_type": "remove_element",
                "target": "element",
                "details": {}
            }
        
        return None
    
    def _build_context_info(self, blueprint: Dict[str, Any], session_id: str) -> str:
        """Build context info string for AI."""
        if not blueprint:
            return "No blueprint found. The user needs to create a website first."
        
        return self.blueprint_editor.get_blueprint_summary(blueprint)
    
    def _build_element_info(self, element: Dict[str, Any]) -> str:
        """Build element info string for AI."""
        if not element:
            return "No element selected"
        
        info_parts = []
        
        tag = element.get('tagName', 'unknown')
        info_parts.append(f"Tag: {tag}")
        
        if element.get('id'):
            info_parts.append(f"ID: {element['id']}")
        
        if element.get('classes'):
            info_parts.append(f"Classes: {element['classes'][:100]}")
        
        if element.get('text'):
            text = element['text'][:100]
            info_parts.append(f"Text: \"{text}\"")
        
        if element.get('styles'):
            styles = element['styles']
            if isinstance(styles, dict):
                style_str = ", ".join([f"{k}: {v}" for k, v in list(styles.items())[:5]])
                info_parts.append(f"Styles: {style_str}")
        
        return "\n".join(info_parts)
    
    def _build_element_info_enhanced(self, element: Dict[str, Any]) -> str:
        """🆕 Build detailed element info string for AI with better context."""
        if not element:
            return "No element selected"
        
        tag = element.get('tagName', 'unknown').lower()
        element_type = element.get('elementType', 'generic')
        
        # Start with clear element identification
        info_parts = [
            f"⚠️ ELEMENT IS SELECTED - Focus on this element only!",
            f"",
            f"📍 Element Type: {tag.upper()} ({element_type})"
        ]
        
        # Add ID if present
        if element.get('id'):
            info_parts.append(f"🆔 ID: #{element['id']}")
        
        # Add text content - IMPORTANT for "kya likha hai" questions
        if element.get('text'):
            text = element['text'].strip()
            # Handle multi-line text
            if '\n' in text:
                text = text.replace('\n', ' ').strip()
            # Truncate if too long
            display_text = text[:200] if len(text) > 200 else text
            info_parts.append(f"📝 Text Content: \"{display_text}\"")
            if len(text) > 200:
                info_parts.append(f"   (Text truncated, total {len(text)} characters)")
        else:
            info_parts.append(f"📝 Text Content: (No text - may be image or container)")
        
        # Add classes
        if element.get('classes'):
            classes = element['classes'][:150] if len(element.get('classes', '')) > 150 else element.get('classes', '')
            info_parts.append(f"🎨 CSS Classes: {classes}")
        
        # Add specific attributes based on element type
        if tag == 'img':
            if element.get('src'):
                info_parts.append(f"🖼️ Image Source: {element['src'][:100]}")
            if element.get('alt'):
                info_parts.append(f"📝 Alt Text: {element['alt']}")
        elif tag == 'a':
            if element.get('href'):
                info_parts.append(f"🔗 Link URL: {element['href']}")
        elif tag in ['input', 'textarea']:
            if element.get('placeholder'):
                info_parts.append(f"📝 Placeholder: {element['placeholder']}")
        
        # Add styles summary
        if element.get('styles') and isinstance(element['styles'], dict):
            styles = element['styles']
            style_summary = []
            if styles.get('color'):
                style_summary.append(f"Text: {styles['color']}")
            if styles.get('backgroundColor'):
                style_summary.append(f"BG: {styles['backgroundColor']}")
            if styles.get('fontSize'):
                style_summary.append(f"Size: {styles['fontSize']}")
            if style_summary:
                info_parts.append(f"🎨 Current Styles: {', '.join(style_summary)}")
        
        # Add session info if available
        if element.get('sessionInfo'):
            session = element['sessionInfo']
            if session.get('isFollowUp'):
                info_parts.append(f"")
                info_parts.append(f"💬 This is a follow-up question (question #{session.get('questionsAsked', 0)+1} about this element)")
        
        return "\n".join(info_parts)
    
    def _is_question_about_element(self, message: str) -> bool:
        """🆕 Detect if message is a question about the element (not an action request)."""
        message_lower = message.lower().strip()
        
        # Question patterns in Hindi/Hinglish/English
        question_patterns = [
            # Hindi/Hinglish
            'kya hai', 'ye kya hai', 'yeh kya hai', 'kya hai ye',
            'isme kya hai', 'isme kya likha', 'kya likha hai', 'likha kya hai',
            'batao', 'bata do', 'batana', 'describe karo',
            'kaisa hai', 'kaisa dikh raha', 'styles kya',
            # English
            'what is this', 'what does this', 'what is written',
            'describe', 'tell me about', 'what text', 'what content',
            'show me', 'explain'
        ]
        
        return any(pattern in message_lower for pattern in question_patterns)
    
    def _enrich_message_with_context(self, message: str, element: Optional[Dict], history: List) -> str:
        """🆕 Add context to message for better AI understanding."""
        enriched = message
        
        # If element is selected, remind AI about it
        if element and element.get('tagName'):
            tag = element.get('tagName', 'element').upper()
            text_preview = element.get('text', '')[:50]
            if text_preview:
                enriched = f"[Context: User is asking about a {tag} element with text '{text_preview}...'] {message}"
            else:
                enriched = f"[Context: User is asking about a {tag} element] {message}"
        
        return enriched
    
    def _infer_element_from_context(
        self, 
        message: str, 
        blueprint: Dict[str, Any], 
        html_content: str
    ) -> Optional[Dict[str, Any]]:
        """
        🆕 Infer which element user wants to edit based on message context.
        Searches HTML to find matching element without explicit selection.
        """
        message_lower = message.lower()
        
        # 1. Detect element type from message keywords
        element_hints = {
            'button': ['button', 'btn', 'cta', 'click', 'action button'],
            'heading': ['heading', 'title', 'headline', 'h1', 'h2', 'h3', 'main title', 'header text'],
            'text': ['text', 'paragraph', 'description', 'content', 'para'],
            'link': ['link', 'anchor', 'url', 'href'],
            'image': ['image', 'img', 'photo', 'picture', 'logo'],
            'nav': ['navigation', 'menu', 'navbar', 'nav'],
            'hero': ['hero', 'banner', 'main section', 'top section'],
            'footer': ['footer', 'bottom'],
            'card': ['card', 'box', 'item']
        }
        
        detected_type = None
        for elem_type, keywords in element_hints.items():
            if any(kw in message_lower for kw in keywords):
                detected_type = elem_type
                break
        
        print(f"[EnhancedChatbotService] 🔍 Detected element type: {detected_type}")
        
        if not detected_type:
            # Try to detect from common action patterns
            if any(word in message_lower for word in ['buy', 'shop', 'order', 'subscribe', 'sign up', 'get started', 'explore', 'click', 'story']):
                detected_type = 'button'
            elif any(word in message_lower for word in ['welcome', 'headline', 'main']):
                detected_type = 'heading'
            # 🆕 Check for "ka text" pattern - likely edit request for some element
            elif 'ka text' in message_lower or "text change" in message_lower or "text ko" in message_lower:
                detected_type = 'button'  # Default to button for text edits
            # 🆕 Check for text editing keywords in Hindi/English
            elif any(word in message_lower for word in ['change', 'update', 'replace', 'karo', 'kardo', 'likho', 'likh do', 'badal', 'badlo']):
                detected_type = 'button'  # Default to button when editing something
            # 🆕 Check for quoted text - user wants to set this text on something
            elif "'" in message or '"' in message:
                detected_type = 'button'  # Default assumption when user provides new text
        
        # 🆕 Still no type? For edit_text actions, default to button search
        if not detected_type:
            print(f"[EnhancedChatbotService] ⚠️ Could not detect element type from message")
            return None
        
        # 2. Search HTML for matching element
        from bs4 import BeautifulSoup
        import re
        
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            target_element = None
            
            # 🆕 Try to extract specific text from message for matching
            # e.g., "explore ka button" -> look for button with text "explore"
            text_patterns = [
                r"['\"]([^'\"]+)['\"]",  # Quoted text
                r"(\w+)\s+ka\s+(?:button|text|heading)",  # "explore ka button"
                r"(\w+)\s+button",  # "explore button"
                r"button\s+(\w+)",  # "button explore"
            ]
            target_text = None
            for pattern in text_patterns:
                match = re.search(pattern, message_lower)
                if match:
                    target_text = match.group(1).strip()
                    break
            
            print(f"[EnhancedChatbotService] 🔍 Target text from message: {target_text}")
            
            if detected_type == 'button':
                # 🆕 First, try to find button with specific text
                if target_text:
                    # Find button/link containing the target text
                    for btn in soup.find_all(['button', 'a']):
                        btn_text = btn.get_text(strip=True).lower()
                        if target_text.lower() in btn_text:
                            target_element = btn
                            print(f"[EnhancedChatbotService] ✅ Found button with text '{btn_text}'")
                            break
                
                # Fallback: find first button or CTA-like element
                if not target_element:
                    target_element = soup.find('button')
                if not target_element:
                    # Try link with button-like classes
                    target_element = soup.find('a', class_=lambda x: x and any(
                        cls in str(x).lower() for cls in ['btn', 'button', 'cta']
                    ))
            
            elif detected_type == 'heading':
                # Find first significant heading
                for tag in ['h1', 'h2', 'h3']:
                    target_element = soup.find(tag)
                    if target_element:
                        break
            
            elif detected_type == 'text':
                # Find first paragraph with substantial content
                for p in soup.find_all('p'):
                    if len(p.get_text(strip=True)) > 20:
                        target_element = p
                        break
            
            elif detected_type == 'link':
                target_element = soup.find('a')
            
            elif detected_type == 'image':
                target_element = soup.find('img')
            
            elif detected_type == 'hero':
                # Find hero section
                target_element = soup.find(['section', 'div'], class_=lambda x: x and 'hero' in str(x).lower())
            
            if target_element:
                # Build element info dict
                return {
                    'tagName': target_element.name,
                    'id': target_element.get('id', ''),
                    'classes': ' '.join(target_element.get('class', [])),
                    'text': target_element.get_text(strip=True)[:200],
                    'elementType': detected_type
                }
                
        except Exception as e:
            print(f"[EnhancedChatbotService] ⚠️ Error parsing HTML: {e}")
        
        return None
    
    
    def _direct_html_text_replace(
        self,
        html_content: str,
        old_text: Optional[str],
        new_text: str,
        message: str
    ) -> Dict[str, Any]:
        """
        🆕 Direct HTML text replacement without element selection.
        Searches for text in HTML and replaces it.
        """
        from bs4 import BeautifulSoup
        import re
        
        if not html_content or not new_text:
            return {"success": False, "message": "Missing HTML or new text"}
        
        try:
            # 1. Extract old text from message if not provided
            if not old_text:
                # Try to find text patterns like:
                # "change X to Y" / "X ko Y karo" / "replace X with Y"
                patterns = [
                    r"['\"]([^'\"]+)['\"].*(?:to|ko|with|se).*['\"]([^'\"]+)['\"]",  # "old" to "new"
                    r"change\s+['\"]?([^'\"]+?)['\"]?\s+(?:to|ko)\s+['\"]?([^'\"]+)['\"]?",  # change old to new
                    r"replace\s+['\"]?([^'\"]+?)['\"]?\s+(?:with|se)\s+['\"]?([^'\"]+)['\"]?",  # replace old with new
                    r"['\"]([^'\"]+)['\"]",  # Just quoted text (new text only)
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, message, re.IGNORECASE)
                    if match:
                        if len(match.groups()) >= 2:
                            old_text = match.group(1).strip()
                            # new_text is already provided from AI
                            print(f"[DirectReplace] Extracted: old='{old_text}', new='{new_text}'")
                        break
            
            soup = BeautifulSoup(html_content, 'html.parser')
            replaced = False
            replaced_in = []
            
            # 2. If we have old_text, try to find and replace it
            if old_text and old_text.strip():
                # Search in text content of all elements
                for elem in soup.find_all(text=True):
                    parent = elem.parent
                    # Skip script/style tags
                    if parent.name in ['script', 'style', 'head', 'meta', 'link']:
                        continue
                    
                    if old_text.lower() in str(elem).lower():
                        # Replace text (case-insensitive match but preserve case in new text)
                        original = str(elem)
                        # Use regex for case-insensitive replacement
                        new_val = re.sub(re.escape(old_text), new_text, original, flags=re.IGNORECASE)
                        elem.replace_with(new_val)
                        replaced = True
                        replaced_in.append(parent.name)
                        print(f"[DirectReplace] Replaced '{old_text}' with '{new_text}' in <{parent.name}>")
            
            # 3. If no old_text or replacement failed, try common button patterns
            if not replaced:
                # Look for buttons with common CTA text and replace with new_text
                common_cta_texts = ['get started', 'learn more', 'explore', 'shop now', 
                                    'sign up', 'subscribe', 'buy now', 'order now',
                                    'view demo', 'try free', 'download', 'contact us']
                
                for btn in soup.find_all(['button', 'a']):
                    btn_text = btn.get_text(strip=True).lower()
                    # Check if message mentions this button
                    if any(cta in btn_text for cta in common_cta_texts):
                        # Check if user's message references this button's text
                        if any(word in message.lower() for word in btn_text.split()):
                            print(f"[DirectReplace] Found matching button: '{btn.get_text(strip=True)}'")
                            btn.string = new_text
                            replaced = True
                            replaced_in.append(f"button ({btn_text})")
                            break
            
            # 4. Last resort: Find first button and replace its text
            if not replaced and ('button' in message.lower() or 'btn' in message.lower()):
                first_btn = soup.find(['button'])
                if first_btn:
                    old_btn_text = first_btn.get_text(strip=True)
                    first_btn.string = new_text
                    replaced = True
                    replaced_in.append(f"first button ({old_btn_text})")
                    print(f"[DirectReplace] Updated first button text to '{new_text}'")
            
            if replaced:
                return {
                    "success": True,
                    "html": str(soup),
                    "message": f"Text updated in: {', '.join(replaced_in)}"
                }
            else:
                return {
                    "success": False,
                    "message": f"Could not find text to replace. Please select the element or be more specific."
                }
                
        except Exception as e:
            print(f"[DirectReplace] Error: {e}")
            return {"success": False, "message": f"Error: {str(e)}"}
    
    
    def _fallback_response(self, message: str, has_element: bool) -> Dict[str, Any]:
        """Generate fallback response."""
        mode = "element" if has_element else "blueprint"
        return {
            "response": message,
            "actions_taken": [],
            "blueprint_updated": False,
            "html_updated": False,
            "updated_html": None,
            "suggestions": None,
            "intent": "general",
            "mode": mode
        }


# Singleton instance
_enhanced_chatbot_instance: Optional[EnhancedChatbotService] = None


def get_enhanced_chatbot_service() -> EnhancedChatbotService:
    """Get or create enhanced chatbot service singleton instance."""
    global _enhanced_chatbot_instance
    if _enhanced_chatbot_instance is None:
        _enhanced_chatbot_instance = EnhancedChatbotService()
    return _enhanced_chatbot_instance
