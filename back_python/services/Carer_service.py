from model.Carer import Carer

fake_db = []

def create_carer(data):

    new_carer = Carer(
        cedula=data.cedula,
        name=data.name,
        
        first_lastname=data.first_lastname,
        second_lastname=data.second_lastname,
        phone=data.phone

    )
    #por si tiene segundo nombre
    if(data.second_name != ""):
        new_carer.second_lastname=data.second_name

    #script agregar cuidadores
    fake_db.append(new_carer)    


    return new_carer

def get_all_carer():
    #se implementará los scripts para recibir los cuidadores
    return fake_db

def get_carer_by_id(cedula):
    for carer in fake_db:
         #se implementará la función para encontrar el cuidador
        if carer.cedula == cedula:
            return carer

def update_carer(cedula,data):

    carer = get_carer_by_id(cedula)

    if not carer:
        return None
    
    carer.name=data.name
    carer.second_name=data.second_name
    carer.first_lastname=data.first_lastname
    carer.second_lastname=data.second_lastname
    carer.phone=data.phone

    return carer

def delete_carer(cedula):

    for carer in fake_db:
        if carer.cedula == cedula:
            fake_db.remove(carer)
            return True
    return False    
    




