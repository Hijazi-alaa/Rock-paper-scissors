import random


def starting_game():
    """
    Creating an input to accept r,p or s as a player answer
    return as invalid data if data provided is anything else
    """
    print("Welcome to the game of Rock, paper and scissors.\n")
    print("rules: rock beat scissors, paper beats rock and scissors beats paper. \n")
    print("Play by entering r for rock, p for paper and s for scissors.")

    try:
        available_choices = ["r", "p", "s"]
        player_input = input("Enter your choice: ")
        if any(player_input in choice for choice in available_choices):
            print(f"You chose {player_input}")
            computer_randomize()
        # need to call function to continue game later
        else:
            raise ValueError()
    except ValueError:
        print(f"Invalid data input: {player_input}, is not a valid input.\n Please enter r for rock p for paper or s for scissors!")


def computer_randomize():
    """
    using random method from imported random to make the computer choose rock, paper or scissors
    """
    computer_choice = random.choice(["r", "p", "s"])   # searched for a way to choose one random item from a list and found the random method at pynative.com
    print(f"computer choise is: {computer_choice}")



starting_game()