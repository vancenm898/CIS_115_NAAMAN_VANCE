# Program should return the postition 0 and 3.(The first and third letter of word.)

# set varaibles
word = input("Enter a 4 letters word or more: ")

# This function will print the 1st and 3rd letter of that word.
def slice_my_string():
    print(word[0:3:2])
# This will call the function
slice_my_string()