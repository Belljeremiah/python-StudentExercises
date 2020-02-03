# Class Cohort
# Defines a type and represents a cohort

# Requirements:
# Name of Cohort
# Array/List/Collection of Students
# Array/list/Collection of Instructors

class Cohort():
    def __init__(self, name):
        self.name = name
        self.students = []
        self.slack_handle = ''
        self.current_exercises = []
        self.instructors = []