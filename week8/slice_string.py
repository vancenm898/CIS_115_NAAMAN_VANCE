# Program should return the postition 0 and 3.(The first and second letter of word.)

# set varaibles
word = input("Enter a 4 letters word or more: ")

# This function will print the 1st and second letter of that word.
def slice_my_string():
    print(word[0:3])
# This will call the function
slice_my_string()