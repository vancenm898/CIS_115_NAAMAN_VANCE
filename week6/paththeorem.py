#Find the hypoteneuse

y = float(input("Enter y: "))
x = float(input("Enter x: "))


def hypoteneuse(y,x):
    
    c =(((y**2)+(x**2))**(1/2))

    print((f"hypotenuse: {c}"))

hypoteneuse(y,x)


