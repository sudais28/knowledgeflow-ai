# KnowledgeFlow AI

> An AI Knowledge Platform built with FastAPI, PostgreSQL, LangChain, LangGraph, FAISS, and Groq.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

KnowledgeFlow AI is a production-inspired Retrieval-Augmented Generation (RAG) platform that enables users to upload documents, build a searchable knowledge base, and interact with their data using natural language.

The project is being developed using modern backend engineering practices, including modular architecture, environment-based configuration, SQLAlchemy ORM, JWT authentication, and scalable AI workflows.

---

# 🚧 Project Status

Current Version: v0.5

Current Sprint: Advanced RAG & Multi-Document Support (Sprint 5)

This project is actively being developed. New features are added incrementally following a production-style development workflow.

---

# ✅ Current Features

## Backend

- FastAPI Application
- Professional Project Architecture
- Environment Configuration (.env)
- SQLAlchemy ORM
- PostgreSQL Integration
- Database Session Management
- User Database Model
- Automatic Database Initialization
- Health Check Endpoint
- REST API Foundation
- Document Upload API
- Document CRUD API
- File Download API
- Ownership-based Authorization
- PDF Text Extraction
- Recursive Text Chunking
- HuggingFace Embedding Generation
- FAISS Vector Database
- Semantic Document Retrieval
- AI Chat Endpoint
- Groq Llama 3.1 Integration
  
---
## Authentication

- JWT Authentication
- User Registration
- User Login
- Password Hashing (bcrypt)
- JWT Access Token Generation
- Protected API Endpoints
- Current User Endpoint (`/auth/me`)
- Swagger OAuth2 Authentication
  
---

# 🚧 In Progress

- PDF Text Extraction
- Text Chunking
- Embedding Generation
- FAISS Vector Indexing
- Retrieval-Augmented Generation (RAG)
  
---

# 📅 Planned Features

## Document Management

- Upload PDF
- Upload DOCX
- Upload TXT
- Upload Markdown Files
- Delete Documents
- Multi-document Support
-  DOCX Upload
- TXT Upload
- Markdown Upload
- File Versioning (Optional)

---

## AI & RAG

- PDF Text Extraction
- Recursive Character Text Splitting
- HuggingFace Sentence Transformer Embeddings
- FAISS Local Vector Store
- Semantic Similarity Search
- Retrieval-Augmented Generation (RAG)
- Groq Llama 3.1 Integration
- Context-Aware Question Answering

---

## Frontend

- React
- Tailwind CSS
- Chat Interface
- Authentication Pages
- File Upload UI
- Chat History
- Responsive Dashboard

---

## DevOps

- Docker
- Docker Compose
- GitHub Actions
- CI/CD Pipeline
- Logging
- AWS Deployment

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|-------------|
| Backend | Python, FastAPI |
| Database | PostgreSQL, SQLAlchemy |
| AI Framework | LangChain, LangGraph |
| LLM | Groq (Llama 3.1) |
| Embeddings | HuggingFace Sentence Transformers |
| Vector Database | FAISS |
| Frontend | React, Tailwind CSS *(Planned)* |
| Deployment | Docker, AWS *(Planned)* |

---

# 🏗 System Architecture

```text
React Frontend (Planned)
        │
        ▼
FastAPI REST API
        │
 ┌──────┴───────────────┐
 │                      │
Authentication      Document Upload
 │                      │
PostgreSQL       PyPDFLoader
 │                      │
 └──────────────┬───────┘
                │
        Text Splitter
                │
     HuggingFace Embeddings
                │
            FAISS Index
                │
      Semantic Retrieval
                │
         Groq Llama 3.1
                │
          AI Response
```

---

# 📁 Project Structure

```text
knowledgeflow-ai/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── prompts/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── vectorstore/
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
├── architecture/
├── docs/
├── screenshots/
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🗺 Development Roadmap

## ✅ Phase 1 — Project Foundation

- [x] Project Setup
- [x] FastAPI Configuration
- [x] Professional Folder Structure
- [x] Environment Configuration
- [x] GitHub Repository
- [x] Health Check Endpoint

---

## ✅ Phase 2 — Database Layer

- [x] PostgreSQL Integration
- [x] SQLAlchemy ORM
- [x] User Model
- [x] Database Session Management
- [x] Automatic Database Initialization

---

## ✅ Phase 3 — Authentication

- [x] User Registration
- [x] User Login
- [x] Password Hashing
- [x] JWT Authentication
- [x] Protected Routes
- [x] Current User Endpoint
- [x] Swagger OAuth2 Integration

---

## ✅ Phase 4 — Document Processing

- [x] PDF Upload
- [x] Document Storage
- [x] Document CRUD
- [x] Download Documents
- [ ] DOCX Upload
- [ ] TXT Upload

---

## ✅ Phase 5 — Vector Search

- [x] HuggingFace Embeddings
- [x] FAISS Indexing
- [x] Semantic Search
- [x] RAG Pipeline
      
---

## 📅 Phase 6.1 — Advanced RAG

- [ ] Multi-document Support
- [ ] Source Citations
- [ ] Conversation Memory
- [ ] Streaming Responses

---

## 📅 Phase 6.2 — AI Agents

- [ ] LangGraph Workflow
- [ ] Conversation Memory
- [ ] Source Citations
- [ ] Streaming Responses
      
---

## 📅 Phase 7 — Frontend

- [ ] React Application
- [ ] Chat Interface
- [ ] Authentication
- [ ] Dashboard

---

## 📅 Phase 8 — Deployment

- [ ] Docker Compose
- [ ] GitHub Actions
- [ ] AWS Deployment
- [ ] Monitoring

---

# 🔌 Current API Endpoints

## System

```http
GET /
GET /health
GET /docs
```

Authentication, document management, and chat endpoints will be added in upcoming sprints.
## Authentication

```http
POST /auth/register
POST /auth/login
GET  /auth/me
```

## Documents

```http
POST   /documents/upload
GET    /documents/
GET    /documents/{id}
PUT    /documents/{id}
DELETE /documents/{id}
GET    /documents/{id}/download
```
---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/sudais28/knowledgeflow-ai.git

cd knowledgeflow-ai
```

## Backend Setup

```bash
cd backend

python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file inside the `backend` directory.

Example:

```env
APP_NAME=KnowledgeFlow AI
APP_VERSION=1.0.0
API_PREFIX=/api/v1

POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=knowledgeflow
```

### Run the Application

```bash
python -m uvicorn app.main:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

---

# 📸 Screenshots

Screenshots of the application will be added as development progresses.

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

- Backend Architecture
- REST API Development
- Database Design
- Authentication & Authorization
- Retrieval-Augmented Generation (RAG)
- AI Agent Workflows
- PostgreSQL
- SQLAlchemy ORM
- Docker
- Cloud Deployment
- Software Engineering Best Practices

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sudais Touseef**

Computer Science Graduate | AI Engineer | Backend Developer

Interested in building scalable AI systems, intelligent agents, Retrieval-Augmented Generation (RAG), and production-ready backend applications.
