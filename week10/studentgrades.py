
students = {"James": 40,
           "Mike": 70,
           "May": 100}

def calculate_average_grade(students):
 
 total = 0
 numofgrades = 0

 for grades in students.values():
    total += grades
    numofgrades += 1
    if numofgrades == 3:
       return total/numofgrades


print(f"The Average grade is: {calculate_average_grade(students)}")
