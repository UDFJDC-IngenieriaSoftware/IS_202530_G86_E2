from fastapi import FastAPI
from sqlalchemy import text
from db.database import get_db
from model import Carer, Patient, Carer_Patient, Treatment 

from routes.Carer_route import router as carer_router
from routes.Patient_route import router as patient_route
from routes.Treatment_route import router as treatment_route
from routes.Reminder_route import router as reminder_router
from routes.Medicine_route import router as medicine_router
from sqlalchemy.orm import declarative_base
from db.database import engine, Base
app = FastAPI()

app.include_router(carer_router)
app.include_router(patient_route)
app.include_router(treatment_route)
app.include_router(medicine_router)
app.include_router(reminder_router)


@app.get("/")
def read_root():
    return {"message": "prueba WhatsPills?"}


Base = declarative_base()
@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
