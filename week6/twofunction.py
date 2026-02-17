def print_message1():
    print("I was called first.")
    print_message2()
def print_message2():
    print("I was from print_message1")

print_message1()