# patient.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.base import Base

class Patient(Base):
    all = []

    
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    appointments = relationship("Appointment", back_populates="patient")
    prescriptions = relationship("Prescription", back_populates="patient")

    def __repr__(self):
        return f"<Patient {self.name} (ID: {self.id})>"
    
