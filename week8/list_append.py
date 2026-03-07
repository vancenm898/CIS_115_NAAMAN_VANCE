#THis program allow user it to create a list of values.

# set a varaible for empty list
userInputs = []

#function take the varable as an argument, and add to a list
def  append_to_list(a):
    
    #adds to list
    userInputs.append(a)

    #prompt users y or n and assins to d (first itiration ends here)
    d = input("Would you like to enter another value to append to the list?(y or n): ")

#while y == d the loop will continue
    while (d == "y" or d =="yes"):
        #Set input varable 
        a = (input("Entervalue: "))

        userInputs.append(a)

        d = input("Would you like to enter another value to append to the list?(y or n): ")

#progam beings here asking for input
a = (input("Entervalue: "))

# call function
append_to_list(a)


print(userInputs)
