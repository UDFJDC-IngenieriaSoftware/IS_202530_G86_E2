from sqlalchemy import Date, Column, String, Integer, CheckConstraint
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()


class Patient(Base):

    __tablename__='paciente'

    cedula = Column('cedula',Integer,primary_key=True,index=True)
    name = Column('primerNombre ',String,nullable=False)
    second_name = Column('segundoNombre ',String,nullable=True)
    first_lastname = Column('primerApellido ',String,nullable=False)
    second_lastname = Column('segundoApellido ',String,nullable=True)
    phone = Column('telefono ',Integer,nullable=False)
    date_of_birth =Column('fechaNacimiento ',Date)

    carers = relationship('Carer_Patient', back_populates="patients")

    __table_args__=(
        CheckConstraint('(fechaNacimiento  < CURRENT_DATE', name='check_fecha_nacimiento')

    )


    
    def to_dict(self):

        return {
           "cedula":self.cedula,
           "name":self.name,
           "second_name":self.second_name,
           "first_lastname":self.first_lastname,
           "second_lastname":self.second_lastname,
           "phone":self.phone,
           "date_of_birth":self.date_of_birth,
           "carers": self.carers,
           "treatments":self.treatments


        }    