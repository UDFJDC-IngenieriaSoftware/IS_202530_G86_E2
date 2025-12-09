from sqlalchemy.orm import Session
from model.Reminder import Recordatorio

def get_all_reminders(db: Session):
    return db.query(Recordatorio).all()

def get_reminder_by_id(db: Session, reminder_id: int):
    return db.query(Recordatorio).filter(Recordatorio.idRecordatorio == reminder_id).first()

def create_reminder(db: Session, data):
    nuevo = Recordatorio(
        idMedicamento=data.idMedicamento,
        idTratamiento=data.idTratamiento,
        estadoEnvio=data.estadoEnvio,
        respuestaPaciente=data.respuestaPaciente,
        minutosFaltantes=data.minutosFaltantes,
        fechaEnvioRecordatorio=data.fechaEnvioRecordatorio,
        fechaRespuesta=data.fechaRespuesta,
        notas=data.notas
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_reminder(db: Session, reminder_id: int, data):
    reminder = get_reminder_by_id(db, reminder_id)
    if not reminder:
        return None

    reminder.idMedicamento = data.idMedicamento
    reminder.idTratamiento = data.idTratamiento
    reminder.estadoEnvio = data.estadoEnvio
    reminder.respuestaPaciente = data.respuestaPaciente
    reminder.fechaEnvioRecordatorio = data.fechaEnvioRecordatorio
    reminder.minutosFaltantes = data.minutosFaltantes
    reminder.fechaRespuesta = data.fechaRespuesta
    reminder.notas = data.notas

    db.commit()
    db.refresh(reminder)
    return reminder

def delete_reminder(db: Session, reminder_id: int):
    reminder = get_reminder_by_id(db, reminder_id)
    if reminder:
        db.delete(reminder)
        db.commit()
        return True
    return False
