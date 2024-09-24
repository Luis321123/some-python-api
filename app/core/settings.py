import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    # App
    APP_NAME:  str = os.environ.get("APP_NAME", "sinaiapp")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))

    # Frontend App
    FRONTEND_HOST: str = os.environ.get("FRONTEND_HOST", "http://localhost:3000")

     # Backend App
    BACKEND_HOST: str = os.environ.get("BACKEND_HOST", "http://localhost:8000")
    
    # PostgreSQL Database Config
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")  
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")  
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")  
    POSTGRES_PORT: int = int(os.environ.get("POSTGRES_PORT"))  
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")  
    DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

     # JWT Secret Key
    JWT_SECRET: str = os.environ.get("JWT_SECRET", "649fb93ef34e4fdf4187709c84d643dd61ce730d91856418fdcf563f895ea40f")
    JWT_ALGORITHM: str = os.environ.get("ACCESS_TOKEN_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES", 45))

    # Seeders of first user
    FIRST_ADMIN_EMAIL: str = os.environ.get("FIRST_ADMIN_EMAIL")
    FIRST_ADMIN_PASSWORD: str =  os.environ.get("FIRST_ADMIN_PASSWORD")
    FIRST_ADMIN_ACCOUNT_NAME: str = os.environ.get("FIRST_ADMIN_ACCOUNT_NAME")
    FIRST_ADMIN_ACCOUNT_LASTNAME: str = os.environ.get("FIRST_ADMIN_ACCOUNT_LASTNAME")

    # App Secret Key
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "8deadce9449770680910741063cd0a3fe0acb62a8978661f421bbcbb66dc41f1")

    # aws settings
    QUEUE_CONNECTION: str = os.environ.get("QUEUE_CONNECTION")
    SQS_ACCESS_KEY_ID: str = os.environ.get("SQS_ACCESS_KEY_ID")
    SQS_SECRET_ACCESS_KEY: str = os.environ.get("SQS_SECRET_ACCESS_KEY")
    SQS_DEFAULT_REGION: str = os.environ.get("SQS_DEFAULT_REGION")
    SQS_PREFIX: str = os.environ.get("SQS_PREFIX")
    SQS_QUEUE: str = os.environ.get("SQS_QUEUE")
    RUTA_SQS: str = os.environ.get("RUTA_SQS")
    AWS_ACCESS_KEY_ID: str = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_REGION: str = os.environ.get("AWS_DEFAULT_REGION")
    AWS_BUCKET: str = os.environ.get("AWS_BUCKET")
    AWS_URL: str = os.environ.get("AWS_URL")
    AWS_USE_PATH_STYLE_ENDPOINT: str = os.environ.get("AWS_USE_PATH_STYLE_ENDPOINT")

@lru_cache()
def get_settings() -> Settings:
    return Settings()
