from fastapi import APIRouter, HTTPException
from schemas.Medicine_schema import MedicineCreate, MedicineResponse
from services.Medicine_service import (
    create_medicine,
    get_all_medicines,
    get_medicine_by_id,
    update_medicine,
    delete_medicine
)

router = APIRouter(prefix="/medicines", tags=["Medicines"])

@router.post("/", response_model=MedicineResponse)
def create_medicine_route(data: MedicineCreate):
    medicine = create_medicine(data)
    return medicine.to_dict()

@router.get("/", response_model=list[MedicineResponse])
def list_medicines():
    return [m.to_dict() for m in get_all_medicines()]

@router.get("/{medicine_id}", response_model=MedicineResponse)
def get_medicine(medicine_id: int):
    medicine = get_medicine_by_id(medicine_id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine.to_dict()

@router.put("/{medicine_id}", response_model=MedicineResponse)
def update_medicine_route(medicine_id: int, data: MedicineCreate):
    medicine = update_medicine(medicine_id, data)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine.to_dict()

@router.delete("/{medicine_id}")
def delete_medicine_route(medicine_id: int):
    success = delete_medicine(medicine_id)
    if not success:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return {"message": "Medicine deleted successfully"}
