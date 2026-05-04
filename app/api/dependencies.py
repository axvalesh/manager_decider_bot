from fastapi import HTTPException, Header
# from core.config import GOOGLE_WEBHOOK_SECRET, TELEGRAM_WEBHOOK_SECRET
from core.config import settings

def verify_google_webhook(token: str = Header(None)):
    if(token != settings.GOOGLE_WEBHOOK_SECRET):
        raise HTTPException(401, detail="Invalid token")
    