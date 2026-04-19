# Product catalog (dictionary) set as variable
catalog = {
    "1": {"description": "USB 128 GB drive", "price": 12.00 },
    "2": {"description": "Mac Book Pro 15 inch", "price": 2900.00 },
    "3": {"description": "Arduino 1010(with blue tooth)", "price": 48.00 },
    "4": {"description": "Ring Camera(wireless)", "price": 156.00  },
    "5": {"description": "Smart TV(TCL 70 inch)", "price": 359.00, }
}  


# product catalog
def productcatalog():
   print("---------------------------------------------------------------")
   print("                     PRODUCT CATALOG                           ")
   print("\n")
   print("---------------------------------------------------------------")
   print(" 1  |               USB Drive(128 GB)               | $12.00   ")
   print("\n")
   print(" 2  |             Mac Book Pro(15 inch)             | $2900.00 ")
   print("\n")
   print(" 3  |         Arduino 1010(with blue tooth)         | $48.00   ")
   print("\n")
   print(" 4  |             Ring Camera(wireless)             | $156.00  ")
   print("\n")
   print(" 5  |             Smart TV(TCL 70 inch)             | $359.00  ")
   print("---------------------------------------------------------------")
   print("\n")
productcatalog()



def addtocart():
   productID = catalog[input("Choose a product ID from the product catalog to continue: ")]
   amount = int(input(f"Enter quantity for product {productID}: "))
   cart = {} # set varaibles empty, Will be passed into later.
   numofproducts = []
    
    
   #adds to cart
   cart.update({"Product":productID,"numofproducts":amount})
    

    #prompt users y or n and assins to d (first itiration ends here)
   d = input("Would you like to add another product (y or n)?: ").lower()

   #while y == d the loop will continue
   while (d == "y" or d =="yes"):
        #Set input varable 
        productID = catalog[input("Choose a product ID from the product catalog to continue: ")]

        cart.update({"Product":productID,"numofproducts":amount})

        d = input("Would you like to enter another value to append to the list?(y or n): ").lower()
   print(cart)

addtocart()
