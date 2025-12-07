from sqlalchemy.orm import Session
from repositories.Medicine_repository import (
    get_all_medicines,
    get_medicine_by_id,
    create_medicine,
    update_medicine,
    delete_medicine
)

def service_get_all(db: Session):
    return get_all_medicines(db)

def service_get_by_id(db: Session, medicine_id: int):
    return get_medicine_by_id(db, medicine_id)

def service_create(db: Session, data):
    return create_medicine(db, data)

def service_update(db: Session, medicine_id: int, data):
    return update_medicine(db, medicine_id, data)

def service_delete(db: Session, medicine_id: int):
    return delete_medicine(db, medicine_id)
