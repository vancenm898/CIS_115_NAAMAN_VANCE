# determine if a word is a palindrome 
word = input("Give a word: ")
reverse_word = word [::-1]
print(reverse_word)

if(word == reverse_word):
    print(f"The word {word} is a palidrome")
elif(word != reverse_word):
    print(f"The word {word} is not a palidrome")