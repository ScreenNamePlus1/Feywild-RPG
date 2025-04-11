it's a work in progress so don't expect it to be bug free yet. 
I just started. I am eventually going to put every single Monster in D&D 3.5 in this game. if it takes me another 40 years I'm going to do it. I'm also going to include a bunch of other stuff for combat and cities. the point of this is to be able to interact with miniatures. I'm sure they'll think of some interesting features. if you have any suggestions drop me a line at screennameplus1@gmail.com. I will probably definitely add them.
this is based on D&D 3.5 and it is set in the Feywild.
Here's a description of the Feywild text-based RPG 
we've been building: 
Feywild: A Text-Based Adventure "Feywild" 
is a text-based RPG set in the vibrant, yet perilous, realm of 
the Feywild, the land above the shadowy Underdark. Players take 
on the role of a Wilden Wilder, a humanoid deeply connected to 
the plant life of this magical realm, who is thrust into a 
desperate struggle for survival.Setting: The game unfolds in a 
lush, ancient grove, a sanctuary on the edge of the Feywild, 
bordering the sinister influence of the Underdark. 
This once-peaceful haven is shattered by a sudden, brutal 
invasion by corrupted Drow forces, their minds and bodies 
twisted by a dark, otherworldly energy. The Feywild's natural 
beauty is rapidly succumbing to this encroaching corruption, 
turning it into a twisted reflection of its former self.
Gameplay:
Players navigate the Feywild using text commands, exploring 
locations described in vivid detail. They'll encounter a variety 
of creatures, both friendly and hostile, and interact with 
randomly generated NPCs, each with their own stories and 
motivations. The game features turn-based combat, where players 
can use both traditional attacks and magical abilities, fueled by 
mana, to overcome their foes.
Key Features:
 * Exploration: Discover diverse locations within the Feywild,
   from ancient groves to corrupted ruins.
 * Combat: Engage in tactical turn-based combat against corrupted
   creatures and Drow invaders.
 * NPC Interaction: Meet and interact with randomly generated NPCs,
   each with unique dialogue and potential quests.
 * Abilities and Spells: Harness the magic of the Feywild with a
   variety of abilities and spells.
 * Inventory: Manage your items and equipment.
 * Leveling and Progression: Gain experience, level up, and improve
   your character's abilities.
 * Random Quests: Undertake procedurally generated quests to earn
   rewards and explore the world.
 * Main Storyline: Unravel the mystery behind the Drow invasion and
   fight to save the Feywild from corruption.
 * City Exploration: Travel to randomly generated cities, and explore
   the districts within.
Story:
The game begins with the player character, a Wilden Wilder, living in
a secluded, ancient grove. The sudden invasion forces them to flee,
witnessing the horrifying corruption of the Feywild firsthand. As they
journey through the land, they encounter other refugees and resistance
fighters, learning the true nature of the invaders and their dark purpose.
The player must gather allies, master their abilities, and fight to protect
the Feywild from the encroaching darkness.
Theme:
"Feywild" explores themes of environmental invasion, the struggle for survival, and
the power of hope in the face of overwhelming darkness.
It captures the whimsical and dangerous nature of the Feywild, where the lines between
reality and illusion are blurred, and where the fate of the land rests on the shoulders
of those who dare to resist.

Friday, April 11th, 2025

# Feywild-RPG

A text-based RPG set in the magical and unpredictable Feywild.

## Running the Game

There are now two ways to run the game:

* **Original Version:**
    ```bash
    python feywild_rpg.py
    ```
* **Console Version (In-Game Code Execution):**
    ```bash
    python feywild_rpg_console.py
    ```

## In-Game Console

The console version of the game allows you to execute Python code directly within the game. This opens up possibilities for customizing your gameplay and experimenting with the game world.

### Example Usage:

* To add an item to your inventory:
    ```
    > game['add_item']('Feywild Flower')
    ```
* To decrease your player health:
    ```
    > game['player_health'] -= 10
    ```

## File Structure:

* `feywild_rpg.py`: The original game logic.
* `feywild_rpg_console.py`: The launcher for the console version.
* `game_data.py`: Contains game state and data.
* `console.py`: Contains the in-game code execution logic.
* `game_logic.py`: Contains the main game loop and input handling for the console version.


Differences between both modes:

1. feywild_rpg.py (Main Game File):
 * Intended Functionality:
   * This file is designed to be the main game entry point.
   * It integrates all the game modules (locations, NPCs, monsters, etc.) and handles the core game logic.
   * It is designed to be expanded to have a richer user interface, possibly a graphical user interface in the future.
   * It is currently a text based interface, but is not designed to be a dedicated console application.
 * Code Execution (Security Risk):
   * As we discussed, the original version of this file included the execute_player_code function, which allowed players to execute arbitrary Python code.
   * This is a major security risk and should be removed or replaced with proper sandboxing.
 * Game Loop:
   * It contains the main game loop, which handles player input, updates the game state, and displays game information.
 * Module Integration:
   * It imports and uses the other game modules to create the game world and its interactions.
2. feywild_rpg_console.py (Console Version):
 * Intended Functionality:
   * This file is specifically designed to provide a text-based console interface for the game.
   * It's a simplified version of the game that focuses on command-line interaction.
   * It is designed to be a dedicated console application.
 * Simplified Game Loop:
   * It contains a basic while loop that prompts the user for input and calls the handle_input function from game_logic.py.
 * game_logic.py Dependency:
   * It relies on the game_logic.py module to handle the actual game logic, separating the console interface from the game's core mechanics.
 * Text-Based Interaction:
   * It's designed for players who prefer a text-based experience and want to interact with the game through commands.
In Summary:
 * feywild_rpg.py is the main game file, meant to be more expandable, and to handle all of the game logic.
 * feywild_rpg_console.py is a simplified, console-specific version that provides a text-based interface.
 * Both versions, at this point, are text based, but feywild_rpg.py is designed to be able to be expanded into a more complex application.
 * feywild_rpg_console.py relies on game_logic.py to separate the user interface from the game logic.
Therefore, you would run feywild_rpg_console.py if you want a dedicated command line experience, and run feywild_rpg.py if you want to run the main game file.

