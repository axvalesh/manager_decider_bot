from pydantic import BaseModel, ConfigDict,Field
from typing import Optional

class ManagerBase(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    telegram_id: Optional[int] = Field(None, alias="Telegram_id")
    name: Optional[str] = Field(None, alias="Name")
    level: Optional[str] = Field(None, alias="Level")
    specialization: Optional[str] = Field(None, alias="Specialization")