from pydantic import BaseModel
from datetime import datetime

class ReminderBase(BaseModel):
    estado_envio: str
    answer_patient: str | None = None
    date_answer: datetime | None = None
    date_reminder: datetime

class ReminderCreate(ReminderBase):
    pass

class ReminderResponse(ReminderBase):
    id_reminder: int
