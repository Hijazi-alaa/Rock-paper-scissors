import random


def main():
    """
    main function to run the game and include other function inside
    """

    print("Welcome to the game of Rock, paper and scissors.\n")
    print("rules: rock beat scissors, paper beats rock and scissors beats paper. \n")
    print("Play by entering r for rock, p for paper and s for scissors.")

   
    def is_winner(player, opponent):
        """
        function to calculate winner on each turn
        """
        if (player == "r" and opponent == "s") or \
            (player == "s" and opponent == "p") \
            or (player == "p" and opponent == "r"):
            return True


    player_score = 0
    computer_score = 0

    while True:
        try:
            available_choices = ["r", "p", "s"]
            player_input = input("Enter your choice: ")
            computer_choice = random.choice(["r", "p", "s"])
            # searched for a way to choose one random item from a list,
            # and found the random method at pynative.com
            print(f"computer chose: {computer_choice}")
            if any(player_input in choice for choice in available_choices):
                print(f"You chose {player_input}")
                is_winner(player_input, computer_choice)
                if player_input == computer_choice:
                    print("It's a tie")
                    print(f"Your score: {player_score} \nComputer score: {computer_score}")
                elif is_winner(player_input, computer_choice):
                    print("You won!")
                    player_score = +1
                    print(f"Your score: {player_score} \nComputer score: {computer_score}")
                elif is_winner(computer_choice, player_input):
                    print("You lost!")
                    computer_score = +1
                    print(f"Your score: {player_score} \nComputer score: {computer_score}")
            else:
                raise ValueError()
        except ValueError:
            print(f"Invalid data input: {player_input}, is not a valid input.\n \
                 Please enter r for rock p for paper or s for scissors!")

main()