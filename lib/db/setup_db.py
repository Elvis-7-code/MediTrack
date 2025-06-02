# lib/db/setup_db.py

import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from lib.db.base import Base

# Ensure the root directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Set up database engine and session
engine = create_engine("sqlite:///lib/db/meditrack_db.sqlite", echo=True)
Session = sessionmaker(bind=engine)
# Base = declarative_base()

def create_tables():
    # Import models after adjusting sys.path
    from lib.models.patient import Patient
    from lib.models.doctor import Doctor
    from lib.models.appointment import Appointment
    from lib.models.prescription import Prescription

    print("📦 Creating tables in the database...")
    Base.metadata.create_all(engine)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    create_tables()