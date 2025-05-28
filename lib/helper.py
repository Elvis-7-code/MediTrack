from lib.models.patient  import Patient
from lib.models.patient import Doctor

def find_patient_by_id(patient_id):
    return((p for p in Patient.all if p.id == patient_id),)