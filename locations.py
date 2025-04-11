# Feywild-RPG: A Text-Based Adventure with Enhanced Terminal Interaction

Embark on a captivating journey into the Feywild, a realm of magic, mystery, and unpredictable creatures. This text-based adventure game combines engaging exploration, dynamic NPC interactions, and thrilling monster encounters, all enhanced by a custom terminal interface and modular design.

## Features

* **Exploration:** Traverse diverse locations, each with unique descriptions, items, and exits.
* **NPC Interactions:** Engage with procedurally generated fey creatures, each with distinct personalities.
* **Monster Encounters:** Battle a variety of monsters, each with unique abilities and descriptions.
* **Local Text Generation:** Uses DistilGPT-2 for dynamic NPC and monster descriptions.
* **Enhanced Terminal Interface:** Utilizes a custom terminal module for improved user experience.
* **Modular Design:** Organized into separate modules for locations, items, NPCs, monsters, and game logic.

## Project Structure

* `feywild_rpg.py`: Main game file, integrating all modules and handling game logic.
* `locations.py`: Defines locations, their descriptions, items, and exits.
* `items.py`: Defines items and their properties.
* `npcs.py`: Generates and manages NPC interactions.
* `monsters.py`: Generates and manages monster encounters.
* `terminal_utils.py`: Provides enhanced terminal functions for improved user experience.
* `utils.py`: contains helper functions.
* `README.md`: Project documentation.
* `LICENSE`: MIT License file.

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/ScreenNamePlus1/Feywild-RPG.git](https://github.com/ScreenNamePlus1/Feywild-RPG.git)
    ```

2.  **Navigate to the Project Directory:**

    ```bash
    cd Feywild-RPG
    ```

3.  **Install Dependencies:**

    ```bash
    pip install transformers
    ```

## Usage

1.  **Run the Game:**

    ```bash
    python feywild_rpg.py
    ```

2.  **Interact with the Game:**

    * Follow the on-screen prompts to navigate and interact with the Feywild.
    * Use the commands listed below to explore, talk, and fight.

## Commands

* `move [direction]`: Move to a different location. Example: `move north`.
* `talk`: Interact with a randomly generated NPC.
* `fight`: Encounter a randomly generated monster.
* `quit`: Exit the game.

## Module Descriptions

* **`locations.py`:**
    * Defines the game's locations as dictionaries, including their names, descriptions, items, and exits.
    * Allows for easy expansion and modification of the game world.
* **`items.py`:**
    * Defines items with their properties, such as names and descriptions.
    * Provides a structured way to manage in-game items.
* **`npcs.py`:**
    * Generates NPCs with random names, species, and personality traits.
    * Uses the `transformers` library to generate dynamic NPC descriptions.
* **`monsters.py`:**
    * Generates monsters with random names, habitats, and abilities.
    * Uses the `transformers` library to generate dynamic monster descriptions.
* **`terminal_utils.py`:**
    * Provides functions for clearing the terminal, displaying text with delays, and other terminal enhancements.
    * Improves the user experience by adding visual effects and interactivity.
* **`utils.py`:**
    * Contains helper functions that are used by various modules.

## Notes

* This game uses a local language model (DistilGPT-2) for text generation. The quality of the generated text may vary.
* Performance may be slow on resource-constrained devices.
* This game is under active development.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
