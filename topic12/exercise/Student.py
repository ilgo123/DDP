from Person import *

class Student(Person):
    pass

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.gradyear}")

y = Student("Hafidh", "Alim", 2023)
y.welcome()
