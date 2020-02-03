class Person():
    def __init__(self, first_name, last_name):
        # writing this as a super class to cover both students and instructors
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = ""
        self.cohortId = ''