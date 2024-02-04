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
    while 0 < totalPoints < 1000:
        totalPoints = int(input("Enter the total score (0-1000): "))
        if totalPoints < 0 or totalPoints > 1000:
            print("You must enter integer values >=0 and <= 1000. Please try again.")
        else:
            return totalPoints


# Convert points into a letter grade
def get_letterGrade(averageEarned):
    averageEarned = (averageEarned / 10.0)
    if 92.0 <= averageEarned <= 1000:
        letterGrade = "A"
    elif 88 <= averageEarned <= 91.99:
        letterGrade = "B+"
    elif 82 <= averageEarned <= 87.99:
        letterGrade = "B"
    elif 78 <= averageEarned <= 81.99:
        letterGrade = "C+"
    elif 70 <= averageEarned <= 77.99:
        letterGrade = "C"
    elif 60 <= averageEarned <= 69.99:
        letterGrade = "D"
    else:
        letterGrade = "F"
    print("You earned an average of " + str(averageEarned) + "%. Letter grade earned: " + str(letterGrade))
    return letterGrade


# Calls for program to run and repeat when prompted.
def main():
    display_title()
    averageEarned = get_totalPoints()
    get_letterGrade(averageEarned)


main()
