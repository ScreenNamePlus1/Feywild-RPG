import random
import monsters

locations = {
    "Feywild Forest": {
        "description": "A dense forest filled with magical creatures.",
        "exits": {"north": "Enchanted Glade"},
        "encounters": ["goblin", "fairy"]
    },
    "Enchanted Glade": {
        "description": "A beautiful glade with glowing flowers.",
        "exits": {"south": "Feywild Forest", "east": "Mystic Cave"},
        "encounters": ["fairy"]
    },
    "Mystic Cave": {
        "description": "A dark cave with strange symbols on the walls.",
        "exits": {"west": "Enchanted Glade"},
        "encounters": ["troll"]
    }
}

def get_location(location_name):
    return locations.get(location_name)

def get_encounter(location):
    encounter = random.choice(location["encounters"])
    if encounter == "goblin":
        return monsters.create_goblin()
    elif encounter == "troll":
        return monsters.create_troll()
    elif encounter == "fairy":
        return monsters.create_fairy()
    else:
        return None
