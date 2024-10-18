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
