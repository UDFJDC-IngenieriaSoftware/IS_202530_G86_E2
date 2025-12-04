from fastapi import APIRouter, HTTPException
from schemas.Treatment_schema import TreatmentCreate,TreatmentResponse
from services.Treatment_service import(

create_treatment,
get_all_treatment_by_id,
get_treatment_by_id,
update_treatment,
delete_treatment

)

router = APIRouter(prefix="/treatment",tags=["Treatments"])

@router.post("/",response_model=TreatmentResponse)
def create_treatment_route(data:TreatmentCreate):
    treatment = create_treatment(data)
    return treatment.to_dict()

@router.get("/}",response_model=list[TreatmentResponse])
def list_treatments():

    return [p.to_dict() for p in get_all_treatment_by_id()]

@router.get("/{id_treatment}",response_model=TreatmentResponse)
def get_treatment(id_treatment:str):
    treatment = get_treatment_by_id(id_treatment)
    if not treatment:
        raise HTTPException(status_code=404,detail="treatment not found")
    return treatment.to_dict( )

@router.put("/{id_treatment}", response_model=TreatmentResponse)
def update_treatment_route(id_treatment: str, data: TreatmentCreate):
    treatment = update_treatment(id_treatment, data)
    if not treatment:
        raise HTTPException(status_code=404, detail="treatment not found")
    return treatment.to_dict()

@router.delete("/{id_treatment}")
def delete_treatment_route(id_treatment: str):
    success = delete_treatment(id_treatment)
    if not success:
        raise HTTPException(status_code=404, detail="treatment not found")
    return {"message": "treatment deleted successfully"}




