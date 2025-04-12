import random
import game_logic
import monsters

def attack(attacker, defender):
    damage = game_logic.calculate_damage(attacker, defender)
    defender["stats"]["health"] -= damage
    print(f"{attacker['name']} attacks {defender['name']} for {damage} damage!")
    if game_logic.is_defeated(defender):
        print(f"{defender['name']} has been defeated!")
    return defender

def combat(player, monster):
    print(f"A {monster['name']} attacks!")
    while not game_logic.is_defeated(player) and not game_logic.is_defeated(monster):
        print(f"\n{player['name']}'s turn:")
        action = input("1. Attack\n2. Flee\nEnter your choice: ")
        if action == "1":
            monster = attack(player, monster)
        elif action == "2":
            if random.random() < 0.5:
                print(f"{player['name']} successfully fled!")
                return
            else:
                print(f"{player['name']} failed to flee!")
        else:
            print("Invalid input.")

        if not game_logic.is_defeated(monster):
            print(f"\n{monster['name']}'s turn:")
            player = attack(monster, player)

    if game_logic.is_defeated(player):
        print(f"{player['name']} has been defeated!")
    else:
        print(f"You defeated the {monster['name']}!")
