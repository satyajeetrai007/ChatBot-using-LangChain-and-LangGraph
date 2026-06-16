import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent # to find the Root Directory
load_dotenv(BASE_DIR / ".env")

class Config:
    # Environment-specific variables (Secrets)
    DATABASE_URL = ""
    API_KEY = ""
    
    # Application constants (Non-secrets)
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    PORT = int(os.getenv("PORT", 8000))
    PAGINATION_LIMIT = 20