# doctor.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.base import Base

class Doctor(Base):
    all = []
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)

    appointments = relationship("Appointment", back_populates="doctor")
    prescriptions = relationship("Prescription", back_populates="doctor")

    def __repr__(self):
        return f"<Doctor {self.name}, ID: {self.id}>"