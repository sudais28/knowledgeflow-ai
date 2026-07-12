from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# 1. Fixed: Changed curly braces to standard string formatting
DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_SERVER}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

# 2. Fixed: Passed arguments directly inside the function parentheses
engine = create_engine(DATABASE_URL, echo=True)

# 3. Fixed: Passed keyword arguments properly and capitalized False
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
