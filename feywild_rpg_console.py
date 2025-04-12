import random
import json
import math

# Character and Enemy Stats
class Character:
    def __init__(self, name, race, class_type, strength, dexterity, constitution, intelligence, wisdom, charisma, hp, level=1, xp=0, mana=20, gold=100):
        self.name = name
        self.race = race
        self.class_type = class_type
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hp = hp
        self.max_hp = hp
        self.level = level
        self.xp = xp
        self.inventory = []
        self.mana = mana
        self.abilities = []
        self.quests = []
        self.gold = gold

    def attack(self, target):
        attack_roll = random.randint(1, 20) + self.strength
        if attack_roll >= 10:
            damage = random.randint(1, 8) + self.strength
            target.hp -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage!")
            return True
        else:
            print(f"{self.name} misses!")
            return False

    def is_alive(self):
        return self.hp > 0

    def show_stats(self):
        print(f"Name: {self.name}, Race: {self.race}, Class: {self.class_type}")
        print(f"HP: {self.hp}/{self.max_hp}, Level: {self.level}, XP: {self.xp}, Gold: {self.gold}")
        print(f"STR: {self.strength}, DEX: {self.dexterity}, CON: {self.constitution}, INT: {self.intelligence}, WIS: {self.wisdom}, CHA: {self.charisma}")
        print(f"Inventory: {self.inventory}")
        print(f"Mana: {self.mana}")
        print("Abilities:")
        for ability in self.abilities:
            print(f"- {ability.name}: {ability.description} ({ability.cost} Mana)")

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        print(f"{self.name} has reached level {self.level}!")

    def use_ability(self, ability, target=None):
        if self.mana >= ability.cost:
            self.mana -= ability.cost
            ability.effect(self, target)
            print(f"{self.name} uses {ability.name}!")
        else:
            print(f"{self.name} doesn't have enough mana!")

    def show_quests(self):
        if self.quests:
            print("Active Quests:")
            for i, quest in enumerate(self.quests):
                print(f"{i + 1}. {quest['description']} (Reward: {quest['reward']})")
                print(f"   Current Stage: {quest['stages'][quest.get('current_stage', 0)]}")
        else:
            print("No active quests.")

class Enemy(Character):
    def __init__(self, name, hit_dice, armor_class, attack_bonus, damage, experience):
        num_dice, die_size = map(int, hit_dice.split('d'))
        hp = random.randint(num_dice, num_dice * die_size)
        super().__init__(name, "Enemy", "Monster", 10, 10, 10, 10, 10, 10, hp, gold = 0)
        self.armor_class = armor_class
        self.attack_bonus = attack_bonus
        self.damage = damage
        self.experience = experience

    def attack(self, target):
        attack_roll = random.randint(1, 20) + self.attack_bonus
        if attack_roll >= target.armor_class:
            num_dice, die_size_bonus = self.damage.split('d')
            if '+' in die_size_bonus:
                die_size, bonus = map(int, die_size_bonus.split('+'))
            else:
                die_size = int(die_size_bonus)
                bonus = 0
            damage = random.randint(1, die_size) + bonus
            target.hp -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage!")
            return True
        else:
            print(f"{self.name} misses!")
            return False

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Ability:
    def __init__(self, name, description, cost, effect):
        self.name = name
        self.description = description
        self.cost = cost
        self.effect = effect

# Example ability effects:
def heal(user, target=None):
    if target is None:
        target = user
    heal_amount = random.randint(5, 10)
    target.hp = min(target.hp + heal_amount, target.max_hp)
    print(f"{target.name} heals for {heal_amount} HP.")

def magic_missile(user, target):
    damage = random.randint(8, 12)
    target.hp -= damage
    print(f"{target.name} takes {damage} damage from magic missile.")

# Status Effects
class StatusEffect:
    def __init__(self, name, duration, effect):
        self.name = name
        self.duration = duration
        self.effect = effect

# Game World and Navigation
MAP_WIDTH = 20
MAP_HEIGHT = 20

world_map = [[None for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

world_map[5][5] = {
    "name": "Grove",
    "description": "A peaceful grove, ancient trees surround you. The air is thick with magic. Suddenly, a dark energy tears through the trees!",
    "connections": {"north": (5, 6), "east": (6, 5), "west": (4, 5), "south": (5,4)},
    "encounters": ["goblin", "orc"],
    "npcs": ["Faelar", "Sylvane"],
    "stability": 0.8,
    "visited": False,
}
# ... (Other World Map Locations) ...

current_location = (5, 5)

# NPC Names
first_names = ["Faelar", "Sylvane", "Bram", "Lyra", "Kaelen", "Nimue", "Torvin", "Anya", "Rylan", "Elara"]
last_names = ["Whisperwind", "Shadowbrook", "Stoneheart", "Silverleaf", "Nightshade", "Sunstrider", "Ironbark", "Moonwhisper", "Thornwood", "Emberglow"]

def generate_npc_name():
    return random.choice(first_names) + " " + random.choice(last_names)

def shift_locations():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            location = world_map[y][x]
            if location and random.random() > location["stability"]:
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT and not world_map[new_y][new_x]:
                    world_map[new_y][new_x] = location
                    world_map[y][x] = None
                    print(f"{location['name']} shifts slightly.")

def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def explore(player):
    global current_location
    location = world_map[current_location[1]][current_location[0]]
    print(location["description"])

    location["visited"] = True

    directions = location["connections"]
    if directions:
        for i, direction in enumerate(directions):
            next_coord = directions[direction]
            next_location = world_map[next_coord[1]][next_coord[0]]
            distance = calculate_distance(current_location, next_coord)
            print(f"{i + 1}. Go {direction.capitalize()} (Distance: {distance:.2f}).")
        choice = input("> ")
        try:
            direction_choice = list(directions.keys())[int(choice) - 1]
            current_location = directions[direction_choice]
        except (ValueError, IndexError):
            print("Invalid choice.")
    else:
        print("There are no exits here.")

    if location["encounters"]:
        encounter_chance = random.randint(1, 4)
        if encounter_chance == 1:
            enemy_name = random.choice(location["encounters"])
            enemy = create_enemy(enemy_name)
            combat(player, enemy)

    if location["npcs"]:
        npc_chance = random.randint(1, 4)
        if npc_chance == 1:
            npc_name = generate_npc_name()
            interact_npc(player, npc_name)

    print(f"Current Coordinates: {current_location}")
    shift_locations()

def load_monster_data():
    try:
        with open("monsters.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: monsters.json not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in monsters.json.")
        return {}

monster_data = load_monster_data()

def create_enemy(enemy_name):
    if enemy_name.lower() in monster_data:
        monster = monster_data[enemy_name.lower()]
        return Enemy(
            monster["name"],
            monster["hit_dice"],
            monster["armor_class"],
            monster["attack"],
            monster["damage"],
            monster["experience"]
        )
    else:
        return Enemy("Unknown Enemy", "1d6", 10, 0, "1d4", 10)

# Combat System
def combat(player, enemy):
    print(f"A {enemy.name} attacks!")
    player_status_effects = []
    enemy_status_effects = []
    while player.is_alive() and enemy.is_alive():
        # Apply Status Effects
        for effect in player_status_effects:
            effect.effect(player)
            effect.duration -= 1
        player_status_effects = [effect for effect in player_status_effects if effect.duration > 0]

        for effect in enemy_status_effects:
            effect.effect(enemy)
            effect.duration -= 1
        enemy_status_effects = [effect for effect in enemy_status_effects if effect.duration > 0]

        print(f"\n{player.name}'s turn:")
        print("1. Attack")
        print("2. Flee")
        print("3. Use Ability")
        choice = input("> ")

        if choice == "1":
            player.attack(enemy)
            if enemy.is_alive():
                enemy.attack(player)
            else:
                print(f"You defeated the {enemy.name}!")
                player.xp += enemy.experience
                player.gold += random.randint(1, enemy.experience)
                if player.xp >= player.level * 100:
                    player.level_up()
                return
        elif choice == "2":
            print("You attempt to flee...")
            flee_roll = random.randint(1, 20) + player.dexterity
            if flee_roll > 10:
                print("You successfully escape!")
                return
            else:
                print("You failed to escape!")
                enemy.attack(player)
        elif choice == "3":
            if player.abilities:
                print("Choose an ability:")
                for i, ability in enumerate(player.abilities):
                    print(f"{i + 1}. {ability.name} ({ability.cost} Mana)")
                ability_choice = input("> ")
                try:
                    ability_index = int(ability_choice) - 1
                    player.use_ability(player.abilities[ability_index], enemy)
                except (ValueError, IndexError):
                    print("Invalid ability choice.")
            else:
                print("You have no abilities.")
            if enemy.is_alive():
                enemy.attack(player)
        else:
            print("Invalid choice.")

        if random.randint(1,10) == 1:
            enemy_status_effects.append(StatusEffect("poison", 3, lambda target: target.hp - random.randint(1,4)))

    if not player.is_alive():
        print("You have been defeated!")

# NPC Interaction (same as before)
# ...

# Random Quest Generation
def generate_goblin_quest():
    return{
        "description": "Goblin Threat",
        "reward": "50 gold, 100 xp",
        "stages": [
            "Talk to the villager.",
            "Enter the thicket.",
            "Slay 5 goblins.",
            "Return to the villager.",
        ],
        "hints": ["Goblins are weak to fire.", "They are in the thicket."],
    }

# City Generation
city_names = ["Silverwood", "Gloomhaven", "Emberfall", "Whisperwind City", "Stonecrest"]
city_districts = ["Market Square", "Tavern District", "Temple District", "Guildhall", "Residential Area", "Docks"]
item_names = ["Sword", "Shield", "Potion", "Staff", "Amulet"]
item_descriptions = ["A sharp sword.", "A sturdy shield.", "A healing potion.", "A magical staff.", "A mystical amulet."]

def generate_city():
    city = {
        "name": random.choice(city_names),
        "description": f"A bustling city of {random.randint(500, 5000)} inhabitants.",
        "districts": random.sample(city_districts, random.randint(3, 5)),
        "npcs": [generate_npc_name() for _ in range(random.randint(3, 6))],
        "shops": [{"item":Item(random.choice(item_names), random.choice(item_descriptions)), "price": random.randint(10, 100)} for _ in range(random.randint(1, 3))],
        "quests": [generate_goblin_quest()]
    }
    return city

def explore_city(player, city):
    print(f"You enter {city['name']}.")
    print(city["description"])
    print("Districts:")
    for i, district in enumerate(city["districts"]):
        print(f"{i + 1}. {district}")
    print("0. Leave City")
    choice = input("> ")
    try:
        district_choice = int(choice) - 1
        if district_choice == -1:
            return
        print(f"You enter the {city['districts'][district_choice]}.")
        if city["districts"][district_choice] == "Market Square":
            for i, shop in enumerate(city["shops"]):
                print(f"{i+1}. {shop['item'].name} - {shop['price']} gold")
            print("0. Exit Market")
            shop_choice = int(input("> ")) -1
            if shop_choice == -1:
                return
            if player.gold >= city["shops"][shop_choice]["price"]:
                player.inventory.append(city["shops"][shop_choice]["item"])
                player.gold -= city["shops"][shop_choice]["price"]
                print(f"You bought {city['shops'][shop_choice]['item'].name}")
            else:
                print("Not enough gold.")

        if city["districts"][district_choice] == "Tavern District":
            print("Play a mini game!")
            # Add minigame logic here.
        if city["districts"][district_choice] == "Guildhall":
            for i, quest in enumerate(city["quests"]):
                print(f"{i+1}. {quest['description']}")
            quest_choice = int(input("> ")) -1
            player.quests.append(city["quests"][quest_choice])
            print("Quest accepted")

    except (ValueError, IndexError):
        print("Invalid choice.")

# Character Creation Function
def create_player_character():
    name = input("Enter your name: ")

    races = ["Wilden", "Human", "Elf", "Dwarf"]
    print("Choose your race:")
    for i, race in enumerate(races):
        print(f"{i + 1}. {race}")
    race_choice = int(input("> ")) - 1
    race = races[race_choice]

    classes = ["Wilder", "Warrior", "Mage", "Rogue"]
    print("Choose your class:")
    for i, class_type in enumerate(classes):
        print(f"{i + 1}. {class_type}")
    class_choice = int(input("> ")) - 1
    class_type = classes[class_choice]

    # Generate stats (you can customize this)
    strength = random.randint(8, 18)
    dexterity = random.randint(8, 18)
    constitution = random.randint(8, 18)
    intelligence = random.randint(8, 18)
    wisdom = random.randint(8, 18)
    charisma = random.randint(8, 18)
    hp = constitution * 5  # Example HP calculation

    player = Character(name, race, class_type, strength, dexterity, constitution, intelligence, wisdom, charisma, hp)
    player.abilities.append(Ability("Heal", "Restores HP.", 5, heal))
    player.abilities.append(Ability("Magic Missile", "Deals magic damage.", 8, magic_missile))

    return player

def save_game(player, current_location, world_map, city):
    """Saves the game state to a JSON file."""
    game_data = {
        "player": {
            "name": player.name,
            "race": player.race,
            "class_type": player.class_type,
            "strength": player.strength,
            "dexterity": player.dexterity,
            "constitution": player.constitution,
            "intelligence": player.intelligence,
            "wisdom": player.wisdom,
            "charisma": player.charisma,
            "hp": player.hp,
            "max_hp": player.max_hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": [item.__dict__ for item in player.inventory],
            "mana": player.mana,
            "abilities": [ability.__dict__ for ability in player.abilities],
            "quests": player.quests,
            "gold": player.gold,
        },
        "current_location": current_location,
        "world_map": world_map,
        "city": city,
    }

    try:
        with open("save_game.json", "w") as f:
            json.dump(game_data, f, indent=4)
        print("Game saved successfully!")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game():
    """Loads the game state from a JSON file."""
    try:
        with open("save_game.json", "r") as f:
            game_data = json.load(f)

        player = Character(
            game_data["player"]["name"],
            game_data["player"]["race"],
            game_data["player"]["class_type"],
            game_data["player"]["strength"],
            game_data["player"]["dexterity"],
            game_data["player"]["constitution"],
            game_data["player"]["intelligence"],
            game_data["player"]["wisdom"],
            game_data["player"]["charisma"],
            game_data["player"]["hp"],
            game_data["player"]["level"],
            game_data["player"]["xp"],
            game_data["player"]["mana"],
            game_data["player"]["gold"]
        )

        player.inventory = [Item(**item_data) for item_data in game_data["player"]["inventory"]]
        player.abilities = [Ability(**ability_data) for ability_data in game_data["player"]["abilities"]]
        player.quests = game_data["player"]["quests"]

        current_location = tuple(game_data["current_location"])
        world_map = game_data["world_map"]
        city = game_data["city"]

        print("Game loaded successfully!")
        return player, current_location, world_map, city
    except FileNotFoundError:
        print("Save file not found. Starting new game.")
        return None, None, None, None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None, None, None

# Main Game Loop
def main():
    player, current_location_load, world_map_load, city_load = load_game()
    if player is None:
        player = create_player_character()
        current_location = (5,5)
        world_map = [[None for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

        world_map[5][5] = {
            "name": "Grove",
            "description": "A peaceful grove, ancient trees surround you. The air is thick with magic. Suddenly, a dark energy tears through the trees!",
            "connections": {"north": (5, 6), "east": (6, 5), "west": (4, 5), "south": (5,4)},
            "encounters": ["goblin", "orc"],
            "npcs": ["Faelar", "Sylvane"],
            "stability": 0.8,
            "visited": False,
        }
        # ... (Other World Map Locations) ...
        city = generate_city()
    else:
        current_location = current_location_load
        world_map = world_map_load
        city = city_load

    print("Welcome to the Feywild!")
    player.show_stats()
    player.inventory.append(Item("Rusty Sword", "A rusty, old sword."))

    while True:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Interact with NPC")
        print("3. Check Stats")
        print("4. Fight Enemy")
        print("5. Check Quests")
        print("6. Enter City")
        print("7. Save Game")
        print("8. Exit")
        choice = input("> ")

        if choice == "1":
            explore(player)
        elif choice == "2":
            location = world_map[current_location[1]][current_location[0]]
            if location and location["npcs"]:
                npc_name = generate_npc_name()
                interact_npc(player, npc_name)
            else:
                print("There are no npcs here.")
        elif choice == "3":
            player.show_stats()
            print("Inventory:")
            for item in player.inventory:
                print(f"- {item.name}: {item.description}")
        elif choice == "4":
            location = world_map[current_location[1]][current_location[0]]
            if location and location["encounters"]:
                enemy = create_enemy(random.choice(location["encounters"]))
                combat(player, enemy)
            else:
                print("There are no enemies here.")
        elif choice == "5":
            player.show_quests()
        elif choice == "6":
            explore_city(player, city)
        elif choice == "7":
            save_game(player, current_location, world_map, city)
        elif choice == "8":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
