# functions go here
def yes_no(question):
    """Checks users enter yes / no"""
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    """Print instructions"""
    print("""
*** Instructions ***
You will be answering questions about area & perimeter. 
Try and get the right answer! Make sure to include the correct units like cm, m, etc.
    """)


# checks for an integer more than 0 (allows <enter> for default 5 rounds)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"
        to_check = input(question)
        if to_check == "":
            return 5  # default to 5 rounds
        try:
            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Main Routine Starts here
rounds_played = 0

print("✖️➗➖ MATHS QUIZ ➖➗✖️")
print()

# ask the user if they want instructions
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

# Ask user for number of rounds
num_rounds = int_check("Press <enter> for 5 rounds or type number of rounds: ")

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds heading
    print(f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿")
    print()

    # Questions
    if rounds_played == 0:
        print("1. A square garden has sides of 4 cm. What is its perimeter? (ans: 16 cm)")
        user_input = input().strip().lower()
        if user_input == "16 cm":
            print("Correct!")
        else:
            print("❌ Incorrect! The correct answer is 16 cm. ❌")
            if user_input == "16":
                print("⚠️ Please include units like cm, m, etc ⚠️")

    elif rounds_played == 1:
        print("2. A rectangle book cover is 5 cm long and 3 cm wide. What is its area? (ans: 15 cm)")
        user_input = input().strip().lower()
        if user_input == "15 cm":
            print("Correct!")
        else:
            print("❌ Incorrect! The correct answer is 15 cm. ❌")
            if user_input == "15":
                print("⚠️ Please include units like cm, m, etc ⚠️")

    elif rounds_played == 2:
        print("3. A triangle sign has a base of 6 cm and a height of 4 cm. What is its area? (ans: 12 cm)")
        user_input = input().strip().lower()
        if user_input == "12 cm":
            print("Correct!")
        else:
            print("❌ Incorrect! The correct answer is 12 cm. ❌")
            if user_input == "12":
                print("⚠️ Please include units like cm, m, etc ⚠️")

    elif rounds_played == 3:
        print("4. A circular plate has a radius of 2 cm. What is its circumference? (ans: 12.6 cm)")
        user_input = input().strip().lower()
        if user_input == "12.6 cm":
            print("Correct!")
        else:
            print("❌ Incorrect! The correct answer is 12.6 cm. ❌")
            if user_input == "12.6":
                print("⚠️ Please include units like cm, m, etc ⚠️")

    elif rounds_played == 4:
        print("5. A square tile has sides of 7 cm. What is its area? (ans: 49 cm)")
        user_input = input().strip().lower()
        if user_input == "49 cm":
            print("Correct!")
        else:
            print("❌ Incorrect! The correct answer is 49 cm. ❌")
            if user_input == "49":
                print("⚠️ Please include units like cm, m, etc ⚠️")

    # Increase rounds played
    rounds_played += 1
