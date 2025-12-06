from sqlalchemy import Column, Integer, String
from config.database import Base

class Medicine(Base):
    __tablename__ = "medicamento"

    idMedicamento = Column(Integer, primary_key=True, autoincrement=True)
    nombreMedicamento = Column(String(100), nullable=False)
    observaciones = Column(String(200), nullable=True)

    def to_dict(self):
        return {
            "idMedicamento": self.idMedicamento,
            "nombreMedicamento": self.nombreMedicamento,
            "observaciones": self.observaciones
        }
