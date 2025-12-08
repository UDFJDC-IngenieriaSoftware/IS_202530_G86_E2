from datetime import datetime
from pydantic import BaseModel
from datetime import date

class TreatmentBase(BaseModel):
    
    cedula_patient:str
    name: str
    especiality: str
    
    start_date: date
    end_date: date

class TreatmentCreate(TreatmentBase):
    pass

class TreatmentResponse(TreatmentBase):
    id_treatment: int

    class Config:
        from_attributes = True

