class Doctor:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show_info(self):
        return f"Name: {self.name}"




new_doctor = Doctor("Kenyi", 28)

print(new_doctor.show_info())