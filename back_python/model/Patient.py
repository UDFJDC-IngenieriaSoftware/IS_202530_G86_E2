

class Patient:
    def __init__(self, cedula, name, first_lastname, second_lastname, phone,date_of_birth):
        self.cedula = cedula
        self.name = name
        self.second_name= ""
        self.first_lastname = first_lastname
        self.second_lastname = second_lastname
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.carers = []  
        self.treatments = []
        #como se debe tratar los cuidadores?

    def add_carer(self, carer):
        self.carers.append(carer)      
    
    def add_treatment(self, treatment):
        self.treatments.append(treatment)

        