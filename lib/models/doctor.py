class Doctor:
    all = []

    def __init__(self, name, specialization):
        self.id = len(Doctor.all) + 1
        self.name = name
        self.specializtion = specialization
        Doctor.all.append(self)