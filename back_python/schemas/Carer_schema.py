from pydantic import BaseModel


class CarerCreate(BaseModel):
    #es necesario que se ingrese la cedula para crear
    cedula: str
    name: str
    second_name: str | None = None
    first_lastname: str
    second_lastname: str
    phone: str


class CarerResponse(BaseModel):
    cedula: str
    name: str
    second_name: str | None = None
    first_lastname: str
    second_lastname: str
    phone: str

    class Config:
        orm_mode = True

