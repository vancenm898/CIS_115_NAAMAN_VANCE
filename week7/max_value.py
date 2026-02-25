
x = int(input("Give integer values: "))
y = int(input("Give integer values: "))

def max(x,y):
    if (x < y):
        print(f"The greater number is: {y}")
    elif x > y:
        print(f"The greater number is: {x}")
    else: 
        print("inputs are equal")

max(x,y)
