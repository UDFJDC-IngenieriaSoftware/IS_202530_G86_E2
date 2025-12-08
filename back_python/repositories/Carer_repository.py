from sqlalchemy.orm import Session
from model.Carer import Carer

class Carer_repository:

    def __init__(self,db: Session):

        self.db=db

    def create(self,carer:Carer):

        self.db.add(carer)
        self.db.commit()
        self.db.refresh(carer)
        return carer
    
    def get_all(self):
        return self.db.query(Carer).all()

    def get_by_id(self, cedula_:str):
        return self.db.query(Carer).filter(Carer.cedula == cedula_).first()


    def update(self,cedula_:str,data:dict):
        carer = self.get_by_id(cedula_)
        if not carer:
            return None
        for key, value in data.items():
            setattr(carer, key, value)
        self.db.commit()
        self.db.refresh(carer)
        return carer

    def delete(self,cedula_:str):
        carer = self.get_by_id(cedula_)
        if carer:
            self.db.delete(carer)
            self.db.commit()
        



