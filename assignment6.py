# Assignment 1: Create a calculator for performing addition, subtraction, division, multiplication operations. Create a separate function for each operation. Call these functions appropriately based on options from user. 
# Input : 
# Ask user what operation needs to be performed.
# Ask user if next operation needs to be performed. Based on the answer repeat same steps or exit. 

print("Welcome to the calculator")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
choice = 'y'
while choice == 'y':
    print("Enter the operation you want to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input())
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    if operation == 1:
        print(add(a,b))
    elif operation == 2:
        print(sub(a,b))
    elif operation == 3:
        print(mul(a,b))
    elif operation == 4:
        print(div(a,b))
    choice = input("Do you want to perform another operation? y/n")
print("Thank you for using the calculator")




# Assignment 2: 
# Repeat specific elements within a tuple. Use functions appropriately.
# Instructions:
# Write a Python program that performs the following tasks:
# Prompt the user to enter a tuple of elements (mixed types allowed) separated by commas.
# Convert the input string to a tuple of elements.
# Prompt the user for an element to repeat and the number of times to repeat it.
# Create a new tuple where the specified element is repeated the given number of times, with the rest of the elements unchanged.
# Display the original tuple and the new tuple.

tuple1 = input("Enter a tuple of elements separated by commas: ")
tuple1 = tuple(tuple1.split(","))
print(f"Original tuple: {tuple1}")
element = input("Enter an element to repeat: ")
repeat = int(input("Enter the number of times to repeat the element: "))
new_tuple = tuple1 + (element,) * repeat
print(f"New tuple: {new_tuple}")


