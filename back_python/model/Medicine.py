from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base

class Medicamento(Base):
    __tablename__ = "medicamento"

    idMedicamento = Column("idmedicamento", Integer, primary_key=True, index=True)
    nombreMedicamento = Column("nombremedicamento", String(100), nullable=False)
    presentacion = Column("presentacion", String(50), nullable=False)
    concentracion = Column("concentracion", String(50), nullable=False)

    def to_dict(self):
        return {
            "idMedicamento": self.idMedicamento,
            "nombreMedicamento": self.nombreMedicamento,
            "presentacion": self.presentacion,
            "concentracion": self.concentracion
        }
