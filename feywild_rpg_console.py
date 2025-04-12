import character_gen
import main_quest
import game_logic
import locations
import npcs
import monsters
import save_load
import os

def main():
    print("Welcome to the Feywild RPG Console!")

    player_character = None
    current_location = None

    while True:
        if player_character is None:
            print("Before initial menu input") #Added print
            action = input("\n1. Load Game\n2. Generate Character\n3. Delete Save\n4. Exit\nEnter your choice: ")
            print(f"Action: {action}") #added print

            if action == "1":
                loaded_character, loaded_location = save_load.load_game("savegame.json")
                if loaded_character and loaded_location:
                    player_character = loaded_character
                    current_location = loaded_location
                    print("Game loaded successfully.")
                    print_character(player_character)
                else:
                    print("Failed to load game.")
            elif action == "2":
                player_character = character_gen.create_character()
                current_location = locations.start_location()
                print("Character generated successfully.")
                print_character(player_character)
            elif action == "3":
                filename = input("Enter the filename to delete: ")
                save_load.delete_save(filename)
            elif action == "4":
                break
            else:
                print("Invalid input.")
        else:
            print("Before in game input") #added print
            main_quest.main_quest(player_character, current_location)

def print_character(character):
    """Displays character information."""
    print(f"\nCharacter: {character['name']}")
    print(f"Race: {character['race']}")
    print(f"Class: {character['class']}")
    print(f"Stats: {character['stats']}")
    print(f"Inventory: {character['inventory']}")

if __name__ == "__main__":
    main()
