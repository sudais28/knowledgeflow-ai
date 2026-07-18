from fastapi import APIRouter, Depends

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

from app.services.rag_service import ask_question

from app.core.dependencies import get_current_user
from app.models.user import User

from sqlalchemy.orm import Session
from app.db.session import get_db


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "/",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return ask_question(
        question=request.question,
        user_id=current_user.id,
    )