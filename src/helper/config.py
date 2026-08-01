from pydantic-settings import BaseSettings

class Setting(BaseSettings):
    """Configuration settings for the application."""
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str


    class Config:
        env_file = "src\.env"

def get_settings():
    """Return the object of settings."""
    return Setting()