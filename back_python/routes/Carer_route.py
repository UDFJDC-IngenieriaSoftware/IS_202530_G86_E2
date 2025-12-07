from fastapi import Depends, APIRouter, HTTPException
from schemas.Carer_schema import CarerCreate,CarerResponse
from services.Carer_service import Carer_service
from repositories.Carer_repository import Carer_repository
from db.database import get_db

router = APIRouter(prefix="/carer",tags=["Carers"])

def get_service(db=Depends(get_db)):
    repo = Carer_repository(db)
    return Carer_service(repo)


@router.post("/",response_model=CarerResponse)
def create_carer_route(data:CarerCreate,service: Carer_service = Depends(get_service)):
    carer = service.create_carer(data.model_dump())
    return carer.to_dict()

@router.get("/",response_model=list[CarerResponse])
def list_carers_route(service: Carer_service = Depends(get_service)):

    return [c.to_dict() for c in service.get_all_carer()]

@router.get("/{cedula}",response_model=CarerResponse)
def get_carer_route(cedula:str,service: Carer_service = Depends(get_service)):
    carer = service.get_carer_by_cedula(cedula)
    if not carer:
        raise HTTPException(status_code=404,detail="carer not found")
    return carer.to_dict( )

@router.put("/{cedula}", response_model=CarerResponse)
def update_carer_route(cedula: str, data: CarerCreate,service: Carer_service = Depends(get_service)):
    carer = service.update_carer(cedula, data.model_dump())
    if not carer:
        raise HTTPException(status_code=404, detail="Carer not found")
    return carer.to_dict()

@router.delete("/{cedula}")
def delete_carer_route(cedula: str,service: Carer_service = Depends(get_service)):
    success = service.delete_carer(cedula)
    if not success:
        raise HTTPException(status_code=404, detail="Carer not found")
    return {"message": "carer deleted successfully"}