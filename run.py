import random


def starting_game():
    """
    Creating an input to accept r,p or s as a player answer
    return as invalid data if data provided is anything else
    """
    print("Welcome to the game of Rock, paper and scissors.")
    print("rules: rock beat scissors, paper beats rock and scissors beats paper. \n")
    print("Play by entering r for rock, p for paper and s for scissors.")

    try:
        player_input = input("Enter your choice: ")
        if player_input == ("r" or "p" or "s"):
            print(f"You chose {player_input}")
        # need to call function to continue game later
        else:
            pass
    except ValueError as e:
        print(f"Invalid data input: {e}, Please enter r for rock p for paper or s for scissors!")

    computer = random.choice(["r", "p", "s"])   # searched for a way to choose one random item from a list and found the random method at pynative.com
    print(f"computer choise is: {computer}")

starting_game()