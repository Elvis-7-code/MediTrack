from lib.models.patient import Patient
from lib.models.doctor import Doctor
from lib.models.appointment import Appointment
from lib.models.prescription import Prescription


def find_patient_by_id(patient_id):
    return next((p for p in Patient.all if p.id == patient_id), None)

def find_doctor_by_id(doctor_id):
    return next((d for d in Doctor.all if d.id == doctor_id), None)       


def exit_program():
    print("Exiting the program. Goodbye!")
    exit(0)

def list_patients():
    print("\n=== List of Patients ===")
    if not Patient.all:
        print("No patients found.")
    else:
        for patient in Patient.all:
            print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}")

def list_doctors():
    print("\n=== List of Doctors ===")
    if not Doctor.all:
        print("No doctors found.")
    else:
        for doctor in Doctor.all:
            print(f"ID: {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}")

def list_appointments():
    print("\n=== List of Appointments ===")
    if not Appointment.all:
        print("No appointments found.")
    else:
        for appointment in Appointment.all:
            patient = find_patient_by_id(appointment.patient_id)
            doctor = find_doctor_by_id(appointment.doctor_id)
            print(f"ID: {appointment.id}, Patient: {patient.name if patient else 'Unknown'}, Doctor: {doctor.name if doctor else 'Unknown'}, Date: {appointment.date}")                  

def list_prescriptions():
    print("\n=== List of Prescriptions ===")
    if not Prescription.all:
        print("No prescriptions found.")
    else:
        for prescription in Prescription.all:
            patient = find_patient_by_id(prescription.patient_id)
            doctor = find_doctor_by_id(prescription.doctor_id)
            print(f"ID: {prescription.id}, Patient: {patient.name if patient else 'Unknown'}, Doctor: {doctor.name if doctor else 'Unknown'}, Medication: {prescription.medication}, Dosage: {prescription.dosage}, Instructions: {prescription.instructions}") 
            
             