import random


def main():
    """
    main function to run the game and include other function inside
    """
    print("Welcome to the game of Rock, paper and scissors.")
    print("rules: rock beat scissors,\
    paper beats rock and scissors beats paper.")
    print("Play by entering r for rock, p for paper and s for scissors. \n")
    print("---------------------------------------------------------------")

    def get_user_player_name():
        """
        function to get the user user name
        """
        username = input("Enter a username to start:\n")
        return username

    def get_random_win_response():
        """
        select a random win response from a list
        """
        list_of_win_responses = ["Nice!", "Good Job!", "That's one point!",
                                 "A win!, can you do it again?",
                                 "Wow! you are good at this game.",
                                 "Well done!"]
        get_random_win = random.choice(list_of_win_responses)
        return get_random_win

    def get_random_lose_response():
        """
        select a random lose response from a list
        """
        list_of_lose_responses = ["Better luck next time!",
                                  "You'll get it right the next time!",
                                  "Opsie", "Im' sure you'll win at some point",
                                  "Try again!"]
        get_random_lose = random.choice(list_of_lose_responses)
        return get_random_lose

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

    username = get_user_player_name()
    print(f"Welcome {username}, good luck! \n")

    while True:
        try:
            available_choices = ["r", "p", "s"]
            player_input = input("Type in your choice of action: \n")

            win_response = get_random_win_response()
            lose_response = get_random_lose_response()
            # Passed the function here to get
            # a new random response every turn and not
            # repeat the same random word

            if any(player_input in choice for choice in available_choices):
                print(f"You chose {player_input} \n")

                computer_choice = random.choice(["r", "p", "s"])
                # searched for a way to choose one random item from a list,
                # and found the random method at pynative.com
                print(f"computer chose: {computer_choice}")

                is_winner(player_input, computer_choice)
                if player_input == computer_choice:
                    print("It's a tie \n")
                    print(f"{username} score: {player_score}\
                    \nComputer score: {computer_score}\n")
                elif is_winner(player_input, computer_choice):
                    print(f"You won! \n{win_response} \n")
                    player_score = player_score + 1
                    print(f"{username} score: {player_score}\
                    \nComputer score: {computer_score}\n")
                elif is_winner(computer_choice, player_input):
                    print(f"You lost! \n{lose_response} \n")
                    computer_score = computer_score + 1
                    print(f"{username} score: {player_score}\
                    \nComputer score: {computer_score}\n")
            else:
                raise ValueError()
        except ValueError:
            print(f"Invalid data input: {player_input}, is not a valid input.\n \
                 Please enter r for rock p for paper or s for scissors!")


main()
