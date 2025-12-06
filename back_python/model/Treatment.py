from sqlalchemy import ForeignKey,Date, Column, String, Integer, CheckConstraint
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()


class Treatment(Base):

    __tablename__='tratamiento'


    id_treatment =Column('idTratamiento',Integer,primary_key=True,index=True,autoincrement=True)
    cedulaPaciente = Column(Integer, ForeignKey('paciente.cedula'), nullable=False)
    name = Column('nombreTratamiento',String,nullable=False)
    especialty = Column('especialidad',String,nullable=False)
    start_date =Column('fechaInicio',Date)
    end_date = Column('fechaInicio',Date)

    __table_args__ = (
        CheckConstraint('fechaInicio < CURRENT_DATE', name='check_fecha_inicio'),
        CheckConstraint('fechaFin > fechaInicio AND fechaFin <= CURRENT_DATE', name='check_fecha_fin'),
    )
    
    patient = relationship("Patient", back_populates="treatments")


    def to_dict(self):

        return {
            "id_treatment":self.id_treatment,
            "name": self.name,
            "especialty": self.especialty,
            "end_date": self.end_date,
            "start_date": self.start_date


        }  