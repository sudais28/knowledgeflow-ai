from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Project
    APP_NAME: str = "KnowledgeFlow AI"
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres123"
    POSTGRES_DB: str = "knowledgeflow"
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    
    GROQ_API_KEY: str


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()