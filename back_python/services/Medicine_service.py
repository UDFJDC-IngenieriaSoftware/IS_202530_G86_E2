from sqlalchemy.orm import Session
from model.Medicine import Medicine
from schemas.Medicine_schema import MedicineCreate

# CREATE
def create_medicine(db: Session, data: MedicineCreate):
    new_medicine = Medicine(
        nombreMedicamento=data.nombreMedicamento,
        observaciones=data.observaciones
    )
    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)
    return new_medicine

# READ ALL
def get_all_medicines(db: Session):
    return db.query(Medicine).all()

# READ ONE
def get_medicine_by_id(db: Session, medicine_id: int):
    return db.query(Medicine).filter(Medicine.idMedicamento == medicine_id).first()

# UPDATE
def update_medicine(db: Session, medicine_id: int, data: MedicineCreate):
    medicine = get_medicine_by_id(db, medicine_id)
    if not medicine:
        return None

    medicine.nombreMedicamento = data.nombreMedicamento
    medicine.observaciones = data.observaciones

    db.commit()
    db.refresh(medicine)
    return medicine

# DELETE
def delete_medicine(db: Session, medicine_id: int):
    medicine = get_medicine_by_id(db, medicine_id)
    if not medicine:
        return None

    db.delete(medicine)
    db.commit()
    return True
