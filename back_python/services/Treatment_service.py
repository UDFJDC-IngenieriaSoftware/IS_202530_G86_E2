from model.Treatment import Treatment

fake_db = []

def create_treatment(data):

    new_treatment = Treatment(
        id_treatment=data.id_treatment,
        name=data.name,
        
        especialty=data.especialty,
        end_date=data.end_date,
        start_date=data.start_date,
       
    )

   
    #script agregar cuidadores
    fake_db.append(new_treatment)

    return new_treatment

def get_all_treatment_by_id(id_treatment):



    #se implementará los scripts para recibir los tratamientos por id del usuario
    return fake_db

def get_treatment_by_id(id_treatment):
    for treatment in fake_db:
         #se implementará la función para encontrar el cuidador
        if treatment.id_treatment == id_treatment:
            return treatment



def update_treatment(id_treatment,data):

    treatment = get_treatment_by_id(id_treatment)

    if not treatment:
        return None
    
    treatment.name=data.name
    treatment.especialty=data.especialty
    treatment.end_date=data.end_date
    treatment.start_date=data.start_date
    

    return treatment

def delete_treatment(id_treatment):

    for treatment in fake_db:
        if treatment.id_treatment == id_treatment:
            fake_db.remove(treatment)
            return True
    return False    
    
