class Staff:
    def __init__(self, staff_id, name, role):
        self.staff_id = staff_id
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.role}: {self.name} (ID: {self.staff_id})"
