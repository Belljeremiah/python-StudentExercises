from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

# Create 4 or more instances of Exercise
fizz_buzz = Exercise("fizzBuzz", "Javascript")
city_spinner = Exercise("citySpinner", "Python")
joints_pizza = Exercise("jointsPizza", "Javython")
cap_stone = Exercise("stoneCapped", "Pyvascript")
bender_protocol = Exercise("Hey Wanna Kill all Humans?", "Python")
slurm_discovery = Exercise("slurmDiscovery", "Javascript")

# Create 3 different instances of cohort
dc36Supremacy = Cohort("Supreme Cohort 36")
dc34 = Cohort("Gone But Not Forgotten Cohort 34")
nc9 = Cohort("My Little Brothers Badass Night Cohort 9 of DARKNESS!!!")
ds5 = Cohort("Spock Like Focused data sciencio Cohort 5")

# Create 4 or more students, and assign to cohorts

jeremiah = Student("Pariah", "Wiggin")
guy = Student("Guy", "Cherkesky")
melody = Student("Melody", "The Bold and Boisterous")
boydhivemind = Student("We are the Boyd", "Resistance is Futile")
crowley = Student("Ryan", "Crowley")
pipochristo = Student("Christian", "Pimpin")
manilawatt = Student("Manila", "Bui")

dc36Supremacy.students.extend([jeremiah, guy, melody, boydhivemind, crowley, pipochristo, manilawatt])


# Create 3, or more, instructors and assign them to one of the cohorts.

joNoSchmo = Instructor("Jo", "Shepherd")
jiskieBuisness = Instructor("Jisie", "David")
jennaKalWitcher = Instructor("Jenna", "Solis")
j3 = Instructor("Their powers combined", "You gonna learn today (bout some code)!")

dc36Supremacy.instructors.extend([joNoSchmo, jiskieBuisness, jennaKalWitcher, j3])

# Have each instructor Assign 2 exercises

for student in dc36Supremacy.students:
    jiskieBuisness.assign_exercise(student, fizz_buzz)
    jiskieBuisness.assign_exercise(student, city_spinner)
    
    joNoSchmo.assign_exercise(student, bender_protocol)
    joNoSchmo.assign_exercise(student, slurm_discovery)
    
    jennaKalWitcher.assign_exercise(student, joints_pizza)
    jennaKalWitcher.assign_exercise(student, cap_stone)
    
    for student in dc36Supremacy.students:
        for exercise in student.current_exercises:
            print(f"{student.first_name} has been assigned {exercise.name} in {exercise.language_type}")
            print()
    
    
    