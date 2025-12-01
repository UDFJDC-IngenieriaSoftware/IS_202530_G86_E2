from model.Reminder import Reminder

reminders_db = []
current_id = 1

def create_reminder(data):
    global current_id
    reminder = Reminder(
        id_reminder=current_id,
        estado_envio=data.estado_envio,
        answer_patient=data.answer_patient,
        date_answer=data.date_answer,
        date_reminder=data.date_reminder
    )
    reminders_db.append(reminder)
    current_id += 1
    return reminder

def get_all_reminders():
    return reminders_db

def get_reminder_by_id(reminder_id):
    for r in reminders_db:
        if r.id_reminder == reminder_id:
            return r
    return None

def update_reminder(reminder_id, data):
    reminder = get_reminder_by_id(reminder_id)
    if reminder:
        reminder.estado_envio = data.estado_envio
        reminder.answer_patient = data.answer_patient
        reminder.date_answer = data.date_answer
        reminder.date_reminder = data.date_reminder
    return reminder

def delete_reminder(reminder_id):
    global reminders_db
    reminders_db = [r for r in reminders_db if r.id_reminder != reminder_id]
    return True
