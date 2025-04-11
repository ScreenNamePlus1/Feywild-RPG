import random
from transformers import pipeline

# Load the DistilGPT-2 pipeline for text generation
generator = pipeline('text-generation', model='distilgpt2')

def generate_npc():
    """Generates a random NPC with name, species, and description."""

    names = ["Elara", "Finn", "Lyra", "Orion", "Sylas"]
    species = ["Pixie", "Eladrin", "Gnome", "Satyr", "Dryad"]
    personalities = ["curious", "mischievous", "wise", "mysterious", "friendly"]

    name = random.choice(names)
    species_choice = random.choice(species)
    personality = random.choice(personalities)

    prompt = f"A {personality} {species_choice} named {name}."
    description = generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']

    npc = {
        "name": name,
        "species": species_choice,
        "description": description,
    }

    return npc

def interact_with_npc():
    """Generates an NPC and displays their information."""
    npc = generate_npc()
    print(f"\nYou encounter {npc['name']}, a {npc['species']}.")
    print(npc['description'])

# Example of how to use the functions
if __name__ == "__main__":
    interact_with_npc()

