# game_data.py

game_state = {
    "player_health": 100,
    "player_mana": 50,
    "player_inventory": [],
    # ... other game variables ...
}

def add_item_to_inventory(item_name):
    game_state["player_inventory"].append(item_name)
    print(f"Added {item_name} to inventory.")

game_state["add_item"] = add_item_to_inventory
