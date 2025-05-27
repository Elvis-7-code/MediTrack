class Patient:
    all = []

    def __init__(self, name, age, gender):
        self.id = len(Patient.all)+1
        self.name = name
        self.age = age
        self.gender = gender
        Patient.all.append(self)

    def __repr__(self):
        return f"<Patient {self.name}(ID: {self.id})>"    