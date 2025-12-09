from datetime import datetime
from pydantic import BaseModel
from datetime import date

class TreatmentBase(BaseModel):
    
    cedula_patient:str
    name: str
    especiality: str
    dose: str
    frequence: int
    start_date: datetime
    end_date: datetime

class TreatmentCreate(TreatmentBase):
    pass

class TreatmentResponse(TreatmentBase):
    id_treatment: int

    class Config:
        from_attributes = True

