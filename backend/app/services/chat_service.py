from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.chat import ChatSession, ChatMessage


def create_chat_session(
    db: Session,
    user_id: int,
    title: str | None = None,
):
    session = ChatSession(
        user_id=user_id,
        title=title,
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session


def get_chat_session(
    db: Session,
    session_id: int,
    user_id: int,
):
    session = (
        db.query(ChatSession)
        .filter(
            ChatSession.id == session_id,
            ChatSession.user_id == user_id,
        )
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Chat session not found.",
        )

    return session


def get_user_sessions(
    db: Session,
    user_id: int,
):
    return (
        db.query(ChatSession)
        .filter(ChatSession.user_id == user_id)
        .order_by(ChatSession.updated_at.desc())
        .all()
    )


def save_message(
    db: Session,
    session_id: int,
    role: str,
    content: str,
):
    session = (
        db.query(ChatSession)
        .filter(ChatSession.id == session_id)
        .first()
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Chat session not found.",
        )

    message = ChatMessage(
        session_id=session_id,
        role=role,
        content=content,
    )

    db.add(message)

    # Update conversation timestamp
    session.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(message)

    return message


def get_chat_history(
    db: Session,
    session_id: int,
    user_id: int,
):
    get_chat_session(
        db=db,
        session_id=session_id,
        user_id=user_id,
    )

    return (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.asc())
        .all()
    )


def get_chat_history_text(
    db: Session,
    session_id: int,
    user_id: int,
):
    """
    Returns formatted conversation history
    ready to send to the LLM.
    """

    messages = get_chat_history(
        db=db,
        session_id=session_id,
        user_id=user_id,
    )

    history = []

    for message in messages:
        history.append(
            f"{message.role}: {message.content}"
        )

    return "\n".join(history)


def delete_chat_session(
    db: Session,
    session_id: int,
    user_id: int,
):
    session = get_chat_session(
        db=db,
        session_id=session_id,
        user_id=user_id,
    )

    db.delete(session)
    db.commit()

    return {
        "message": "Chat session deleted successfully."
    }