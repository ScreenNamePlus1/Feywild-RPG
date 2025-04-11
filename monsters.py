# monsters.py

import random
from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

def generate_text_local(prompt, max_length=100):
    try:
        output = generator(prompt, max_length=max_length)
        return output[0]["generated_text"].strip()
    except Exception as e:
        print(f"Generation error: {e}")
        return "..."

def generate_monster_description(name, habitat, abilities):
    prompt = f"Generate a description for a monster called {name} that lives in {habitat} and has the following abilities: {abilities}. Keep it to 2-3 sentences."
    return generate_text_local(prompt)

monster_names = ["Gloomwing", "Thornbeast", "Mistwraith", "Shadowstalker", "Sparkfang"]
monster_habitats = ["a dark forest", "a thorny thicket", "a misty swamp", "shadowy caves", "volcanic caverns"]
monster_abilities = ["shadow manipulation", "poisonous thorns", "illusionary mists", "fiery breath", "teleportation"]

def generate_monster():
    name = random.choice(monster_names)
    habitat = random.choice(monster_habitats)
    abilities = ", ".join(random.sample(monster_abilities, 2))
    return f"{name}: {generate_monster_description(name, habitat, abilities)}"

def encounter_monster():
    print(generate_monster())
