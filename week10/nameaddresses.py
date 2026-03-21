
# List of dictionaries

names_and_addresses =[
        {"FirstName": "John", 
        "LastName":"Henery", 
        "city": "Raeford",
        "state": "NC",
        "zipCode": "28367",
        "phoneNumber": "910-123-4567"},

        {"FirstName": "Mike", 
        "LastName":"Tight", 
        "city": "Raeford",
        "state": "NC",
        "zipCode": "28369",
        "phoneNumber": "910-987-6543"},

        {"FirstName": "May", 
        "LastName":"Day", 
        "city": "Raeford",
        "state": "NC",
        "zipCode": "28374",
        "phoneNumber": "910-246-8102"}]

# function will print 
def print_dictionary(names_and_addresses):
    x = names_and_addresses
    for person in x:
        print("---------")
        print(person)
        print("\n")


print_dictionary(names_and_addresses)
