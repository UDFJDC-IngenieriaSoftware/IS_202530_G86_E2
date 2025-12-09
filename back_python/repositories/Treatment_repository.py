from sqlalchemy.orm import Session
from model.Treatment import Treatment

class TreatmentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Treatment).all()

    def get_by_data(self, nombre: str, cedula: str):
        return self.db.query(Treatment).filter(
            (Treatment.name == nombre) &
            (Treatment.cedula_patient == cedula)
            ).first()
    def get_by_id(self, id_: int):
        return self.db.query(Treatment).filter(
            (Treatment.id_treatment == id_)
        ).first()

    def create(self, treatment: Treatment):
        self.db.add(treatment)
        self.db.commit()
        self.db.refresh(treatment)
        return treatment

    def delete(self, id_: int):
        treatment = self.get_by_id(id_)
        if treatment:
            self.db.delete(treatment)
            self.db.commit()
        return treatment

    def update(self, id_: int, data: dict):
        treatment = self.get_by_id(id_)
        if not treatment:
            return None
        for key, value in data.items():
            setattr(treatment, key, value)
        self.db.commit()
        self.db.refresh(treatment)
        return treatment
