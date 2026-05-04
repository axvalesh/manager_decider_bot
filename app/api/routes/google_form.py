from fastapi import APIRouter, Depends,Header
from schemas.form import FormSubmission
from ..dependencies import verify_google_webhook
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from schemas.manager import ManagerBase
from services.ai_service import ai_service
from bot.bot import send_info_to_manager
from core.config import settings
# 1. Setup the scope and credentials
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(settings.PATH_TO_GOOGLE_CREDENTIALS, scope)
client = gspread.authorize(creds)
sheet = client.open("Managers").sheet1

router = APIRouter()

@router.post('/google-form')
async def google_form_webhook(
    data: FormSubmission,
    _: None = Depends(verify_google_webhook)
):

    print('New form submission')
    print(data)
    managers = await get_managers_google_sheet()

    result = await ai_service.choose_manager(
        student=data,
        managers=managers
    )

    print(managers)

    await send_info_to_manager(result)
    return {
        "status": "ok",
        "ai_result": result
    }

async def get_managers_google_sheet() -> list[ManagerBase]: 
    data = sheet.get_all_records()
    models: list[ManagerBase] = [ManagerBase(**item) for item in data]
    
    return models
