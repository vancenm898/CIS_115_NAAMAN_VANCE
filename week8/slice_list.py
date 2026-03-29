# Program should return the postition 0 and 3.(The first and second letter of word.)

# set varaibles, for the months of the year.
months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

# This function will return months 4-6 from the list.
def slice_list():
    x = months[3:6:]
    #print(x)
    return x

# This will call the function set the funtions result to a varaible. 
result = slice_list()
# Print Varaible
print(result)