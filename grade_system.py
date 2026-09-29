# Accept student mark, validates the inputs and assigns the Grade
# Displays the result and allows the user to enter another mark
answer = "yes"
while answer == "yes":
    #Accept student mark
    try:
        mark = int(input("Enter your mark: "))
        if mark < 0 or mark > 100:
            print("Invalid mark, please enter a valid mark between 0 and 100")
        else:
            if mark >= 90:
                grade = "A"
            elif mark >= 80:
                grade = "B"
            elif mark >= 70:
                grade = "C"
            elif mark >= 60:
                grade = "D"
            else:
                grade = "E"
            print(f"Your mark is {mark} and your grade is {grade}")

    except ValueError:
        print("Incorrect data. Please enter a valid mark between 0 and 100")
    #
    # Ask whether the user wants to continue
    answer = input("Do you want to enter another mark? (yes/no): ").lower()
    #
    # Keep asking until the user provides yes or no
    while answer not in ["yes","no"]:
        print("Please respond with Yes or No")
        answer = input("Do you want to enter another mark? (yes/no):").lower()
    #
    # Exit message
    if answer == "no":
        print("You have chosen not to continue. Exiting the program")
    