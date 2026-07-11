from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application configuration loaded from environment variables.

    APP_NAME: str = "KnowledgeFlow AI"
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    # Return a cached Settings instance
    return Settings()


settings = get_settings()