from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db

from schemas.Reminder_schema import ReminderCreate, ReminderResponse
from services.Reminder_service import (
    create_reminder,
    get_all_reminders,
    get_reminder_by_id,
    update_reminder,
    delete_reminder
)

router = APIRouter(prefix="/reminders", tags=["Reminders"])


@router.post("/", response_model=ReminderResponse)
def create(data: ReminderCreate, db: Session = Depends(get_db)):
    return create_reminder(db, data)


@router.get("/", response_model=list[ReminderResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_reminders(db)


@router.get("/{reminder_id}", response_model=ReminderResponse)
def get(reminder_id: int, db: Session = Depends(get_db)):
    reminder = get_reminder_by_id(db, reminder_id)
    if not reminder:
        raise HTTPException(404, "Reminder not found")
    return reminder


@router.put("/{reminder_id}", response_model=ReminderResponse)
def update(reminder_id: int, data: ReminderCreate, db: Session = Depends(get_db)):
    reminder = update_reminder(db, reminder_id, data)
    if not reminder:
        raise HTTPException(404, "Reminder not found")
    return reminder


@router.delete("/{reminder_id}")
def delete(reminder_id: int, db: Session = Depends(get_db)):
    ok = delete_reminder(db, reminder_id)
    if not ok:
        raise HTTPException(404, "Reminder not found")
    return {"message": "Reminder deleted"}
