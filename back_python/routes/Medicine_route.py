from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.Medicine_schema import MedicineCreate, MedicineResponse
from services.Medicine_service import (
    service_get_all,
    service_get_by_id,
    service_create,
    service_update,
    service_delete
)

router = APIRouter(prefix="/medicines", tags=["Medicines"])

@router.get("/", response_model=list[MedicineResponse])
def list_all(db: Session = Depends(get_db)):
    return service_get_all(db)

@router.get("/{medicine_id}", response_model=MedicineResponse)
def get_by_id(medicine_id: int, db: Session = Depends(get_db)):
    med = service_get_by_id(db, medicine_id)
    if not med:
        raise HTTPException(404, "Medicine not found")
    return med

@router.post("/", response_model=MedicineResponse)
def create(data: MedicineCreate, db: Session = Depends(get_db)):
    return service_create(db, data)

@router.put("/{medicine_id}", response_model=MedicineResponse)
def update(medicine_id: int, data: MedicineCreate, db: Session = Depends(get_db)):
    med = service_update(db, medicine_id, data)
    if not med:
        raise HTTPException(404, "Medicine not found")
    return med

@router.delete("/{medicine_id}")
def delete(medicine_id: int, db: Session = Depends(get_db)):
    ok = service_delete(db, medicine_id)
    if not ok:
        raise HTTPException(404, "Medicine not found")
    return {"message": "Medicine deleted"}
