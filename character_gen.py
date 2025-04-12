import random

def create_character():
    """Creates a player character."""
    name = input("Enter your character's name: ")
    race = input("Enter your character's race (human, elf, dwarf): ").lower()
    character_class = input("Enter your character's class (warrior, mage, rogue): ").lower()

    # Base stats
    stats = {
        "strength": random.randint(8, 15),
        "dexterity": random.randint(8, 15),
        "intelligence": random.randint(8, 15),
        "health": 100,
        "defense": 5
    }

    # Racial bonuses
    if race == "elf":
        stats["dexterity"] += 2
    elif race == "dwarf":
        stats["strength"] += 2

    # Class bonuses
    if character_class == "warrior":
        stats["strength"] += 3
        stats["health"] += 20
        stats["defense"] += 2
    elif character_class == "mage":
        stats["intelligence"] += 3
    elif character_class == "rogue":
        stats["dexterity"] += 3

    inventory = []
    return {"name": name, "race": race, "class": character_class, "stats": stats, "inventory": inventory}
