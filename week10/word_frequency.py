# counts the words in dictionary
def word_frequency(mysentence):

    words = mysentence.split() #this will slip the sentence provide by user turnin it into a dictionary 
    #print(words)

    wordfrequency = {} # Here is varaible a place holder that will receive a count as word repeats

    #Loops over over the dictionary
    for word in words:
        word = word.lower() # Takes list add lowercase the words
        # As dictionary is looped over adds a 1 for every word
        if word in wordfrequency:
            wordfrequency[word] += 1 # example if "x" is 0 that means x+= 5 is (x= 0+5 ) meain 5 is assined to x now
        else:
            wordfrequency[word] = 1 # for words that only appear once.
    return wordfrequency


# Here program should accept a sentence provided by the user(input) before calling function
mysentence = input("Type your sentence: ")
result = word_frequency(mysentence)
print(result)