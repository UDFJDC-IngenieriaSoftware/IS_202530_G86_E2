

class Treatment:

    def __init__(self, id_treatment, name, especialty, end_date, start_date):
        self.id_treatment = id_treatment
        self.name = name
        self.especialty = especialty
        self.end_date = end_date
        self.start_date = start_date
        self.medicines = []

    def add_medicine(self, medicine):
        self.medicines.append(medicine)    