from sqlalchemy.orm import Session
from model.Reminder import Reminder
from schemas.Reminder_schema import ReminderCreate


def create_reminder(db: Session, data: ReminderCreate):
    reminder = Reminder(
        idMedicamento=data.idMedicamento,
        idTratamiento=data.idTratamiento,
        estadoEnvio=data.estadoEnvio,
        respuestaPaciente=data.respuestaPaciente,
        fechaEnvioRecordatorio=data.fechaEnvioRecordatorio,
        fechaRespuesta=data.fechaRespuesta,
        notas=data.notas
    )
    db.add(reminder)
    db.commit()
    db.refresh(reminder)
    return reminder


def get_all_reminders(db: Session):
    return db.query(Reminder).all()


def get_reminder_by_id(db: Session, reminder_id: int):
    return db.query(Reminder).filter(Reminder.idRecordatorio == reminder_id).first()


def update_reminder(db: Session, reminder_id: int, data: ReminderCreate):
    reminder = get_reminder_by_id(db, reminder_id)

    if not reminder:
        return None

    reminder.idMedicamento = data.idMedicamento
    reminder.idTratamiento = data.idTratamiento
    reminder.estadoEnvio = data.estadoEnvio
    reminder.respuestaPaciente = data.respuestaPaciente
    reminder.fechaEnvioRecordatorio = data.fechaEnvioRecordatorio
    reminder.fechaRespuesta = data.fechaRespuesta
    reminder.notas = data.notas

    db.commit()
    db.refresh(reminder)
    return reminder


def delete_reminder(db: Session, reminder_id: int):
    reminder = get_reminder_by_id(db, reminder_id)
    if not reminder:
        return None
    db.delete(reminder)
    db.commit()
    return True
