import random

# checks for yes/no input

def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes / no") # This shows when they don't put in either answer.

# displays game instructions

def instructions():
    print("""
*** Instructions ***
You will be asked random math questions about area, perimeter, or circumference.
Type 'xxx' anytime to quit.
    """)

# checks for an integer with optional lower/upper bounds and exit code

def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
    elif low is not None and high is None:
        error = f"Please enter an integer that is more than / equal to {low}"
    else:
        error = f"Please enter an integer that is between {low} and {high} (inclusive)"

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# generates a random math question and its correct answer

def generate_random_question():
    question = ""
    answer = ""
    shape = random.choice(["square", "rectangle", "triangle"])

    if shape == "square":
        side = random.randint(2, 10)  # This is the random numbers it can be between
        if random.choice(["area", "perimeter"]) == "area":
            question = f"A square garden has sides of {side} cm. What is its area?"  # This generates area questions
            answer = f"{side * side}"  # This generates the answer
        else:
            question = f"A square garden has sides of {side} cm. What is its perimeter?"
            answer = f"{side * 4}"  # This function generates perimeter questions

    elif shape == "rectangle":
        length = random.randint(2, 10)
        width = random.randint(2, 10)
        if random.choice(["area", "perimeter"]) == "area":
            question = f"A rectangle is {length} cm long and {width} cm wide. What is its area?"
            answer = f"{length * width}"   # This  calculates the answer.
        else:
            question = f"A rectangle is {length} cm long and {width} cm wide. What is its perimeter?"
            answer = f"{2 * (length + width)}"   # the length and width stuff is randomly generated

    elif shape == "triangle":
        base = random.randint(2, 10)    # These random numbers pick a random number for the sides
        height = random.randint(2, 10)
        question = f"A triangle has a base of {base} cm and a height of {height} cm. What is its area?"
        answer = f"{int(0.5 * base * height)}"

    return question, answer

# Main Routine
print("\n✖️➗➖ MATHS QUIZ ➖➗✖️\n")

if yes_no("Do you want to see the instructions? ") == "yes":
    instructions()  # shows instructions if they want 'em

# keep track of score
rounds_played = 0
rounds_won = 0
rounds_lost = 0
game_history = []

print("\nInfinite Mode: Type 'xxx' to quit any time\n")
num_rounds = int_check("Rounds <enter> for infinite> Or Insert Number: ", low=1, exit_code="")  # ask user for num of rounds or infinite mode

# let the player know what they chose
if num_rounds == "":
    print("You chose infinite mode.")
else:
    print(f"You chose {num_rounds} rounds.")

# Main game loop
while True:
    if num_rounds != "" and rounds_played >= num_rounds:
        break

    question, answer = generate_random_question()
    print(f"\nQuestion {rounds_played + 1}:")
    print(question)

    # forces player to enter a whole number (no letters, no decimals)
    while True:
        user_input = input("Your answer: ").strip().lower()
        if user_input == "xxx":
            break
        try:
            user_int = int(user_input)
            if user_int < 1:
                print("Please enter an integer that is more than / equal to 1")
            else:
                break
        except ValueError:
            print("Please enter an integer that is more than / equal to 1")

    if user_input == "xxx":
        break

    rounds_played += 1

    if user_input == answer:
        print("✅ Correct!")
        rounds_won += 1
        feedback = "Correct!"   # Displays wether they got it wrong or right
    else:
        print(f"❌ Incorrect! The correct answer was {answer}.")
        rounds_lost += 1
        feedback = "Incorrect."

    game_history.append(f"Round {rounds_played}: You answered '{user_input}' — {feedback}")

# Game Summary
if rounds_played > 0:
    percent_won = rounds_won / rounds_played * 100  # Percent won and lost
    percent_lost = rounds_lost / rounds_played * 100

    print("\n📊 Game Statistics 📊")
    print(f"Questions Answered: {rounds_played}")  # Calculates and shows user stats
    print(f"👍 Correct: {rounds_won} ({percent_won:.2f}%)")
    print(f"❌ Incorrect: {rounds_lost} ({percent_lost:.2f}%)")

    if yes_no("Do you want to see your game history? ") == "yes":
        for item in game_history:  # Displays stats
            print(item)

    print("\nThanks for playing!")
else:
    print("🐔 You didn't answer any questions. Come back when you're ready!") # User does not answer questions
