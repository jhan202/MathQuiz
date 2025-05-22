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
You will be answering questions about area & perimeter, try and get the right answer!
    """)


# Main Routine Starts here
rounds_played = 0
rounds_won = 0
rounds_lost = 0
game_history = []
user_input = []

print("✖️➗➖ MATHS QUIZ ➖➗✖️")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()
    input("Press <enter> to start the game.\n")  # Pause thing added here Note : debug
else:
    input("Press <enter> to start the game.\n")  # Even if no instructions, still pause

num_rounds = 5  # Set number of rounds after the pause

# Game loop starts here
while rounds_played < num_rounds:

    print(f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿")
    print()

    feedback = ""
    correct = False

    # The area/ perimeter questions
    if rounds_played == 0:
        print("1. A square garden has sides of 4 cm. What is its perimeter? (Answer: 16 cm)")
        user_input = input().strip().lower()
        if user_input == "16 cm":
            print("Correct!")
            correct = True
        else:
            print("❌Incorrect! The correct answer is 16 cm.❌")
            if user_input == "16":
                print("⚠️ Please include units (cm, m, etc). ⚠️")

    elif rounds_played == 1:
        print("2. A rectangle book cover is 5 cm long and 3 cm wide. What is its area? (Answer: 15 cm)")
        user_input = input().strip().lower()
        if user_input == "15 cm":
            print("Correct!")
            correct = True
        else:
            print("❌Incorrect! The correct answer is 15 cm.❌")
            if user_input == "15":
                print("⚠️ Please include units (cm, m, etc). ⚠️")

    elif rounds_played == 2:
        print("3. A triangle sign has a base of 6 cm and a height of 4 cm. What is its area? (Answer: 12 cm)")
        user_input = input().strip().lower()
        if user_input == "12 cm":
            print("Correct!")
            correct = True
        else:
            print("❌Incorrect! The correct answer is 12 cm.❌")
            if user_input == "12":
                print("⚠️ Please include units (cm, m, etc). ⚠️")

    elif rounds_played == 3:
        print("4. A circular plate has a radius of 2 cm. What is its circumference? (Answer: 12.6 cm)")
        user_input = input().strip().lower()
        if user_input == "12.6 cm":
            print("Correct!")
            correct = True
        else:
            print("❌Incorrect! The correct answer is 12.6 cm.❌")
            if user_input == "12.6":
                print("⚠️ Please include units (cm, m, etc). ⚠️")

    elif rounds_played == 4:
        print("5. A square tile has sides of 7 cm. What is its area? (Answer: 49 cm)")
        user_input = input().strip().lower()
        if user_input == "49 cm":
            print("Correct!")
            correct = True
        else:
            print("❌Incorrect! The correct answer is 49 cm.❌")
            if user_input == "49":
                print("⚠️ Please include units (cm, m, etc). ⚠️")



    # Tracks wins and losses and add to game history thingy
    if correct:
        rounds_won += 1
        feedback = "✅ Correct!"
    else:
        rounds_lost += 1
        feedback = "❌ Incorrect!"

    game_history.append(f"Round {rounds_played + 1}: You answered '{user_input}' — {feedback}")
    rounds_played += 1


# Game History / Statistics area
if rounds_played > 0:
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    print("\n📊📊📊 Game statistics 📊📊📊")
    print(f"👍 Won: {rounds_won} ({percent_won:.2f}%)")
    print(f"😢 Lost: {rounds_lost} ({percent_lost:.2f}%)")

    see_history = yes_no("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print("\nThanks for playing.")



