#write progam that use a for-loop and loop over the list printing each value in the list

def printwordlist():

    word = ["Apples","Bananas","Pears","Carrots"]
    
    for item in word:
        print(item)
        print(word.index(item))

printwordlist()
