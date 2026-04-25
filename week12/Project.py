# Product catalog (dictionary) set as variable
catalog = {
    "1": {"SKU": "usb_k981", "description": "USB 128 GB drive", "price": 12.00, "Qty on Hand": 1000 },
    "2": {"SKU": "mbpro_490", "description": "Mac Book Pro 15 inch", "price": 2900.00, "Qty on Hand": 45 },
    "3": {"SKU": "chip_1010", "description": "Arduino 1010(with blue tooth)", "price": 48.00, "Qty on Hand": 325 },
    "4": {"SKU": "cam_78", "description": "Ring Camera(wireless)", "price": 156.00, "Qty on Hand": 98 },
    "5": {"SKU": "smt_tv_100", "description": "Smart TV(TCL 70 inch)", "price": 359.00, "Qty on Hand": 225 }
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



def addtocart(catalog):
   
   cart = {} # set varaibles empty, Will be passed into later.
    
   #adds to cart
   
   d = "y"

   #while y == d the loop will continue
   while (d == "y" or d =="yes"):
      #Set input varable 
      print("\n")
      productID = input("Choose a product ID from the product catalog to continue: ")
      
      amount = int(input(f"Enter quantity for product {productID}: "))
      price = catalog[productID]["price"] * amount

      if productID in cart:
           cart[productID]["quantity"] += amount
           cart[productID]["Total Price"] += price
      else:
         cart[productID] = {
                "SKU": catalog[productID]["SKU"],
                "description": catalog[productID]["description"],
                "price": catalog[productID]["price"],
                "quantity": amount,
                "Total Price": price
            }
         #prompt users y or n and assins to d (first itiration ends here)

      x = input("Would you like to add another product (y or n)?: ").lower()
      if (x == "n") or (x == "no"):
         x = input("Are you ready to check out?(y or n):  ").lower()
         if (x == "y") or (x == "yes"):
            d = "n"
         else:
            d = "y"
   return cart

MyCart = addtocart(catalog)
MCT = 0
for item in MyCart.values():
   MCT += item["Total Price"]
#print(MyCart)
#print(MCT)
print("\n")
print("\n")


print("Enter your billing/shipping information:")
fn = input("First Name: ")
ln = input("Last Name: ")
a = input("Address: ")
c = input("City: ")
s = input("State: ")
zp = input("Zip Code/Post code: ")
e = input("Email: ")
n = input("Phone: ")
print("\n")
print("\n")

# Modcheck to run cridit card check
def validateCreditCard():
   ccNum = input("Give credit card number: ") # Ask the user to enter a credit card number (stored as a string)
   x = int(1)  # x is used as a loop control variable (1 = keep looping, 0 = stop)
   while x == 1:  # This loop keeps running until while x is 1
      cn2 = [] # set a varaible for empty list
      for character in ccNum:
         cn2.append(int(character))  # loop over string and Convert each character into an integer then adds to list
      even = cn2[0::2] # takes every other num in list(cn2) and make new list 
      odd = cn2[1::2] # Make list using the other set of num not in first list
      even2 = [] # set a varaible for empty list
      for value in even: # doubles the values by 2 then takes the num >9 and -9 from it
         value = value*2 
         if value > 9:
            value -= 9 
         even2.append(value) # add them to new list
      total = sum(even2) + sum(odd) # add the new lists (even2) and (odd)
      if total % 10 == 0: # Check if total can divid with 0 remainder, ends loop if it does
         x=0
         print(f"The credit card number; {ccNum} is valid!")
      else: # Keeps loop if num dosn't divid without remainder
         x=1
         ccNum = input("Invalid credit card entered. Please try again.: ")
   input("Enter the expiration date on your card: ")
   input("Please enter your CVV: ")
validateCreditCard() # call function
print("\n")

print("\n")
print("\n")
print("---------------------------------------------------------------")
print("\n")
print("                Billing/Shipping Information:                  ")
print("\n")
print("---------------------------------------------------------------")
print(f" Name:           {fn} {ln}           ")
print("\n")
print(f" Address:              {a}           ")
print(f" City:                 {c}           ")
print(f" State:                {s}           ")
print(f" Zip Code/Post code:   {zp}          ")
print(f" Email:                {e}           ")
print(f" Phone:                {n}           ")
print("---------------------------------------------------------------")
print("\n")
print("                Shopping Cart Information:                     ")
print("\n")
print("---------------------------------------------------------------")
print("ProductID |    SKU   | Qty | Price | Description       | Total ")
print("---------------------------------------------------------------")
print("\n")
for pid, info in MyCart.items():
   print(f"     {pid}    | {info["SKU"]} |  {info["quantity"]}  | ${info["price"]} | {info["description"]} | ${info["Total Price"]}")
print("---------------------------------------------------------------\n")
print("Cart Total:", MCT)
print("\n")