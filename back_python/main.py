from fastapi import FastAPI
from routes.Carer_route import router as carer_router
from routes.Patient_route import router as patient_route
from routes.Treatment_route import router as treatment_route


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "prueba WhatsPills?"}









app.include_router(carer_router)
app.include_router(patient_route)
app.include_router(treatment_route)