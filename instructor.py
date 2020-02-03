from person import Person
from exercise import Exercise

class Instructor(Person):
    
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        # self.first_name = ""
        # self.last_name = ""
        # self.slack_handle = ""
        # cohort = []
        self.specialty = ""
        
    def assign_exercise(self, student, exercise):
        student.current_exercises.append(exercise)
        