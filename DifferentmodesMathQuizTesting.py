import random

from B_01_Game import num_rounds


def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes / no")    # Function that asks users yes / no


def instructions():
    print("""
*** Instructions ***
You will be asked random math questions about area, perimeter, or circumference. 
Answer with correct units (e.g. cm). Type 'xxx' anytime to quit.    
    """) # The instructions that are shown


def generate_random_question():
    shape = random.choice(["square", "rectangle", "triangle", "circle"]) # list of the shapes that will be  asked in the questions

    if shape == "square":    # <------ Randomly generating numbers for area and perm for the shape
        side = random.randint(2, 10)
        if random.choice(["area", "perimeter"]) == "area":
            question = f"A square has sides of {side} cm. What is its area?"
            answer = f"{side * side} cm"
        else:
            question = f"A square has sides of {side} cm. What is its perimeter?"
            answer = f"{side * 4} cm"

    elif shape == "rectangle":
        length = random.randint(2, 10)  # <----- This function thing is used to randomly generate numbers
        width = random.randint(2, 10)
        if random.choice(["area", "perimeter"]) == "area":
            question = f"A rectangle is {length} cm long and {width} cm wide. What is its area?"
            answer = f"{length * width} cm"
        else:
            question = f"A rectangle is {length} cm long and {width} cm wide. What is its perimeter?"
            answer = f"{2 * (length + width)} cm"

    elif shape == "triangle":
        base = random.randint(2, 10)
        height = random.randint(2, 10)
        question = f"A triangle has a base of {base} cm and a height of {height} cm. What is its area?"
        answer = f"{int(0.5 * base * height)} cm"

    return question, answer


# Main Routine

print("✖️➗➖ MATHS QUIZ ➖➗✖️\n")

if yes_no("Do you want to see the instructions? ") == "yes":
    instructions()  # Displays instructions if asked to do so

rounds_played = 0
rounds_won = 0
rounds_lost = 0
game_history = []
num_rounds = []

print("\n Please select a mode <regular> for Normal Mode and <inf> for endless mode,"
      " Type 'xxx' to quit any time.  \n")  # Infinite Mode: Type 'xxx' to quit any time


if num_rounds == "regular":
    mode = "Normal"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    rounds_heading = f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"
    print(rounds_heading)
    print()

    # Question 1 - Square garden perimeter
    if rounds_played == 0:
        print("1 A square garden has sides of 4 cm. What is its perimeter?(ans : 16 cm)")
        user_input = input().strip().lower()
        if user_input == "16 cm":
            print("Correct!")
        else:
            print("❌Incorrect! The correct answer is 16 cm.❌")
            if user_input == "16":
                print("⚠️Please input units cm , m , etc⚠️")  # Unit checker thing!!

    # Question 2 - Rectangle book cover area
    elif rounds_played == 1:
        print("\n 2 rectangle book cover is 5 cm long and 3 cm wide. What is its area?(ans : 15 cm)")
        user_input = input().strip().lower()
        if user_input == "15 cm":
            print("Correct!")
        else:
            print("❌Incorrect! The correct answer is 15 cm ❌.")
            if user_input == "15":
                print("⚠️Please input units cm , m , etc⚠️")

    # Question 3 - Triangle sign area
    elif rounds_played == 2:
        print("\n 3 A triangle sign has a base of 6 cm and a height of 4 cm. What is its area?(ans : 12 cm)")
        user_input = input().strip().lower()
        if user_input == "12 cm":
            print("Correct!")
        else:
            print("❌Incorrect! The correct answer is 12 cm ❌ .")
            if user_input == "12":
                print("⚠️Please input units cm , m , etc⚠️")

    # Question 4 - Circular plate circumference
    elif rounds_played == 3:
        print("\n 4. A circular plate has a radius of 2 cm. What is its circumference?(12.6 cm)")
        user_input = input().strip().lower()
        if user_input == "12.6 cm":
            print("Correct!")
        else:
            print("❌Incorrect! The correct answer is 12.6 cm ❌.")
        if user_input == "12.6":
            print("⚠️Please input units cm , m , etc⚠️")

    # Question 5 - Square tile area
    elif rounds_played == 4:
        print("\n 5. A square tile has sides of 7 cm. What is its area?(49 cm)")
        user_input = input().strip().lower()
        if user_input == "49 cm":
            print("Correct!")
        else:
            print("❌Incorrect! The correct answer is 49 cm ❌.")
            if user_input == "49":
                print("⚠️Please input units cm , m , etc⚠️")

    # Increase rounds after question
    rounds_played += 1




while True:
    question, answer = generate_random_question()
    rounds_played += 1
    print(f"\n Question {rounds_played}:")
    print(question)

    user_input = input("Your answer: ").strip().lower()
    if user_input == "xxx":
        break

    if user_input == answer:   # Checks and displays if a user got the question wrong or right.
        print("✅ Correct!")
        rounds_won += 1
        feedback = "Correct!"
    else:
        print(f"❌ Incorrect! The correct answer was {answer}.")
        if user_input == answer.replace(" cm", ""):
            print("⚠️ Don’t forget the unit (e.g. cm)! ⚠️")
        rounds_lost += 1
        feedback = "Incorrect."

    game_history.append(f"Round {rounds_played}: You answered '{user_input}' — {feedback}")

# Game history

if rounds_played > 0:
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    print("\n📊 Game Statistics 📊")
    print(f"Questions Answered: {rounds_played}")
    print(f"👍 Correct: {rounds_won} ({percent_won:.2f}%)")
    print(f"❌ Incorrect: {rounds_lost} ({percent_lost:.2f}%)")

    if yes_no("Do you want to see your game history? ") == "yes":
        for item in game_history:
            print(item)

    print("\nThanks for playing!")

else:
        print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔!")
