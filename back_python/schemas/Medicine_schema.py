from pydantic import BaseModel

class MedicineBase(BaseModel):
    nombreMedicamento: str
    presentacion: str
    concentracion: str 



class MedicineCreate(MedicineBase):
    pass


class MedicineResponse(MedicineBase):
    idMedicamento: int

    class Config:
        from_attributes = True
