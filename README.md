# Memory-Powered AI Assistant
## Complete Implementation Guide

Version: 1.0

---

# 1. Project Overview

## Objective

Build a production-ready AI Assistant similar to ChatGPT with:

- User Authentication
- Persistent Memory
- Multi-Session Conversations
- PDF & Document Chat
- Retrieval Augmented Generation (RAG)
- Web Search Capability
- Secure User Isolation
- Modern Responsive UI
- GitHub Deployment Workflow
- Docker Containerization
- Hugging Face Spaces Deployment

---

# 2. Technology Stack

## Frontend

- React
- Vite
- TailwindCSS
- ShadCN UI
- React Router
- Axios
- Framer Motion

---

## Backend

- FastAPI
- Uvicorn
- Pydantic
- Python 3.12+

---

## AI Layer

- Gemini API (Google AI Studio)

Responsibilities:

- Chat completion
- Response generation
- Context understanding
- Tool orchestration

---

## Vector Database

- ChromaDB

Responsibilities:

- Knowledge retrieval
- Memory retrieval
- Document search

---

## Authentication

- Firebase Authentication

Providers:

- Google Sign-In
- Email & Password

---

## Database

- Firestore

Stores:

- User Profiles
- Conversations
- Metadata
- Preferences

---

## Hosting

- Hugging Face Spaces

Type:

- Docker Space

---

# 3. System Architecture

```text
Frontend
   │
   ▼
FastAPI Backend
   │
   ├──── Gemini
   │
   ├──── Chroma
   │
   ├──── Firestore
   │
   └──── Web Search
```

---

# 4. Security Requirements

## User Isolation

Every user must have:

```text
user_id
```

associated with:

```text
memory
documents
conversations
embeddings
```

Never query without filtering:

```python
where={"user_id": current_user}
```

---

## Secrets

Never store:

```env
API_KEYS
FIREBASE_KEYS
JWT_SECRETS
```

inside code.

Create:

```env
.env
.env.production
```

Add to:

```gitignore
.env*
```

---

## Uploaded Files

Store privately.

Never:

```text
Public URL
Anonymous Access
```

---

# 5. Repository Structure

```text
ai-assistant/
│
├── frontend/
│
├── backend/
│
├── chroma_db/
│
├── uploads/
│
├── docs/
│
├── tests/
│
├── Dockerfile
│
├── docker-compose.yml
│
├── .env
│
└── README.md
```

---

# 6. Frontend Setup

## Create Project

```bash
npm create vite@latest frontend
```

Select:

```text
React
JavaScript
```

Install:

```bash
npm install
```

---

## Install Dependencies

```bash
npm install axios
npm install react-router-dom
npm install firebase
npm install framer-motion
```

---

## Tailwind

Install:

```bash
npm install -D tailwindcss
```

Initialize:

```bash
npx tailwindcss init -p
```

---

# 7. Frontend Pages

Create:

```text
src/pages
```

Pages:

```text
Login.jsx
Dashboard.jsx
Chat.jsx
Settings.jsx
Documents.jsx
```

---

# 8. Frontend Components

Create:

```text
components/
```

Components:

```text
Sidebar
Navbar
ChatWindow
MessageBubble
UploadModal
SearchBar
MemoryPanel
SettingsPanel
```

---

# 9. Chat Interface Design

Layout:

```text
┌───────────────┬────────────────┐
│ Sidebar       │ Chat Window    │
│ Conversations │                │
│ Documents     │ Messages       │
│ Settings      │                │
└───────────────┴────────────────┘
```

Features:

- Auto scroll
- Regenerate
- Copy response
- Markdown support
- Code blocks

---

# 10. Firebase Setup

Create:

```text
Firebase Project
```

Enable:

```text
Authentication
Firestore
```

---

## Authentication

Enable:

```text
Google
Email/Password
```

---

## Firestore Collections

```text
users
conversations
messages
settings
```

---

# 11. Firestore Schema

## Users

```json
{
  "uid": "",
  "email": "",
  "created_at": "",
  "last_login": ""
}
```

---

## Conversations

```json
{
  "conversation_id": "",
  "user_id": "",
  "title": ""
}
```

---

## Messages

```json
{
  "conversation_id": "",
  "role": "",
  "content": "",
  "timestamp": ""
}
```

---

# 12. Backend Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate environment.

Install:

```bash
pip install fastapi
pip install uvicorn
pip install python-dotenv
pip install chromadb
pip install google-genai
pip install firebase-admin
```

---

# 13. FastAPI Structure

```text
backend/
│
├── main.py
├── routes/
├── services/
├── rag/
├── memory/
├── auth/
├── models/
└── utils/
```

---

# 14. API Endpoints

## Authentication

```text
POST /auth/login
POST /auth/logout
```

---

## Chat

```text
POST /chat
GET /chat/history
DELETE /chat/history
```

---

## Documents

```text
POST /documents/upload
GET /documents
DELETE /documents/{id}
```

---

# 15. Gemini Integration

Create:

```text
services/gemini_service.py
```

Responsibilities:

- Build prompts
- Call Gemini
- Parse responses
- Stream responses

---

# 16. Document Upload Pipeline

Flow:

```text
Upload
↓
Save
↓
Parse
↓
Chunk
↓
Embed
↓
Store
```

---

# 17. PDF Parsing

Install:

```bash
pip install pypdf
```

Extract:

```text
Raw Text
Metadata
Page Count
```

---

# 18. Chunking Strategy

Recommended:

```text
Chunk Size: 1000
Overlap: 200
```

Purpose:

```text
Context retention
```

---

# 19. Embeddings

Use:

```text
Google Embeddings
or
Sentence Transformers
```

Store:

```text
Chunk
Vector
Metadata
```

---

# 20. ChromaDB Setup

Collections:

```text
documents
memory
chat_history
```

---

Metadata:

```json
{
  "user_id": "...",
  "document_id": "...",
  "source": "pdf"
}
```

---

# 21. Retrieval Flow

```text
Question
↓
Embed Question
↓
Search Chroma
↓
Top K Results
↓
Build Context
↓
Gemini
```

Default:

```text
k = 5
```

---

# 22. Memory System

Types:

## Short Term

Current conversation.

---

## Long Term

Stored facts.

Example:

```text
Favourite Language
Project Name
Personal Preferences
```

---

# 23. Memory Extraction

After each assistant response:

```text
Analyze Conversation
↓
Identify Facts
↓
Store Facts
```

Store as:

```json
{
  "fact": "",
  "confidence": 0.95
}
```

---

# 24. Web Search

Only trigger when:

```text
Information may be outdated
```

Examples:

```text
News
Prices
Documentation
Releases
```

Workflow:

```text
Question
↓
Search
↓
Summarize
↓
Gemini
```

---

# 25. Prompt Engineering

Prompt Structure:

```text
System Prompt

Retrieved Memory

Retrieved Documents

Web Results

Current Question
```

---

# 26. Conversation Titles

Generate automatically.

Prompt:

```text
Summarize this conversation in 5 words.
```

---

# 27. Error Handling

Create:

```text
Global Exception Middleware
```

Handle:

```text
API failures
Timeouts
Missing files
Auth errors
```

---

# 28. Logging

Use:

```bash
pip install loguru
```

Create logs:

```text
chat.log
error.log
system.log
```

---

# 29. Rate Limiting

Apply:

```text
User
IP
Endpoint
```

Examples:

```text
30 requests/min
```

---

# 30. Deployment

Dockerize application.

Build:

```bash
docker build -t ai-assistant .
```

Run:

```bash
docker run -p 7860:7860 ai-assistant
```

Push:

```text
GitHub
```

Connect:

```text
Hugging Face Space
```

---

# 31. Production Checklist

## Functional

- Login works
- Logout works
- Chat works
- Memory works
- PDF search works
- Web search works

---

## Security

- Secrets protected
- Firestore rules configured
- User isolation verified

---

## Performance

- Fast retrieval
- Cached responses
- Optimized queries

---

# 32. MVP Completion Criteria

A user can:

1. Register
2. Login
3. Chat with Gemini
4. Upload PDF
5. Ask questions about PDF
6. Retrieve previous conversations
7. Be remembered across sessions
8. Use web search
9. Access only their data

Project status:

```text
Production Ready
```


==================Security Rules==============
collection.query(
    query_embeddings=[embedding],
    where={
        "user_id": 
