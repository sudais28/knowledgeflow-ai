from fastapi import APIRouter, Depends

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

from app.services.rag_service import ask_question

from app.core.dependencies import get_current_user
from app.models.user import User


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
    current_user: User = Depends(get_current_user),
):

    return ask_question(
        request.question
    )