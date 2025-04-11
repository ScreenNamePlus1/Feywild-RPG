# feywild_rpg.py (Conceptual and Highly Insecure)

import locations
import npcs
import monsters
import builtins
import subprocess  # VERY DANGEROUS

# Extremely insecure sandboxing attempt
restricted_globals = {
    "__builtins__": {
        name: builtins.__dict__[name]
        for name in ["print", "len", "range", "input", "int", "float", "str", "list", "dict", "tuple"]
    }
}

def execute_player_code(code):
    try:
        # VERY DANGEROUS: Using subprocess to execute code in a separate process
        # This is not a proper sandbox and is highly vulnerable.
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True, timeout=5)  # 5 second timeout to prevent infinite loops.
        print(result.stdout)
        print(result.stderr)
    except Exception as e:
        print(f"Error executing code: {e}")

def display_location(location):
    print(f"\nYou are now in {location['name']}.")
    print(location['description'])
    if location['items']:
        print("Items here:")
        for item in location['items']:
            print(f"- {item}")
    if location['exits']:
        print("Exits:")
        for direction, exit_location in location['exits'].items():
            print(f"- {direction}: {exit_location['name']}")

def move(current_location, direction):
    if direction in current_location['exits']:
        return current_location['exits'][direction]
    else:
        print("You can't go that way.")
        return current_location

def main():
    current_location = locations.locations['start']
    display_location(current_location)

    while True:
        action = input("\nWhat do you want to do? (move [direction], talk, fight, code, quit): ").lower()

        if action.startswith("move"):
            direction = action.split(" ")[1]
            current_location = move(current_location, direction)
            display_location(current_location)
        elif action == "talk":
            npcs.interact_with_npc()
        elif action == "fight":
            monsters.encounter_monster()
        elif action == "code":
            player_code = input("Enter Python code: ")
            execute_player_code(player_code)
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
