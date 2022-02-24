def start_game():
    """
    Starting game with an input for the player to enter:
    (rock, paper or scissors)input
    """
    print("Welcome to the game of Rock , paper and scissors.")
    print("rules: rock beat scissors, paper beats rock and scissors beats paper. \n")
    print("Play by entering r for rock, p for paper and s for scissors.")
    game_field = input("Enter your choice: ")

    try:
        if game_field == r or s or p:
            print(f"you chose {game_field}")
    except ValueError as e:
        print(f"Invalid data input {e}, Please enter r for rock p for paper or s for scissors!")



start_game()