#


def printwordlist():

    word = ["Apples","Bananas","Pears","Carrots"]
    
    #loops through and prints every value in list
    for item in word: 
       #added \n for demonstration clarity
       print("----------")
       print(item)
       print("\n")

       #prints every chara in worrd selected by outerloop iteration
       for c in item:
           #print(word.index(item))thought value == index
           print(c)

printwordlist()