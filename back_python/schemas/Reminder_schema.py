from pydantic import BaseModel
from datetime import datetime
from model.Reminder import EstadoEnvioEnum, RespuestaPacienteEnum

class ReminderBase(BaseModel):
    idMedicamento: int
    idTratamiento: int
    estadoEnvio: EstadoEnvioEnum
    respuestaPaciente: RespuestaPacienteEnum
    fechaEnvioRecordatorio: datetime
    fechaRespuesta: datetime | None = None
    notas: str | None = None

class ReminderCreate(ReminderBase):
    pass

class ReminderResponse(ReminderBase):
    idRecordatorio: int

    class Config:
        from_attributes = True
