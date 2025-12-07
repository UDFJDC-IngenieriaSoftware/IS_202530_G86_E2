from repositories.Carer_repository import Carer_repository

from model.Carer import Carer



class Carer_service:

    def __init__(self, repo: Carer_repository):
        self.repo= repo

    def create_carer(self,data):
        carer= Carer(**data)
        return self.repo.create(carer)
    
    def get_all_carer(self):
        return self.repo.get_all()


    def get_carer_by_cedula(self,cedula_):
        return self.repo.get_by_id(cedula_)    



    def update_carer(self,cedula_,data):

        return self.repo.update(cedula_,data)

    def delete_carer(self,cedula_):
        self.repo.delete(cedula_)
        return 'eliminado correctamente '


    


