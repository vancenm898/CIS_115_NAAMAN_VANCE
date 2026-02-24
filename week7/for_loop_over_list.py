#use list and for-loops to loop over the list and print it out.

def getmylist():
    list = [10,20,30,40,50,60]
    count = 0

    for item in list:
        count = count + 1
        print(item)
    
    return count
total = getmylist()
print(f"The total count is: {total}")
