import random


print("Welcome to the game of Rock, paper and scissors.\n")
print("rules: rock beat scissors, paper beats rock and scissors beats paper. \n")
print("Play by entering r for rock, p for paper and s for scissors.")


def computer_randomize():
    """
    using random method from imported random to make the computer choose rock, paper or scissors
    and the result if both the player and computer had the same choice
    """
    computer_choice = random.choice(["r", "p", "s"])   # searched for a way to choose one random item from a list and found the random method at pynative.com
    print(f"computer chose: {computer_choice}")

    if player_input == computer_choice:
        print("It's a tie")

def calculating_winner(player, opponent):
    """
    function to calculate winner on each turn
    """
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True

try:
    available_choices = ["r", "p", "s"]
    player_input = input("Enter your choice: ")
    if any(player_input in choice for choice in available_choices):
        print(f"You chose {player_input}")
        computer_randomize()
        computer_input = random.choice(["r", "p", "s"])
        if calculating_winner(player_input, computer_input):
            print("You won!")
        elif calculating_winner(computer_input, player_input):
            print("You lost!")
    else:
        raise ValueError()

except ValueError:
    print(f"Invalid data input: {player_input}, is not a valid input.\n Please enter r for rock p for paper or s for scissors!")

