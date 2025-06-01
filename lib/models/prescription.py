# prescription.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup_db import Base

class Prescription(Base):
    __tablename__ = 'prescriptions'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    medication = Column(String)
    dosage = Column(String)
    instructions = Column(String)

    patient = relationship("Patient", back_populates="prescriptions")
    doctor = relationship("Doctor", back_populates="prescriptions")

    def __repr__(self):
        return f"<Prescription {self.medication} for {self.patient.name}>"