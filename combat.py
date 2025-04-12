import random

def attack(attacker, defender):
    """Handles an attack between two characters."""
    damage = max(0, attacker["stats"]["strength"] - defender["stats"]["defense"] + random.randint(1, 6))
    defender["stats"]["health"] -= damage
    print(f"{attacker['name']} attacks {defender['name']} for {damage} damage!")
    if defender["stats"]["health"] <= 0:
        print(f"{defender['name']} has been defeated!")
    return defender

def combat(player, monster):
    """Handles a combat encounter."""
    print(f"A {monster['name']} attacks!")
    while player["stats"]["health"] > 0 and monster["stats"]["health"] > 0:
        # Player's turn
        print(f"\n{player['name']}'s turn:")
        action = input("1. Attack\n2. Flee\nEnter your choice: ")
        if action == "1":
            monster = attack(player, monster)
        elif action == "2":
            if random.random() < 0.5:  # 50% chance to flee
                print(f"{player['name']} successfully fled!")
                return
            else:
                print(f"{player['name']} failed to flee!")
        else:
            print("Invalid input.")

        # Monster's turn (if alive)
        if monster["stats"]["health"] > 0:
            print(f"\n{monster['name']}'s turn:")
            player = attack(monster, player)

    if player["stats"]["health"] <= 0:
        print(f"{player['name']} has been defeated!")
    else:
        print(f"You defeated the {monster['name']}!")

# Example monster
def create_goblin():
    return {"name": "Goblin", "stats": {"health": 30, "strength": 8, "defense": 5}}

# Example player.
def create_player():
    return {"name": "Player", "stats": {"health": 100, "strength": 12, "defense": 8}}
