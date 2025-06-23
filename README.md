# MediTrack

#Introduction To MediTrack-CLI Application
> MediTrack is command line system that entails doctors, patients details with reference to their appointments and prescriptions as well

# Models used are:
 - Python
 - SQLAlchemy
# Project-Structure

```
├── lib
│   ├── cli.py
│   ├── db
│   │   ├── base.py
│   │   ├── create_tables.py
│   │   ├── meditrack_db.sqlite
│   │   ├── __pycache__
│   │   │   ├── base.cpython-38.pyc
│   │   │   ├── seed.cpython-38.pyc
│   │   │   └── setup_db.cpython-38.pyc
│   │   ├── seed.py
│   │   └── setup_db.py
│   ├── debug.py
│   ├── helper.py
│   ├── __init__.py
│   ├── models
│   │   ├── appointment.py
│   │   ├── doctor.py
│   │   ├── __init__.py
│   │   ├── patient.py
│   │   ├── prescription.py
│   │   └── __pycache__
│   │       ├── appointment.cpython-38.pyc
│   │       ├── doctor.cpython-38.pyc
│   │       ├── __init__.cpython-38.pyc
│   │       ├── patient.cpython-38.pyc
│   │       └── prescription.cpython-38.pyc
│   └── __pycache__
│       ├── cli.cpython-38.pyc
│       ├── helper.cpython-38.pyc
│       └── __init__.cpython-38.pyc
├── Pipfile
├── Pipfile.lock
└── README.md
```
