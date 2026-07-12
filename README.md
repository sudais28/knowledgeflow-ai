# KnowledgeFlow AI

> An AI Knowledge Platform built with FastAPI, PostgreSQL, LangChain, LangGraph, FAISS, and Groq.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

KnowledgeFlow AI is a production-inspired Retrieval-Augmented Generation (RAG) platform that enables users to upload documents, build a searchable knowledge base, and interact with their data using natural language.

The project is being developed using modern backend engineering practices, including modular architecture, environment-based configuration, SQLAlchemy ORM, JWT authentication, and scalable AI workflows.

---

# 🚧 Project Status

**Current Version:** v0.2

**Current Sprint:** Authentication & User Management

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

---

# 🚧 In Progress

- JWT Authentication
- User Registration
- User Login
- Password Hashing (bcrypt)
- Protected API Endpoints

---

# 📅 Planned Features

## Document Management

- Upload PDF
- Upload DOCX
- Upload TXT
- Upload Markdown Files
- Delete Documents
- Multi-document Support

---

## AI & RAG

- Semantic Search
- HuggingFace Embeddings
- FAISS Vector Database
- Retrieval-Augmented Generation (RAG)
- Groq Llama 3 Integration
- Source Citations
- Conversation History

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

## 🚧 Phase 3 — Authentication

- [ ] User Registration
- [ ] User Login
- [ ] Password Hashing
- [ ] JWT Authentication
- [ ] Protected Routes

---

## 📅 Phase 4 — Document Processing

- [ ] PDF Upload
- [ ] DOCX Upload
- [ ] TXT Upload
- [ ] Document Storage

---

## 📅 Phase 5 — Vector Search

- [ ] HuggingFace Embeddings
- [ ] FAISS Indexing
- [ ] Semantic Search
- [ ] RAG Pipeline

---

## 📅 Phase 6 — AI Agents

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
