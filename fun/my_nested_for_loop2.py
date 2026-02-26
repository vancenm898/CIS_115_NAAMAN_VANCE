#This the play around file


def printwordlist():

    word = ["Apples","Bananas","Pears","Carrots"]
    
      #loops through and prints every value in list
    for item in word: 
        count = word.index(item)
        range()
        
        
        print("\n")
        print("*****begin outer loop iteration****")
        #added \n for demonstration clarity
        print(f"counter for outer loop: {count + 1}")
        print(item + " :outer loop")
        
        #prints every value in list per outer loop iteration
        for item in word:
            #if (word.index(item) == count):
            innercount = word.index(item)
            print(f"----begin inner loop iteration: {innercount + 1}----")
            print(item)
            print(f"----end inner loop iteration: {innercount + 1}----")
            #print("*********end of outer loops current iteration*******")
            #print("\n")
                
                
            #print(word.index(item))thought value == index
            #print(item) #assuming value means items
printwordlist()

