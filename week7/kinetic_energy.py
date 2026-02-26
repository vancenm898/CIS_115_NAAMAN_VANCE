# Find kinetic Energy

m = int(input("Whats the mass in kilograms?: "))
v = int(input("what the velocity in meters per sec? "))


def kinetic_energy(m,v):

    k = 1/2*(m*v**2)
    
    print(k)

kinetic_energy(m,v)