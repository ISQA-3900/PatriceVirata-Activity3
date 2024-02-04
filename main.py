print("Name: Patrice Virata")
print("ISQA3900-001 January 30th, 2024")
print("This program evaluates the letter grade for a class in a scale of 1000 points.")


# Displays the title of the program
def display_title():
    print("Welcome to the Grade Calculator")
    print()


# Get total points from input and repeat if input does not meet expected values.
def get_totalPoints():
    totalPoints = 0.0
    averageEarned = totalPoints
    while totalPoints == 0.0:
        try:
            totalPoints = int(input("Enter the total score (0-1000): "))
            if totalPoints < 0 or totalPoints > 1000:
                print("You must enter integer values >= 0 and <= 1000. Please try again.")
                totalPoints = 0.0
                print()
            else:
                return totalPoints
        except ValueError:
            print("You must enter integer values >= 0 and <= 1000. Please try again.")
            print()


# Convert points into a letter grade
def get_letterGrade(averageEarned):
    averageEarned = averageEarned/10
    if 92.0 <= averageEarned <= 1000:
        letterGrade = "A"
    elif 88.0 <= averageEarned <= 91.99:
        letterGrade = "B+"
    elif 82.0 <= averageEarned <= 87.99:
        letterGrade = "B"
    elif 78.0 <= averageEarned <= 81.99:
        letterGrade = "C+"
    elif 70.0 <= averageEarned <= 77.99:
        letterGrade = "C"
    elif 60.0 <= averageEarned <= 69.99:
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
    print()
    repeatAgain = str(input("Would you like to enter another score (y/n)? ").lower())
    print()
    while repeatAgain == "y":
        averageEarned = get_totalPoints()
        get_letterGrade(averageEarned)
        print()
        repeatAgain = str(input("Would you like to enter another score (y/n)? ").lower())
        print()
    print("Thank you")


main()
