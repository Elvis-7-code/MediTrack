

from helper import (
    exit_program,
    list_patients,
    list_doctors,
    list_appointments,
    list_prescriptions
)

def main():
    while True:
        menu()
        choice = input("> ").strip()
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_patients()
        elif choice == "2":
            list_doctors()
        elif choice == "3":
            list_appointments()
        elif choice == "4":
            list_prescriptions()
        else:
            print("Invalid choice. Please try again.\n")

def menu():
    print("\n=== MediTrack Hospital Management System ===")
    print("0. Exit")
    print("1. List Patients")
    print("2. List Doctors")
    print("3. List Appointments")
    print("4. List Prescriptions")

if __name__ == "__main__":
    main()