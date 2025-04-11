# feywild_rpg_console.py

from game_logic import handle_input, game_state  # Import the game loop and state

# Main game loop for the console version
while True:
    user_input = input(">> ")
    handle_input(user_input, game_state)
