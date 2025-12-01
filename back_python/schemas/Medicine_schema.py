from pydantic import BaseModel

class MedicineCreate(BaseModel):
    name: str
    dose: str
    frequency: str
    route_of_administration: str
    observations: str | None = None

class MedicineResponse(BaseModel):
    id_medicine: int
    name: str
    dose: str
    frequency: str
    route_of_administration: str
    observations: str | None = None

    class Config:
        orm_mode = True
