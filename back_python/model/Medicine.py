class Medicine:

    def __init__(self, id_medicine, name, dose, frequency, route_of_administration, observations):
        self.id_medicine = id_medicine
        self.name = name
        self.dose = dose
        self.frequency = frequency
        self.route_of_administration = route_of_administration
        self.observations = observations
        self.reminders = []

    def add_reminder(self, reminder):
        self.reminders.append(reminder)

    def to_dict(self):
        return {
            "id_medicine": self.id_medicine,
            "name": self.name,
            "dose": self.dose,
            "frequency": self.frequency,
            "route_of_administration": self.route_of_administration,
            "observations": self.observations,
            "reminders": self.reminders
        }
