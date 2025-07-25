from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./requests.db"
    API_KEY: str = "supersecretkey"
    KAFKA_BOOTSTRAP: str = "localhost:9092"

    class Config:
        env_file = ".env"

settings = Settings()
