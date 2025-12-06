from sqlalchemy import Column, Integer, String, TIMESTAMP, Enum, ForeignKey
from config.database import Base
import enum


class EstadoEnvioEnum(enum.Enum):
    Pendiente = "Pendiente"
    Enviado = "Enviado"
    Error_al_enviar = "Error al enviar"


class RespuestaPacienteEnum(enum.Enum):
    Confirmado = "Confirmado"
    Sin_respuesta = "Sin respuesta"


class Reminder(Base):
    __tablename__ = "recordatorio"

    idRecordatorio = Column(Integer, primary_key=True, autoincrement=True)
    idMedicamento = Column(Integer, ForeignKey("medicamento.idMedicamento"))
    idTratamiento = Column(Integer, ForeignKey("tratamiento.idTratamiento"))

    estadoEnvio = Column(Enum(EstadoEnvioEnum), nullable=False)
    respuestaPaciente = Column(Enum(RespuestaPacienteEnum), nullable=False)

    fechaEnvioRecordatorio = Column(TIMESTAMP, nullable=False)
    fechaRespuesta = Column(TIMESTAMP, nullable=False)

    notas = Column(String(200), nullable=True)

    def to_dict(self):
        return {
            "idRecordatorio": self.idRecordatorio,
            "idMedicamento": self.idMedicamento,
            "idTratamiento": self.idTratamiento,
            "estadoEnvio": self.estadoEnvio.value,
            "respuestaPaciente": self.respuestaPaciente.value,
            "fechaEnvioRecordatorio": str(self.fechaEnvioRecordatorio),
            "fechaRespuesta": str(self.fechaRespuesta),
            "notas": self.notas,
        }
