# Assignment 1: Voting System for Favorite Movies
# Implement a function manage_votes() that manages votes for a list of movies.
# Dictionary: 
# Key : movie name (string) 
# Value : Number of votes (integer)
# Implement the following operations:
# Add a new movie: Add a new movie to the voting list with 0 initial votes.
# Vote for a movie: Increment the vote count for a specific movie.
# Remove a movie: Remove a movie from the voting list.
# Display voting results: Display the current vote count for each movie.
# Find the top movie: Find and return the movie with the highest number of votes.

def manage_votes():
    votes = {}
    while True:
        print("1. Add a new movie")
        print("2. Vote for a movie")
        print("3. Remove a movie")
        print("4. Display voting results")
        print("5. Find the top movie")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            movie = input("Enter the movie name: ")
            votes[movie] = 0
        elif choice == 2:
            movie = input("Enter the movie name: ")
            if movie in votes:
                votes[movie] += 1
            else:
                print("Movie not found")
        elif choice == 3:
            movie = input("Enter the movie name: ")
            if movie in votes:
                del votes[movie]
            else:
                print("Movie not found")
        elif choice == 4:
            for movie, vote in votes.items():
                print(f"{movie}: {vote}")
        elif choice == 5:
            top_movie = max(votes, key=votes.get)
            print(f"Top movie: {top_movie}")
        elif choice == 6:
            break

manage_votes()

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

