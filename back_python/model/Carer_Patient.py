from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey, CheckConstraint
from db import Base
from sqlalchemy.orm import relationship,declarative_base
from datetime import date


Base = declarative_base()

class Carer_Patient(Base):
    
    __tablename__='cuidador_paciente'
    
    
    cedula_pacient=Column('cedulaPaciente', Integer, ForeignKey('paciente.cedula'), primary_key=True)
    cedula_carer=Column('cedulaCuidador', Integer, ForeignKey('cuidador.cedula'), primary_key=True)
    date_asign=Column('fechaAsignacion', Date)
    relationship=Column('relacion', String, nullable=True)
    
    carer = relationship("Carer", back_populates="carer_patients")


    __table_args__=(
        CheckConstraint('fechaAsignacion < CURRENT_DATE', name='check_fecha')

    )

    def assign_today(self):
        
        self.fechaAsignacion = date.today()
