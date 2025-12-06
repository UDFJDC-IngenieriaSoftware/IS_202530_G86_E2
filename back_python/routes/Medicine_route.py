from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.Medicine_schema import MedicineCreate, MedicineResponse
from services.Medicine_service import (
    create_medicine,
    get_all_medicines,
    get_medicine_by_id,
    update_medicine,
    delete_medicine,
)

router = APIRouter(prefix="/medicines", tags=["Medicines"])

@router.post("/", response_model=MedicineResponse)
def create(data: MedicineCreate, db: Session = Depends(get_db)):
    return create_medicine(db, data)

@router.get("/", response_model=list[MedicineResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_medicines(db)

@router.get("/{medicine_id}", response_model=MedicineResponse)
def get(medicine_id: int, db: Session = Depends(get_db)):
    med = get_medicine_by_id(db, medicine_id)
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return med

@router.put("/{medicine_id}", response_model=MedicineResponse)
def update(medicine_id: int, data: MedicineCreate, db: Session = Depends(get_db)):
    med = update_medicine(db, medicine_id, data)
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return med

@router.delete("/{medicine_id}")
def delete(medicine_id: int, db: Session = Depends(get_db)):
    ok = delete_medicine(db, medicine_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return {"message": "Medicine deleted successfully"}
