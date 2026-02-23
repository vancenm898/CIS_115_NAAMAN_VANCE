# A program that finds degree.

import math



def degree():
    y = float(input("Enter y: "))
    x = float(input("Enter x: "))
    a = float(math.atan2(y,x))
    b = float(a * (180 / 3.14))
    print((f"degree: {b}"))

degree()