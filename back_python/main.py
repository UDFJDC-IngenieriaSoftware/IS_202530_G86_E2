from fastapi import FastAPI
from routes.Carer_route import router as carer_router
from routes.Patient_route import router as patient_route
from routes.Treatment_route import router as treatment_route
from sqlalchemy import text
from db.database import get_db



def test_connection():
    db_generator = get_db()
    db = next(db_generator)  
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        print("Conexión exitosa, prueba:", result)
    finally:
        next(db_generator, None) 

if __name__ == "__main__":
    test_connection()


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "prueba WhatsPills?"}









app.include_router(carer_router)
app.include_router(patient_route)
app.include_router(treatment_route)