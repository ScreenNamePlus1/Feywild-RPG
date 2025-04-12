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
