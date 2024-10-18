class Patient:
    """
    Represents a patient in the hospital management system.
    """
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = []

    def add_medical_record(self, record):

        # Adds a medical record to the patient's medical history.

        self.medical_history.append(record)

    def get_medical_history(self):
        """
        Returns the patient's medical history.
        """
        return self.medical_history

