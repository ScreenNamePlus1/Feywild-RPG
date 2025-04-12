import random
from transformers import pipeline
import character_generation
import locations  # the locations.py from the previous response.

generator = pipeline("text-generation", model="distilgpt2")

def generate_encounter(location):
    """Generates a random encounter based on the location."""
    if "forest" in location["name"].lower():
        creatures = ["pixie", "dryad", "treant"]
    elif "plains" in location["name"].lower():
        creatures = ["centaur", "unicorn", "fey beast"]
    else:
        creatures = ["sprite", "gnome", "fey creature"]

    creature = random.choice(creatures)
    prompt = f"A {creature} encounter in the {location['name']}."
    description = generator(prompt, max_length=50, num_return_sequences=1)[0]["generated_text"]
    print(f"\nEncounter: {description}")

def explore_location(character, location):
    """Explores a location and generates encounters."""
    print(f"\nYou are exploring {location['name']}.")
    print(location["description"])
    if location["items"]:
        print(f"You see: {', '.join(location['items'])}")
    generate_encounter(location)

def move_to_location(character, current_location, destination_name):
    """Moves the character to a new location."""
    if destination_name in current_location["exits"]:
        destination = locations.locations[
            current_location["exits"][destination_name].lower().replace(" ", "_")
        ]
        return destination
    else:
        print("You can't go that way.")
        return current_location

def main_quest(character):
    """Main quest arc."""
    print("\nYou awaken in a strange wilderness...")
    current_location = locations.locations["whispering_glade"]  # Starting location.
    explore_location(character, current_location)

    while True:
        action = input("\nWhat do you want to do? (explore, move [direction], quit): ").lower()

        if action == "explore":
            explore_location(character, current_location)
        elif action.startswith("move"):
            direction = action.split(" ")[1]
            current_location = move_to_location(character, current_location, direction)
            explore_location(character, current_location)
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    player_character = character_generation.create_character()
    main_quest(player_character)
