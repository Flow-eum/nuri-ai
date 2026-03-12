from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "NURI AI"
    API_V1_STR: str = "/api/v1"

    OPENAI_API_KEY: str
    SUMMARY_MODEL: str = "gpt-4o"
    SUMMARY_TEMPERATURE: float = 0.5

    MAX_SUMMARY_TEXT_LENGTH: int = 5000
    LLM_TIMEOUT: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

    API_AUTH_TOKEN: str = "~~~"

settings = Settings()