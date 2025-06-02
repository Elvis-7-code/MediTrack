# lib/db/seed.py

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.base import Base
from lib.models.patient import Patient
from lib.models.doctor import Doctor
from lib.models.appointment import Appointment
from lib.models.prescription import Prescription

# Setup database engine and session (adjust path if needed)
engine = create_engine("sqlite:///lib/db/meditrack_db.sqlite", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    # Clear existing data (optional)
    session.query(Prescription).delete()
    session.query(Appointment).delete()
    session.query(Patient).delete()
    session.query(Doctor).delete()
    session.commit()

    # Create doctors
    dr_smith = Doctor(name="John Smith", specialization="Cardiology")
    dr_jones = Doctor(name="Emily Jones", specialization="Dermatology")

    # Create patients
    patient_anna = Patient(name="Anna Brown", age=29, gender="Female")
    patient_mike = Patient(name="Mike Davis", age=45, gender="Male")

    # Add doctors and patients to session
    session.add_all([dr_smith, dr_jones, patient_anna, patient_mike])
    session.commit()

    # Create appointments
    appt1 = Appointment(
        patient_id=patient_anna.id,
        doctor_id=dr_smith.id,
        appointment_date=datetime.date(2025, 6, 5),
        notes="Routine check-up"
    )
    appt2 = Appointment(
        patient_id=patient_mike.id,
        doctor_id=dr_jones.id,
        appointment_date=datetime.date(2025, 6, 10),
        notes="Skin rash evaluation"
    )

    # Create prescriptions
    presc1 = Prescription(
        patient_id=patient_anna.id,
        doctor_id=dr_smith.id,
        medication="Atorvastatin",
        dosage="10mg",
        instructions="Take once daily after dinner"
    )
    presc2 = Prescription(
        patient_id=patient_mike.id,
        doctor_id=dr_jones.id,
        medication="Hydrocortisone Cream",
        dosage="Apply twice daily",
        instructions="Apply to affected area"
    )

    # Add appointments and prescriptions
    session.add_all([appt1, appt2, presc1, presc2])
    session.commit()

    print("✅ Seed data added successfully!")

if __name__ == "__main__":
    seed_data()