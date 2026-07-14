from app.db.base_class import Base

from app.models.user import User
from app.models.document import Document

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass