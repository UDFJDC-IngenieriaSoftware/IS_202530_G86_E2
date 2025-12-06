from sqlalchemy import  Column, String, Integer, CheckConstraint
from sqlalchemy.orm import declarative_base,relationship



Base = declarative_base()


class Carer(Base):

    __tablename__= "cuidador"


    cedula = Column('cedula ',Integer,primary_key=True,index=True)
    name = Column('primerNombre ', String,nullable=False)
    second_name = Column('segundoNombre  ',String,nullable=True)
    first_lastname = Column('primerApellido ',String,nullable=False)
    second_lastname = Column('segundoApellido ',String,nullable=True)
    phone = Column('telefono ',Integer,nullable=False)

        # el carer debe poder agregar pacientes
    __table_args__=(

        CheckConstraint('telefono>0',name='check_telefono')

    )


    #relación

    patients = relationship('Carer_Patient', back_populates="carers")#carers es la lista de pacientes
    



   
    def to_dict(self):

        return {
           "cedula":self.cedula,
           "name":self.name,
           "second_name":self.second_name,
           "first_lastname":self.first_lastname,
           "second_lastname":self.second_lastname,
           "phone":self.phone,
           "patients": self.patients


        }
        

