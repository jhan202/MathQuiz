#  functions go here
def yes_no(question):
    """Checks users enter yes / no"""

    while True:
        response = input(question).lower()

        """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Print instructions"""

    print("""
*** Instructions ***
 You will be answering questions about area & perimeter , try and get the right answer!
    """)


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("✖️➗➖ MATHS QUIZ ➖➗✖️")
print()

# ask the user if they want instructions (check they say / no)
want_instructions = yes_no("Do you want to see the instructions?")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check(" Push <enter> to start: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} (5 rounds)💿💿💿 "
    else:
        rounds_heading = f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

# if users are in infinite mode, increase number of rounds!
if mode == "infinite":
    num_rounds += 1


