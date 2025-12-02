from model.Patient import Patient

fake_db = []

def create_patient(data):

    new_patient = Patient(
        cedula=data.cedula,
        name=data.name,
        
        first_lastname=data.first_lastname,
        second_lastname=data.second_lastname,
        phone=data.phone,
        date_of_birth=data.date_of_birth
    )

    if(data.second_name != ""):
        new_patient.second_lastname=data.second_name

    #script agregar cuidadores
    fake_db.append(new_patient)

    return new_patient

def get_all_patient():

    #se implementará los scripts para recibir los cuidadores
    return fake_db

def get_patient_by_id(cedula):
    for patient in fake_db:
         #se implementará la función para encontrar el cuidador
        if patient.cedula == cedula:
            return patient



def update_patient(cedula,data):

    patient = get_patient_by_id(cedula)

    if not patient:
        return None
    
    patient.name=data.name
    patient.second_name=data.second_name
    patient.first_lastname=data.first_lastname
    patient.second_lastname=data.second_lastname
    patient.phone=data.phone
    patient.date_of_birth=data.date_of_birth

    return patient

def delete_patient(cedula):

    for patient in fake_db:
        if patient.cedula == cedula:
            fake_db.remove(patient)
            return True
    return False    
    





