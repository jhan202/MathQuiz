import random


def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print("""
*** Instructions ***
You will be asked random math questions about area, perimeter, or circumference.
Answer with correct units (e.g. cm). Type 'xxx' anytime to quit.
    """)


def generate_random_question():
    shape = random.choice(["square", "rectangle", "triangle", "circle"])

    if shape == "square":
        side = random.randint(2, 10)
        if random.choice(["area", "perimeter"]) == "area":
            question = f"A square has sides of {side} cm. What is its area?"
            answer = f"{side * side} cm"
        else:
            question = f"A square has sides of {side} cm. What is its perimeter?"
            answer = f"{side * 4} cm"

    elif shape == "rectangle":
        length = random.randint(2, 10)
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

    elif shape == "circle":
        radius = random.randint(1, 5)
        question = f"A circle has a radius of {radius} cm. What is its circumference? (Use π ≈ 3.14)"
        circumference = round(2 * 3.14 * radius, 1)
        answer = f"{circumference} cm"

    return question, answer


# ----- Main Routine -----

print("✖️➗➖ MATHS QUIZ ➖➗✖️\n")

if yes_no("Do you want to see the instructions? ") == "yes":
    instructions()

rounds_played = 0
rounds_won = 0
rounds_lost = 0
game_history = []

print("\n🔁 Infinite Mode: Type 'xxx' to quit any time 🔁\n")

while True:
    question, answer = generate_random_question()
    rounds_played += 1
    print(f"\n📘 Question {rounds_played}:")
    print(question)

    user_input = input("Your answer: ").strip().lower()
    if user_input == "xxx":
        break

    if user_input == answer:
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

# ----- Game Summary -----

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
    print("🐔 You didn't answer any questions. Come back when you're ready!")
