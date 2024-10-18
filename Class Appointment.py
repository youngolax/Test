from abc import ABC, abstractmethod

class Appointment(ABC):
    def __init__(self, appointment_id, patient, doctor):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor

    @abstractmethod
    def book_appointment(self):
        pass
