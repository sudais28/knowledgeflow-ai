from datetime import datetime
from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class ChatSource(BaseModel):
    filename: str | None = None
    page: int | None = None
    document_id: int | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[ChatSource]


class ChatSessionCreate(BaseModel):
    title: str | None = None


class ChatSessionResponse(BaseModel):
    id: int
    title: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


class ChatMessageResponse(BaseModel):
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True