# program that finds the greater number

x = int(input("Give integer values: "))
y = int(input("Give integer values: "))
# this determined whitch number is greater
def max(x,y):
    if (x < y):
        print(f"The greater number is: {y}")
    # uses elif for a second if statment
    elif x > y:
        print(f"The greater number is: {x}")
    # incase user give the same number or number that are equal in value.
    else: 
        print("inputs are equal")

max(x,y)
