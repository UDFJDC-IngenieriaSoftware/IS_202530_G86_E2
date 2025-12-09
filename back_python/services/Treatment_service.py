from repositories.Treatment_repository import TreatmentRepository

from model.Treatment import Treatment



class Treatment_service:

    def __init__(self, repo: TreatmentRepository):
        self.repo= repo

    def create_treatment(self,data):
        treatment= Treatment(**data)
        return self.repo.create(treatment)
    
    def get_all_treatment(self):
        return self.repo.get_all()


    def get_treatment_by_data(self,nombre, cedula):
        return self.repo.get_by_data(nombre,)    

    def get_treatment_by_id(self,id):
        return self.repo.get_by_id(id)    


    def update_treatment(self,id_,data):

        return self.repo.update(id_,data)

    def delete_treatment(self,id_):
        self.repo.delete(id_)
        return 'eliminado correctamente '    
