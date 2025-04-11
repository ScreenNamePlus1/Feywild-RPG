# npcs.py

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

def generate_npc_personality(name, species, traits):
    prompt = f"Generate a personality description for {name}, a {species}, with the following traits: {traits}. Keep it to 2-3 sentences."
    return generate_text_local(prompt)

fey_names = ["Sylvanius", "Lirien", "Oberon", "Titania", "Puck"]
fey_species = ["Pixie", "Satyr", "Dryad", "Sprite", "Redcap"]

def generate_npc():
    name = random.choice(fey_names)
    species = random.choice(fey_species)
    traits = ", ".join(random.sample(["friendly", "mischievous", "wise", "mysterious", "greedy"], 3))
    return f"{name} the {species}: {generate_npc_personality(name, species, traits)}"

def interact_with_npc():
    print(generate_npc())
