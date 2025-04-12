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
            action = input("\n1. Load Game\n2. Generate Character\n3. Delete Save\n4. Exit\nEnter your choice: ")

            if action == "1":
                loaded_character, loaded_location = save_load.load_game()
                if loaded_character and loaded_location:
                    player_character = loaded_character
                    current_location = loaded_location
                    print("Game loaded successfully.")
                    print_character(player_character)  # Display loaded character
                else:
                    print("Failed to load game.")
            elif action == "2":
                player_character = character_gen.create_character()
                current_location = locations.start_location()
                print("Character generated successfully.")
                print_character(player_character)  # Display generated character
            elif action == "3":
                filename = input("Enter the filename to delete: ")
                save_load.delete_save(filename)
            elif action == "4":
                break
            else:
                print("Invalid input.")
        else:
            action = input("\n1. Save Game\n2. Continue Quest\n3. Delete Save\n4. Exit\nEnter your choice: ")

            if action == "1":
                filename = input("Enter the filename to save to: ")
                save_load.save_game(player_character, current_location, filename)
            elif action == "2":
                play_game(player_character, current_location)
            elif action == "3":
                filename = input("Enter the filename to delete: ")
                save_load.delete_save(filename)
            elif action == "4":
                save_choice = input("Would you like to save before exiting? (yes/no): ").lower()
                if save_choice == "yes":
                    filename = input("Enter the filename to save to: ")
                    save_load.save_game(player_character, current_location, filename)
                break
            else:
                print("Invalid input.")

def print_character(character):
    """Displays character information."""
    print(f"\nCharacter: {character['name']}")
    print(f"Race: {character['race']}")
    print(f"Class: {character['class']}")
    print(f"Stats: {character['stats']}")
    print(f"Inventory: {character['inventory']}")

def play_game(player_character, current_location):
    """Handles the main game loop."""
    print(f"\nYou are in {current_location}.")
    location_data = locations.get_location(current_location)
    encounter = locations.get_encounter(location_data)
    if encounter:
        combat.combat(player_character, encounter)
    input("Press Enter to continue...")
    next_location = location_data["exits"].get("north") #example movement.
    if next_location:
        main_quest.main_quest(player_character, next_location)
    else:
        print("There is no exit in that direction.")

if __name__ == "__main__":
    main()
