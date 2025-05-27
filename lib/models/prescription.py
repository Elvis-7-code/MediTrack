class Prescription:
    all = []

    def _init_(self, patient, doctor, medication, dosage, instructions):
        self.id = len(Prescription.all) +1
        self.patient = patient
        self.doctor = doctor
        self.medication = medication
        self.dosage = dosage
        self.instruction = instructions 
        Prescription.all.append(self)

    def __repr__(self):
        return f"<Prescription {self.medication} for {self.patient.name}>"    