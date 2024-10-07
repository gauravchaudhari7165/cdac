# Assignment 1: 
# Try following string operations:
# Removing Leading Characters - lstrip(chars)
# Removing Trailing Characters - rstrip(chars)
# Joining a List into a String with a Space – “ ”.join(listname)
# Joining a List into a String with a Custom Separator – “#”

list1 = ['Hello', 'World']
list2 = ['Python', 'Programming']
s = string.lstrip().rstrip()
words = list1 + list2
joined_space = " ".join(map(str, words))
joined_custom = "#".join(map(str, words))

print("After removing characters:", s)
print("Joined with space:", joined_space)
print("Joined with custom separator:", joined_custom)



# Assignment 2 : 
# Write a program that asks the user how many days are in a particular month, and what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that month. For example, here is the output for a 30-day month that begins on day 4 (Thursday):ffff

days_in_month = int(input("Days in month: "))
start_day = int(input("Start day (0=Mon, 1=Tue, ...): "))

print("Mon Tue Wed Thu Fri Sat Sun")
print("    " * start_day, end="")

for day in range(1, days_in_month + 1):
    print(f"{day:2}", end=" ")
    if (day + start_day) % 7 == 0:
        print()


# Assignment 3: Reverse a list in Python

list1 = [1,2,3,4,5,6,7,8,9,10]
list1.reverse()
print(f"reversed list: {list1}")

# Assignment 4: Concatenate two lists index-wise.
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = []
for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
print(f"concatinated two lists index wise: {list3}")


# Assignment 5: Write a Python program to multiply all the items in a list.
list1 = [1,2,3,4,5]
result = 1
for i in list1:
    result *= i
print(result)


# Assignment 6: Write a Python program to get the smallest number from a list.
list1 = [1,2,3,4,5,6,7,8,9,10]
print(f"Smallest number in the list: {min(list1)}")


# Assignment 7: Write a python program to extract 3rd to 9th characters from a long string. 
string = "Hello, welcome to the world of Python programming."
print(f" 3rd to 9th characters: {string[2:9]}")


# Assignment 8: Replace Every Alternate Word in a Paragraph
# Input: 
# A single string paragraph that represents a paragraph of text.
# Output: 
# A new string where every alternate word in the input paragraph is replaced with the word 'replaced'.
# Logic : 
# Use the split() method to divide the paragraph into a list of words. 
# Replacing Alternate Words:
# Iterate through the list of words. Use the index of each word to determine if it is an alternate word. Replace every second word (i.e., words at odd indices) with the word 'replaced'.
# Joining Words:
# Combine the list of modified words back into a single string using the join() method, ensuring that words are separated by spaces. Print the new paragraph.

string = "Hello, I am a Python Developer"
words = string.split()
new_words = []
for i in range(len(words)):
    if i % 2 == 0:
        new_words.append(words[i])
    else:
        new_words.append("replaced")
new_string = " ".join(new_words)
print(new_string)


