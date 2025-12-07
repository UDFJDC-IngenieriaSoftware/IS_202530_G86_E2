from fastapi import Depends,APIRouter, HTTPException
from schemas.Patient_schema import PatientCreate,PatientResponse
from services.Patient_service import Patient_service
from  repositories.Patient_repository import Patient_repository
from db.database import get_db


router = APIRouter(prefix="/patient",tags=["Patients"])

def get_service(db=Depends(get_db)):
    repo = Patient_repository(db)
    return Patient_service(repo)


@router.post("/",response_model=PatientResponse)
def create_patient_route(data:PatientCreate,service: Patient_service = Depends(get_service)):
    patient = service.create_patient(data.model_dump())
    return patient.to_dict()

@router.get("/",response_model=list[PatientResponse])
def list_patients_route(service: Patient_service = Depends(get_service)):

    return [p.to_dict() for p in service.get_all_patient()]

@router.get("/{cedula}",response_model=PatientResponse)
def get_patient_route(cedula:str,service: Patient_service = Depends(get_service)):
    patient = service.get_patient_by_cedula(cedula)
    if not patient:
        raise HTTPException(status_code=404,detail="patient not found")
    return patient.to_dict( )

@router.put("/{cedula}", response_model=PatientResponse)
def update_patient_route(cedula: str, data: PatientCreate,service: Patient_service = Depends(get_service)):
    patient = service.update_patient(cedula, data.model_dump())
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    return patient.to_dict()

@router.delete("/{cedula}")
def delete_patient_route(cedula: str,service: Patient_service = Depends(get_service)):
    success = service.delete_patient(cedula)
    if not success:
        raise HTTPException(status_code=404, detail="patient not found")
    return {"message": "patient deleted successfully"}