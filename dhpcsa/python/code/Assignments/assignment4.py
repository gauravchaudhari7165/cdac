# Assignment 11: Write a program that checks whether a given string is a palindrome (a string that reads the same backward as forward).
# Input:
# Prompt the user to enter a string.
# Logic:
# Remove any spaces and convert the string to lowercase.
# Check if the string reads the same forward and backward.
# Output:
# Display whether the string is a palindrome.

string = input("Enter a string: ")
string = string.replace(" ", "").lower()
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    


