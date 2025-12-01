from model.Medicine import Medicine

# Simulación de una base de datos temporal en memoria
fake_db = []
current_id = 1

def create_medicine(data):
    global current_id
    
    new_medicine = Medicine(
        id_medicine=current_id,
        name=data.name,
        dose=data.dose,
        frequency=data.frequency,
        route_of_administration=data.route_of_administration,
        observations=data.observations
    )

    fake_db.append(new_medicine)
    current_id += 1

    return new_medicine

def get_all_medicines():
    return fake_db

def get_medicine_by_id(medicine_id):
    for medicine in fake_db:
        if medicine.id_medicine == medicine_id:
            return medicine
    return None

def update_medicine(medicine_id, data):
    medicine = get_medicine_by_id(medicine_id)
    if not medicine:
        return None

    medicine.name = data.name
    medicine.dose = data.dose
    medicine.frequency = data.frequency
    medicine.route_of_administration = data.route_of_administration
    medicine.observations = data.observations

    return medicine

def delete_medicine(medicine_id):
    for medicine in fake_db:
        if medicine.id_medicine == medicine_id:
            fake_db.remove(medicine)
            return True
    return False
