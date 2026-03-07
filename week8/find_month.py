# program allows you to search up a mounth

# sets varaibles, the (.lower()) lower cases the input of user to provent error.
month = input("Give your month: ").lower()
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "novenber", "december"]

# this function uses if/else the and "in", determines if (input) is "in" [list]
def search(month):
    if (month in months):
        print(f"We found {month} in the months list. Search successful!")
    else:
        print(f"We could not find {month} in the months list.")
#calls functions
search(month)