from typing import Optional
from pydantic import BaseModel


class FormSubmission(BaseModel):
    timestamp: Optional[str] = None
    name: Optional[str] = None
    date_of_birth: Optional[str] = None
    current_english_level: Optional[str] = None
    goal: Optional[str] = None
    telegram_username: Optional[str] = None