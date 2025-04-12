import character_gen  # Changed import name
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
        if player_character is None:  # Initial menu (load/generate)
            action = input("\n1. Load Game\n2. Generate Character\n3. Delete Save\n4. Exit\nEnter your choice: ")

            if action == "1":
                loaded_character, loaded_location = save_load.load_game()
                if loaded_character and loaded_location:
                    player_character = loaded_character
                    current_location = loaded_location
                    print("Game loaded successfully.")
                else:
                    print("Failed to load game.")
            elif action == "2":
                player_character = character_gen.create_character()
                current_location = locations.start_location() #set start location.
                print("Character generated successfully.")
            elif action == "3":
                filename = input("Enter the filename to delete: ")
                save_load.delete_save(filename)
            elif action == "4":
                break
            else:
                print("Invalid input.")
        else:  # In-game menu (save/quest/exit)
            action = input("\n1. Save Game\n2. Continue Quest\n3. Delete Save\n4. Exit\nEnter your choice: ")

            if action == "1":
                filename = input("Enter the filename to save to: ")
                save_load.save_game(player_character, current_location, filename)
            elif action == "2":
                main_quest.main_quest(player_character)
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

if __name__ == "__main__":
    main()
