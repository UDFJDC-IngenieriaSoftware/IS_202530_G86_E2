from repositories.Patient_repository import Patient_repository

from model.Patient import Patient


class Patient_service:

    def __init__(self, repo: Patient_repository):
        self.repo= repo

    def create_patient(self,data):
        patient= Patient(**data)
        return self.repo.create(patient)
    
    def get_all_patient(self):
        return self.repo.get_all()


    def get_patient_by_cedula(self,cedula_):
        return self.repo.get_by_id(cedula_)    



    def update_patient(self,cedula_,data):

        return self.repo.update(cedula_,data)

    def delete_patient(self,cedula_):
        self.repo.delete(cedula_)
        return 'eliminado correctamente '


    


