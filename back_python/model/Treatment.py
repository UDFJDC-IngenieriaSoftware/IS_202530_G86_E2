from sqlalchemy import ForeignKey,Date, Column, String, Integer, CheckConstraint
from sqlalchemy.orm import declarative_base,relationship
from db.database import Base

class Treatment(Base):

    __tablename__='tratamiento'


    id_treatment =Column('idtratamiento',Integer,primary_key=True,index=True,autoincrement=True)
    cedula_patient = Column('cedulapaciente',String, ForeignKey('paciente.cedula'), nullable=False)
    name = Column('nombretratamiento',String,nullable=False)
    dose = Column('dosis', String, nullable=False)
    frequence = Column('frecuencia', Integer, nullable=False)
    especiality = Column('especialidad',String,nullable=False)
    start_date =Column('fechainicio',Date)
    end_date = Column('fechafin',Date)

    __table_args__ = (
        CheckConstraint('fechainicio <= fechafin', name='check_fecha_inicio_fin'),
        CheckConstraint('fechafin > CURRENT_DATE', name='check_fecha_fin_futura'),
    )
    
    patient = relationship("Patient", back_populates="treatments")


    def to_dict(self):

        return {
            "id_treatment":self.id_treatment,
            "cedula_patient": self.cedula_patient,
            "name": self.name,
            "especiality": self.especiality,
            "end_date": self.end_date,
            "start_date": self.start_date,
            "dose":  self.dose,
            "frequence": self.frequence

        }  