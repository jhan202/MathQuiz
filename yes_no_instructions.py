
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
        elif response == "xxx":
            break
        else:
            print("please enter yes / no")


# Main routine


while True:
    want_instructions = yes_no("Do you want to see the instructions? ").lower()
    print(f"you chose {want_instructions}")

    print("we done")
