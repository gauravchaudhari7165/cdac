#Assignment 1: Count occurrence of letter ‘a’ in a String.

def count_a(string):
    count = 0
    for i in string:
        if i == 'a':
            count += 1
    return count

string = input("Enter a string: ")
print("Number of 'a' in the string: ", count_a(string))



#Assignment 2: Ask for a number from a user and count occurrence of digit 0 in it. Print the number and the number of zeros in the number. Ask the user if she wants to add a new number. If yes, check for zeros again. Continue until the user says ‘N’. 
num = input("Enter a number: ")
count = 0
for i in num:
    if i == '0':
        count += 1
print("Number of '0' in the number: ", count)
while True:
    choice = input("Do you want to add a new number? (Y/N): ")
    if choice == 'Y':
        num = input("Enter a number: ")
        count = 0
        for i in num:
            if i == '0':
                count += 1
        print("Number of '0' in the number: ", count)
    else:
        break


#Assignment 3: Create a Pyramid pattern of stars.

for row in range(5):
    empty_spaces = ' ' * (4 - row)
    star_pattern = '*' * (2 * row + 1)
    print(empty_spaces + star_pattern)




    