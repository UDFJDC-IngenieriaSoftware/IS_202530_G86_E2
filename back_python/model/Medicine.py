from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base

class Medicamento(Base):
    __tablename__ = "medicamento"

    idMedicamento = Column("idmedicamento", Integer, primary_key=True, index=True)
    nombreMedicamento = Column("nombremedicamento", String(100), nullable=False)
    observaciones = Column("observaciones", String(200), nullable=True)

    def to_dict(self):
        return {
            "idMedicamento": self.idMedicamento,
            "nombreMedicamento": self.nombreMedicamento,
            "observaciones": self.observaciones
        }
