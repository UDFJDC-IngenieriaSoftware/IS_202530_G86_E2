from fastapi import APIRouter, HTTPException
from schemas.Patient_schema import PatientCreate,PatientResponse
from services.Patient_service import (

create_patient,
get_all_patient,
get_patient_by_id,
update_patient,
delete_patient

)

router = APIRouter(prefix="/patient",tags=["Patients"])

@router.post("/",response_model=PatientResponse)
def create_patient_route(data:PatientCreate):
    patient = create_patient(data)
    return patient.to_dict()

@router.get("/",response_model=list[PatientResponse])
def list_patients():

    return [p.to_dict() for p in get_all_patient()]

@router.get("/{cedula}",response_model=PatientResponse)
def get_patient(cedula:str):
    patient = get_patient_by_id(cedula)
    if not patient:
        raise HTTPException(status_code=404,detail="patient not found")
    return patient.to_dict( )

@router.put("/{cedula}", response_model=PatientResponse)
def update_patient_route(cedula: str, data: PatientCreate):
    patient = update_patient(cedula, data)
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    return patient.to_dict()

@router.delete("/{cedula}")
def delete_patient_route(cedula: str):
    success = delete_patient(cedula)
    if not success:
        raise HTTPException(status_code=404, detail="patient not found")
    return {"message": "patient deleted successfully"}