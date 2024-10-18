class InPersonAppointment(Appointment):
    """
    Represents an in-person appointment.
"""
    def __init__(self, appointment_id, patient, doctor, room_number):
        super().__init__(appointment_id, patient, doctor)
        self.room_number = room_number

    def book_appointment(self):
        print(f"In-person appointment booked for {self.patient.name} with {self.doctor.name} in room {self.room_number}.")


class VirtualAppointment(Appointment):
    """
    Represents a virtual appointment.
    """
    def __init__(self, appointment_id, patient, doctor, meeting_link):
        super().__init__(appointment_id, patient, doctor)
        self.meeting_link = meeting_link

    def book_appointment(self):
        print(f"Virtual appointment booked for {self.patient.name} with {self.doctor.name}. Meeting link: {self.meeting_link}")
