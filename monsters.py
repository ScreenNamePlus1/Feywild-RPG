import random

monster_names = ["Goblin", "Troll", "Fairy", "Orc", "Skeleton"]

def create_goblin():
    return {"name": "Goblin", "stats": {"health": 30, "strength": 8, "defense": 5}}

def create_troll():
    return {"name": "Troll", "stats": {"health": 60, "strength": 15, "defense": 10}}

def create_fairy():
    return {"name": "Fairy", "stats": {"health": 20, "strength": 5, "defense": 3}}

def create_random_monster():
    """Creates a random monster."""
    name = random.choice(monster_names)
    health = random.randint(20, 80)
    strength = random.randint(5, 15)
    defense = random.randint(3, 10)
    return {"name": name, "stats": {"health": health, "strength": strength, "defense": defense}}
