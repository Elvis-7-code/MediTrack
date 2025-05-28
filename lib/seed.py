from lib.models.patient import Patient
from lib.models.doctor import Doctor
from lib.models.appointment import Appointment
from lib.models.prescription import Prescription
def seed_data():
    p1 = Patient("Alice", 30, "Female")
    p2 = Patient("Bob", 45, "Male")

    d1 = Doctor("Dr. Smith", "Cardiology")
    d2 = Doctor("Dr. Abby", "Dermatology")

    a1 = Appointment(p1, d1, "2025-06-01", "Routine checkup")
    a2 = Appointment(p2, d2, "2025-06-02", "Skin rash evaluation")
    
    pr1 = Prescription(p1, d1, "Aspirin", "100mg", "Take after meals")
    pr2 = Prescription(p2, d2,"Hydrocorticone","Apply twice a day", "For external use only")

    print("Seed data loaded.")

    if _name_ == "_main_":
        seed_data()