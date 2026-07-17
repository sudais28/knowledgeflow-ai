from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class Source(BaseModel):
    filename: str | None = None
    page: int | None = None
    document_id: int | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]