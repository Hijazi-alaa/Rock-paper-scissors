import random


def starting_game():
    """
    Creating an input to accept r,p or s as a player answer
    return as invalid data if data provided is anything else
    """
    print("Welcome to the game of Rock, paper and scissors.")
    print("rules: rock beat scissors, paper beats rock and scissors beats paper. \n")
    print("Play by entering r for rock, p for paper and s for scissors.")

    moves = ["r", "p", "s"]
    player_input = input("Enter your choice: ")
    computer = random.choice(["r", "p", "s"]) #searched for a way to choose one random item from a list and found the random method at pynative.com
    print(f"computer choise is: {computer}")


def valedating_input(value):
    try:
        if move in moves = player_input
        print(f"You chose {player_input}")
    else:
        pass


#   except ValueError:
#        print(f"Invalid data input: {player_input}, Please enter r for rock p for paper or s for scissors!")

starting_game()