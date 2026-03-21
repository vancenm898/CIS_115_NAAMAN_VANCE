# list assigned to varaible
students = {"James": 40,
           "Mike": 70,
           "May": 100}
#Function will average the grades
def calculate_average_grade(students):
 # place holder values assigned to varabiles
 total = 0
 numofgrades = 0
# loop over list counting and adding up values then divid them
 for grades in students.values():
    total += grades 
    numofgrades += 1
    if numofgrades == 3: # only three grades ends for in loop
       return total/numofgrades

#Calls function
print(f"The Average grade is: {calculate_average_grade(students)}")
