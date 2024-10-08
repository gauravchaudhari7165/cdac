
# Assignment 1: Objective: Create a program that converts inches to feet, meters and centimeters and continue until the user wishes to

# while True:
#     value = float(input("Enter the value in inches: "))

#     print("Select the target unit for conversion:")
#     print("1. Feet")
#     print("2. Meters")
#     print("3. Centimeters")
#     choice = int(input("Enter the number corresponding to your choice: "))
    
#     if choice == 1:
#         converted_value = value / 12
#         unit = "feet"
#     elif choice == 2:
#         converted_value = value * 0.0254
#         unit = "meters"
#     elif choice == 3:
#         converted_value = value * 2.54
#         unit = "centimeters"
#     else:
#         print("Invalid choice. Please try again.")
#         continue
    
#     print(f"{value} inches is equal to {converted_value} {unit}.")
    
  
#     repeat = input("Do you want to perform another conversion? (Yes/No): ").strip().lower()
#     if repeat != 'yes':
#         break
    
    
    
    
    
#    Assignment 2: Build a calculator for +, -, * and / operations using if and else condition statements
   
# while True:
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
    
#     choice = input("Enter choice (1/2/3/4): ")

#     if choice == '1':
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         result = num1 + num2
#         operation = "addition"
#     elif choice == '2':
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         result = num1 - num2
#         operation = "subtraction"
#     elif choice == '3':
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         result = num1 * num2
#         operation = "multiplication"
#     elif choice == '4':
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         if num2 != 0:
#             result = num1 / num2
#             operation = "division"
#         else:
#             print("Error! Division by zero.")
#             continue
#     else:
#         print("Invalid input. Please enter a number between 1 and 4.")
#         continue

#     print(f"The result of the {operation} is: {result}")

#     repeat = input("Do you want to perform another calculation? (Yes/No): ").strip().lower()
#     if repeat != 'yes':
#         break



# Assignment 3: Print a Fibonacci series of numbers starting from 2 go until 100

# a, b = 2, 3
# print("Fibonacci series starting from 2 up to 100:")
# while a <= 100:
#     print(a, end=" ")
#     a, b = b, a + b
# print()