# Assignment 1: Temperature convertor
# Input from user : 
# Temperature value and unit 
# Temperature unit to convert to
# Functions : 
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# celsius_to_kelvin(celsius)
# Employ exception handling for checking numeric values. 
# Finally and else block

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

try:
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the temperature unit (C/F/K): ")
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is equal to {fahrenheit}°F and {kelvin}K.")
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{temperature}°F is equal to {celsius}°C and {kelvin}K.")
    elif unit == 'K':
        celsius = temperature - 273.15
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{temperature}K is equal to {celsius}°C and {fahrenheit}°F.")
    else:
        print("Invalid unit")

except ValueError:
    print("Invalid temperature value")
except:
    print("An error occurred")
else:
    print("Conversion successful")
finally:
    print("Program execution complete")

    
# Assignment 2: Handle file not found exception

try:
    with open('file.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
except:
    print("An error occurred")
else:
    print("File read successfully")
finally:
    print("Program execution complete")

    