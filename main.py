print("Name: Patrice Virata")
print("ISQA3900-001 January 30th, 2024")
print("This program evaluates the letter grade for a class in a scale of 1000 points.")


# Displays the title of the program
def display_title():
    print("Welcome to the Grade Calculator")
    print("")


# Get total points from input and repeat if input does not meet expected values.
def get_totalPoints():
    totalPoints = 0.0
    while (totalPoints == 0):
        try:
            totalPoints = float(input("Enter the total score (0-1000): "))
            if totalPoints < 0 or totalPoints > 1000:
                print("You must enter integer values >=0 and <= 1000. Please try again.")
            else:
                return totalPoints
        except ValueError:
            print("You must enter integer values >=0 and <= 1000. Please try again.")
