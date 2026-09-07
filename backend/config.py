import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

FIREBASE_CREDENTIALS = os.getenv(
    "FIREBASE_CREDENTIALS"
)

CHROMA_PATH = "chroma_db"

UPLOAD_FOLDER = "uploads"
