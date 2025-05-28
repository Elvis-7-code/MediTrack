def seed_data():
    p1 = Patient("Alice", 30, "Female")
    p2 = Patient("Bob", 45, "Male")

    d1 = Doctor("Dr. Smith", "Cardiology")
    d2 = Doctor("Dr. Abby", "Dermatology")

    a1 = Appointment(p1, d1, "2025-06-01", "Routine checkup")
    a2 = Appointment(p2, d2, "2025-06-02", "Skin rash evaluation")
    