from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User

from app.services.document_service import save_document
from app.schemas.document import DocumentResponse
      
from typing import List

from fastapi.responses import FileResponse

from app.schemas.document import (
    DocumentResponse,
    DocumentUpdate,
    MessageResponse,
)

from app.services.document_service import (
    save_document,
    get_user_documents,
    get_document,
    update_document,
    delete_document,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentResponse,
)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return save_document(
        db=db,
        file=file,
        owner_id=current_user.id,
    )
    
    
@router.get(
    "/",
    response_model=list[DocumentResponse],
)
def list_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_user_documents(
        db=db,
        owner_id=current_user.id,
    )

@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_single_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_document(
        db=db,
        document_id=document_id,
        owner_id=current_user.id,
    )
    
@router.put(
    "/{document_id}",
    response_model=DocumentResponse,
)
def rename_document(
    document_id: int,
    data: DocumentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_document(
        db=db,
        document_id=document_id,
        owner_id=current_user.id,
        filename=data.filename,
    )
    
@router.delete(
    "/{document_id}",
    response_model=MessageResponse,
)
def remove_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_document(
        db=db,
        document_id=document_id,
        owner_id=current_user.id,
    )

@router.get(
    "/{document_id}/download",
)
def download_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    document = get_document(
        db=db,
        document_id=document_id,
        owner_id=current_user.id,
    )

    return FileResponse(
        path=document.file_path,
        filename=document.filename,
        media_type=document.filetype,
    )