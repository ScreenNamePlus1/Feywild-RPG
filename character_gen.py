import random
l
def generate_ability_scores():
    # ... (same as before) ...

def create_character():
    # ... (same as before) ...
    character = {
        # ... (same as before) ...
        "xp": 0,
        "level": 1,
        "inventory": ["basic equipment"],
    }ll
    return character

def level_up(character):
    """Levels up the character."""
    if character["level"] < 20:
        character["level"] += 1
        print(f"{character['name']} leveled up to level {character['level']}!")
        # Add level-up bonuses here (e.g., HP increase, skill points)
    else:
        print(f"{character['name']} is already at max level.")

def gain_xp(character, xp):
    """Gains XP for the character and checks for level up."""
    character["xp"] += xp
    print(f"{character['name']} gained {xp} XP.")

    # D&D 3.5 XP thresholds (simplified)
    xp_thresholds = [0, 1000, 3000, 6000, 10000, 15000, 21000, 28000, 36000, 45000, 55000, 66000, 78000, 91000, 105000, 120000, 136000, 153000, 171000, 190000]
    if character["level"] < 20 and character["xp"] >= xp_thresholds[character["level"]]:
        level_up(character)
