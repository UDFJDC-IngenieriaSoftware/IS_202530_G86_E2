
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
        
    def to_dict(self):

        return {
           "cedula":self.cedula,
           "name":self.name,
           "second_name":self.second_name,
           "first_lastname":self.first_lastname,
           "second_lastname":self.second_lastname,
           "phone":self.phone,
           "patients": self.patients


        }
        

