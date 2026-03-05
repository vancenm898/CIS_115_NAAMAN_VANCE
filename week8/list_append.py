#THis program allow user it to create a list of values.

userInputs = []

#function take the varable as an argument, and add to a list
def  append_to_list(a):
    
    userInputs.append(a)
    d = input("Would you like to enter another value to append to the list?(y or n): ")

    while (d == "y" or d =="yes"):
        #Set input varable 
        a = (input("Entervalue: "))
        userInputs.append(a)
        d = input("Would you like to enter another value to append to the list?(y or n): ")


a = (input("Entervalue: "))
append_to_list(a)


print(userInputs)
