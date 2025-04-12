import json

def save_game(character, location, filename="savegame.json"):
    """Saves the game state to a JSON file."""
    save_data = {
        "character": character,
        "location": location,
    }
    with open(filename, "w") as f:
        json.dump(save_data, f)
    print("Game saved.")

def load_game(filename="savegame.json"):
    """Loads the game state from a JSON file."""
    try:
        with open(filename, "r") as f:
            save_data = json.load(f)
        print("Game loaded.")
        return save_data["character"], save_data["location"]
    except FileNotFoundError:
        print("No saved game found.")
        return None, None
