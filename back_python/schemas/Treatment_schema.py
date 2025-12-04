from datetime import datetime
from pydantic import BaseModel

class TreatmentBase(BaseModel):
    id_treatment:str
    name: str
    especialty: str
    end_date: str
    start_date: str

class TreatmentCreate(TreatmentBase):
    pass

class TreatmentResponse(TreatmentBase):
    pass

