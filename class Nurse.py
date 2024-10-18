class Nurse(Staff):
    """
    Represents a nurse, inheriting from the Staff class.
"""
    def __init__(self, staff_id, name):
        super().__init__(staff_id, name, "Nurse")

    def assist_doctor(self, doctor, patient):
        """
        Assists the doctor in treating the patient.
        """
        print(f"Nurse {self.name} is assisting {doctor.name} with patient {patient.name}.")
