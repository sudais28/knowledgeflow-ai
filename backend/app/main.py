from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.init_db import init_db
from app.api.auth import router as auth_router

from app.api.health import router as health_router
from app.core.config import settings

from app.api.documents import router as document_router

from app.api import chat

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Knowledge AI Platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)


@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }
    
@app.on_event("startup")
async def startup_event():
    init_db()

# authentication routes
app.include_router(auth_router)

# document routes
app.include_router(document_router)
    
# chat routes    
app.include_router(
    chat.router
)