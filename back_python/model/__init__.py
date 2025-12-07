# model/__init__.py
from db.database import Base

# Import ALL models here - this registers them with SQLAlchemy
from .Carer import Carer
from .Patient import Patient
from .Carer_Patient import Carer_Patient
from .Treatment import Treatment  # If you have this
# ... import any other models you have

# Make them available when importing from model
__all__ = ["Base", "Carer", "Patient", "Carer_Patient", "Treatment"]