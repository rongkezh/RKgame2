import random

class Player:
    def __init__(self, name, type, max_health, level):
        self.name = name
        self.type = type
        self.max_health = max_health
        self.current_health = max_health
        self.level = level

    def attack(self, other):
        damage = random.randint(1, 10) * (self.level / 2)
        other.take_damage(damage)
        print(f"{self.name} attacked {other.name} and dealt {damage} damage!")

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)
        print(f"{self.name} took {damage} damage. {self.name}'s health: {self.current_health}/{self.max_health}")

    def is_fainted(self):
        return self.current_health == 0

def main():
    # Create Pokemonyers
    player1 = Player("player1", "Electric", 50, 10)
    player2 = Player("player2", "Fire", 45, 8)

    print("Start Battle!")
    print(f"{player1.name} (Level {player1.level}) vs. {player2.name} (Level {player2.level})")

    while not player1.is_fainted() and not player2.is_fainted():
        # player1 attacks player2
        player1.attack(player2)

        # Check if player2 is fainted
        if player2.is_fainted():
            print(f"{player2.name} fainted. {player1.name} wins!")
            break

        # player2 attacks player1
        player2.attack(player1)

        # Check if player1 is fainted
        if player1.is_fainted():
            print(f"{player1.name} fainted. {player2.name} wins!")
            break

if __name__ == "__main__":
    main()
