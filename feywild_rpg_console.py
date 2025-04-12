import random
import json

# Character and Enemy Stats
class Character:
    def __init__(self, name, race, class_type, strength, dexterity, constitution, intelligence, wisdom, charisma, hp, level=1, xp=0, mana=20):
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
        print(f"HP: {self.hp}/{self.max_hp}, Level: {self.level}, XP: {self.xp}")
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

class Enemy(Character):
    def __init__(self, name, hit_dice, armor_class, attack_bonus, damage, experience):
        num_dice, die_size = map(int, hit_dice.split('d'))
        hp = random.randint(num_dice, num_dice * die_size)
        super().__init__(name, "Enemy", "Monster", 10, 10, 10, 10, 10, 10, hp)
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

# Game World and Navigation
world_map = {
    "Grove": {
        "description": "A peaceful grove, ancient trees surround you. The air is thick with magic. Suddenly, a dark energy tears through the trees!",
        "north": "Thicket",
        "east": "Path",
        "west": "Dark Grove",
        "encounters": ["goblin", "orc"],
        "npcs": ["Faelar", "Sylvane"]
    },
    "Thicket": {
        "description": "A dense thicket, thorns and vines block your path. The light is dim.",
        "south": "Grove",
        "east": "Ruins",
        "encounters": ["goblin"],
        "npcs": []
    },
    "Path": {
        "description": "A winding path, leading through the forest. The sounds of nature fill the air.",
        "west": "Grove",
        "east": "Meadow",
        "encounters": ["orc"],
        "npcs": ["Bram"]
    },
    "Dark Grove": {
        "description": "A dark grove, the trees here are twisted and corrupted. A sense of dread fills you.",
        "east": "Grove",
        "encounters": ["goblin", "orc"],
        "npcs": []
    },
    "Ruins": {
        "description": "Ancient ruins, overgrown with vines. The stones whisper of forgotten magic.",
        "west": "Thicket",
        "south": "Meadow",
        "encounters": ["orc"],
        "npcs": []
    },
    "Meadow": {
        "description": "A wide open meadow, with tall waving grasses, and flowers that glow with a faint light.",
        "north": "Ruins",
        "west": "Path",
        "encounters": ["goblin"],
        "npcs": []
    }
}

current_location = "Grove"

# NPC Names
first_names = ["Faelar", "Sylvane", "Bram", "Lyra", "Kaelen", "Nimue", "Torvin", "Anya", "Rylan", "Elara"]
last_names = ["Whisperwind", "Shadowbrook", "Stoneheart", "Silverleaf", "Nightshade", "Sunstrider", "Ironbark", "Moonwhisper", "Thornwood", "Emberglow"]

def generate_npc_name():
    return random.choice(first_names) + " " + random.choice(last_names)

def explore(player):
    global current_location
    location = world_map[current_location]
    print(location["description"])

    directions = [d for d in ["north", "east", "west", "south"] if d in location]

    if directions:
        for i, direction in enumerate(directions):
            print(f"{i + 1}. Go {direction.capitalize()}.")
        choice = input("> ")
        try:
            direction_choice = directions[int(choice) - 1]
            current_location = location[direction_choice]
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
    while player.is_alive() and enemy.is_alive():
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

    if not player.is_alive():
        print("You have been defeated!")

# NPC Interaction
npc_dialogue = {
    "Faelar Whisperwind": ["Greetings, traveler. The forest is restless.", "Have you seen any strange creatures lately?", "Be careful on the path."],
    "Sylvane Shadowbrook": ["The whispers of the trees grow louder.", "The ancient grove is in danger.", "We must protect the feywild."],
    "Bram Stoneheart": ["I've seen dark things in the shadows.", "The old ruins are not safe.", "Stay away from the dark grove."],
    "Lyra Silverleaf": ["The flowers are dying, and the trees are weeping.", "The dark energy is spreading.", "We need help."],
    "Kaelen Nightshade": ["I used to be a guardian, but now I'm lost.", "The corruption has taken everything.", "Leave while you can."],
    "Nimue Sunstrider": ["Hope is not lost, traveler. We can still fight.", "The ancient magic still lives.", "Join us."],
    "Torvin Ironbark": ["The earth trembles, and the shadows grow long.", "We must stand together.", "Are you with us?"],
    "Anya Moonwhisper": ["The stars weep for the feywild.", "The darkness threatens to consume us all.", "Find the light."],
    "Rylan Thornwood": ["I know the secrets of these woods.", "The Drow are not the only threat.", "There is something worse."],
    "Elara Emberglow": ["The fire of the feywild still burns.", "We will not surrender.", "Fight with us."]
}

def interact_npc(player, npc_name):
    print(f"You meet {npc_name}.")
    if npc_name in npc_dialogue:
        for line in npc_dialogue[npc_name]:
            print(f"{npc_name}: '{line}'")
        print("1. Talk again.")
        print("2. Leave.")
        choice = input("> ")
        if choice == "1":
            print(random.choice(npc_dialogue[npc_name]))
        else:
            print("You move on.")
    else:
        print(f"{npc_name}: 'I have nothing to say to you.'")

# Random Quest Generation
def generate_quest():
    quest_types = ["Retrieve", "Slay", "Explore"]
    quest_type = random.choice(quest_types)
    if quest_type == "Retrieve":
        item = random.choice(["Enchanted Flower", "Ancient Stone", "Lost Scroll"])
        return f"Retrieve the {item}."
    elif quest_type == "Slay":
        monster = random.choice(["goblin", "orc"])
        return f"Slay the {monster}."
    elif quest_type == "Explore":
        location = random.choice(["Whispering Caves", "Forgotten Ruins", "Haunted Meadow"])
        return f"Explore the {location}."

# City Generation
city_names = ["Silverwood", "Gloomhaven", "Emberfall", "Whisperwind City", "Stonecrest"]
city_districts = ["Market Square", "Tavern District", "Temple District", "Guildhall", "Residential Area", "Docks"]

def generate_city():
    city = {
        "name": random.choice(city_names),
        "description": f"A bustling city of {random.randint(500, 5000)} inhabitants.",
        "districts": random.sample(city_districts, random.randint(3, 5)),
        "npcs": [generate_npc_name() for _ in range(random.randint(3, 6))],
        "shops": [],
        "quests": []
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
        # Add district interaction logic here
    except (ValueError, IndexError):
        print("Invalid choice.")

# Main Game Loop
def main():
    player_name = input("Enter your name: ")
    player = Character(player_name, "Wilden", "Wilder", 16, 14, 15, 12, 13, 10, 50)
    player.abilities.append(Ability("Heal", "Restores HP.", 5, heal))
    player.abilities.append(Ability("Magic Missile", "Deals magic damage.", 8, magic_missile))

    print("Welcome to the Feywild!")
    player.show_stats()
    player.inventory.append(Item("Rusty Sword", "A rusty, old sword."))

    city = generate_city()

    while True:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Interact with NPC")
        print("3. Check Stats")
        print("4. Fight Enemy")
        print("5. Get Quest")
        print("6. Exit")
        print("7. Enter City")
        choice = input("> ")

        if choice == "1":
            explore(player)
        elif choice == "2":
            location = world_map[current_location]
            if location["npcs"]:
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
            enemy = create_enemy(random.choice(["goblin", "orc"]))
            combat(player, enemy)
        elif choice == "5":
            print(generate_quest())
        elif choice == "6":
            break
        elif choice == "7":
            explore_city(player, city)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()