from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.orm import relationship
from db.database import Base
import enum

# Enums alineados con PostgreSQL
class EstadoEnvioEnum(str, enum.Enum):
    Pendiente = "Pendiente"
    Enviado = "Enviado"
    Error = "Error al enviar"

class RespuestaPacienteEnum(str, enum.Enum):
    Confirmado = "Confirmado"
    SinRespuesta = "Sin respuesta"

class Recordatorio(Base):
    __tablename__ = "recordatorio"

    idRecordatorio = Column("idrecordatorio", Integer, primary_key=True, index=True)
    idMedicamento = Column("idmedicamento", Integer, ForeignKey("medicamento.idmedicamento"))
    idTratamiento = Column("idtratamiento", Integer, ForeignKey("tratamiento.idtratamiento"))

    estadoEnvio = Column("estadoenvio", Enum(EstadoEnvioEnum), nullable=False)
    respuestaPaciente = Column("respuestapaciente", Enum(RespuestaPacienteEnum), nullable=False)

    fechaEnvioRecordatorio = Column("fechaenviorecordatorio", TIMESTAMP, nullable=False)
    fechaRespuesta = Column("fecharespuesta", TIMESTAMP, nullable=True)
    notas = Column("notas", String(200), nullable=True)

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
