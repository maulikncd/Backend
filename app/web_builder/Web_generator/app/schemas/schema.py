"""
Schemas for Web_generator module
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class BlueprintRequest(BaseModel):
    session_id: str
    force_regenerate: Optional[bool] = False  # If True, delete old blueprint and regenerate fresh

class GenerateRequest(BaseModel):
    session_id: str
    blueprint: Optional[Dict[str, Any]] = None
    force_regenerate: Optional[bool] = False  # If True, ignore cached code and regenerate from Blueprint

class ChatMessageRequest(BaseModel):
    session_id: str
    message: str

class DraftCodeRequest(BaseModel):
    session_id: str
    component: str
    requirements: Optional[Dict[str, Any]] = None

class SaveCodeRequest(BaseModel):
    session_id: str
    code: str
    file_path: str

class UpdatePropertyRequest(BaseModel):
    """Request to update a property in Blueprint from PropertiesPanel."""
    session_id: str
    component_id: str  # e.g., "hero", "about", "menu"
    field: str  # e.g., "title", "description", "subtitle"
    value: Any  # The new value
    element_info: Optional[Dict[str, Any]] = None  # Additional element context

class ApplyChangesRequest(BaseModel):
    """Request to save Blueprint and regenerate code."""
    session_id: str
    regenerate_code: bool = True  # Whether to regenerate HTML from Blueprint

class UndoRedoRequest(BaseModel):
    session_id: str

class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    message: str
    timestamp: Optional[str] = None

class ChatHistoryRequest(BaseModel):
    session_id: str
    messages: List[ChatMessage]

class BlueprintResponse(BaseModel):
    blueprint: Dict[str, Any]

class GenerateResponse(BaseModel):
    code: str
    status: str

class ChatResponse(BaseModel):
    response: str

class DraftCodeResponse(BaseModel):
    """Response from draft code generation with version info."""
    draft: str
    version: int = 1
    can_undo: bool = False
    can_redo: bool = False
    status: str = "generated"

class SaveCodeResponse(BaseModel):
    """Response from save code with draft cleanup info."""
    status: str
    file_path: str
    drafts_cleared: bool = True
    success: bool = True

class UndoRedoResponse(BaseModel):
    """Response from undo/redo with code and version info."""
    status: str
    code: str
    version: int = 1
    can_undo: bool = False
    can_redo: bool = False

class LatestCodeResponse(BaseModel):
    """Response for get latest code endpoint."""
    code: str
    source: str = "draft"  # "draft" or "saved"
    version: int = 1
    can_undo: bool = False
    can_redo: bool = False
    success: bool = True

class ChatHistoryResponse(BaseModel):
    chat_history: List[ChatMessage]

class ChatSaveRequest(BaseModel):
    uid: int
    session_id: str
    chat_id: str
    conversion_id: int
    user_input: str
    AI_response: str

class UserChatHistoryRequest(BaseModel):
    uid: int

class ChatByIdRequest(BaseModel):
    uid: int
    chat_id: str


# Enhanced Chatbot Response Schemas
class ChatbotAction(BaseModel):
    """Represents an action taken by the chatbot on the blueprint."""
    type: str  # "edit", "add", "remove"
    component: str  # Component that was modified
    field: Optional[str] = None  # Field that was changed (for edits)
    message: str  # Human-readable description


class EnhancedChatResponse(BaseModel):
    """Enhanced response from AI-powered chatbot."""
    response: str  # AI message to user
    actions_taken: List[ChatbotAction] = []
    blueprint_updated: bool = False
    suggestions: Optional[List[str]] = None
    intent: str = "general"  # suggestion, edit, add, remove, general


class SuggestionItem(BaseModel):
    """A single improvement suggestion."""
    title: str
    description: str
    component: Optional[str] = None
    priority: str = "medium"  # high, medium, low


class SuggestionsResponse(BaseModel):
    """Response containing improvement suggestions."""
    suggestions: List[SuggestionItem] = []


# ============================================================
# CONVERSATION & HISTORY SCHEMAS
# ============================================================

class CreateConversationRequest(BaseModel):
    """Request to create a new conversation."""
    session_id: str
    title: Optional[str] = None  # Auto-generated if not provided


class CreateConversationResponse(BaseModel):
    """Response after creating a conversation."""
    conversation_id: str
    session_id: str
    title: str
    created_at: str


class ConversationListItem(BaseModel):
    """Single conversation for history sidebar."""
    conversation_id: str
    title: str
    last_message: Optional[str] = None
    message_count: int = 0
    created_at: str
    updated_at: str


class ConversationListResponse(BaseModel):
    """Response with list of conversations for sidebar."""
    conversations: List[ConversationListItem] = []
    total_count: int = 0


class MessageItem(BaseModel):
    """Single message in a conversation."""
    message_id: str
    role: str  # "user" or "assistant"
    content: str
    message_type: str = "text"  # text, suggestion, code_change, blueprint_change
    metadata: Optional[Dict[str, Any]] = None
    created_at: str


class ConversationMessagesResponse(BaseModel):
    """Response with all messages in a conversation."""
    conversation_id: str
    title: str
    messages: List[MessageItem] = []


class SelectedElementData(BaseModel):
    """Data about the currently selected element for chatbot context."""
    tagName: str
    id: Optional[str] = None
    classes: Optional[str] = None
    text: Optional[str] = None
    src: Optional[str] = None
    href: Optional[str] = None
    styles: Optional[Dict[str, Any]] = None
    elementType: Optional[str] = None
    sessionInfo: Optional[Dict[str, Any]] = None


class EnhancedChatMessageRequest(BaseModel):
    """Enhanced chat request with conversation and element support."""
    session_id: str
    message: str
    conversation_id: Optional[str] = None  # If None, creates new conversation
    selected_element: Optional[SelectedElementData] = None  # If element is selected
    html_content: Optional[str] = None  # Current HTML for element editing


class EnhancedChatMessageResponse(BaseModel):
    """Enhanced chat response with full details including element edits."""
    response: str
    conversation_id: str
    message_id: str
    actions_taken: List[Dict[str, Any]] = []
    blueprint_updated: bool = False
    code_updated: bool = False
    html_updated: bool = False  # True if HTML was directly modified
    updated_html: Optional[str] = None  # Updated HTML content if html_updated
    suggestions: Optional[List[str]] = None
    intent: str = "general"
    mode: str = "conversation"  # conversation, element, blueprint


class UpdateConversationTitleRequest(BaseModel):
    """Request to update conversation title."""
    title: str


class DeleteConversationResponse(BaseModel):
    """Response after deleting a conversation."""
    success: bool
    message: str
