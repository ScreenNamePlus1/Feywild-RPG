import random
from transformers import pipeline
import character_generation
import locations
import save_load

generator = pipeline("text-generation", model="distilgpt2")

def generate_encounter(location, character): #added character as a parameter.
    # ... (same as before) ...
    character_generation.gain_xp(character, random.randint(100, 500)) # Gain xp from encounter.
    print(f"You gained xp.")

def explore_location(character, location):
    # ... (same as before) ...
    generate_encounter(location, character)

def main_quest(character):
    # ... (same as before) ...
    while True:
        action = input("\nWhat do you want to do? (explore, move [direction], save, load, quit): ").lower() #added save and load

        if action == "explore":
            explore_location(character, current_location)
        elif action.startswith("move"):
            # ... (same as before) ...
        elif action == "save":
            save_load.save_game(character, current_location)
        elif action == "load":
            character, current_location = save_load.load_game()
            if character and current_location:
                print("Game loaded successfully.")
                explore_location(character, current_location)
        elif action == "quit":
            # ... (same as before) ...

if __name__ == "__main__":
    player_character = character_generation.create_character()
    main_quest(player_character)
