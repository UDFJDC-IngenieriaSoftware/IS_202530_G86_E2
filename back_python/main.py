from fastapi import FastAPI
from routes.Medicine_route import router as medicine_router
from routes.Reminder_route import router as reminder_router

app = FastAPI()
app.include_router(medicine_router)
app.include_router(reminder_router)

@app.get("/")
def read_root():
    return {"message": "prueba WhatsPills?"}