# Product catalog set as variable
catalog = {
    "usb_k981": {"price": 12.00, "description": "USB 128 GB drive"},
    "mbpro_490": {"price": 2900.00, "description": "Mac Book Pro 15 inch"},
    "mouse_001": {"price": 25.00, "description": "Wireless Mouse"}
}  

cart = {} # set varaibles empty, Will be passed into later.

# Modcheck for cridit card
ccNum = input("Give credit card number: ") # Ask the user to enter a credit card number (stored as a string)
def validateCreditCard(ccNum):
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
validateCreditCard(ccNum) # call function

