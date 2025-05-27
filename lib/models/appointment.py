class Appointment:
    all = []

    def __init__(self, patient, doctor, appointment_date, notes=""):
        self.id = len(Appointment.all)+1
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.notes = notes
        Appointment.all.append(self)

    def _repr_(self):
        return f"<Appointment #{self.id} on {self.appointment_date} for patient {self.patient.name}>"    