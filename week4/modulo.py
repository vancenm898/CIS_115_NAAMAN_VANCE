#This is my Ten Python program

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = float(num1) % float(num2)

print(result)

if(result % 2 == 0):
  print("even")

else: 
  print("odd")