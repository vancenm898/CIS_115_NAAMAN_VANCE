# a program that counts the frequency of each word in a given sentence. 
# Your program should accept a sentence from a user using the input() function and
#  you should implement a user-defined function named word_frequency() that accepts one argument. 
# Your word_frequency() function should use a dictionary to help you determine how many times 
# a given word occurs in the sentence and you should use the split() function to split the sentence into an array/list 



def word_frequency(mysentence):

    words = mysentence.split() #this will slip the sentence provide by user turnin it into a dictionary 
    #print(words)

    wordfrequency = {} # Here is varaible a place holder that will receive a count as word repeats

    for word in words:
        word = word.lower() # 
        if word in wordfrequency:
            wordfrequency[word] += 1
        else:
            wordfrequency[word] = 1
    return wordfrequency


# Here program should accept a sentence provided by the user(input) before calling function
mysentence = input("Type your sentence: ")
result = word_frequency(mysentence)
print(result)