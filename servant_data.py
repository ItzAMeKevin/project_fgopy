import os

ASSETS_DIR = "images"

CARD_IMG_W = 256
CARD_IMG_H = 362

FULL_IMG_W = 512
FULL_IMG_H = 724

CHARACTERS = {
    "Knights of the Round Table": [
        {"name": "Lancelot", "image": os.path.join(ASSETS_DIR, "lancelot_saber.jpg")},
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
            "description": (
                "A divine blade of immaculate purity, its frosted edge channels the chill of a perfect "
                "strike and empowers the knight who bears it."
            ),
            "effects": [
                "<b>Grace of the Unburdened Knight:</b> You gain a <b>+1 bonus to AC</b> while you are not "
                "wearing Heavy Armor.",
                
                "<b>Chilled Momentum:</b> Your movement speed increases by <b>5 feet</b>.",
                
                "<b>Frostbrand Edge:</b> When you hit a creature affected by Freeze, your attack deals "
                "<b>+2 cold damage</b>."
            ],
            "effects_data": [
                {"id": "ac_bonus_no_heavy", "value": 1},
                {"id": "speed_bonus", "value": 5},
                {"id": "cold_damage_vs_freeze", "value": 2}
            ]
        },
        {
            "name": "Knight of Owner",
            "type": "Enchantment",
            "description": (
                "A chaotic manifestation of Lancelot’s frenzied mastery—where any object becomes a lethal "
                "weapon and momentum turns into unstoppable aggression."
            ),
            "effects": [
                "<b>Improvised Armament Mastery:</b> You are proficient with all improvised weapons, which "
                "count as martial weapons for you. Improvised weapons you wield deal <b>1d6 damage</b>.",
                
                "<b>Momentum Overload:</b> If you hit a creature more than once on your turn, you gain a "
                "<b>+1 bonus to damage rolls</b> until the end of your next turn (maximum +3).",
                
                "<b>Unbroken Assault:</b> Once per turn, when you reduce a creature to 0 HP, you may move "
                "up to <b>10 feet</b> without provoking opportunity attacks."
            ],
            "effects_data": [
                {"id": "improvised_weapon_damage", "value": "1d6"},
                {"id": "momentum_max_bonus", "value": 3},
                {"id": "unbroken_assault_move", "value": 10}
            ]
        }
    ],

    "Gawain": [
        {
            "name": "Excalibur Galatine",
            "type": "Greatsword",
            "description": (
                "The sword of the sun, a radiant sister-blade to Excalibur. Galatine channels the light of "
                "the heavens into overwhelming solar might, burning away darkness with sacred brilliance."
            ),
            "effects": [
                "<b>Solar Edge:</b> Your weapon attacks deal <b>+2 radiant damage</b>.",
                
                "<b>Blazing Momentum:</b> When you hit a creature with a weapon attack on your turn, you "
                "gain a <b>+1 bonus to the next damage roll you make</b> before the end of your next turn "
                "(maximum +3).",
                
                "<b>Noon Ascendant:</b> While you are in bright light, your movement speed increases by "
                "<b>5 feet</b>."
            ],
            "effects_data": [
                {"id": "radiant_damage_bonus", "value": 2},
                {"id": "momentum_bonus_max", "value": 3},
                {"id": "bright_light_speed_bonus", "value": 5}
            ]
        },
        {
            "name": "Aegis Solaria",
            "type": "Mantle",
            "description": (
                "A radiant mantle woven from the blessing of the sun itself. Its shining threads shield the "
                "noble knight with solar grace, empowering his endurance and illuminating the battlefield "
                "with holy brilliance."
            ),
            "effects": [
                "<b>Solar Resilience:</b> You gain <b>resistance to radiant damage</b>.",
                
                "<b>Sunlit Ward:</b> While you are in bright light, you gain a <b>+1 bonus to AC</b>.",
                
                "<b>Dawnflare Presence:</b> When a creature starts its turn within 5 feet of you and you "
                "are in bright light, it takes <b>1 radiant damage</b>."
            ],
            "effects_data": [
                {"id": "radiant_resistance", "value": 1},
                {"id": "ac_bonus_bright_light", "value": 1},
                {"id": "aura_radiant_damage", "value": 1}
            ]
        },
    ],

    "Mordred": [
        {
            "name": "Clarent",
            "type": "Greatsword",
            "description": (
                "The Sword of Peace, twisted and tainted by Mordred’s resentment. Its corrupted edge crackles "
                "with volatile lightning and burning fury, reflecting her rebellious spirit and explosive might."
            ),
            "effects": [
                "<b>Rebel’s Edge:</b> Your weapon attacks deal <b>+2 lightning damage</b>.",

                "<b>Voltcinder Pulse:</b> When you hit a creature afflicted with Burn, your attack deals "
                "<b>+2 fire damage</b>.",

                "<b>Unruly Momentum:</b> While you are below half of your maximum hit points, your weapon "
                "attacks deal an additional <b>+1d4 thunder damage</b>."
            ],
            "effects_data": [
                {"id": "lightning_damage_bonus", "value": 2},
                {"id": "fire_bonus_vs_burn", "value": 2},
                {"id": "thunder_bonus_low_hp", "value": "1d4"}
            ]
        },
        {
            "name": "Prydwen",
            "type": "Ride-Armament",
            "description": (
                "A manifested storm-forged mount, taking the form of a magical motorcycle or glider. "
                "Fueled by Mordred’s rebellious spirit, Prydwen channels crackling lightning into "
                "unmatched battlefield mobility and shocking, high-speed assaults."
            ),
            "effects": [
                "<b>Stormspeed Drift:</b> Your movement speed increases by <b>5 feet</b>.",
                
                "<b>Thundertrail Wake:</b> If you move at least 10 feet on your turn, the first creature "
                "you hit with a weapon attack takes <b>+1 lightning damage</b>.",
                
                "<b>Impact Ignition:</b> If you move at least 15 feet before hitting a creature with a "
                "weapon attack, that creature is afflicted with <b>Shock (potency 1, duration 1)</b>. "
                "This can only occur once per turn."
            ],
            "effects_data": [
                {"id": "speed_bonus", "value": 5},
                {"id": "lightning_damage_motion_bonus", "value": 1},
                {"id": "shock_on_motion_hit", "value": 1}
            ]
        },
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
            "incantation": "Let winter claim your weakness… Frostbite Slash!",
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
            "name": "Cryo Blade",
            "action_type": "Attack Action",
            "prerequisite": "Frostbite Slash",
            "description": (
                "Arondight erupts in a surge of biting cold that crawls up your enemy’s limbs. "
                "The impact sends a shock of frost deep into their body, slowing them to a standstill."
            ),
            "incantation": "Shatter beneath the weight of eternal frost! Cryo Blade!",
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
            "name": "Coldlight Aegis",
            "action_type": "Reaction",
            "prerequisite": "Arondight",
            "description": (
                "A shimmer of argent light erupts from Arondight as you brace for impact. "
                "The holy radiance hardens your stance and lashes out with freezing judgment."
            ),
            "incantation": "Radiance, shield my resolve! Coldlight Aegis!",
            "effects": [
                "<b>Trigger:</b> A creature within 5 feet hits you with a melee attack.",
                "You gain <b>resistance to radiant or cold damage</b> until the end of the current turn.",
                "The attacker becomes afflicted with <b>Freeze (potency 1, duration 1)</b>."
            ],
            "tags": ["Defense", "Reaction", "Freeze"]
        },
        {
            "name": "Sacred Counter",
            "action_type": "Bonus Action",
            "prerequisite": "Coldlight Aegis",
            "description": (
                "A flash of sacred light courses through Arondight as you turn defense into retaliation. "
                "The blade strikes back with dazzling precision, empowered by divine brilliance."
            ),
            "incantation": "Light that judges the wicked—strike with me! Sacred Counter!",
            "effects": [
                "<b>Trigger:</b> You used Coldlight Aegis since the end of your last turn.",
                "Make <b>one weapon attack</b> as a Bonus Action.",
                "If the target is afflicted with Freeze, the attack deals <b>+3d6 radiant damage</b>."
            ],
            "tags": ["Radiant", "Bonus Action", "Offense"]
        },
        {
            "name": "Frostwind Step",
            "action_type": "Bonus Action",
            "prerequisite": "Arondight",
            "description": (
                "Cold air spirals beneath your feet as your form blurs with supernatural speed. "
                "Your weapon strike triggers a burst of frost that propels you across the battlefield."
            ),
            "incantation": "Wind of winter, carry my blade! Frostwind Step!",
            "effects": [
                "<b>Trigger:</b> You take this ability as a Bonus Action.",
                "The <b>first time</b> you hit a creature with a weapon attack this turn:",
                "You may move <b>10 feet</b> without provoking opportunity attacks.",
                "If the creature is afflicted with Freeze, you may instead move <b>15 feet</b>.",
                "You may apply <b>Freeze (potency 1, duration 1)</b> to that creature."
            ],
            "tags": ["Mobility", "Freeze", "Bonus Action"]
        },
        {
            "name": "Tempest Break",
            "action_type": "Attack Action",
            "prerequisite": "Frostwind Step",
            "description": (
                "You gather Arondight’s frosted power into a devastating burst. "
                "The blade crashes down with explosive force, releasing a shockwave of piercing cold "
                "that ripples through nearby foes."
            ),
            "incantation": "Gather, storm of ice—unleash devastation! Tempest Break!",
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make a single, empowered weapon attack.",
                "On hit, the target takes <b>+2d6 cold damage</b>.",
                "Creatures within 5 feet take <b>1d6 cold damage</b>.",
                "If the target is afflicted with Freeze: Remove Freeze and deal an additional <b>+2d6 cold damage</b>.",
                "All creatures damaged by this effect become afflicted with <b>Freeze</b> "
                "(potency 1, duration 1)."
            ],
            "tags": ["Cold", "AoE", "Freeze", "Detonation"]
        }
    ],

    "Knight of Owner": [
        {
            "name": "Breakform Shift",
            "action_type": "Bonus Action",
            "prerequisite": "Knight of Owner",
            "incantation": "Steel or stone—your form bends to my will! Breakform Shift!",
            "description": (
                "Chaotic mana courses through your weapon as its shape twists and reforges mid-battle, "
                "allowing you to adapt instantly to any threat."
            ),
            "effects": [
                "<b>Trigger:</b> You use this ability as a Bonus Action.",
                "Choose one temporary weapon transformation that lasts until the start of your next turn:",
                "<b>Heavy Form:</b> Your next hit with the weapon deals <b>+2 damage</b>.",
                "<b>Reach Form:</b> Your next attack with the weapon gains the <b>Reach</b> property.",
                "<b>Swift Form:</b> Your next hit applies <b>Freeze (potency 1, duration 1)</b>.",
                "Only one Breakform Shift may be active at a time."
            ],
            "tags": ["Improvised", "Transformation", "Bonus Action", "Utility", "Freeze"]
        },
        {
            "name": "Arsenal Reel",
            "action_type": "Attack Action",
            "prerequisite": "Breakform Shift",
            "incantation": "Momentum binds all weapons as one—Arsenal Reel!",
            "description": (
                "You flow seamlessly between shifting weapon forms mid-swing, unleashing an unpredictable "
                "strike that blends precision with chaotic improvisation."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose <b>one</b> weapon attack you make this turn.",
                "The attack deals <b>+2d6 damage</b> of your choice: bludgeoning, piercing, or slashing.",
                "If you currently have Breakform Shift active, the attack also applies <b>Freeze</b> "
                "(potency 1, duration 1).",
                "Only one attack may benefit from this feature per turn."
            ],
            "tags": ["Improvised", "Cold", "Single-Hit", "Combo"]
        },
        {
            "name": "Overrun Vault",
            "action_type": "Attack Action",
            "prerequisite": "Knight of Owner",
            "incantation": "No wall stands against unchecked fury—Overrun Vault!",
            "description": (
                "You surge forward with explosive force, vaulting past defenses as raw momentum carries "
                "your improvised strike into the enemy."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Move up to <b>10 feet</b> in a straight line before making one weapon attack.",
                "If you moved at least 10 feet, the attack deals <b>+1d6 damage</b>.",
                "If the target is afflicted with Freeze, you may immediately move <b>5 feet</b> without "
                "provoking opportunity attacks."
            ],
            "tags": ["Mobility", "Momentum", "Cold", "Attack Action"]
        },
        {
            "name": "Limit Shatter",
            "action_type": "Attack Action",
            "prerequisite": "Overrun Vault",
            "incantation": "Let my will break the chains of fate—Limit Shatter!",
            "description": (
                "You unleash the peak of your chaotic momentum into a devastating strike, your improvised "
                "weapon cracking with unstable magical force before detonating against your foe."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make a single, empowered weapon attack.",
                "On hit, the target takes <b>+2d6 force damage</b>.",
                "If you hit a creature more than once on your previous turn (Momentum Overload triggered), "
                "the attack deals an additional <b>+2d6 damage</b>.",
                "If the target is afflicted with Freeze: Remove Freeze and deal <b>+2d6 cold damage</b>",
                "Creatures within 5 feet of the target take <b>1d6 damage</b> of the same type as the main hit."
            ],
            "tags": ["Force", "Cold", "AoE", "Detonation", "Attack Action"]
        }
    ],

    "Excalibur Galatine": [
        {
            "name": "Searing Arc",
            "action_type": "Attack Action",
            "prerequisite": "Excalibur Galatine",
            "incantation": "By the sun’s searing blaze—strike! Searing Arc!",
            "description": (
                "You swing Galatine in a blazing crescent, trailing fire that scorches the battlefield "
                "and ignites anything too close."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose one weapon attack you make this turn.",
                "The attack deals <b>+1d6 fire damage</b>.",
                "Creatures adjacent to the target take <b>1 fire damage</b>.",
                "If you are in bright light, the target is afflicted with "
                "<b>Burn (potency 1, duration 1)</b>."
            ],
            "tags": ["Fire", "Burn", "AoE", "Attack Action"]
        },
        {
            "name": "Galatine Blaze",
            "action_type": "Attack Action",
            "prerequisite": "Searing Arc",
            "incantation": "Sunfire, consume all before me—GALATINE BLAZE!",
            "description": (
                "Galatine erupts in an inferno of holy solar flame, unleashing a burning strike that "
                "scorches enemies caught in its blazing wake."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make one weapon attack.",
                "On hit, the attack deals <b>+2d6 fire damage</b>.",
                "Creatures within 5 feet of the target take <b>1d6 fire damage</b>.",
                "If you are in bright light, all creatures hit by this effect are afflicted with "
                "<b>Burn (potency 1, duration 1)</b>.",
                "If the target already has Burn, the attack deals an additional <b>+2 fire damage</b>."
            ],
            "tags": ["Fire", "Burn", "AoE", "Attack Action"]
        },
        {
            "name": "Dawnstride Ember",
            "action_type": "Bonus Action",
            "prerequisite": "Excalibur Galatine",
            "incantation": "Embers of dawn—guide my step! Dawnstride Ember!",
            "description": (
                "Your steps ignite with sunlit fire as you dash across the battlefield, leaving a trail "
                "of burning light that fuels your next strike."
            ),
            "effects": [
                "<b>Trigger:</b> You use this ability as a Bonus Action.",
                "Move up to <b>10 feet</b> without provoking opportunity attacks.",
                "Your next weapon attack this turn deals <b>+1 fire damage</b>.",
                "If you are in bright light, your next attack also applies "
                "<b>Burn (potency 1, duration 1)</b>."
            ],
            "tags": ["Fire", "Burn", "Mobility", "Bonus Action"]
        },
        {
            "name": "Zenith Flare",
            "action_type": "Attack Action",
            "prerequisite": "Dawnstride Ember",
            "incantation": "O blazing sun—let your verdict fall! ZENITH FLARE!",
            "description": (
                "You channel the zenith sun’s scorching fury into a single overwhelming strike, erupting "
                "into a blazing burst that engulfs the battlefield in solar fire."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make a single empowered weapon attack.",
                "On hit, the attack deals <b>+2d6 fire damage</b>.",
                "Create a <b>10-foot radius</b> zone of searing solar flame centered on the target "
                "until the start of your next turn.",
                "Creatures who enter or start their turn in this zone take <b>1 fire damage</b>.",
                "If you were in bright light when using this skill, the target is afflicted with "
                "<b>Burn (potency 1, duration 1)</b>.",
                "If the target is already afflicted with Burn, the attack deals an additional "
                "<b>+1d6 fire damage</b>."
            ],
            "tags": ["Fire", "Burn", "Zone", "AoE", "Attack Action"]
        }
    ],

    "Aegis Solaria": [
        {
            "name": "Radiant Shielding",
            "action_type": "Reaction",
            "prerequisite": "Aegis Solaria",
            "incantation": "Light of the sun, guard me—Radiant Shielding!",
            "description": (
                "You flare your mantle with blinding sunlight, deflecting a blow with radiant force and "
                "burning nearby foes with its solar brilliance."
            ),
            "effects": [
                "<b>Trigger:</b> A creature hits you with an attack.",
                "Reduce the damage you take by <b>1d6</b>.",
                "Enemies adjacent to <b>you</b> take <b>1 fire damage</b>.",
                "If you are in bright light, the attacker is afflicted with "
                "<b>Burn (potency 1, duration 1)</b>."
            ],
            "tags": ["Defense", "Fire", "Burn", "Reaction"]
        },
        {
            "name": "Solar Counterflare",
            "action_type": "Reaction",
            "prerequisite": "Radiant Shielding",
            "incantation": "By the sun’s wrath—flare and repel! Solar Counterflare!",
            "description": (
                "You unleash a violent solar flare in response to an enemy's attack, scorching them with "
                "burning sunlight and dazzling the battlefield with blinding brilliance."
            ),
            "effects": [
                "<b>Trigger:</b> You reduce damage with Radiant Shielding.",
                "The attacker takes <b>1d6 fire damage</b>.",
                "All other creatures within 5 feet of the attacker take <b>1 fire damage</b>.",
                "If you are in bright light, the attacker is <b>blinded</b> until the start of its next turn."
            ],
            "tags": ["Fire", "Burn", "AoE", "Control", "Reaction"]
        },
        {
            "name": "Dawnlight Mend",
            "action_type": "Bonus Action",
            "prerequisite": "Aegis Solaria",
            "incantation": "Gentle light of dawn—restore my strength! Dawnlight Mend!",
            "description": (
                "You channel the healing warmth of the dawn through your mantle, mending your wounds "
                "with gentle solar radiance."
            ),
            "effects": [
                "<b>Trigger:</b> You use this ability as a Bonus Action.",
                "You regain <b>1d4 hit points</b>.",
                "If you are in bright light, you instead regain <b>1d6 hit points</b>.",
                "Your next weapon attack this turn deals <b>+1 fire damage</b>."
            ],
            "tags": ["Healing", "Fire", "Bonus Action"]
        },
        {
            "name": "Zenith Aegis",
            "action_type": "Action",
            "prerequisite": "Dawnlight Mend",
            "incantation": "Sun at zenith—sanctify this ground! ZENITH AEGIS!",
            "description": (
                "You anchor a radiant barrier of sunlight around you, shielding allies with solar grace "
                "while igniting enemies who dare enter its blazing sanctum."
            ),
            "effects": [
                "<b>Trigger:</b> You take this action.",
                "Create a <b>10-foot radius</b> zone of shimmering sunlight centered on you until the "
                "start of your next turn.",
                "You and allies in the zone gain a <b>+1 bonus to AC</b>.",
                "Enemies who enter or start their turn in the zone are afflicted with "
                "<b>Burn (potency 1, duration 1)</b>.",
                "If you were in bright light when using this skill, you gain "
                "<b>resistance to fire damage</b> until the start of your next turn."
            ],
            "tags": ["Zone", "Defense", "Fire", "Support", "Action"]
        }
    ],

    "Clarent": [
        {
            "name": "Tempest Slash",
            "action_type": "Attack Action",
            "prerequisite": "Clarent",
            "incantation": "Obey me, thunder—cut them down! Tempest Slash!",
            "description": (
                "You force Clarent to unleash a violent surge of lightning, empowering your strike at "
                "the cost of your own vitality."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose one weapon attack you make this turn.",
                "On hit, the attack deals <b>+2d6 lightning damage</b>.",
                "After the attack resolves, you take <b>6 lightning damage</b>.",
                "The target is afflicted with <b>Shock (potency 1, duration 1)</b>."
            ],
            "tags": ["Lightning", "Shock", "Attack Action", "High Risk"]
        },
        {
            "name": "Clarent Breakburst",
            "action_type": "Attack Action",
            "prerequisite": "Tempest Slash",
            "incantation": "My fury is lightning—BURN! CLARENT BREAKBURST!",
            "description": (
                "You unleash Clarent’s corrupted core in a devastating lightning detonation, its power "
                "reaching its peak when your life hangs by a thread."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose one weapon attack you make this turn.",
                "On hit, the attack deals <b>+2d6 lightning damage</b>.",
                "If you are at or below half of your maximum hit points, the attack deals an additional "
                "<b>+2d6 lightning damage</b>.",
                "The target is afflicted with <b>Shock (potency 1, duration 1)</b>.",
                "After all effects resolve, you regain <b>1d4 hit points</b>."
            ],
            "tags": ["Lightning", "Shock", "Attack Action", "High Risk", "Finisher"]
        },
        {
            "name": "Rebellious Charge",
            "action_type": "Bonus Action",
            "prerequisite": "Clarent",
            "incantation": "Outta my way!! Rebellious Charge!",
            "description": (
                "You surge forward in a burst of chaotic lightning, recklessly closing the distance to "
                "deliver a volatile charged strike."
            ),
            "effects": [
                "<b>Trigger:</b> You use this ability as a Bonus Action.",
                "Move up to <b>10 feet</b> in a straight line without provoking opportunity attacks.",
                "Your next weapon attack this turn deals <b>+1 lightning damage</b>.",
                "If you moved at least 10 feet before that attack, the target is afflicted with "
                "<b>Shock (potency 1, duration 1) once per turn</b>."
            ],
            "tags": ["Lightning", "Shock", "Mobility", "Bonus Action"]
        },
        {
            "name": "Stormshatter Drop",
            "action_type": "Attack Action",
            "prerequisite": "Rebellious Charge",
            "incantation": "Fall and break, you bastard—STORMSHATTER DROP!",
            "description": (
                "You crash down on your foe with Clarent blazing, detonating stormfire on impact. When "
                "the target is already electrically primed, the blade unleashes its full destructive force."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make one empowered weapon attack.",
                "On hit, the attack deals <b>+2d6 lightning damage</b>.",
                "If you moved at least 10 feet before this attack, the attack deals an additional "
                "<b>+1d6 thunder damage</b>.",
                "If the target is afflicted with Shock, clear the Shock and deal <b>+2d6 fire damage</b> instead."
            ],
            "tags": ["Lightning", "Shock", "Attack Action", "Finisher"]
        }
    ],

    "Prydwen": [
        {
            "name": "Drift Spark",
            "action_type": "Bonus Action",
            "prerequisite": "Prydwen",
            "incantation": "Winds at my back—DRIFT SPARK!",
            "description": (
                "You manifest Prydwen for a brief instant, sliding with crackling momentum before unleashing "
                "a lightning-charged strike."
            ),
            "effects": [
                "<b>Trigger:</b> You use this ability as a Bonus Action.",
                "Move up to <b>10 feet</b> without provoking opportunity attacks.",
                "Your next weapon attack this turn deals <b>+1 lightning damage</b>.",
                "If you moved at least 10 feet before that attack, the target takes an additional "
                "<b>+1 lightning damage</b>."
            ],
            "tags": ["Lightning", "Mobility", "Bonus Action"]
        },

        {
            "name": "Thunder Drift Assault",
            "action_type": "Attack Action",
            "prerequisite": "Drift Spark",
            "incantation": "Ride the storm—THUNDER DRIFT ASSAULT!",
            "description": (
                "You perform a high-speed lightning drift around your enemy before striking, leaving a "
                "trail of crackling voltage in your wake."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make one weapon attack.",
                "On hit, the attack deals <b>+2d6 lightning damage</b>.",
                "If you moved at least 10 feet before this attack, the target is afflicted with "
                "<b>Shock (potency 1, duration 1)</b>.",
                "This Shock can only be applied <b>once per turn</b>.",
                "After the attack resolves, you may move <b>5 feet</b> without provoking opportunity attacks."
            ],
            "tags": ["Lightning", "Shock", "Mobility", "Attack Action"]
        },

        {
            "name": "Gale Step",
            "action_type": "Bonus Action",
            "prerequisite": "Prydwen",
            "incantation": "Lift me higher—GALE STEP!",
            "description": (
                "You manifest Prydwen beneath you as a sudden updraft, vaulting into the air on a burst "
                "of wind and lightning."
            ),
            "effects": [
                "<b>Trigger:</b> You use this ability as a Bonus Action.",
                "Jump up to <b>10 feet</b> in any direction (horizontal or vertical).",
                "Your next weapon attack this turn deals <b>+1 thunder damage</b>.",
                "If you land adjacent to a creature, that creature takes <b>1 lightning damage</b>."
            ],
            "tags": ["Lightning", "Wind", "Mobility", "Bonus Action"]
        },

        {
            "name": "Stormvault Crash",
            "action_type": "Attack Action",
            "prerequisite": "Gale Step",
            "incantation": "Fall like lightning—STORMVAULT CRASH!",
            "description": (
                "Launching from Prydwen’s manifested surface, you crash down upon your foe in a violent "
                "lightning dive, detonating with stormfire on impact."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make one empowered weapon attack.",
                "On hit, the attack deals <b>+2d6 lightning damage</b>.",
                "If you moved or jumped at least 10 feet before this attack, it deals an additional "
                "<b>+1d6 thunder damage</b>.",
                "If the target is afflicted with Shock, clear the Shock and deal <b>+2d6 fire damage</b> instead."
            ],
            "tags": ["Lightning", "Shock", "Attack Action", "Finisher"]
        }
    ],


}
