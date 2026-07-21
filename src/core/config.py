from functools import lru_cache
from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
     # ------------------------
    # Application
    # ------------------------
    environment: str = "development"
    log_level: str = "INFO"

    # ------------------------
    # OpenAI
    # ------------------------
    openai_api_key: str

    # ------------------------
    # LangSmith
    # ------------------------
    langchain_api_key: str
    langchain_tracing_v2: bool = True
    langchain_project: str

    # ------------------------
    # Models
    # ------------------------
    cheap_model: str
    standard_model: str
    reasoning_model: str

    # ------------------------
    # Database
    # ------------------------
    database_url: str

    # ------------------------
    # Qdrant
    # ------------------------
    qdrant_url: str
    qdrant_collection: str

    model_config=SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )

@lru_cache
def get_settings()->Settings:
    return Settings()

settings=get_settings()