from lib.models.patient  import Patient
from lib.models.patient import Doctor

def find_patient_by_id(patient_id):
    return((p for p in Patient.all if p.id == patient_id),)
def find_doctor_by_id(doctor_id):
    return next((d for d in Doctor.all if d.id == doctor_id), None)