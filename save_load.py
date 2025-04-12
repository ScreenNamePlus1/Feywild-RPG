import json
import os

def save_game(player_character, current_location, filename):
    """Saves the player's character and location to a file."""
    game_data = {
        "player": player_character,
        "location": current_location
    }
    try:
        with open(filename, "w") as f:
            json.dump(game_data, f, indent=4)  # Add indent for readability
        print(f"Game saved to {filename}.")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game(filename):
    """Loads the player's character and location from a file."""
    try:
        with open(filename, "r") as f:
            game_data = json.load(f)
        return game_data["player"], game_data["location"]
    except FileNotFoundError:
        print("Save file not found.")
        return None, None
    except json.JSONDecodeError:
        print("Save file is corrupted.")
        return None, None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None

def delete_save(filename):
    """Deletes a save game file."""
    try:
        os.remove(filename)
        print(f"Save file '{filename}' deleted.")
    except FileNotFoundError:
        print(f"Save file '{filename}' not found.")
    except Exception as e:
        print(f"Error deleting save: {e}")
