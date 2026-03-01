# Porgam should tell you the Months between ranges.

# Set varibles
print("months designated 1-12")
startmonth = int(input("Give your start month as #: "))-1
endmonth = int(input("Give your start month as #: "))-1
months = ["Jan", "Feb", "March", "Apil", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

# def a function
def months_of_year(startmonth,endmonth):
    for i in range(startmonth,endmonth +1):
        print(months[i])
    


months_of_year(startmonth,endmonth)