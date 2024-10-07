# Assignment 1: Repeat specific elements within a tuple. Use functions appropriately.
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







