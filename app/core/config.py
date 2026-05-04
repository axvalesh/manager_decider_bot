import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET")
    BASE_URL = os.getenv("BASE_URL")
    GOOGLE_WEBHOOK_SECRET = os.getenv("GOOGLE_WEBHOOK_SECRET")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    PATH_TO_GOOGLE_CREDENTIALS = os.getenv("PATH_TO_GOOGLE_CREDENTIALS")

settings = Settings()