

class Reminder:
    def __init__(self, id_reminder, estado_envio, answer_patient, date_answer,date_reminder):
        self.id_reminder = id_reminder
        self.estado_envio = estado_envio
        self.answer_patient = answer_patient
        self.date_answer = date_answer
        self.date_reminder = date_reminder

    def set_answer(self, answer_patient, date_answer):
        self.answer_patient = answer_patient
        self.date_answer = date_answer    