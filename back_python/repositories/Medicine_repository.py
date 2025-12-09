from sqlalchemy.orm import Session
from model.Medicine import Medicamento
from schemas.Medicine_schema import MedicineCreate

def get_all_medicines(db: Session):
    return db.query(Medicamento).all()

def get_medicine_by_name(db: Session, medicine_name: str, concentracion: str, presentacion: str):
    return db.query(Medicamento).filter(
        (Medicamento.nombreMedicamento == medicine_name)
        & (Medicamento.concentracion == concentracion) 
        & (Medicamento.presentacion == presentacion)
        ).first()
    
def get_medicine_by_id(db: Session, medicine_id:int):
    return db.query(Medicamento).filter(
        Medicamento.idMedicamento == medicine_id
    ).first()
    
def create_medicine(db: Session, data: MedicineCreate):

    # Verificar si ya existe
    existente = get_medicine_by_name(db, data.nombreMedicamento, data.concentracion, data.presentacion)
    if existente:
        return None  # lo manejamos en el servicio

    nuevo = Medicamento(
        nombreMedicamento=data.nombreMedicamento,
        presentacion=data.presentacion,
        concentracion=data.concentracion
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_medicine(db: Session, medicine_id: int, data):
    med = get_medicine_by_id(db, medicine_id)
    if not med:
        return None

    med.nombreMedicamento = data.nombreMedicamento
    med.observaciones = data.observaciones

    db.commit()
    db.refresh(med)
    return med

def delete_medicine(db: Session, medicine_id: int):
    med = get_medicine_by_id(db, medicine_id)
    if med:
        db.delete(med)
        db.commit()
        return True
    return False
