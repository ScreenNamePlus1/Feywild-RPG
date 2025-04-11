# console.py

def execute_code(code_string, game_state):
    allowed_globals = {
        "game": game_state,
        "print": print,
        # Add other safe functions and variables here
    }
    allowed_locals = {}
    try:
        exec(code_string, allowed_globals, allowed_locals)
    except Exception as e:
        print(f"Error: {e}")
