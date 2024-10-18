class Doctor(Staff):

    def __init__(self, staff_id, name, specialty):
        super().__init__(staff_id, name, "Doctor")
        self.specialty = specialty

    def diagnose(self, patient, diagnosis):
        """
        Diagnoses a patient and adds the diagnosis to their medical history.
        """
        patient.add_medical_record({
            "Doctor": self.name,
            "Specialty": self.specialty,
            "Diagnosis": diagnosis
        })
        print(f"Dr. {self.name} has diagnosed {patient.name} with {diagnosis}.")

