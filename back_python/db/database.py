
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os


load_dotenv()

DATABASE_URL = os.getenv("SUPABASE_DB_URL")

if not DATABASE_URL:
    raise ValueError("La variable SUPABASE_DB_URL no está definida en el entorno o .env")


engine = create_engine(
    DATABASE_URL,
    pool_size=10,        
    max_overflow=5,      
    pool_pre_ping=True   
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
