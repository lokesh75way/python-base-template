from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    CORS_ORIGINS: str
    VAPI_API_KEY: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
