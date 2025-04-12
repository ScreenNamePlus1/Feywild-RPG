import random

def generate_ability_scores():
    """Generates ability scores using 4d6 drop lowest."""
    scores = []
    for _ in range(6):
        rolls = sorted([random.randint(1, 6) for _ in range(4)])
        scores.append(sum(rolls[1:]))  # Drop the lowest
    return scores

def create_character():
    """Creates a character with ability scores, race, and class."""
    print("Character Creation:")

    # Ability Scores
    scores = generate_ability_scores()
    ability_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for i, score in enumerate(scores):
        print(f"{ability_names[i]}: {score}")

    # Race
    races = ["Human", "Elf", "Gnome", "Eladrin"]
    print("Choose a race:")
    for i, race in enumerate(races):
        print(f"{i + 1}. {race}")
    race_choice = int(input("Enter race number: ")) - 1
    race = races[race_choice]

    # Class
    classes = ["Fighter", "Wizard", "Rogue", "Fey Wanderer"]
    print("Choose a class:")
    for i, cls in enumerate(classes):
        print(f"{i + 1}. {cls}")
    class_choice = int(input("Enter class number: ")) - 1
    cls = classes[class_choice]

    # Name
    name = input("Enter character name: ")

    character = {
        "name": name,
        "race": race,
        "class": cls,
        "ability_scores": dict(zip(ability_names, scores)),
        "xp": 0,
        "level": 1,
        "inventory": ["basic equipment"],
    }
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
