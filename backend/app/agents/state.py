from typing import TypedDict
from langchain_core.documents import Document


class AgentState(TypedDict):

    # Input
    question: str
    user_id: int

    # Generated
    rewritten_question: str

    # Retrieval
    documents: list[Document]
    context: str

    # Grading
    is_relevant: bool

    # Output
    answer: str