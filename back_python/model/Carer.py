
class Carer:

    def __init__(self, cedula, name, first_lastname, second_lastname, phone):
        self.cedula = cedula
        self.name = name            
        self.second_name= ""
        self.first_lastname = first_lastname
        self.second_lastname = second_lastname
        self.phone = phone
        self.patients = []

        # el carer debe poder agregar pacientes?

    def add_patient(self, patient):
        self.patients.append(patient)    
        
    