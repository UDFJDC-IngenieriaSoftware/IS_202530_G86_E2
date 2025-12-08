from sqlalchemy import  Column, String, CheckConstraint
from sqlalchemy.orm import declarative_base,relationship

from db.database import Base



class Carer(Base):

    __tablename__= "cuidador"


    cedula = Column('cedula',String,primary_key=True,index=True)
    name = Column('primernombre', String,nullable=False)
    second_name = Column('segundonombre',String,nullable=True)
    first_lastname = Column('primerapellido',String,nullable=False)
    second_lastname = Column('segundoapellido',String,nullable=True)
    phone = Column('telefono',String,nullable=False)

        # el carer debe poder agregar pacientes
    __table_args__=(

        CheckConstraint("telefono ~ '^[0-9]+$'", name='check_telefono'),

    )


    #relación con carer_patients

    carer_patients = relationship("Carer_Patient", back_populates="carer")

    patients = relationship(
        "Patient",
        secondary="cuidador_paciente",
        primaryjoin="Carer.cedula == Carer_Patient.cedula_carer",
        secondaryjoin="Patient.cedula == Carer_Patient.cedula_patient",
        viewonly=True
    )



   
    def to_dict(self):

        return {
           "cedula":self.cedula,
           "name":self.name,
           "second_name":self.second_name,
           "first_lastname":self.first_lastname,
           "second_lastname":self.second_lastname,
           "phone":self.phone
          

        }
        

