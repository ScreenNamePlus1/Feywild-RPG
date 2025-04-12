import random
try:
    from transformers import pipeline
    generator = pipeline("text-generation", model="distilgpt2")
    transformers_available = True
except ImportError:
    transformers_available = False
import character_gen
import locations
import save_load

def generate_encounter(location, character):
    creatures = ["pixie", "dryad", "treant"]
    creature = random.choice(creatures)
    if transformers_available:
        prompt = f"A {creature} encounter in the {location['name']}."
        description = generator(prompt, max_length=50, num_return_sequences=1)[0]["generated_text"]
    else:
        description = f"A {creature} encounter in the {location['name']}."  # Use simple string as fallback
    print(f"\nEncounter: {description}")
    character_gen.gain_xp(character, random.randint(100, 500))
    print("You gained xp.")

def explore_location(character, location):
    print(f"\nYou are exploring {location['name']}.")
    print(location["description"])
    if location["items"]:
        print(f"You see: {', '.join(location['items'])}")
    generate_encounter(location, character)

def move_to_location(character, current_location, destination_name):
    if destination_name in current_location["exits"]:
        destination = locations.locations[current_location["exits"][destination_name].lower().replace(" ", "_")]
        return destination
    else:
        print("You can't go that way.")
        return current_location

def main_quest(character):
    current_location = locations.locations["whispering_glade"]
    explore_location(character, current_location)

    while True:
        action = input("\nWhat do you want to do? (explore, move [direction], save, load, quit): ").lower()

        if action == "explore":
            explore_location(character, current_location)
        elif action.startswith("move"):
            direction = action.split(" ")[1]
            current_location = move_to_location(character, current_location, direction)
            explore_location(character, current_location)
        elif action == "save":
            save_load.save_game(character, current_location)
        elif action == "load":
            loaded_character, loaded_location = save_load.load_game()
            if loaded_character and loaded_location:
                character = loaded_character
                current_location = loaded_location
                print("Game loaded successfully.")
                explore_location(character, current_location)
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    player_character = character_gen.create_character()
    main_quest(player_character)
