import os

ASSETS_DIR = "images"

CARD_IMG_W = 256
CARD_IMG_H = 362

FULL_IMG_W = 512
FULL_IMG_H = 724

CHARACTERS = {
    "Knights of the Round Table": [
        {"name": "Lancelot", "image": os.path.join(ASSETS_DIR, "lancelot.jpg")},
        {"name": "Gawain",   "image": os.path.join(ASSETS_DIR, "gawain.jpg")},
        {"name": "Mordred", "image": os.path.join(ASSETS_DIR, "mordred.jpg")},
    ],

    "Shinsengumi": [
        {"name": "Okita Souji", "image": os.path.join(ASSETS_DIR, "okita.jpg")},
        {"name": "Saito Hajime", "image": os.path.join(ASSETS_DIR, "hajime.jpg")},
        {"name": "Nagakura Shinpachi", "image": os.path.join(ASSETS_DIR, "shinpachi.jpg")},
    ],

    "Argonauts": [
        {"name": "Heracles", "image": os.path.join(ASSETS_DIR, "heracles.jpg")},
        {"name": "Caenis", "image": os.path.join(ASSETS_DIR, "caenis.jpg")},
        {"name": "Atalanta", "image": os.path.join(ASSETS_DIR, "atalanta.jpg")},
    ],
}

# Armament sets per character
CHAR_ARMAMENTS = {
    "Lancelot": [
        {"name": "Arondight", "description": "Legendary sword.", "type": "Longsword"},
        {"name": "Knight of Owner", "description": "Proof of mastery.", "type": "Enchantment"},
    ],

    "Gawain": [
        {"name": "Excalibur Galatine", "description": "Holy sword of light.", "type": "Broadsword"},
        {"name": "Sunlight Sword", "description": "Radiant blade.", "type": "Sword"},
    ],

    "Mordred": [
        {"name": "Clarent", "description": "Sword of betrayal.", "type": "Sword"},
        {"name": "Clarent Blood Arthur", "description": "Cursed version of Clarent.", "type": "Cursed Sword"},
    ],

    "Okita Souji": [
        {"name": "Coat of Oaths", "description": "Symbol of her honor.", "type": "Clothing"},
        {"name": "Iaijutsu", "description": "Assassin techniques.", "type": "Ability"},
    ],

    "Saito Hajime": [
        {"name": "Gatotsu", "description": "Piercing thrust.", "type": "Sword Technique"},
        {"name": "Silent Blade", "description": "Stealth attack.", "type": "Ability"},
    ],

    "Nagakura Shinpachi": [
        {"name": "Twin Swords", "description": "Dual wielding katanas.", "type": "Katanas"},
        {"name": "Swift Strike of the Iron Valley in the Mountain Beast Lord's Domain this is just a long text to test it out.", "description": "Quick attack.", "type": "Ability"},
    ],

    "Heracles": [
        {"name": "God's Hand", "description": "Description.", "type": "Ability"},
        {"name": "Nine Lives", "description": "Description.", "type": "Ability"},
    ],
    
    "Caenis": [
        {"name": "Divine Lance", "description": "Sacred spear.", "type": "Spear"},
        {"name": "Transformation", "description": "Description.", "type": "Ability"},
    ],

    "Atalanta": [
        {"name": "Hunting Bow", "description": "Bow of the huntress.", "type": "Bow"},
        {"name": "Wild Instinct", "description": "Description.", "type": "Ability"},
    ],
}

ARMAMENT_SKILLS = {
    "Arondight": [
        {"name": "Lightning Strike", "description": "Lightning based slash.", "prerequisite": "Arondight"},
        {"name": "Unyielding Blade", "description": "Increases wielder's defense.", "prerequisite": "Lightning Strike"},
        {"name": "Freezing Strike", "description": "Cold based slash.", "prerequisite": "Arondight"},
        {"name": "Glacial Edge", "description": "Slows enemies on hit.", "prerequisite": "Freezing Strike"},
        {"name": "Blazing Strike", "description": "Fire based slash.", "prerequisite": "Arondight"},
        {"name": "Flameburst", "description": "Burns enemies on hit.", "prerequisite": "Blazing Strike"},
    ],
    "Knight of Owner": [
        {"name": "Master's Command", "description": "Boosts allies' morale.", "prerequisite": "Knight of Owner"},
        {"name": "Loyal Protector", "description": "Reduces damage taken by allies.", "prerequisite": "Master's Command"},
    ],

    "Excalibur Galatine": [
        {"name": "Holy Slash", "description": "Sacred sword attack.", "prerequisite": "Excalibur Galatine"},
        {"name": "Divine Shield", "description": "Increases defense against dark forces.", "prerequisite": "Holy Slash"},
    ],
    "Sunlight Sword": [
        {"name": "Radiant Strike", "description": "Blinding sword attack.", "prerequisite": "Sunlight Sword"},
        {"name": "Solar Flare", "description": "Stuns enemies on hit.", "prerequisite": "Radiant Strike"},
    ],
}
