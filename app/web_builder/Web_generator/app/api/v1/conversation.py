"""
Conversation & Chat History API Endpoints
Handles conversation management, message storage, and history fetching
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
from app.Auth.core.dependencies import get_current_user
from app.Auth.models.user import User
from app.web_builder.Web_generator.app.crud.crud import get_session
from app.web_builder.Web_generator.app.crud.conversation_crud import (
    create_conversation,
    get_conversations_by_session,
    get_conversation,
    get_messages,
    save_message,
    delete_conversation,
    update_conversation_title,
    get_or_create_conversation,
    generate_title_from_message,
    get_recent_messages,
    get_conversation_count
)
from app.web_builder.Web_generator.app.schemas.schema import (
    CreateConversationRequest,
    CreateConversationResponse,
    ConversationListResponse,
    ConversationListItem,
    ConversationMessagesResponse,
    MessageItem,
    EnhancedChatMessageRequest,
    EnhancedChatMessageResponse,
    UpdateConversationTitleRequest,
    DeleteConversationResponse
)
from app.web_builder.Web_generator.app.services.chatbot import get_chatbot_service, get_enhanced_chatbot_service

router = APIRouter()


# ============================================================
# CONVERSATION MANAGEMENT ENDPOINTS
# ============================================================

@router.get("/conversations/{session_id}", response_model=ConversationListResponse)
def list_conversations(
    session_id: str,
    limit: int = Query(default=50, le=100),
    user: User = Depends(get_current_user)
):
    """
    Get all conversations for a session (sidebar history list).
    
    Returns conversations sorted by last activity (newest first).
    Each conversation includes:
    - conversation_id
    - title
    - last_message preview
    - message_count
    - timestamps
    """
    # Verify session access
    session = get_session(session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session access")
    
    # Get conversations
    conversations = get_conversations_by_session(session_id, user.user_id, limit)
    total = get_conversation_count(session_id, user.user_id)
    
    return ConversationListResponse(
        conversations=[
            ConversationListItem(**conv) for conv in conversations
        ],
        total_count=total
    )


@router.post("/conversation/new", response_model=CreateConversationResponse)
def create_new_conversation(
    data: CreateConversationRequest,
    user: User = Depends(get_current_user)
):
    """
    Create a new conversation for a session.
    
    Called when user clicks the "+" button to start a new chat.
    """
    # Verify session access
    session = get_session(data.session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session access")
    
    # Create conversation
    result = create_conversation(user.user_id, data.session_id, data.title)
    
    if "error" in result:
        raise HTTPException(500, result["error"])
    
    return CreateConversationResponse(
        conversation_id=result["conversation_id"],
        session_id=data.session_id,
        title=result["title"],
        created_at=result["created_at"]
    )


@router.get("/conversation/{conversation_id}", response_model=ConversationMessagesResponse)
def get_conversation_messages(
    conversation_id: str,
    limit: int = Query(default=100, le=500),
    offset: int = Query(default=0, ge=0),
    user: User = Depends(get_current_user)
):
    """
    Get all messages for a specific conversation.
    
    Called when user clicks on a conversation in the history sidebar.
    Returns all messages in chronological order.
    """
    # Get conversation and verify access
    conv = get_conversation(conversation_id, user.user_id)
    if not conv:
        raise HTTPException(404, "Conversation not found")
    
    # Get messages
    messages = get_messages(conversation_id, limit, offset)
    
    return ConversationMessagesResponse(
        conversation_id=conversation_id,
        title=conv["title"],
        messages=[MessageItem(**msg) for msg in messages]
    )


@router.patch("/conversation/{conversation_id}")
def update_conversation(
    conversation_id: str,
    data: UpdateConversationTitleRequest,
    user: User = Depends(get_current_user)
):
    """
    Update conversation title.
    """
    # Verify access
    conv = get_conversation(conversation_id, user.user_id)
    if not conv:
        raise HTTPException(404, "Conversation not found")
    
    success = update_conversation_title(conversation_id, data.title, user.user_id)
    
    if not success:
        raise HTTPException(500, "Failed to update conversation")
    
    return {"success": True, "title": data.title}


@router.delete("/conversation/{conversation_id}", response_model=DeleteConversationResponse)
def delete_conversation_endpoint(
    conversation_id: str,
    user: User = Depends(get_current_user)
):
    """
    Delete a conversation and all its messages.
    """
    # Verify access
    conv = get_conversation(conversation_id, user.user_id)
    if not conv:
        raise HTTPException(404, "Conversation not found")
    
    success = delete_conversation(conversation_id, user.user_id)
    
    if not success:
        raise HTTPException(500, "Failed to delete conversation")
    
    return DeleteConversationResponse(
        success=True,
        message="Conversation deleted successfully"
    )


# ============================================================
# ENHANCED CHAT MESSAGE ENDPOINT
# ============================================================

@router.post("/chat", response_model=EnhancedChatMessageResponse)
def send_chat_message(
    data: EnhancedChatMessageRequest,
    user: User = Depends(get_current_user)
):
    """
    Send a chat message and get AI response.
    
    This is the main chat endpoint that:
    1. Creates/uses conversation
    2. Saves user message
    3. Processes with AI (ChatbotService)
    4. Saves AI response
    5. Returns full response with actions
    
    If conversation_id is not provided, creates a new conversation.
    
    Returns:
        - response: AI message text
        - conversation_id: ID of the conversation
        - message_id: ID of the assistant's message
        - actions_taken: List of blueprint/code changes made
        - blueprint_updated: Whether blueprint was modified
        - code_updated: Whether code was modified
        - suggestions: Optional improvement suggestions
        - intent: Detected intent (edit, add, remove, general, etc.)
    """
    # Verify session access
    session = get_session(data.session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    
    session_user_id = session.get("user_id")
    if session_user_id and str(session_user_id) != str(user.user_id):
        raise HTTPException(403, "Unauthorized session access")
    
    print(f"[ChatEndpoint] 📩 Received message from user {user.user_id}, session: {data.session_id}")
    
    # Get or create conversation
    conversation = get_or_create_conversation(
        user.user_id, 
        data.session_id, 
        data.conversation_id
    )
    
    if "error" in conversation:
        raise HTTPException(500, conversation["error"])
    
    conversation_id = conversation["conversation_id"]
    is_new_conversation = data.conversation_id is None
    
    print(f"[ChatEndpoint] 💬 Using conversation: {conversation_id} (new: {is_new_conversation})")
    
    # Save user message
    user_msg = save_message(
        conversation_id=conversation_id,
        role="user",
        content=data.message,
        message_type="text"
    )
    
    if "error" in user_msg:
        print(f"[ChatEndpoint] ❌ Failed to save user message: {user_msg['error']}")
        raise HTTPException(500, "Failed to save message")
    
    print(f"[ChatEndpoint] ✅ Saved user message: {user_msg.get('message_id')}")
    
    # Update conversation title if first message
    if is_new_conversation:
        title = generate_title_from_message(data.message)
        update_conversation_title(conversation_id, title, user.user_id)
    
    # Get recent messages for context (last 30 messages for better context)
    recent_messages = get_recent_messages(conversation_id, 30)
    conversation_history = []
    for msg in recent_messages:
        conversation_history.append({
            "role": msg.get("role", "user"),
            "content": msg.get("content", "")
        })
    
    print(f"[ChatEndpoint] 📜 Loaded {len(conversation_history)} messages for context")
    
    # Determine which chatbot service to use
    # 🆕 Always use enhanced service - it handles both element mode AND infers elements from message
    has_element = data.selected_element is not None
    
    # 🆕 ALWAYS use enhanced chatbot - can infer elements from message context
    chatbot = get_enhanced_chatbot_service()
    
    # Convert Pydantic model to dict
    element_dict = data.selected_element.model_dump() if data.selected_element else None
    
    if has_element:
        # Element mode - user explicitly selected an element
        print(f"[ChatEndpoint] 🎯 Element mode - editing element:")
        print(f"  - TagName: {element_dict.get('tagName') if element_dict else 'None'}")
        print(f"  - Text: {(element_dict.get('text') or '')[:50]}..." if element_dict else "  - Text: None")
        print(f"  - ID: {element_dict.get('id') if element_dict else 'None'}")
        print(f"  - Session Info: {element_dict.get('sessionInfo') if element_dict else 'None'}")
    else:
        # No element selected - enhanced service will try to infer from message
        print(f"[ChatEndpoint] 🔍 No element selected - using smart inference mode")
        print(f"  - HTML content length: {len(data.html_content) if data.html_content else 0}")
    
    result = chatbot.process_message(
        session_id=data.session_id,
        message=data.message,
        user_id=user.user_id,
        selected_element=element_dict,
        html_content=data.html_content,
        conversation_history=conversation_history
    )
    
    # Determine message type based on actions
    message_type = "text"
    if result.get("html_updated"):
        message_type = "element_change"
    elif result.get("blueprint_updated"):
        message_type = "blueprint_change"
    elif result.get("actions_taken"):
        message_type = "code_change"
    elif result.get("suggestions"):
        message_type = "suggestion"
    
    # Prepare metadata
    metadata = {
        "actions_taken": result.get("actions_taken", []),
        "blueprint_updated": result.get("blueprint_updated", False),
        "html_updated": result.get("html_updated", False),
        "suggestions": result.get("suggestions"),
        "intent": result.get("intent", "general"),
        "mode": result.get("mode", "conversation")
    }
    
    # Save assistant message
    assistant_msg = save_message(
        conversation_id=conversation_id,
        role="assistant",
        content=result.get("response", ""),
        message_type=message_type,
        metadata=metadata
    )
    
    if "error" in assistant_msg:
        print(f"[ChatEndpoint] ❌ Failed to save assistant message: {assistant_msg['error']}")
        raise HTTPException(500, "Failed to save response")
    
    print(f"[ChatEndpoint] ✅ Saved assistant message: {assistant_msg.get('message_id')}")
    
    return EnhancedChatMessageResponse(
        response=result.get("response", ""),
        conversation_id=conversation_id,
        message_id=assistant_msg["message_id"],
        actions_taken=result.get("actions_taken", []),
        blueprint_updated=result.get("blueprint_updated", False),
        code_updated=False,
        html_updated=result.get("html_updated", False),
        updated_html=result.get("updated_html"),
        suggestions=result.get("suggestions"),
        intent=result.get("intent", "general"),
        mode=result.get("mode", "conversation")
    )


# ============================================================
# QUICK SUGGESTIONS ENDPOINT
# ============================================================

@router.get("/suggestions/{session_id}")
def get_chat_suggestions(
    session_id: str,
    conversation_id: Optional[str] = None,
    user: User = Depends(get_current_user)
):
    """
    Get AI-powered improvement suggestions for the blueprint.
    
    Can be called standalone or with a conversation context.
    Returns actionable suggestions the user can click to apply.
    """
    # Verify session access
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


# ============================================================
# BACKWARD COMPATIBLE ENDPOINT
# ============================================================

@router.post("/chat-message")
def chat_message_legacy(
    data: EnhancedChatMessageRequest,
    user: User = Depends(get_current_user)
):
    """
    Legacy endpoint for backward compatibility.
    Uses the new conversation system internally.
    
    Maps to POST /chat endpoint.
    """
    print(f"[LegacyChat] 🔄 Routing legacy /chat-message to new send_chat_message")
    return send_chat_message(data, user)
