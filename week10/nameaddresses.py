
# List of dictionaries assigned to varaible
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

# function will print the values in the dictionary
def print_dictionary(names_and_addresses):
    x = names_and_addresses
    #loops over dictionary and seperate the info of the three indivauls
    for person in x:
        print("---------")
        print(person)
        print("\n")

# this will call the function
print_dictionary(names_and_addresses)
