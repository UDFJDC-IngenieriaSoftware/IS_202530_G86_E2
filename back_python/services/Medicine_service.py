from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.Medicine_repository import create_medicine, get_medicine_by_name, get_all_medicines, update_medicine, delete_medicine, get_medicine_by_id
from schemas.Medicine_schema import MedicineCreate

from repositories.Medicine_repository import (
    get_all_medicines,
    get_medicine_by_name,
    create_medicine,
    update_medicine,
    delete_medicine,
    get_medicine_by_id
)

def service_get_all(db: Session):
    return get_all_medicines(db)

def service_get_by_name(db: Session, medicine_name: str, concentracion: str, presentacion: str):
    return get_medicine_by_name(db, medicine_name, concentracion, presentacion)

def service_create(db: Session, data):
    return create_medicine(db, data)

def service_update(db: Session, medicine_id: int, data):
    return update_medicine(db, medicine_id, data)

def service_delete(db: Session, medicine_id: int):
    return delete_medicine(db, medicine_id)

def service_get_by_id(db: Session, medicine_id: int):
    return get_medicine_by_id(db, medicine_id)

def service_create(db: Session, data: MedicineCreate):
    nuevo = create_medicine(db, data)
    if nuevo is None:
        raise HTTPException(
            status_code=400,
            detail="El medicamento ya existe en la base de datos."
        )
    return nuevo