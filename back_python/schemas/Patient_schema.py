from datetime import datetime
from pydantic import BaseModel

class PatientBase(BaseModel):

    cedula: str
    name: str
    second_name: str | None = None
    first_lastname: str
    second_lastname: str
    phone: str
    date_of_birth: datetime

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    pass