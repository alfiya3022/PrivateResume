import os
from dotenv import load_dotenv
load_dotenv()
APP_NAME = os.getenv("APP_NAME", "PrivateResume API")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "privateresume")
POSTGRES_USER = os.getenv("POSTGRES_USER", "privateresume")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")