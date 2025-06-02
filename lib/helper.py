from lib.models.patient import Patient
from lib.models.doctor import Doctor
from lib.models.appointment import Appointment
from lib.models.prescription import Prescription
from lib.db.setup_db import Session  # import the sessionmaker

def find_patient_by_id(session, patient_id):
    return session.query(Patient).filter_by(id=patient_id).first()

def find_doctor_by_id(session, doctor_id):
    return session.query(Doctor).filter_by(id=doctor_id).first()

def exit_program():
    print("Exiting the program. Goodbye!")
    exit(0)

def list_patients(session):
    print("\n=== List of Patients ===")
    patients = session.query(Patient).all()
    if not patients:
        print("No patients found.")
    else:
        for patient in patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}")

def list_doctors(session):
    print("\n=== List of Doctors ===")
    doctors = session.query(Doctor).all()
    if not doctors:
        print("No doctors found.")
    else:
        for doctor in doctors:
            print(f"ID: {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}")

def list_appointments(session):
    print("\n=== List of Appointments ===")
    appointments = session.query(Appointment).all()
    if not appointments:
        print("No appointments found.")
    else:
        for appointment in appointments:
            patient = find_patient_by_id(session, appointment.patient_id)
            doctor = find_doctor_by_id(session, appointment.doctor_id)
            print(f"ID: {appointment.id}, Patient: {patient.name if patient else 'Unknown'}, Doctor: {doctor.name if doctor else 'Unknown'}, Date: {appointment.appointment_date}")

def list_prescriptions(session):
    print("\n=== List of Prescriptions ===")
    prescriptions = session.query(Prescription).all()
    if not prescriptions:
        print("No prescriptions found.")
    else:
        for prescription in prescriptions:
            patient = find_patient_by_id(session, prescription.patient_id)
            doctor = find_doctor_by_id(session, prescription.doctor_id)
            print(f"ID: {prescription.id}, Patient: {patient.name if patient else 'Unknown'}, Doctor: {doctor.name if doctor else 'Unknown'}, Medication: {prescription.medication}, Dosage: {prescription.dosage}, Instructions: {prescription.instructions}")