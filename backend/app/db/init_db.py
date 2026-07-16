from app.db.base import Base
from app.db.session import engine



# Import models 
from app.models.user import User
from app.models.document import Document



def init_db():
    Base.metadata.create_all(bind=engine)