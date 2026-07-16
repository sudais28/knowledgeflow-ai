from langchain_community.vectorstores import FAISS

from app.services.embedding_service import get_embeddings

import os

from fastapi import HTTPException

VECTOR_DB = "vectorstore/faiss_index"


def create_vector_store(chunks):
    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings,
    )

    vectorstore.save_local(VECTOR_DB)

    return vectorstore


def load_vector_store():

    if not os.path.exists(VECTOR_DB):
        raise HTTPException(
            status_code=404,
            detail="No vector database found. Upload a document first."
        )

    embeddings = get_embeddings()

    return FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True,
    )