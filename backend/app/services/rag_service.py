from urllib import response

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from app.core.config import settings
from app.services.vector_service import load_vector_store

from fastapi import HTTPException

import logging 

logger = logging.getLogger(__name__)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=settings.GROQ_API_KEY,
)


def ask_question(question: str, user_id: int):

    # Load FAISS
    try:
        vector_store = load_vector_store(user_id)

    except FileNotFoundError:
        raise HTTPException(
        status_code=404,
        detail="Please upload a document before asking questions."
    )
    logger.info(f"Current User: {user_id}")

    # Retrieve relevant chunks
    docs = vector_store.similarity_search(
        question,
        k=4
    )
    if not docs:
        return {
        "answer": "No relevant information was found in your uploaded documents.",
        "sources": []
    }
    logger.info("Retrieved relevant chunks.")

    for i, doc in enumerate(docs):
        logger.info(f"Retrieved Chunk {i + 1}")
        logger.info(doc.page_content[:200])

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = ChatPromptTemplate.from_template(
        """
        You are KnowledgeFlow AI, an intelligent document assistant.

        Your job is to answer the user's question ONLY using the provided context.

        Rules:
        - Use only the information found in the context.
        - Do not make up facts or assumptions.
        - If the answer is not present in the context, reply exactly:
        "I don't know based on the uploaded documents."
        - Keep answers clear and concise.
        - Use bullet points when listing multiple items.
        - Do not mention that you are an AI model.
        - Do not include information outside the uploaded documents.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    chain = prompt | llm
    try:    
        response = chain.invoke(
            {
            "context": context,
            "question": question,
         }
    )
    except Exception:
        raise HTTPException(
        status_code=500,
        detail="Unable to generate an answer. Please try again later."
    )
    
    # Extract structural sources from metadata
    sources = []
    seen = set()

    for doc in docs:
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
        "answer": response.content,
        "sources": sources,
    }
