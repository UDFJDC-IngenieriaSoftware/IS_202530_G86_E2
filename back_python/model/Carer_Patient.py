from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey, CheckConstraint

from sqlalchemy.orm import relationship,declarative_base
from datetime import date


from db.database import Base


class Carer_Patient(Base):
    
    __tablename__='cuidador_paciente'
    
    
    cedula_patient=Column('cedulapaciente', Integer, ForeignKey('paciente.cedula'), primary_key=True)
    cedula_carer=Column('cedulacuidador', Integer, ForeignKey('cuidador.cedula'), primary_key=True)
    date_asign=Column('fechaasignacion', Date)
    relation_type=Column('relacion', String, nullable=True)
    
    carer = relationship("Carer", back_populates="carer_patients")
    patient = relationship("Patient", back_populates="carer_patients")


    __table_args__=(
        CheckConstraint('fechaasignacion < CURRENT_DATE', name='check_fecha'),
    )

    def assign_today(self):
        
        self.date_asign = date.today()
