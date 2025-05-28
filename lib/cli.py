from lib.models.patient import Patient
from lib.models.doctor import Doctor
from lib.models.appointment import Appointment
from lib.models.prescription import Prescription

def main():
    print("=== MediTrack Hospital Management System ===\n")

    print("Patients:")
    for p in Patient.all:
        print(f" - {p}")