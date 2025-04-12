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
        "inventory": ["basic equipment"],
    }
    return character

if __name__ == "__main__":
    player_character = create_character()
    print("\nCharacter created:")
    print(player_character)
