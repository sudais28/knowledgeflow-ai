import os
import logging

from langchain_community.vectorstores import FAISS

from app.services.embedding_service import get_embeddings

logger = logging.getLogger(__name__)


def get_user_vector_path(user_id: int):
    """
    Returns the FAISS directory for a specific user.
    """
    return f"vectorstore/user_{user_id}"


def create_vector_store(chunks, user_id: int):
    """
    Creates a new FAISS vector store or appends
    new document chunks to an existing one.
    """

    logger.info("Loading embedding model...")
    embeddings = get_embeddings()

    vector_db = get_user_vector_path(user_id)

    # Ensure parent folder exists
    os.makedirs(os.path.dirname(vector_db), exist_ok=True)

    if os.path.exists(vector_db):

        logger.info("Existing FAISS index found. Loading...")

        vector_store = FAISS.load_local(
            vector_db,
            embeddings,
            allow_dangerous_deserialization=True,
        )

        logger.info("Adding new chunks to existing index...")
        vector_store.add_documents(chunks)

    else:

        logger.info("Creating new FAISS index...")

        vector_store = FAISS.from_documents(
            chunks,
            embeddings,
        )

    logger.info("Saving FAISS index...")
    vector_store.save_local(vector_db)

    logger.info(f"FAISS index saved at: {vector_db}")

    return vector_store


def load_vector_store(user_id: int):
    """
    Loads the FAISS vector store for a user.
    """

    embeddings = get_embeddings()

    vector_db = get_user_vector_path(user_id)

    if not os.path.exists(vector_db):
        raise FileNotFoundError(
            f"FAISS index not found for user {user_id}. Upload a document first."
        )

    logger.info(f"Loading FAISS index for user {user_id}")

    return FAISS.load_local(
        vector_db,
        embeddings,
        allow_dangerous_deserialization=True,
    )