from pydantic import BaseModel
from datetime import datetime


class ReminderBase(BaseModel):
    idMedicamento: int
    idTratamiento: int
    estadoEnvio: str
    respuestaPaciente: str
    fechaEnvioRecordatorio: datetime
    fechaRespuesta: datetime
    notas: str | None = None


class ReminderCreate(ReminderBase):
    pass


class ReminderResponse(ReminderBase):
    idRecordatorio: int

    class Config:
        from_attributes = True
