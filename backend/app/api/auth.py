from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import register_user, login_user

from app.core.dependencies import get_current_user
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return register_user(db, user)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = UserLogin(
        email=form_data.username,
        password=form_data.password,
    )

    return login_user(db, user)

@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": current_user.username,
    }