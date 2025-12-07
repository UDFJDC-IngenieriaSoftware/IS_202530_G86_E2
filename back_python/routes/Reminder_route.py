from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.Reminder_schema import ReminderCreate, ReminderResponse
from services.Reminder_service import (
    service_get_all,
    service_get_by_id,
    service_create,
    service_update,
    service_delete
)

router = APIRouter(prefix="/reminders", tags=["Reminders"])

@router.get("/", response_model=list[ReminderResponse])
def list_all(db: Session = Depends(get_db)):
    return service_get_all(db)

@router.get("/{reminder_id}", response_model=ReminderResponse)
def get_by_id(reminder_id: int, db: Session = Depends(get_db)):
    rem = service_get_by_id(db, reminder_id)
    if not rem:
        raise HTTPException(404, "Reminder not found")
    return rem

@router.post("/", response_model=ReminderResponse)
def create(data: ReminderCreate, db: Session = Depends(get_db)):
    return service_create(db, data)

@router.put("/{reminder_id}", response_model=ReminderResponse)
def update(reminder_id: int, data: ReminderCreate, db: Session = Depends(get_db)):
    rem = service_update(db, reminder_id, data)
    if not rem:
        raise HTTPException(404, "Reminder not found")
    return rem

@router.delete("/{reminder_id}")
def delete(reminder_id: int, db: Session = Depends(get_db)):
    ok = service_delete(db, reminder_id)
    if not ok:
        raise HTTPException(404, "Reminder not found")
    return {"message": "Reminder deleted"}
