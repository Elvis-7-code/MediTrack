from setup_db import engine, Base

# Import all model classes so SQLAlchemy knows about them
from lib.models.patient import Patient
from lib.models.doctor import Doctor
from lib.models.appointment import Appointment
from lib.models.prescription import Prescription

def create_tables():
    print("📦 Creating tables in the database...")
    Base.metadata.create_all(engine)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    create_tables()
