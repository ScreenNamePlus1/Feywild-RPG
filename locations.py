locations = {
    "court_of_seasons": {
        "name": "The Court of Seasons",
        "description": "A grand, ever-shifting palace that reflects the current season. In Summer, it's a sun-drenched garden; in Winter, an ice palace. The air hums with potent magic and political intrigue.",
        "items": ["a seasonal flower", "a court invitation"],
        "exits": {
            "eldertree_forest": "Eldertree Forest",
            "crystal_labyrinth": "Crystal Labyrinth",
            "myth_drannor": "Myth Drannor"
        }
    },
    "eldertree_forest": {
        "name": "The Eldertree Forest",
        "description": "An ancient, primeval forest filled with towering trees, glowing flora, and primal creatures. The air is thick with raw, untamed magic.",
        "items": ["ancient bark", "a primal feather"],
        "exits": {
            "court_of_seasons": "Court of Seasons",
            "crystal_labyrinth": "Crystal Labyrinth",
            "river_of_dreams": "River of Dreams",
            "whispering_glade": "Whispering Glade",
            "ancient_barrow": "Ancient Barrow",
            "wild_hills": "Wild Hills"
        }
    },
    "crystal_labyrinth": {
        "name": "The Crystal Labyrinth",
        "description": "A vast, ever-shifting maze made of shimmering crystal and illusions. It's a place of trials, tests, and hidden rewards.",
        "items": ["a crystal shard", "a map of shifting paths"],
        "exits": {
            "court_of_seasons": "Court of Seasons",
            "eldertree_forest": "Eldertree Forest",
            "shifting_city": "Shifting City",
            "clockwork_city": "Clockwork City",
            "whispering_plains": "Whispering Plains"
        }
    },
    "river_of_dreams": {
        "name": "The River of Dreams",
        "description": "A magical river that flows through the Feywild, carrying dreams, memories, and emotions. Its waters shimmer with ethereal light.",
        "items": ["a dream-woven thread", "a memory stone"],
        "exits": {
            "eldertree_forest": "Eldertree Forest",
            "shifting_city": "Shifting City",
            "glowing_fen": "Glowing Fen"
        }
    },
    "shifting_city": {
        "name": "The Shifting City",
        "description": "A city of constant change, with buildings that morph and streets that lead to unexpected places. Its inhabitants are as unpredictable as the city itself.",
        "items": ["a shifting ornament", "a map of the city's current layout"],
        "exits": {
            "crystal_labyrinth": "Crystal Labyrinth",
            "river_of_dreams": "River of Dreams",
            "glowing_fen": "Glowing Fen"
        }
    },
    "whispering_glade":{
        "name": "The Whispering Glade",
        "description": "a small clearing within the Eldertree forest, where the trees seem to whisper secrets.",
        "items": ["a whispering leaf"],
        "exits": {
            "eldertree_forest": "Eldertree Forest"
        }
    },
    "ancient_barrow":{
        "name": "The Ancient Barrow",
        "description": "an ancient burial mound within the Eldertree forest, where ancient fey spirits are said to linger.",
        "items": ["an ancient bone"],
        "exits": {
            "eldertree_forest": "Eldertree Forest"
        }
    },
    "glowing_fen": {
        "name": "The Glowing Fen",
        "description": "A swampy area filled with bioluminescent flora and strange, croaking sounds. The air is thick with mist and the scent of damp earth.",
        "items": ["glowing reeds", "a waterlogged journal"],
        "exits": {"wild_hills": "Wild Hills", "shifting_city": "Shifting City", "river_of_dreams": "River of Dreams"},
    },
    "wild_hills": {
        "name": "The Wild Hills",
        "description": "Rolling hills covered in vibrant wildflowers and ancient standing stones. The wind carries whispers of forgotten songs.",
        "items": ["a handful of wildflowers", "a smooth, grey stone"],
        "exits": {"glowing_fen": "Glowing Fen", "eldertree_forest": "Eldertree Forest", "clockwork_city": "Clockwork City"},
    },
    "whispering_plains":{
        "name": "The Whispering Plains",
        "description": "A vast, open plain where tall, golden grass sways in the wind. Faint, ethereal whispers seem to emanate from the ground itself.",
        "items": ["a golden grass stalk", "a small, smooth stone"],
        "exits": {"glimmering_bazaar": "Glimmering Bazaar", "crystal_labyrinth": "Crystal Labyrinth"}
    },
    "myth_drannor": {
        "name": "Myth Drannor",
        "description": "A city of ancient eladrin magic, its towers shimmering with arcane energy. The air is filled with the sound of music and the scent of exotic flowers.",
        "items": ["an eladrin artifact", "a magical scroll"],
        "exits": {"court_of_seasons": "Court of Seasons", "glowing_fen": "Glowing Fen"},
    },
    "glimmering_bazaar": {
        "name": "The Glimmering Bazaar",
        "description": "A bustling marketplace where faeries and other Feywild creatures trade strange and wondrous goods. The air is alive with the chatter of merchants and the scent of exotic spices.",
        "items": ["a shimmering silk scarf", "a bottle of starlight"],
        "exits": {"whispering_plains": "Whispering Plains"},
    },
    "clockwork_city": {
        "name": "Clockwork City",
        "description": "A city built with intricate clockwork mechanisms, and full of gnome contraptions. The city is full of the sounds of gears, and steam.",
        "items": ["a clockwork gear", "a blueprint"],
        "exits": {"crystal_labyrinth": "Crystal Labyrinth", "wild_hills": "Wild Hills"}
    }
}

