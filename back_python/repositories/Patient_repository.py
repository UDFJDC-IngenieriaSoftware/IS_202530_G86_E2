from sqlalchemy.orm import Session
from model.Patient import Patient

class Patient_repository:

    def __init__(self,db: Session):

        self.db=db

    def create(self,patient:Patient):

        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient
    
    def get_all(self):
        return self.db.query(Patient).all()

    def get_by_id(self, cedula_:int):
        return self.db.query(Patient).filter(Patient.cedula == cedula_).first()


    def update(self,cedula_:int,data:dict):
        patient = self.get_by_id(cedula_)
        if not patient:
            return None
        for key, value in data.items():
            setattr(patient, key, value)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def delete(self,cedula_:int):
        patient = self.get_by_id(cedula_)
        if patient:
            self.db.delete(patient)
            self.db.commit()
        return patient



