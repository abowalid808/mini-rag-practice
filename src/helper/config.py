from pydantic_settings import BaseSettings
from typing import Optional
class Setting(BaseSettings):
    """Configuration settings for the application."""
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: Optional[str] = None

    file_allowed_extensions: list = ['text/plain', 'application/pdf']
    file_allowed_size: int = 10 * 1024 * 1024  # 10 MB
    file_chunk_size: int = 1024 * 1024  # 1 MB
    
    class Config:
        env_file = "src/.env"

def get_settings():
    """Return the object of settings."""
    return Setting()