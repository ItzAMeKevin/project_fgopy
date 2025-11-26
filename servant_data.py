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
        {
            "name": "Arondight",
            "type": "Longsword",
            "description": "A divine sword of unmatched purity, enhancing its wielder’s icy might.",
            "effects": [
                "+1 AC while wearing Heavy Armor",
                "+5 ft movement speed",
                "+2 cold damage when hitting a target affected by Freeze"
            ],
            "effects_data": [
                {"id": "ac_bonus_heavy", "value": 1},
                {"id": "speed_bonus", "value": 5},
                {"id": "cold_damage_vs_freeze", "value": 2}
            ]
        },

        {
            "name": "Knight of Owner",
            "type": "Enchantment",
            "description": "Proof of Lancelot’s unmatched mastery.",
            "effects": [],
            "effects_data": []
        }
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
        {
            "name": "Frostbite Slash",
            "action_type": "Attack Action",
            "prerequisite": "Arondight",
            "description": (
                "You channel the chilling essence of Arondight into a single decisive strike. "
                "A pale mist trails the blade as frost blooms across your target on impact."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose <b>one</b> weapon attack you make this turn.",
                "On hit, the attack applies <b>Freeze (potency 1, duration 1)</b>.",
                "If the target is already afflicted with Freeze, the attack instead deals <b>+2 cold damage</b>.",
                "Only one attack can benefit from this feature per turn."
            ],
            "tags": ["Freeze", "Cold", "Single-Hit"]
        },
        {
            "name": "Glacial Sever",
            "action_type": "Attack Action",
            "prerequisite": "Frostbite Slash",
            "description": (
                "Arondight erupts in a surge of biting cold that crawls up your enemy’s limbs. "
                "The impact sends a shock of frost deep into their body, slowing them to a standstill."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose <b>one</b> weapon attack you make this turn.",
                "The attack deals <b>+2d6 cold damage</b> if the target is afflicted with Freeze.",
                "If the target has Freeze at <b>maximum potency</b>, its speed becomes <b>0</b> "
                "until the end of its next turn.",
                "Only one attack can be designated for this feature per turn."
            ],
            "tags": ["Cold", "Control", "Single-Hit"]
        },
        {
            "name": "Radiant Guard",
            "action_type": "Reaction",
            "prerequisite": "Arondight",
            "description": (
                "A shimmer of argent light erupts from Arondight as you brace for impact. "
                "The holy radiance hardens your stance and lashes out with freezing judgment."
            ),
            "effects": [
                "<b>Trigger:</b> A creature within 5 feet hits you with a melee attack.",
                "You gain <b>resistance to radiant or cold damage</b> until the end of the current turn.",
                "The attacker becomes afflicted with <b>Freeze (potency 1, duration 1)</b>."
            ],
            "tags": ["Defense", "Reaction", "Freeze"]
        },
        {
            "name": "Shining Reversal",
            "action_type": "Bonus Action",
            "prerequisite": "Radiant Guard",
            "description": (
                "A flash of sacred light courses through Arondight as you turn defense into retaliation. "
                "The blade strikes back with dazzling precision, empowered by divine brilliance."
            ),
            "effects": [
                "<b>Trigger:</b> You used Radiant Guard since the end of your last turn.",
                "Make <b>one weapon attack</b> as a Bonus Action.",
                "If the target is afflicted with Freeze, the attack deals <b>+1d6 radiant damage</b>."
            ],
            "tags": ["Radiant", "Bonus Action", "Offense"]
        },
        {
            "name": "Flashfreeze Step",
            "action_type": "Bonus Action",
            "prerequisite": "Arondight",
            "description": (
                "Cold air spirals beneath your feet as your form blurs with supernatural speed. "
                "Your weapon strike triggers a burst of frost that propels you across the battlefield."
            ),
            "effects": [
                "<b>Trigger:</b> You take this ability as a Bonus Action.",
                "The <b>first time</b> you hit a creature with a weapon attack this turn:",
                "- You may move <b>10 feet</b> without provoking opportunity attacks.",
                "- If the creature is afflicted with Freeze, you may instead move <b>15 feet</b>.",
                "- You may apply <b>Freeze (potency 1, duration 1)</b> to that creature.",
                "Only the first hit can trigger this effect."
            ],
            "tags": ["Mobility", "Freeze", "Bonus Action"]
        },
        {
            "name": "Tempest Break",
            "action_type": "Attack Action",
            "prerequisite": "Flashfreeze Step",
            "description": (
                "You gather Arondight’s frosted power into a devastating burst. "
                "The blade crashes down with explosive force, releasing a shockwave of piercing cold "
                "that ripples through nearby foes."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make a single, empowered weapon attack.",
                "On hit, the target takes <b>+2d6 cold damage</b>.",
                "Creatures within 5 feet take <b>1d6 cold damage</b>.",
                "If the target is afflicted with Freeze:",
                "- Remove Freeze.",
                "- The target takes an additional <b>+2d6 cold damage</b>.",
                "All creatures damaged by this effect become afflicted with <b>Freeze</b> "
                "(potency 1, duration 1)."
            ],
            "tags": ["Cold", "AoE", "Freeze", "Detonation"]
        }
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
