from fastapi import APIRouter, HTTPException
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
def create(data: ReminderCreate):
    reminder = create_reminder(data)
    return reminder.to_dict()

@router.get("/", response_model=list[ReminderResponse])
def list_all():
    return [r.to_dict() for r in get_all_reminders()]

@router.get("/{reminder_id}", response_model=ReminderResponse)
def get(reminder_id: int):
    reminder = get_reminder_by_id(reminder_id)
    if not reminder:
        raise HTTPException(404, "Reminder not found")
    return reminder.to_dict()

@router.put("/{reminder_id}", response_model=ReminderResponse)
def update(reminder_id: int, data: ReminderCreate):
    reminder = update_reminder(reminder_id, data)
    if not reminder:
        raise HTTPException(404, "Reminder not found")
    return reminder.to_dict()

@router.delete("/{reminder_id}")
def delete(reminder_id: int):
    delete_reminder(reminder_id)
    return {"message": "Reminder deleted"}
