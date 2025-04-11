# game_logic.py

from console import execute_code
from game_data import game_state, add_item_to_inventory #Import game state and functions.

def handle_input(user_input, game_state):
    if user_input.startswith(">"):
        code = user_input[1:].strip()
        execute_code(code, game_state)
    else:
        # Handle regular game commands
        process_game_command(user_input, game_state)

def process_game_command(command, game_state):
    # Your game command processing logic
    print(f"processing {command}")

# Main game loop
while True:
    user_input = input(">> ")
    handle_input(user_input, game_state)
