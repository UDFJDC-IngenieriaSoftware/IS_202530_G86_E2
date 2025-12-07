from sqlalchemy import Date, Column, String, Integer, CheckConstraint
from sqlalchemy.orm import declarative_base,relationship
from db.database import Base


class Patient(Base):

    __tablename__='paciente'

    cedula = Column('cedula',Integer,primary_key=True,index=True)
    name = Column('primernombre',String,nullable=False)
    second_name = Column('segundonombre',String,nullable=True)
    first_lastname = Column('primerapellido',String,nullable=False)
    second_lastname = Column('segundoapellido',String,nullable=True)
    phone = Column('telefono',Integer,nullable=False)
    date_of_birth =Column('fechanacimiento',Date)

    carer_patients = relationship("Carer_Patient", back_populates="patient")
    treatments = relationship("Treatment", back_populates="patient")

    carers = relationship(
        "Carer",#ria
        secondary="cuidador_paciente",
        primaryjoin="Patient.cedula == Carer_Patient.cedula_patient",
        secondaryjoin="Carer.cedula == Carer_Patient.cedula_carer",
        viewonly=True
    )


    __table_args__=(
        CheckConstraint('fechanacimiento  < CURRENT_DATE', name='check_fecha_nacimiento'),

    )


    
    def to_dict(self):

        return {
           "cedula":self.cedula,
           "name":self.name,
           "second_name":self.second_name,
           "first_lastname":self.first_lastname,
           "second_lastname":self.second_lastname,
           "phone":self.phone,
           "date_of_birth":self.date_of_birth
     
           


        }    