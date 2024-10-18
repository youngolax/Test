class Staff:

    def __init__(self, staff_id, name,age, gender, role):
        self.staff_id = staff_id
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role

    def __str__(self):
        return f"{self.role}: {self.name}: {self.age}: {self.gender}:(ID: {self.staff_id})"

#Defining doctor class which inherist from staff
class Doctor(Staff):

    def __init__(self, staff_id, name, age, gender, specialty):
        super().__init__(staff_id, name, age, gender,"Doctor")
        self.specialty = specialty

    def diagnose(self, patient, diagnosis):
        #Diagnoses a patient and adds the diagnosis to their medical history.

        patient.add_medical_record({
            "Doctor": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Specialty": self.specialty,
            "Diagnosis": diagnosis
        })
        print(f"Dr. {self.name} has diagnosed {patient.name} with {diagnosis}.")

    def __str__(self):
        return f"Dr. {self.name} (Specialty: {self.specialty})"

#Definition of Nurse class that extends staff class
class Nurse(Staff):
    def __init__(self, staff_id, name, age, gender):
        super().__init__(staff_id, name, age, gender,"Nurse")

    def assist_doctor(self, doctor, patient):
        """
        Assists the doctor in treating the patient.
        """
        print(f"Nurse {self.name} is assisting {doctor.name} with patient {patient.name}.")

#Defining class patient
class Patient:

    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = []

    def add_medical_record(self, record):
        self.medical_history.append(record)

    def get_medical_history(self):
        return self.medical_history

    def __str__(self):
        return f"Patient {self.name}, Age: {self.age}"

from abc import ABC, abstractmethod

class Appointment(ABC):
    def __init__(self, appointment_id, patient, doctor):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor

    @abstractmethod
    def book_appointment(self):
        pass

class InPersonAppointment(Appointment):
    def __init__(self, appointment_id, patient, doctor, room_number):
        super().__init__(appointment_id, patient, doctor)
        self.room_number = room_number

    def book_appointment(self):
        print(f"In-person appointment booked for {self.patient.name} with {self.doctor.name} in room {self.room_number}.")

class VirtualAppointment(Appointment):
    def __init__(self, appointment_id, patient, doctor, meeting_link):
        super().__init__(appointment_id, patient, doctor)
        self.meeting_link = meeting_link

    def book_appointment(self):
        print(f"Online appointment booked for {self.patient.name} with {self.doctor.name}. Meeting link: {self.meeting_link}")

class Billing:
    def __init__(self, patient):
        self.patient = patient
        self.charges = 0.0

    def add_charge(self, amount):
        if amount < 0:
            raise ValueError("Charge amount must be positive.")
        self.charges += amount
        print(f"Added Ugx{amount} to {self.patient.name}'s bill.")

    def get_total_bill(self):
        return self.charges

if __name__ == "__main__":
    # Create a doctor and a nurse
    doctor1 = Doctor(1000, "Dr. Tugame Ali", "Cardiology", "Female",45)
    nurse1 = Nurse(2001, "Nurse Scovia","Female",34)

    # Create a patient
    patient1 = Patient(3001, "Emmanuel Olato", 37)

    # Doctor diagnoses patient
    doctor1.diagnose(patient1, "Heart Disease")

    # Nurse assists the doctor with the patient
    nurse1.assist_doctor(doctor1, patient1)

    # Create appointments
    in_person_appointment = InPersonAppointment(1, patient1, doctor1, "Room 001")
    virtual_appointment = VirtualAppointment(2, patient1, doctor1, "https://us05web.zoom.us/j/82251353489?pwd=zykKaRhYiADnIMGRu5AJ4sumzOUqBR.1")

    # Book appointments (polymorphism)
    in_person_appointment.book_appointment()
    virtual_appointment.book_appointment()

    # Billing system
    billing1 = Billing(patient1)
    billing1.add_charge(25000.00)  # Charge for consultation
    billing1.add_charge(30000.00)  # Charge for medication
    print(f"Total bill for {patient1.name}: Ugx{billing1.get_total_bill()}")

    # Display patient's medical history
    print("\nMedical History:")
    for record in patient1.get_medical_history():
        print(record)
