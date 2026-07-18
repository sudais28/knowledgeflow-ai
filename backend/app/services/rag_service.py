from fastapi import HTTPException
from sqlalchemy.orm import Session

import logging

from app.agents.graph import graph

logger = logging.getLogger(__name__)


def ask_question(
    question: str,
    user_id: int,
):

    try:
        result = graph.invoke(
            {
                "question": question,
                "user_id": user_id,

            }
        )

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Please upload a document before asking questions.",
        )

    except Exception:
        logger.exception(
            "Error while executing LangGraph workflow"
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to generate an answer. Please try again later.",
        )


    sources = []
    seen = set()

    for doc in result.get("documents", []):

        source = {
            "filename": doc.metadata.get("filename"),
            "page": doc.metadata.get("page"),
            "document_id": doc.metadata.get("document_id"),
        }

        key = (
            source["document_id"],
            source["page"],
        )

        if key not in seen:
            seen.add(key)
            sources.append(source)


    return {
        "answer": result["answer"],
        "sources": sources,
    }