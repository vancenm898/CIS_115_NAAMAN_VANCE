# determine if a word is a palindrome 
word = input("Give a word: ") #Takes user input assigns to variable
reverse_word = word [::-1] # reverses the input and assigms to new variable
print(reverse_word) # Print new word

if(word == reverse_word): # checks if word reversed is the same if so it prints.
    print(f"The word {word} is a palidrome")
elif(word != reverse_word):# checks if word reversed is the same if not it prints.
    print(f"The word {word} is not a palidrome")