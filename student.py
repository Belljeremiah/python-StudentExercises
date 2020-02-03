# import super class or subtype to give common traits to student from person
from person import Person

class Student(Person):
    
    def__init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        # Establishing the properties of each student
        # self.first_name = ""
        # self.last_name = ""
        # self.slack_handle = ""
        # self.cohort = ""
        # the above is redundant because I am doing this with a person class now see imported person.py
        self.assigned_exercises = []