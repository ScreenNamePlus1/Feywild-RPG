# Feywild-RPG

A text-based role-playing game set in the mystical Feywild.

## Table of Contents

-   [Project Description](#project-description)
-   [Modules](#modules)
-   [Console Usage](#console-usage)
-   [Installation](#installation)
-   [Contributing](#contributing)
-   [License](#license)

## Project Description

Feywild-RPG is a console-based RPG where players explore a magical world, battle creatures, interact with NPCs, and complete quests. The game utilizes a modular design to separate concerns and improve maintainability.

## Modules

### `feywild_rpg_console.py`

* **Purpose:** This is the main script that runs the console version of the game. It handles user input, game logic, and output.
* **Key Functions/Classes:**
    * `main()`: The main game loop.
    * `Character`: Class representing player and enemy characters.
    * `Enemy`: Class representing enemy characters.
    * `Item`: Class representing items.
    * `Ability`: Class representing special abilities.
    * `create_player_character()`: Handles player character creation.
    * `explore()`: Handles world exploration.
    * `combat()`: Handles combat encounters.
    * `interact_npc()`: Handles NPC interactions.
    * `generate_quest()`: Handles quest generation.
    * `generate_city()`: Handles city generation.
    * `explore_city()`: Handles city exploration.
    * `create_enemy()`: Creates enemy objects.
    * `load_monster_data()`: Loads monster data from Json file.
* **Dependencies:** `random`, `json`

### `monsters.json`

* **Purpose:** stores the data for all monsters within the game, including their stats, names, and attacks.

## Console Usage

To run the game, navigate to the project directory in your terminal and execute:

```bash
python feywild_rpg_console.py

# Feywild RPG Console

Welcome to the Feywild RPG Console! This is a text-based adventure where you'll explore the mystical and dangerous Feywild, encounter strange creatures, and undertake epic quests.

## Getting Started

1.  **Run the game:** Execute the `Feywild_rpg_console.py` script using Python.
2.  **Create your character:** Follow the prompts to name your character, choose a race, and select a class.
3.  **Explore the Feywild:** Use the "Explore" option in the main menu to travel to different locations.

## How to Start the Main Quest

To begin the main questline, you'll need to interact with specific NPCs who offer these quests. Here's how:

1.  **Identify Quest-Giving NPCs:**
    * Look for NPCs with important information or quests. In the current game, `Faelar Whisperwind` and `Bram Stoneheart` are known to have quests.

2.  **Locate the NPCs:**
    * Use the in-game map or explore different locations to find these NPCs.
    * `Faelar Whisperwind` is located in the "Grove".
    * `Bram Stoneheart` is located on the "Path".

3.  **Travel to the NPC's Location:**
    * Use the "Explore" option (option 1) to navigate to the location where the NPC is.
    * Follow the on-screen prompts and use the provided connections to move between locations.

4.  **Interact with the NPC:**
    * Once you're in the same location as the NPC, use the "Interact with NPC" option (option 2) in the main menu.
    * **Note:** The game randomly selects an NPC from the location's list. You might need to try interacting multiple times to find the specific NPC.

5.  **Accept the Quest:**
    * The NPC will present the quest information.
    * Type "yes" and press enter to accept the quest.

## Example: Starting "The Corrupted Grove" Quest

1.  Start the game.
2.  Select "Explore" (option 1).
3.  You begin in the "Grove" (5, 5), where Faelar is.
4.  Select "Interact with NPC" (option 2).
5.  Faelar will talk to you and offer the "The Corrupted Grove" quest.
6.  Type "yes" and press Enter to accept the quest.

## Additional Tips

* Explore thoroughly and talk to all the NPCs you encounter.
* Pay attention to the in-game descriptions and hints.
* Be prepared for combat!

## Contributing

If you'd like to contribute to the development of this game, please feel free to submit pull requests or open issues on GitHub.

## License

This project is licensed under the [Your License] License.

