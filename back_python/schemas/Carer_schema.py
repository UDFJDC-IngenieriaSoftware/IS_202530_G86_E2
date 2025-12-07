from pydantic import BaseModel


class CarerCreate(BaseModel):
    #es necesario que se ingrese la cedula para crear
    cedula: int
    name: str
    second_name: str | None = None
    first_lastname: str
    second_lastname: str
    phone: int


class CarerResponse(BaseModel):
    cedula: int
    name: str
    second_name: str | None = None
    first_lastname: str
    second_lastname: str
    phone: int

    model_config = {
        "from_attributes": True
    }