# This program will alow user to enter up to 10m grades

x = 0
Count = 0

while (x == 0):
    numofgrades = int(input("How grades would you like to enter?: "))
    if(0 < numofgrades <= 10):
        x = 1
    else:
        print("Please enter a valid number greater than 0 and less then or equal to 10.")

while (Count < numofgrades):
    grades = input("Enter your Grade: ")
    
    Count = Count + 1

print("The user entered", numofgrades, "grades and is now done")

    
