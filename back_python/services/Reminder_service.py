from sqlalchemy.orm import Session
from repositories.Reminder_repository import (
    get_all_reminders,
    get_reminder_by_id,
    create_reminder,
    update_reminder,
    delete_reminder
)

def service_get_all(db: Session):
    return get_all_reminders(db)

def service_get_by_id(db: Session, reminder_id: int):
    return get_reminder_by_id(db, reminder_id)

def service_create(db: Session, data):
    return create_reminder(db, data)

def service_update(db: Session, reminder_id: int, data):
    return update_reminder(db, reminder_id, data)

def service_delete(db: Session, reminder_id: int):
    return delete_reminder(db, reminder_id)
