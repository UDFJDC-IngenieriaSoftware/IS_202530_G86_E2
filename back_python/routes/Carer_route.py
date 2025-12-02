from fastapi import APIRouter, HTTPException
from schemas.Carer_schema import CarerCreate,CarerResponse
from services.Carer_service import (

create_carer,
get_all_carer,
get_carer_by_id,
update_carer,
delete_carer

)

router = APIRouter(prefix="/carer",tags=["Carers"])

@router.post("/",response_model=CarerResponse)
def create_carer_route(data:CarerCreate):
    carer = create_carer(data)
    return carer.to_dict()

@router.get("/",response_model=list[CarerResponse])
def list_carers():

    return [c.to_dict() for c in get_all_carer()]

@router.get("/{cedula}",response_model=CarerResponse)
def get_carer(cedula:str):
    carer = get_carer_by_id(cedula)
    if not carer:
        raise HTTPException(status_code=404,detail="carer not found")
    return carer.to_dict( )

@router.put("/{cedula}", response_model=CarerResponse)
def update_carer_route(cedula: str, data: CarerCreate):
    carer = update_carer(cedula, data)
    if not carer:
        raise HTTPException(status_code=404, detail="Carer not found")
    return carer.to_dict()

@router.delete("/{cedula}")
def delete_carer_route(cedula: str):
    success = delete_carer(cedula)
    if not success:
        raise HTTPException(status_code=404, detail="Carer not found")
    return {"message": "carer deleted successfully"}