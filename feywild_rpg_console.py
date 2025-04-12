import character_gen  # Changed import name
import main_quest
import game_logic
import locations
import npcs
import monsters
import save_load

def main():
    print("Welcome to the Feywild RPG Console!")

    while True:
        action = input("\nWould you like to load a game? (yes/no): ").lower()
        if action == "yes":
            loaded_character, loaded_location = save_load.load_game()
            if loaded_character and loaded_location:
                player_character = loaded_character
                main_quest.main_quest(player_character)
                break
        elif action == "no":
            player_character = character_gen.create_character()  # Changed module name
            main_quest.main_quest(player_character)
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
