# 1

# Assignment 1:  Convert Celsius to Fahrenheit
# Use a lambda function with map() to convert a list of temperatures from Celsius to Fahrenheit.
# Given a list of temperatures in Celsius [0, 20, 37, 100], use map() and a lambda function to convert each value to Fahrenheit using the formula F = (C * 9/5) + 32.
# Expected Output: [32.0, 68.0, 98.6, 212.0]


celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)



#2
# Assignment 2: Add Two Lists Element-wise
# Use a lambda function with map() to add corresponding elements from two lists.
# Given two lists [1, 2, 3] and [4, 5, 6], use map() and a lambda function to return a new list where each element is the sum of the corresponding elements from the two lists.
# Expected Output: [5, 7, 9]


list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)


# Assignment 3: Capitalize Words in a List
# Use a lambda function with map() to capitalize the first letter of each word in a list.
# Given a list of lowercase words ['apple', 'banana', 'cherry'], use map() and a lambda function to capitalize each word.
# Expected Output: ['Apple', 'Banana', 'Cherry']


words = ['apple', 'banana', 'cherry']
capitalized_words = list(map(lambda word: word.capitalize(), words))
print(capitalized_words)


# Assignment 4: Find the Length of Strings
# Use a lambda function with map() to find the length of each string in a list.
# Given a list of strings ['hello', 'world', 'python'], use map() and a lambda function to return a new list containing the length of each string.
# Expected Output: [5, 5, 6]


strings = ['hello', 'world', 'python']
lengths = list(map(lambda string: len(string), strings))
print(lengths)




# Assignment 5: Daily Temperature Tracker
# Create a dictionary to store and manipulate daily temperature data for a week.
# Write a program that stores daily high temperatures for a week in a dictionary, where keys are days of the week and values are temperatures. The program should:
# Allow the user to update the temperature for any day.
# Calculate the average temperature for the week.
# Example Input: {'Monday': 30, 'Tuesday': 32, 'Wednesday': 29, 'Thursday': 31, 'Friday': 30, 'Saturday': 28, 'Sunday': 27}
# Expected Output: Average temperature: 29.57°C.


temperatures = {'Monday': 30, 'Tuesday': 32, 'Wednesday': 29, 'Thursday': 31, 'Friday': 30, 'Saturday': 28, 'Sunday': 27}
total = sum(temperatures.values())
average = total / len(temperatures)
print(f"Average temperature: {average}°C")

# Assignment 6: Bird Species Observation Tracker
# Create a dictionary to track the number of sightings of different bird species.
# Given a dictionary where keys are bird species (e.g., 'sparrow', 'eagle') and values are the number of sightings, write a program to:
# Add a new species with its count.
# Update the sighting count for an existing species.
# Display the bird with the highest number of sightings.
# Example Input: {'sparrow': 10, 'eagle': 5, 'hawk': 7}
# Expected Output: The bird with the highest sightings is 'sparrow'.


birds = {'sparrow': 10, 'eagle': 5, 'hawk': 7}
birds['crow'] = 15
birds['sparrow'] += 2
most_sighted = max(birds, key=birds.get)
print(f"The bird with the highest sightings is '{most_sighted}'.")
print(birds)

