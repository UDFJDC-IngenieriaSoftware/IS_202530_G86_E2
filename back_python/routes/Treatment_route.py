from fastapi import Depends,APIRouter, HTTPException
from schemas.Treatment_schema import TreatmentCreate,TreatmentResponse
from services.Treatment_service import Treatment_service
from repositories.Treatment_repository import TreatmentRepository
from db.database import get_db

router = APIRouter(prefix="/treatment",tags=["Treatments"])

def get_service(db=Depends(get_db)):
    repo = TreatmentRepository(db)
    return Treatment_service(repo)



@router.post("/",response_model=TreatmentResponse)
def create_treatment_route(data:TreatmentCreate,service: Treatment_service = Depends(get_service)):
    treatment = service.create_treatment(data.model_dump())
    return treatment.to_dict()

@router.get("/}",response_model=list[TreatmentResponse])
def list_treatments_route(service: Treatment_service = Depends(get_service)):

    return [p.to_dict() for p in service.get_all_treatment_by_id()]

@router.get("/{id_treatment}",response_model=TreatmentResponse)
def get_treatment_route(id_treatment:str,service: Treatment_service = Depends(get_service)):
    treatment = service.get_treatment_by_id(id_treatment)
    if not treatment:
        raise HTTPException(status_code=404,detail="treatment not found")
    return treatment.to_dict( )

@router.put("/{id_treatment}", response_model=TreatmentResponse)
def update_treatment_route(id_treatment: str, data: TreatmentCreate,service: Treatment_service = Depends(get_service)):
    treatment = service.update_treatment(id_treatment, data.model_dump())
    if not treatment:
        raise HTTPException(status_code=404, detail="treatment not found")
    return treatment.to_dict()

@router.delete("/{id_treatment}")
def delete_treatment_route(id_treatment: str,service: Treatment_service = Depends(get_service)):
    success = service.delete_treatment(id_treatment)
    if not success:
        raise HTTPException(status_code=404, detail="treatment not found")
    return {"message": "treatment deleted successfully"}




