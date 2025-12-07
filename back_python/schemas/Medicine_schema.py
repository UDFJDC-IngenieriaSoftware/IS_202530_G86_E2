from pydantic import BaseModel

class MedicineBase(BaseModel):
    nombreMedicamento: str
    observaciones: str | None = None


class MedicineCreate(MedicineBase):
    pass


class MedicineResponse(MedicineBase):
    idMedicamento: int

    class Config:
        from_attributes = True
