#


def printwordlist():

    word = ["Apples","Bananas","Pears","Carrots"]
    
    #loops through and prints every value in list
    for item in word: 
       #added \n for demonstration clarity
       print("\n")
       print(item)
       print("----------")

       #prints every chara in worrd selected by outerloop iteration
       for c in item:
    
        print(c)
        

printwordlist()