from datetime import datetime
from pydantic import BaseModel

class PatientBase(BaseModel):

    cedula: int
    name: str
    second_name: str | None = None
    first_lastname: str
    second_lastname: str
    phone: int
    date_of_birth: datetime

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    pass