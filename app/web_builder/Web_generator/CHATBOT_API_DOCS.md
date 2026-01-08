# 🤖 Chatbot & Conversation History System - API Documentation

## Overview
This document provides complete API reference for the chatbot and conversation history system. Use these endpoints to implement the chat UI with sidebar history.

---

## 📡 Base URL
```
http://localhost:4000/web-generator
```

All endpoints require authentication via Bearer token in the header:
```javascript
headers: {
  'Authorization': `Bearer ${token}`,
  'Content-Type': 'application/json'
}
```

---

## 🗂️ API Endpoints Reference

### 1️⃣ GET `/conversations/{session_id}` - List All Conversations (Sidebar)

**Purpose:** Load conversation history for the sidebar when chat panel opens.

**URL:** `GET /web-generator/conversations/{session_id}?limit=50`

**Response:**
```json
{
  "conversations": [
    {
      "conversation_id": "conv_abc123xyz",
      "title": "Change website name",
      "last_message": "Done! I've updated your website name to...",
      "message_count": 4,
      "created_at": "2026-01-05T16:50:00",
      "updated_at": "2026-01-05T17:30:00"
    }
  ],
  "total_count": 5
}
```

**Frontend Usage:**
```javascript
const loadConversationHistory = async (sessionId) => {
  const response = await fetch(`${API_BASE}/web-generator/conversations/${sessionId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const data = await response.json();
  setConversations(data.conversations);
};

// Call on chat panel open
useEffect(() => {
  if (chatPanelOpen) {
    loadConversationHistory(sessionId);
  }
}, [chatPanelOpen]);
```

---

### 2️⃣ POST `/conversation/new` - Create New Conversation

**Purpose:** Called when user clicks the "+" button to start a fresh chat.

**URL:** `POST /web-generator/conversation/new`

**Request Body:**
```json
{
  "session_id": "your-session-id",
  "title": "Optional custom title"  // Optional, auto-generated if not provided
}
```

**Response:**
```json
{
  "conversation_id": "conv_new123abc",
  "session_id": "your-session-id",
  "title": "New Conversation",
  "created_at": "2026-01-05T17:00:00"
}
```

**Frontend Usage:**
```javascript
const handleNewConversation = async () => {
  const response = await fetch(`${API_BASE}/web-generator/conversation/new`, {
    method: 'POST',
    headers: { 
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ session_id: sessionId })
  });
  const data = await response.json();
  
  // Set the new conversation as active
  setActiveConversationId(data.conversation_id);
  setMessages([]);  // Clear messages for new chat
  
  // Refresh sidebar
  loadConversationHistory(sessionId);
};
```

---

### 3️⃣ GET `/conversation/{conversation_id}` - Get Conversation Messages

**Purpose:** Load all messages when user clicks on a conversation in history.

**URL:** `GET /web-generator/conversation/{conversation_id}?limit=100&offset=0`

**Response:**
```json
{
  "conversation_id": "conv_abc123xyz",
  "title": "Change website name",
  "messages": [
    {
      "message_id": "msg_user123",
      "role": "user",
      "content": "Change my website name to TechCo",
      "message_type": "text",
      "metadata": null,
      "created_at": "2026-01-05T16:50:00"
    },
    {
      "message_id": "msg_asst456",
      "role": "assistant",
      "content": "Done! I've updated your website name to 'TechCo'.",
      "message_type": "blueprint_change",
      "metadata": {
        "actions_taken": [
          {
            "type": "edit",
            "component": "root",
            "field": "projectName",
            "message": "Updated projectName to 'TechCo'"
          }
        ],
        "blueprint_updated": true,
        "intent": "edit"
      },
      "created_at": "2026-01-05T16:50:05"
    }
  ]
}
```

**Frontend Usage:**
```javascript
const loadConversation = async (conversationId) => {
  const response = await fetch(`${API_BASE}/web-generator/conversation/${conversationId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const data = await response.json();
  
  setActiveConversationId(conversationId);
  setConversationTitle(data.title);
  setMessages(data.messages);
};

// Call when user clicks on a conversation in sidebar
const handleHistoryItemClick = (conversationId) => {
  loadConversation(conversationId);
};
```

---

### 4️⃣ POST `/chat` - Send Chat Message (Main Endpoint)

**Purpose:** Send user message, get AI response with blueprint/code changes.

**URL:** `POST /web-generator/chat`

**Request Body:**
```json
{
  "session_id": "your-session-id",
  "message": "Change the primary color to blue",
  "conversation_id": "conv_abc123xyz"  // Optional - creates new if not provided
}
```

**Response:**
```json
{
  "response": "Done! I've updated your primary color to blue (#3B82F6).",
  "conversation_id": "conv_abc123xyz",
  "message_id": "msg_response789",
  "actions_taken": [
    {
      "type": "edit",
      "component": "theme",
      "field": "colorPalette.primary",
      "message": "Updated primary color to #3B82F6"
    }
  ],
  "blueprint_updated": true,
  "code_updated": false,
  "suggestions": [
    "Consider updating the secondary color to complement blue",
    "Add a gradient effect to your hero section"
  ],
  "intent": "edit"
}
```

**Frontend Usage:**
```javascript
const sendMessage = async (message) => {
  setIsLoading(true);
  
  // Add user message to UI immediately
  const userMsg = {
    role: 'user',
    content: message,
    message_type: 'text',
    created_at: new Date().toISOString()
  };
  setMessages(prev => [...prev, userMsg]);
  
  try {
    const response = await fetch(`${API_BASE}/web-generator/chat`, {
      method: 'POST',
      headers: { 
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        session_id: sessionId,
        message: message,
        conversation_id: activeConversationId  // null for new conv
      })
    });
    
    const data = await response.json();
    
    // If this was a new conversation, update the active ID
    if (!activeConversationId) {
      setActiveConversationId(data.conversation_id);
    }
    
    // Add assistant response to messages
    const assistantMsg = {
      role: 'assistant',
      content: data.response,
      message_type: data.blueprint_updated ? 'blueprint_change' : 'text',
      metadata: {
        actions_taken: data.actions_taken,
        blueprint_updated: data.blueprint_updated,
        suggestions: data.suggestions
      },
      created_at: new Date().toISOString()
    };
    setMessages(prev => [...prev, assistantMsg]);
    
    // If blueprint was updated, refresh preview
    if (data.blueprint_updated) {
      refreshPreview();
    }
    
    // Show suggestions if available
    if (data.suggestions) {
      setSuggestions(data.suggestions);
    }
    
  } catch (error) {
    console.error('Chat error:', error);
  } finally {
    setIsLoading(false);
  }
};
```

---

### 5️⃣ DELETE `/conversation/{conversation_id}` - Delete Conversation

**Purpose:** Delete a conversation from history.

**URL:** `DELETE /web-generator/conversation/{conversation_id}`

**Response:**
```json
{
  "success": true,
  "message": "Conversation deleted successfully"
}
```

**Frontend Usage:**
```javascript
const deleteConversation = async (conversationId) => {
  if (!confirm('Delete this conversation?')) return;
  
  const response = await fetch(`${API_BASE}/web-generator/conversation/${conversationId}`, {
    method: 'DELETE',
    headers: { 'Authorization': `Bearer ${token}` }
  });
  
  if (response.ok) {
    // Refresh sidebar
    loadConversationHistory(sessionId);
    
    // If current conversation was deleted, clear chat
    if (activeConversationId === conversationId) {
      setActiveConversationId(null);
      setMessages([]);
    }
  }
};
```

---

### 6️⃣ GET `/suggestions/{session_id}` - Get AI Suggestions

**Purpose:** Get improvement suggestions for the current blueprint.

**URL:** `GET /web-generator/suggestions/{session_id}`

**Response:**
```json
{
  "suggestions": [
    {
      "title": "Add testimonials section",
      "description": "Include customer testimonials to build trust",
      "component": "comp-testimonials",
      "priority": "high"
    },
    {
      "title": "Optimize hero headline",
      "description": "Make your headline more compelling",
      "component": "comp-home",
      "priority": "medium"
    }
  ]
}
```

---

## 🎨 Complete Frontend Implementation Example

### React Component Structure:
```jsx
const ChatPanel = ({ sessionId }) => {
  const [conversations, setConversations] = useState([]);
  const [activeConversationId, setActiveConversationId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Load conversations on mount
  useEffect(() => {
    loadConversationHistory(sessionId);
  }, [sessionId]);

  return (
    <div className="chat-panel">
      {/* Sidebar */}
      <div className="chat-sidebar">
        <button onClick={handleNewConversation}>
          + New Chat
        </button>
        
        <div className="conversation-list">
          {conversations.map(conv => (
            <div 
              key={conv.conversation_id}
              className={`conversation-item ${activeConversationId === conv.conversation_id ? 'active' : ''}`}
              onClick={() => loadConversation(conv.conversation_id)}
            >
              <span className="title">{conv.title}</span>
              <span className="preview">{conv.last_message}</span>
              <button onClick={(e) => {
                e.stopPropagation();
                deleteConversation(conv.conversation_id);
              }}>🗑️</button>
            </div>
          ))}
        </div>
      </div>

      {/* Chat Area */}
      <div className="chat-main">
        <div className="messages">
          {messages.map((msg, i) => (
            <ChatMessage key={i} message={msg} />
          ))}
          {isLoading && <TypingIndicator />}
        </div>

        <div className="chat-input">
          <input
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage(inputValue)}
            placeholder="Type your message..."
          />
          <button onClick={() => sendMessage(inputValue)}>Send</button>
        </div>
      </div>
    </div>
  );
};
```

---

## 📊 Flow Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    CHAT PANEL OPENED                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
               GET /conversations/{session_id}
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
    Has History          No History          Loading
         │                    │                    │
         ▼                    ▼                    ▼
   Display in           Show Empty           Spinner
   Sidebar              State
         │                    │
         └────────┬───────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
  Click +     Click on      User
  Button      History       Types
    │           Item          │
    │             │           │
    ▼             ▼           ▼
POST /new   GET /conv/{id}  POST /chat
    │             │           │
    │             │           │
    ▼             ▼           ▼
  New          Load        AI Response
  Conv ID      Messages    + Actions
    │             │           │
    └─────────────┴───────────┘
                  │
                  ▼
           Update UI
```

---

## 🔑 Key Points

1. **Always pass `session_id`** - Required for all operations
2. **`conversation_id` is optional for `/chat`** - Creates new if not provided
3. **Handle `blueprint_updated` flag** - Refresh preview when true
4. **Show suggestions** - Display as clickable chips user can apply
5. **Message types matter** - Use `message_type` for UI styling:
   - `text` - Normal text message
   - `blueprint_change` - Show with "✅ Blueprint Updated" badge
   - `code_change` - Show with "📝 Code Changed" badge
   - `suggestion` - Show with suggestion styling
