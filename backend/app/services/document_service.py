import os
import shutil
import logging

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.models.document import Document

from app.services.document_loader import load_document
from app.services.text_splitter import split_documents
from app.services.vector_service import create_vector_store

UPLOAD_FOLDER = "uploads"

logger = logging.getLogger(__name__)


def save_document(
    db: Session,
    file: UploadFile,
    owner_id: int,
):
    # Only allow PDF files
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )
    existing_document = (
        db.query(Document)
        .filter(
            Document.owner_id == owner_id,
            Document.filename == file.filename,
        )
        .first()
    )

    if existing_document:
        raise HTTPException(
            status_code=400,
            detail="You have already uploaded this document."
        )

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Create uploads folder
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Save uploaded file
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename,
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    documents = load_document(file_path)

    if not documents:
        raise HTTPException(
            status_code=400,
            detail="No text found in PDF."
        )

    logger.info("=" * 60)
    logger.info(f"Pages extracted: {len(documents)}")

    # Split into chunks
    chunks = split_documents(documents)

    logger.info(f"Total chunks created: {len(chunks)}")

    # Preview chunks BEFORE embedding
    for i, chunk in enumerate(chunks[:5]):
        logger.info(f"\nChunk {i + 1}")
        logger.info("-" * 40)
        logger.info(f"Metadata: {chunk.metadata}")
        logger.info(chunk.page_content[:300])

    # --------------------------------------------------
    # Save document metadata in PostgreSQL FIRST
    # --------------------------------------------------

    document = Document(
        filename=file.filename,
        file_path=file_path,
        filetype=file.content_type,
        owner_id=owner_id,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    # --------------------------------------------------
    # Add metadata to every chunk
    # --------------------------------------------------

    for chunk in chunks:
        chunk.metadata["document_id"] = document.id
        chunk.metadata["owner_id"] = owner_id
        chunk.metadata["filename"] = document.filename

    logger.info("=" * 60)
    logger.info("First Chunk Metadata")
    logger.info(chunks[0].metadata)
    logger.info("=" * 60)

    # --------------------------------------------------
    # NOW create/update FAISS
    # --------------------------------------------------

    create_vector_store(chunks, owner_id)

    logger.info("FAISS vector store created successfully.")

    return document


def get_document(
    db: Session,
    document_id: int,
    owner_id: int,
):
    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.owner_id == owner_id,
        )
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document


def get_user_documents(
    db: Session,
    owner_id: int,
):
    return (
        db.query(Document)
        .filter(
            Document.owner_id == owner_id
        )
        .all()
    )


def update_document(
    db: Session,
    document_id: int,
    owner_id: int,
    filename: str,
):
    document = get_document(
        db,
        document_id,
        owner_id,
    )

    document.filename = filename

    db.commit()
    db.refresh(document)

    return document


def delete_document(
    db: Session,
    document_id: int,
    owner_id: int,
):
    document = get_document(
        db,
        document_id,
        owner_id,
    )

    # Delete physical file
    if os.path.exists(document.file_path):
        os.remove(document.file_path)

    # Delete database record
    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }