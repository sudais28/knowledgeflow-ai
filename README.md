# KnowledgeFlow AI

> Enterprise AI Knowledge Platform powered by FastAPI, LangChain, LangGraph, FAISS, PostgreSQL, and Groq.

KnowledgeFlow AI is a production-ready Retrieval-Augmented Generation (RAG) platform that enables organizations to upload documents and interact with them using natural language. The platform combines semantic search, Large Language Models (LLMs), and modern backend engineering practices to deliver accurate, source-grounded responses.

Unlike a basic chatbot, KnowledgeFlow AI is designed with scalability, modularity, and maintainability in mind, following a layered architecture similar to production AI systems.

---

# Features

## Authentication

- JWT Authentication
- User Registration
- User Login
- Secure Password Hashing
- Protected API Endpoints

---

## Document Management

- Upload PDF
- Upload DOCX
- Upload TXT
- Upload Markdown Files
- Delete Documents
- View Uploaded Documents
- Multi-document Support

---

## AI & RAG

- Semantic Search
- Retrieval-Augmented Generation (RAG)
- HuggingFace Embeddings
- FAISS Vector Database
- Groq LLM Integration
- Context-aware Responses
- Source Citations
- Conversation History

---

## Backend

- FastAPI
- REST API
- Pydantic Validation
- SQLAlchemy ORM
- PostgreSQL
- Async Endpoints
- Environment Configuration

---

## Frontend (Coming Soon)

- React
- Tailwind CSS
- Chat Interface
- Drag & Drop Upload
- Authentication Pages
- Chat History
- Responsive Design

---

## DevOps

- Docker
- Docker Compose
- GitHub Actions
- Environment Variables
- Logging
- Health Checks

---

# Tech Stack

| Category | Technologies |
|-----------|-------------|
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| AI | LangChain, LangGraph |
| LLM | Groq (Llama 3.1) |
| Embeddings | HuggingFace Sentence Transformers |
| Vector Database | FAISS |
| Frontend | React, Tailwind CSS |
| Deployment | Docker, Railway, Vercel |

---

# System Architecture

```
                React Frontend
                      │
                      ▼
              FastAPI REST API
                      │
      ┌───────────────┼────────────────┐
      │               │                │
 Authentication   Chat Service   Upload Service
      │               │                │
 PostgreSQL      LangGraph Agent  Document Loader
      │               │                │
      └───────────────┼────────────────┘
                      │
              Text Splitter
                      │
              HuggingFace Embeddings
                      │
                   FAISS
                      │
                Groq LLM
                      │
              Final AI Response
```

---

# Project Structure

```
knowledgeflow-ai
│
├── backend
│   ├── app
│   ├── api
│   ├── auth
│   ├── config
│   ├── database
│   ├── models
│   ├── schemas
│   ├── services
│   ├── agents
│   ├── prompts
│   ├── vectorstore
│   ├── utils
│   └── main.py
│
├── frontend
│
├── docs
│
├── architecture
│
├── screenshots
│
├── docker-compose.yml
│
├── Dockerfile
│
├── requirements.txt
│
├── .env.example
│
└── README.md
```

---

# Roadmap

## Phase 1

- [ ] Project Setup
- [ ] FastAPI
- [ ] Configuration
- [ ] Docker
- [ ] PostgreSQL

---

## Phase 2

- [ ] JWT Authentication
- [ ] User Registration
- [ ] Login
- [ ] Protected Routes

---

## Phase 3

- [ ] PDF Upload
- [ ] DOCX Upload
- [ ] TXT Upload
- [ ] Document Storage

---

## Phase 4

- [ ] Embeddings
- [ ] FAISS Indexing
- [ ] Semantic Search
- [ ] RAG Pipeline

---

## Phase 5

- [ ] LangGraph Agent
- [ ] Conversation Memory
- [ ] Source Citations
- [ ] Streaming Responses

---

## Phase 6

- [ ] React Frontend
- [ ] Chat Interface
- [ ] File Management
- [ ] User Dashboard

---

## Phase 7

- [ ] Docker Compose
- [ ] GitHub Actions
- [ ] Cloud Deployment
- [ ] Monitoring

---

# API Endpoints

## Authentication

```
POST /auth/register
POST /auth/login
GET  /auth/me
```

---

## Documents

```
POST   /documents/upload
GET    /documents
DELETE /documents/{id}
```

---

## Chat

```
POST /chat
GET  /chat/history
DELETE /chat/history
```

---

## System

```
GET /health
GET /docs
```

---

# Installation

```bash
git clone https://github.com/<your-username>/knowledgeflow-ai.git

cd knowledgeflow-ai

python -m venv .venv

source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key
DATABASE_URL=postgresql://...
SECRET_KEY=your_secret_key
```

Run the application

```bash
uvicorn app.main:app --reload
```

---

# Future Enhancements

- Multi-Agent Architecture
- OCR Support
- Image Understanding
- Audio Transcription
- YouTube Knowledge Base
- Website Crawler
- Role-Based Access Control
- Hybrid Search
- Redis Caching
- Elasticsearch Integration

---

# License

This project is licensed under the MIT License.

---

# Author

**Sudais Touseef**

Computer Science Graduate | AI Engineer | Backend Developer

Interested in building scalable AI systems, intelligent agents, Retrieval-Augmented Generation (RAG), and production-ready backend applications.
