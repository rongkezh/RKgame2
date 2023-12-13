class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def get_choice(self):
        print(f"{self.name}, choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter your choice (1/2/3): ")
        self.choice = int(choice)
        return self.choice

def determine_pvp_winner(player1, player2):
    if player1.choice == player2.choice:
        return "It's a tie!"
    elif (player1.choice == 1 and player2.choice == 3) or \
         (player1.choice == 2 and player2.choice == 1) or \
         (player1.choice == 3 and player2.choice == 2):
        return f"{player1.name} wins!"
    else:
        return f"{player2.name} wins!"

def print_pvp_choices(player1, player2):
    print(f"{player1.name} chose {player1.choice}")
    print(f"{player2.name} chose {player2.choice}")

def play_pvp_game(rounds):
    print(f"Welcome to Best of {rounds} PvP Rock, Paper, Scissors!")

    player1 = Player(input("Enter Player 1 name: "))
    player2 = Player(input("Enter Player 2 name: "))

    rounds_played = 0
    player1_wins = 0
    player2_wins = 0

    while rounds_played < rounds:
        player1.get_choice()
        player2.get_choice()

        print_pvp_choices(player1, player2)

        result = determine_pvp_winner(player1, player2)
        print(result)

        if "wins" in result:
            if result.startswith(player1.name):
                player1_wins += 1
            else:
                player2_wins += 1

        rounds_played += 1

    if player1_wins > player2_wins:
        print(f"{player1.name} wins the best of {rounds}!")
    elif player1_wins < player2_wins:
        print(f"{player2.name} wins the best of {rounds}!")
    else:
        print(f"It's a tie in the best of {rounds}!")

if __name__ == "__main__":
    try:
        rounds_choice = int(input("Enter the number of rounds: "))
        if rounds_choice < 1:
            raise ValueError("Number of rounds should be at least 1.")
        
        play_pvp_game(rounds_choice)
    except ValueError as e:
        print(f"Invalid input: {e}")
