import os

ASSETS_DIR = "fgo_app/images"

def getCharacter(name):
    for archetype, characters in CHARACTERS.items():
        for character in characters:
            if character["name"] == name:
                return character
    return None

def get_archetype_for_character(name):
    for archetype, characters in CHARACTERS.items():
        for c in characters:
            if c["name"] == name:
                return archetype
    return None

ARCHETYPES = {
    "Knights of the Round Table": (
        """<h2>Knight's Resolve</h2>
        <p>Your noble willpower manifests as Resolve, a combat resource generated through decisive action and chivalric mastery. 
        Resolve can be spent to perform powerful techniques that enhance your elemental combat style. You can hold up to <b>6 Resolve.</b></p>

        <h3>Gaining Resolve (+1)</h3>
        <ul>
            <li>Hit a target afflicted by your Primary Element for the first time in a round</li>
            <li>Reduce a creature to 0 HP</li>
            <li>Protect an ally</li>
            <li>Apply your Primary Element for the first time in a round</li>
        </ul>
        <h3>Spending 3 Resolve — Knight's Valor</h3>
        <p>Use a bonus action to activate Knight's Valor.</p>
        <ul>
            <li><b>Elemental Edge:</b> You remove the primary elemental status effect on the target and your next 
            attack before the end of your turn gains bonus damage equal to the applied elemental potency.</li>
            <li><b>Chivalric Defense:</b> Gain resistance to your Primary Element until the start of your next turn.</li>
            <li><b>Hero's Surge:</b> Make one additional weapon attack as part of your attack action.</li>
            <li><b>Radiant Shield:</b> Gain temporary HP equal to your Proficiency Bonus + your Character Level / 2 (rounded down).</li>
        </ul>
        <h3>Spending 6 Resolve — Critical Exploit</h3>
        <p>A devastating elemental finisher unique to each Knight. See an individual character page for details.</p>"""
    ),
    "Shinsengumi": (
        """<h2>Iaijutsu Chain</h2>
        <p>The Shinsengumi excel in precise, ruthless swordplay that flows from one decisive strike into the next.
        Their combat style is built on <b>sequencing physical weaknesses</b> to create lethal finishing opportunities.
        Each strike sets up the next, allowing the Shinsengumi to dismantle their foes through escalating pressure.</p>

        <h3>Iaijutsu Chain Basics</h3>
        <p>Whenever you hit a creature with a weapon attack and inflict or extend one of the following status effects:</p>
        <ul>
            <li><b>Bleed</b></li>
            <li><b>Crush</b></li>
            <li><b>Vulnerable</b></li>
        </ul>
        <p>you advance your <b>Iaijutsu Chain</b> by 1 step. The chain has three steps:</p>

        <ol>
            <li><b>Step 1 — First Weakness</b>: You have inflicted the first physical status effect this turn.</li>
            <li><b>Step 2 — Second Weakness</b>: You have inflicted a different physical status effect from the first.</li>
            <li><b>Step 3 — Execution Point</b>: You have inflicted all three <i>distinct</i> physical statuses this turn.</li>
        </ol>

        <p><b>You can only advance the Iaijutsu Chain by applying a status you have NOT applied earlier in the same turn.</b></p>
        <p>The Iaijutsu Chain resets to <b>0</b> at the start of each of the chain intiator's turn.</p>

        <h3>Execution Point</h3>
        <p>When you reach <b>Step 3</b> of the Iaijutsu Chain, your next weapon attack before the end of your turn becomes an Execution Technique:</p>

        <h4>Standard Execution</h4>
        <ul>
            <li>You have <b>advantage</b> on the attack roll.</li>
            <li>The attack deals an additional <b>2d6 damage</b> of your weapon’s damage type.</li>
            <li>You may remove <b>one</b> of Bleed, Crush, or Vulnerable from the target to deal <b>+2d6</b> bonus damage of the associated type:</li>
        </ul>

        <ul>
            <li><b>Bleed removed:</b> +2d6 slashing damage.</li>
            <li><b>Crush removed:</b> +2d6 bludgeoning damage.</li>
            <li><b>Vulnerable removed:</b> +2d6 piercing damage.</li>
        </ul>

        <h4>Execution Arts</h4>
        <p>Each Shinsengumi Servant Core gains a unique form of <b>Execution Art</b> when performing an Execution Technique.<br>
        Instead of using a Standard Execution, you can choose to replace it with a powerful finisher that scales with <br>
        the Servant’s signature status effect.</p>
        <p>See each individual character page for full details.</p>

        <p>The Iaijutsu Chain ends immediately after performing an Execution Technique.</p>

        <h3>Perfect Style</h3>
        <p>When you perform an Execution Technique, you gain <b>Perfect Style</b> until the end of your next turn:</p>
        <ul>
            <li>Your movement does not provoke opportunity attacks.</li>
            <li>Your weapon attacks ignore half cover.</li>
        </ul>

        <p>This reflects the Shinsengumi’s unmatched battlefield footwork and cutting precision.</p>"""
    ),
    "Argonauts": (
        """<h2>Placeholder</h2>"""
    )
}

CHARACTERS = {
    "Knights of the Round Table": [
        {
            "name": "Lancelot",
            "image": os.path.join(ASSETS_DIR, "lancelot_saber.jpg"),
            "image2": os.path.join(ASSETS_DIR, "lancelot_berserker.jpg"),
            "description": {
                "summary": (
                    "<h3>Lancelot — The Knight of the Lake</h3>"
                    "<p>Lancelot excels as a disciplined frost duelist who controls the battlefield through precision, "
                    "speed, and methodical application of <b>Freeze</b>. His playstyle revolves around building and "
                    "consuming Freeze stacks to enhance damage and to slow enemies, rewarding players who plan their turns "
                    "carefully and manipulate enemy movement.</p>"

                    "<p>Arondight empowers him with fluid, icy strikes that hinder opponents while opening opportunities "
                    "for devastating follow-ups. Lancelot’s abilities allow him to weave between offense and defense—"
                    "counterattacking foes who threaten him, repositioning with supernatural grace, and unleashing "
                    "powerful finishing blows when Freeze reaches its peak.</p>"

                    "<p>Players who enjoy tactical combat, precise timing, and escalating elemental pressure will find "
                    "Lancelot a deeply rewarding Servant who controls the flow of every engagement.</p>"
                ),
                "mini_ult": (
                    "<h3>Critical Exploit — Ice Shatter</h3>"
                    "<p><b>Trigger:</b> You spend 6 Resolve as a bonus action. "
                    "On your next successful weapon attack, if the target is afflicted with <b>Freeze</b>, "
                    "<i>Ice Shatter</i> activates.</p>"

                    "<h4>Effect</h4>"
                    "<ul>"
                        "<li><b>If Freeze is at maximum potency:</b>"
                            "<ul>"
                                "<li>Deal cold damage equal to <b>Freeze Potency × 5</b></li>"
                                "<li>The target is <b>knocked prone</b></li>"
                                "<li><b>Freeze is removed</b> from the target</li>"
                            "</ul>"
                        "</li>"

                        "<li><b>If Freeze is NOT at max potency:</b>"
                            "<ul>"
                                "<li>Deal cold damage equal to <b>Freeze Potency × 3</b></li>"
                                "<li><b>Freeze is removed</b> from the target</li>"
                            "</ul>"
                        "</li>"
                    "</ul>"
                )
            }
        },
        {
            "name": "Gawain",
            "image": os.path.join(ASSETS_DIR, "gawain.jpg"),
            "description": {
                "summary": (
                    "<h3>Gawain — The Knight of the Sun</h3>"
                    "<p>Gawain embodies overwhelming strength empowered by blazing sunlight. "
                    "As a frontline juggernaut, he excels at sustained offense—his power rising "
                    "dramatically when fighting in bright light. His abilities leverage solar fire "
                    "to inflict Burn stacks on foes, bolster his defenses, and dominate close-quarters "
                    "combat with radiant might.</p>"

                    "<p>Wielding Excalibur Galatine, Gawain sweeps the battlefield with wide arcs "
                    "of flame and holy radiance. His momentum builds as he lands consecutive blows, "
                    "letting him scale in damage over the course of a fight. With proper positioning "
                    "and control of light conditions, Gawain transforms into a relentless beacon of "
                    "burning destruction.</p>"

                    "<p>Players who enjoy heroic aggression, explosive fire bursts, and a “power-up” "
                    "playstyle will find Gawain’s solar combat both satisfying and spectacular.</p>"
                ),
                "mini_ult": (
                    "<h3>Critical Exploit — Solar Flare</h3>"
                    "<p><b>Trigger:</b> You spend 6 Resolve with a bonus action. "
                    "On your next successful attack, if the target is afflicted with <b>Burn</b>, "
                    "<i>Solar Flare</i> activates.</p>"

                    "<h4>Effect</h4>"
                    "<ul>"
                        "<li>Deal <b>fire damage equal to Burn Potency × 2</b> to the target.</li>"
                        "<li>The target emits a <b>Solar Shockwave</b>:"
                            "<ul>"
                                "<li>All creatures adjacent (within 5 feet / 4 tiles around) take "
                                "<b>fire damage equal to Burn Potency</b>.</li>"
                            "</ul>"
                        "</li>"
                        "<li>You gain <b>temporary HP equal to Burn Potency</b>.</li>"
                        "<li><b>Burn is removed</b> from the target.</li>"
                    "</ul>"
                )
            }
        },
        {
            "name": "Mordred",
            "image": os.path.join(ASSETS_DIR, "mordred.jpg"),
            "description": {
                "summary": (
                    "<h3>Mordred — The Knight of Rebellion</h3>"
                    "<p>Mordred thrives on reckless aggression, channeling volatile lightning and burning fury "
                    "through Clarent. She is a close-range bruiser whose damage output skyrockets when she fights "
                    "at low HP, rewarding bold plays and unrelenting momentum. Shock and burning effects fuel her "
                    "chaotic style, letting her tear through enemies with explosive burst damage.</p>"

                    "<p>Her attacks often come with a cost—Mordred willingly harms herself to unleash Clarent’s "
                    "corrupted power. Yet her kit also provides ways to stabilize or recover through fiery backlash, "
                    "letting her walk the razor’s edge between survival and destruction. Players who enjoy high-risk, "
                    "high-reward gameplay will find Mordred’s lightning-charged rage both dangerous and exhilarating.</p>"

                    "<p>Prydwen serves as her alternate armament, granting unmatched mobility and aerial maneuvering. "
                    "It enables blistering movement-based combos that prime her targets with <b>Shock</b> before "
                    "delivering devastating finishers.</p>"
                ),
                "mini_ult": (
                    "<h3>Critical Exploit — Overload</h3>"
                    "<p><b>Trigger:</b> You spend 6 Resolve with a bonus action. "
                    "On your next successful attack, if the target is afflicted with <b>Shock</b>, "
                    "<i>Overload</i> activates.</p>"

                    "<h4>Effect</h4>"
                    "<ul>"
                        "<li>Deal <b>lightning damage equal to Shock Potency × 4</b> to the target.</li>"
                        "<li>The target <b>loses its Reaction</b> until the start of your next turn.</li>"
                        "<li>The target has <b>disadvantage on concentration checks</b> until the start of your next turn.</li>"
                        "<li><b>Shock is removed</b> from the target.</li>"
                    "</ul>"
                )
            }
        },
    ],

    "Shinsengumi": [
        {
            "name": "Okita Souji",
            "image": os.path.join(ASSETS_DIR, "okita.jpg"),
            "description": {
                "summary": (
                    """<h2>Okita Souji</h2>

                    <p>A swift and graceful swordswoman of the Shinsengumi, Okita Souji fights with a drifting elegance that
                    belies the lethality of her technique. Her blade strikes like falling petals—light, effortless, and
                    deceptively fatal. She flows across the battlefield in silent diagonal steps, slipping through blind
                    angles before carving precise, blooming wounds into her foes.</p>

                    <p>Okita specializes in <b>Bleed</b>, drawing out her enemy’s vitality through rapid, refined cuts.
                    Whether she drifts in a smooth cherry-blossom flow or dances through impossible angles beneath a
                    moonless sky, her combat style revolves around building and exploiting openings with perfect timing.</p>

                    <p>Her Iaijutsu Chain rewards striking from new weaknesses in sequence, culminating in a decisive
                    Execution Technique that reflects her mastery of drifting swordplay. Okita’s two armaments shape her
                    approach: <b>Sakura-Nagashi</b> offers fluid motion and elegant Bleed pressure, while
                    <b>Mugetsu-no-Hamon</b> challenges the most skilled fighters to leverage flawless positioning and
                    spatial awareness.</p>

                    <p>In the hands of a tactician who values efficiency, precision, and movement, Okita becomes a crimson
                    storm—an artist painting death in flowing strokes of drifting petals and moonless cuts.</p>"""
                ),
                "mini_ult": (
                    """
                    <h3>Execution Art — Zantetsu-sen (斬鉄閃)</h3>
                    <p><b>Trigger:</b> When you reach <b>Execution Point</b>, you may choose to use this Execution Art
                    instead of performing a Standard Execution. It enhances the next weapon attack you make this turn.</p>

                    <h4>Effect</h4>
                    <ul>
                        <li>You have <b>advantage</b> on the attack roll.</li>
                        <li>The attack deals an additional <b>2d6 slashing damage</b>.</li>
                        <li>If the target is afflicted with <b>Bleed</b>, the attack deals additional slashing damage
                        equal to <b>Bleed Potency × 2</b>.</li>
                        <li>If the attack reduces a creature to 0 hit points, you may move <b>up to 10 feet</b> without provoking opportunity attacks.</li>
                    </ul>

                    <p>Zantetsu-sen ends the Iaijutsu Chain and immediately grants <b>Perfect Style</b>.</p>
                    """
                )
            }
        },
        {
            "name": "Saitō Hajime",
            "image": os.path.join(ASSETS_DIR, "hajime.jpg"),
            "description": {
                "summary": (
                    """
                    <h2>Saitō Hajime</h2>

                    <p>A cold, quiet master of the blade, Saitō Hajime is the Shinsengumi’s most disciplined and unshakable swordsman.
                    Where others advance with flourish or brute strength, Saitō stands in absolute stillness—an immovable pillar of
                    composure whose killing intent is sharp enough to cut before the sword ever moves.</p>

                    <p>His combat philosophy is built on <b>clarity of intent</b>: he reads his opponent’s centerline, studies their breath,
                    and strikes at the exact instant their stance falters. Whether through the rapid-fire aggression of
                    <b>Happa-zuki</b> or the steadfast counterduelist posture of <b>Mibu no Kurai</b>, Saitō dismantles his enemies not with
                    flashy spectacle, but with overwhelming precision.</p>

                    <p>Saitō specializes in inflicting <b>Vulnerable</b>, exposing the weak points he predicts through impeccable timing and
                    observation. His techniques reward players who attack with purpose—either by maintaining relentless pressure with
                    multi-hit thrusts or by standing firm and punishing enemy aggression with devastating counterstrikes. Few warriors
                    can match his mastery of centerline control or his icy calm under pressure.</p>

                    <p>Through the Iaijutsu Chain, Saitō sets up lethal finishing opportunities, culminating in his Execution Art,
                    <b>Migiri no Tachi</b>—a perfectly timed, insight-driven thrust delivered at the precise moment the opponent’s guard
                    shatters. In the hands of a tactician who values poise, decisiveness, and surgical precision, Saitō becomes a
                    one-man execution squad… the quiet edge that ends a battle before it begins.</p>
                    """
                ),
                "mini_ult": (
                    """
                    <h3>Execution Art — Migiri no Tachi (見切りの太刀)</h3>
                    <p><b>Trigger:</b> When you reach <b>Execution Point</b>, you may replace your Standard Execution
                    with this technique.</p>
                    <ul>
                        <li>You have <b>advantage</b> on the attack roll.</li>
                        <li>The attack deals an additional <b>1d10 piercing damage</b>.</li>
                        <li>If the target made an attack against you since the start of your last turn, 
                            deal an additional <b>+2d6 piercing damage</b>.</li>
                        <li>If the enemy is afflicted with <b>Vulnerable</b>, increase its <b>duration by +1</b> and add 
                            <b>+1d6 slashing damage</b>.</li>
                    </ul>

                    <p>Migiri no Tachi ends the Iaijutsu Chain and immediately grants <b>Perfect Style</b>.</p>
                    """
                )
            }
        },
        {
            "name": "Nagakura Shinpachi",
            "image": os.path.join(ASSETS_DIR, "shinpachi.jpg"),
            "description": {
                "summary": (
                    """
                    <h2>Nagakura Shinpachi</h2>

                    <p>Nagakura Shinpachi charges into battle with the unstoppable confidence of a warrior who refuses to yield. 
                    Loud, bold, and brimming with fighting spirit, he is the Shinsengumi’s frontline brawler—one who overwhelms 
                    enemies not with finesse, but with sheer force and relentless pressure. Where Okita moves like wind and Saitō 
                    strikes with precision, Shinpachi hurls himself forward like a battering ram, crushing anyone who stands in his path.</p>

                    <p>Shinpachi specializes in exploiting <b>Crush</b> by driving opponents across the battlefield with full-body shoves. 
                    Through <b>Kuzushi-no-Kamae</b>, he bodies through foes with unstoppable momentum, slamming them into walls, staggering 
                    their footing, and following through with brutal takedowns. His rushdown style allows him to shove, trip, and even 
                    impale prone enemies in a single fluid sequence. Once a target hits the ground, Shinpachi can lock them in a crushing 
                    grapple, twisting limbs and applying joint-cracking pressure until their defenses collapse entirely.</p>

                    <p>Alternatively, he can adopt <b>Oni-Satsu</b> to focus on raw destructive power—striking harder with each blow, 
                    controlling the space directly in front of him, and punishing weakened enemies with overwhelming force. 
                    Whether barreling through lines of soldiers or pinning opponents beneath his weight, Shinpachi dominates the 
                    close-quarters fight with chaotic, physical aggression.</p>

                    <p>At the height of his fury, Shinpachi unleashes <b>Ryougeki</b>, a thunderous execution that sends shockwaves 
                    rippling across the battlefield. Armor buckles, formations break, and enemies scatter as he announces with 
                    full volume and full strength that the Shinsengumi’s loudest warrior has claimed another victory.</p>
                    """
                ),
                "mini_ult": (
                    """
                    <b>Execution Art — Ryougeki (轟撃)</b><br>
                    <p>A deafening smash that sends shockwaves across the battlefield.</p>

                    <ul>
                        <li>You gain <b>advantage</b> on the attack roll.</li>
                        <li>Deal <b>+2d6 thunder damage</b>.</li>
                        <li>If the target is afflicted with <b>Crush</b>, you may remove it to deal <b>+2d8</b> bonus damage.</li>
                        <li>All creatures adjacent to the target must succeed on a <b>DC 14 Strength save</b> or be pushed <b>5 feet</b>.</li>
                    </ul>

                    <p>Shinpachi yells something triumphant as he smacks everyone away with sheer force.</p>
                    """
                )
            }
        },
    ],

    "Argonauts": [
        {
            "name": "Heracles",
            "image": os.path.join(ASSETS_DIR, "heracles.jpg"),
            "description": {
                "summary": (
                    "<h2>Placeholder</h2>"
                ),
                "mini_ult": (
                    "<h2>Placeholder</h2>"
                )
            }
        },
        {
            "name": "Caenis",
            "image": os.path.join(ASSETS_DIR, "caenis.jpg"),
            "description": {
                "summary": (
                    "<h2>Placeholder</h2>"
                ),
                "mini_ult": (
                    "<h2>Placeholder</h2>"
                )
            }
        },
        {
            "name": "Atalanta",
            "image": os.path.join(ASSETS_DIR, "atalanta.jpg"),
            "description": {
                "summary": (
                    "<h2>Placeholder</h2>"
                ),
                "mini_ult": (
                    "<h2>Placeholder</h2>"
                )
            }
        },
    ],
}

# Armament sets per character
CHAR_ARMAMENTS = {
    "Lancelot": [
        {
            "key": "Arondight",
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
                
                "<b>Thundertrail Wake:</b> If you move at least 10 feet straight on your turn, the first creature "
                "you hit with a weapon attack takes <b>+1 lightning damage</b>.",
                
                "<b>Impact Ignition:</b> If you move at least 15 feet straight before hitting a creature with a "
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
        {
            "name": "Sakura-Nagashi — Drifiting Sakura",
            "type": "Katana",
            "description": (
                "A graceful katana whose pale edge drifts like falling blossoms in the wind. Its slashes are light, "
                "effortless, and deceptively lethal—each cut leaving a winding crimson trail. Sakura-Nagashi embodies "
                "Okita's elegant, flowing swordsmanship, turning every motion into a drifting petal of death."
            ),
            "effects": [
                "<b>Petalstep Footwork:</b> Your movement speed increases by <b>5 feet</b>.",

                "<b>Winding Petals:</b> When you hit a creature already afflicted with <b>Bleed</b>, your attack deals "
                "<b>+2 slashing damage</b>.",

                "<b>Crimson Drift:</b> Once per turn, when you hit a creature with a weapon attack, you may move "
                "<b>5 feet</b> without provoking opportunity attacks.",

                "<b>Cherryblade Form:</b> The first time each turn you apply <b>Bleed</b>, its <b>duration</b> increases "
                "by <b>+1</b>."
            ],
            "effects_data": [
                {"id": "sakura_speed_bonus", "value": 5},
                {"id": "sakura_bleed_bonus_damage", "value": 2},
                {"id": "sakura_crimson_drift", "value": 5},
                {"id": "sakura_bleed_duration_increase", "value": 1}
            ]
        },
        {
            "name": "Mugetsu-no-Hamon — Moonless Blade Pattern",
            "type": "Katana",
            "description": ("""
                A pitch-black cursed katana whose edge glows faintly pink, like moonlight reflected in blood.
                Its hamon is broken and moonless — a phantom edge said to cleave through impossible angles.
                Only those with perfect footwork and flawless spatial awareness can unlock its true potential.
            """),
            "effects": [
                "<b>Moonless Footwork:</b> If you move at least <b>15 feet</b> on your turn, moving <i>only diagonally</i> "
                "and without entering any space you have previously occupied since the start of your turn, your first "
                "weapon attack this turn deals <b>+2 slashing damage</b>.",

                "<b>Shadowline Cut:</b> Once per turn, when you make a weapon attack, it gains <b>+5 feet of reach</b>. "
                "This extended reach applies only to that attack.",

                "<b>Blind-Angle Opening:</b> When you hit a creature that is <b>flanked</b> (two allies threatening it "
                "from opposite sides), you apply <b>Vulnerable (potency 1, duration 1)</b>. This can occur "
                "<b>once per turn</b>.",

                "<b>Crescent Void Edge:</b> When you perform an <b>Execution Technique</b>, if the target has "
                "<b>no adjacent allies</b>, the attack deals an additional <b>1d6 slashing damage</b>."
            ],
            "effects_data": [
                {"id": "mugetsu_moonless_footwork_bonus", "value": 2},
                {"id": "mugetsu_extended_reach", "value": 5},
                {"id": "mugetsu_vulnerable_on_flank", "value": 1},
                {"id": "mugetsu_execution_isolated_bonus", "value": "1d6"}
            ]
        },
    ],

    "Saitō Hajime": [
        {
            "name": "Mibu no Kurai",
            "type": "Katana",
            "description": (
                "<b>Mibu no Kurai</b> embodies the stillness and discipline of a true duelist’s stance. Rather than "
                "chasing openings through motion, this style roots the swordsman in unshakable posture, reading the "
                "enemy’s intent and striking back with precise, punishing counterthrusts the moment their guard falters."
            ),
            "effects": [
                "<b>Stillness of Mibu:</b> If you move <b>5 feet or less</b> on your turn, you gain <b>+1 AC</b> until "
                "the start of your next turn.",
                
                "<b>Deflect and Pierce:</b> When a creature within your reach makes an attack against you, you may use "
                "your <b>reaction</b> to impose <b>disadvantage</b> on the attack roll. After the attack resolves, if the "
                "creature is within reach, you may make <b>one weapon attack</b> against it.",
                
                "<b>Counter-Expose:</b> If your reaction attack from Deflect and Pierce hits, apply "
                "<b>Vulnerable (potency 1, duration 1)</b>.",
                
                "<b>Unyielding Posture:</b> You cannot be moved against your will while you are standing on solid ground."
            ],
            "effects_data": [
                {"id": "mibu_stillness_ac_bonus", "value": 1},
                {"id": "mibu_deflect_reaction", "value": 1},
                {"id": "mibu_vulnerable_on_counter", "value": 1},
                {"id": "mibu_immovable", "value": 1}
            ]
        },
        {
            "name": "Happa-zuki",
            "type": "Katana",
            "description": (
                "<b>Happa-zuki</b> is a rapid-fire thrusting style built on overwhelming pressure. Rather than waiting "
                "for perfect openings or holding a steady stance, this form unleashes a barrage of sharp, consecutive "
                "piercing attacks—each one incrementally widening the opponent’s guard. The name evokes the imagery of "
                "“eight breaks”: a relentless sequence of thrusts that shatters defenses step by step."
            ),
            "effects": [
                "<b>Rapid Pressure:</b> If you make more than <b>one</b> weapon attack on your turn, your <b>last</b> "
                "attack this turn gains <b>+1 piercing damage</b>.",
                
                "<b>Sequence Momentum:</b> Once per turn, when you hit a creature with a weapon attack, you may "
                "immediately deal <b>1 piercing damage</b> to the same target as a follow-up flick thrust.",
                
                "<b>Guard Fracture:</b> If you hit the same creature with <b>two or more</b> attacks on your turn, "
                "apply <b>Vulnerable (potency 1, duration 1)</b>.",
                
                "<b>Break Rhythm:</b> If all attacks you made this turn targeted the <b>same creature</b>, increase "
                "your next weapon attack’s damage by <b>+1d4 piercing</b>."
            ],
            "effects_data": [
                {"id": "happa_rapid_pressure_bonus", "value": 1},
                {"id": "happa_sequence_momentum_poke", "value": 1},
                {"id": "happa_vulnerable_on_chain", "value": 1},
                {"id": "happa_break_rhythm_bonus", "value": "1d4"}
            ]
        }
    ],

    "Nagakura Shinpachi": [
        {
            "name": "Oni-Satsu",
            "type": "Katana",
            "description": (
                "<b>Oni-Satsu</b> embodies the raw, overwhelming power needed to cut down even demons. This style focuses "
                "on simple, brutal strikes—each swing delivering crushing force without need for finesse or technique. "
                "A perfect choice for warriors who want to hit hard and hit often."
            ),
            "effects": [
                "<b>Heavy Swing:</b> Your first weapon attack each turn deals <b>+2 damage</b>.",
                
                "<b>Crush Specialist:</b> When you apply <b>Crush</b> to a creature, increase its <b>potency by +1</b> "
                "(once per turn).",
                
                "<b>Brutal Momentum:</b> When you hit a creature afflicted with <b>Crush</b>, deal an additional "
                "<b>+1 bludgeoning damage</b>.",
                
                "<b>Simple Power:</b> Once per turn, when you hit a creature with a weapon attack, you may deal "
                "<b>1 extra damage</b> of your weapon’s type."
            ],
            "effects_data": [
                {"id": "onisatsu_first_swing_bonus", "value": 2},
                {"id": "onisatsu_crush_potency", "value": 1},
                {"id": "onisatsu_bonus_damage_on_crush", "value": 1},
                {"id": "onisatsu_simple_power", "value": 1}
            ]
        },
        {
            "name": "Kuzushi-no-Kamae",
            "type": "Katana",
            "description": (
                "<b>Kuzushi-no-Kamae</b> transforms Shinpachi’s fighting style into a full-force bull rush. Through sheer "
                "physical dominance, he shoves enemies across the battlefield, crashing them into walls or allies while "
                "charging directly behind them with unstoppable momentum. This stance turns forced movement into a "
                "devastating combo engine, generating Crush, crash damage, and powerful follow-up attacks."
            ),
            "effects": [
                "<b>Shove Rush:</b> Use your <b>Bonus Action</b> to Shove a creature (push or knock prone), then immediately "
                "move the same distance in the same direction. This movement does <b>not provoke Opportunity Attacks</b>, "
                "and you must end adjacent to the creature. The following effects can only be activated from this Shove Rush.",
                
                "<b>Crash and Crush:</b> If a shoved creature collides with a wall, object, or another creature, it takes "
                "<b>1d4 bludgeoning damage for every 5 feet</b> it was shoved and it gains <b>Crush (potency 1, duration 1)</b>..",
                
                "<b>Crush on Prone:</b> If you shove a creature prone—or if you attack a creature that became prone from "
                "your shove—your next weapon attack against that creature applies <b>Crush (potency 1, duration 1)</b> on hit.",
                
                "<b>Momentum Strike:</b> After Shove Rush, your next weapon attack this turn deals <b>+1 damage</b> of your "
                "weapon’s type.",
                
                "<b>Driving Advantage:</b> If you shoved a creature <b>10 feet or more</b>, your next weapon attack this "
                "turn has <b>advantage</b>.",
                
                "<b>Crush Displacement:</b> If the target is afflicted with <b>Crush</b>, your shove distance increases "
                "to <b>10 feet</b> instead of 5."
            ],
            "effects_data": [
                {"id": "rush_shove_distance", "value": 5},
                {"id": "rush_shove_distance_crush", "value": 10},
                {"id": "momentum_bonus_damage", "value": 1},
                {"id": "advantage_distance_threshold", "value": 10},
                {"id": "crash_damage_per_5ft", "value": "1d4"},
                {"id": "crush_applied_on_collision", "value": 1},
                {"id": "crush_applied_on_prone_attack", "value": 1}
            ]
        }
    ],

    "Heracles": [
        {
            "name": "God's Hand",
            "type": "Ability",
            "description": "Description.",
            "effects": [],
            "effects_data": []
        },
        {
            "name": "Placeholder",
            "type": "placeholder",
            "description": "Description.",
            "effects": [],
            "effects_data": []
        },
    ],
    
    "Caenis": [
        {
            "name": "Placeholder",
            "type": "placeholder",
            "description": "Something",
            "effects": [],
            "effects_data": []
        },
        {
            "name": "Placeholder",
            "type": "placeholder",
            "description": "Description.",
            "effects": [],
            "effects_data": []
        },
    ],

    "Atalanta": [
        {
            "name": "Placeholder",
            "type": "placeholder",
            "description": "Description",
            "effects": [],
            "effects_data": []
        },
        {
            "name": "Placeholder",
            "type": "placeholder",
            "description": "Description.",
            "effects": [],
            "effects_data": []
        },
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
                "Choose one weapon attack you make this turn before you hit.",
                "On hit, the attack applies <b>Freeze (potency 1, duration 2)</b>.",
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
                "Choose one weapon attack you make this turn before you hit.",
                "The attack deals <b>+2d6 cold damage</b> if the target is afflicted with Freeze.",
                "If the target has Freeze at <b>maximum potency</b>, its speed becomes <b>0</b> "
                "until the end of its next turn."
                "Then, at last, the target is afflicted by Freeze (potency 1, duration 1)."
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
                "You gain <b>resistance to radiant or cold damage</b> until the start of your next turn.",
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
                "All creatures damaged by Tempest Break become afflicted with <b>Freeze</b> "
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
                "Choose one weapon attack you make this turn before you hit.",
                "The attack deals <b>+2d6 damage</b> of your choice: bludgeoning, piercing, or slashing.",
                "If you currently have Breakform Shift active, the attack also applies <b>Freeze</b> "
                "(potency 1, duration 1).",
                "Only one attack may benefit from this feature per turn."
            ],
            "tags": ["Improvised", "Cold", "Single-Hit", "Combo"]
        },
        {
            "name": "Overrun Vault",
            "action_type": "Action",
            "prerequisite": "Knight of Owner",
            "incantation": "No wall stands against unchecked fury—Overrun Vault!",
            "description": (
                "You surge forward with explosive force, vaulting past defenses as raw momentum carries "
                "your improvised strike into the enemy."
            ),
            "effects": [
                "<b>Trigger:</b> When you use this Action.",
                "Move up to <b>10 feet</b> in a straight line, then make one weapon attack.",
                "If you moved at least 10 feet, the attack deals <b>+2 cold damage</b> ",
                "and the target is afflicted with Freeze (potency 1, duration 1)."
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
                "Choose one weapon attack you make this turn before you hit.",
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
                "Choose one weapon attack you make this turn before you hit.",
                "The attack deals <b>+1d6 fire damage</b>.",
                "Creatures adjacent to the target take <b>1 fire damage</b>.",
                "If you are in bright light, the target is afflicted with "
                "<b>Burn (potency 1, duration 2)</b>."
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
                "Choose one weapon attack this turn before you hit.",
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
                "<b>Trigger:</b> A creature within 5 feet hits you with an attack.",
                "Reduce the damage you take by <b>1d6</b>.",
                "Enemies adjacent to <b>you</b> take <b>1 fire damage</b>.",
                "If you are in bright light, the attacker is afflicted with "
                "<b>Burn (potency 1, duration 1)</b>."
            ],
            "tags": ["Defense", "Fire", "Burn", "Reaction"]
        },
        {
            "name": "Solar Counterflare",
            "action_type": "Special",
            "prerequisite": "Radiant Shielding",
            "incantation": "By the sun’s wrath—flare and repel! Solar Counterflare!",
            "description": (
                "You unleash a violent solar flare in response to an enemy's attack, scorching them with "
                "burning sunlight and dazzling the battlefield with blinding brilliance."
            ),
            "effects": [
                "<b>Trigger:</b> You reduce damage with Radiant Shielding.",
                "The attacker takes <b>1d6 fire damage</b>.",
                "The attacker also is inflicted by <b>Burn (potency 1, duration 1)</b>"
                "All other creatures within 5 feet of the attacker take <b>2 fire damage</b>.",
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
                "Enemies who enter or start their turn for the first time in the zone are afflicted with "
                "<b>Burn (potency 1, duration 1)</b>.",
                "If you were in bright light when using this skill, the Burn effect is changed "
                "<b>(potency 2, duration 2)</b>."
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
                "Choose one weapon attack you make in this turn before you hit.",
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
                "Choose one weapon attack you make this turn before you hit.",
                "On hit, the attack deals <b>+2d6 lightning damage</b>.",
                "If you are at or below half of your maximum hit points, the attack deals an additional "
                "<b>+2d6 lightning damage</b> and the target is afflicted with "
                "<b>Shock (potency 2, duration 1)</b>.",
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
                "<b>+2 lightning damage</b>."
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
                "Choose one weapon attack this turn before you hit.",
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
                "Choose one weapon attack this turn before you hit.",
                "On hit, the attack deals <b>+2d6 lightning damage</b>.",
                "If you moved or jumped at least 10 feet before this attack, it deals an additional "
                "<b>+1d6 thunder damage</b>.",
                "If the target is afflicted with Shock, clear the Shock and deal <b>+2d6 fire damage</b>."
            ],
            "tags": ["Lightning", "Shock", "Attack Action", "Finisher"]
        }
    ],

    "Sakura-Nagashi — Drifiting Sakura": [
        {
            "name": "Sakura-giri — Petal Cut",
            "action_type": "Attack Action",
            "prerequisite": "Sakura-Nagashi — Drifiting Sakura",
            "incantation": "A single petal cleaves… Sakura-giri!",
            "description": (
                "Your blade flicks forward like a drifting cherry petal, slicing a clean opening and drawing first blood. "
                "A precise Bleed-focused opener to Sakura-Nagashi’s flowing form."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose <b>one</b> weapon attack you make this turn before you hit.",
                "On hit, apply <b>Bleed (potency 1, duration 1)</b>.",
                "If the target already has Bleed, the attack deals <b>+1d4 slashing damage</b>.",
                "If Bleed is at <b>maximum duration</b>, increase its <b>potency by +1</b> (respecting max potency)."
            ],
            "tags": ["Bleed", "Attack Action", "Single-Hit"]
        },

        {
            "name": "Nagare-zan — Flowing Rend",
            "action_type": "Attack Action",
            "prerequisite": "Sakura-giri — Petal Cut",
            "incantation": "Flow with the wind—Nagare-zan!",
            "description": (
                "A drifting horizontal cut that deepens the wound in a flowing arc, extending Sakura-Nagashi’s bleeding "
                "pressure before a blooming finish."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>one</b> weapon attack.",
                "On hit, deal <b>+1d6 slashing damage</b>.",
                "If the target is afflicted with <b>Bleed</b>, extend its <b>duration by +1</b>.",
                "If you moved at least <b>5 feet</b> this turn, this attack deals an additional <b>+1 slashing damage</b>."
            ],
            "tags": ["Bleed", "Attack Action", "Finisher", "Setup"]
        },

        {
            "name": "Kurenai-ippo — Crimson Step",
            "action_type": "Bonus Action",
            "prerequisite": "Sakura-Nagashi — Drifiting Sakura",
            "incantation": "Step through the bloom… Kurenai-ippo!",
            "description": (
                "A drifting crimson stride that positions Okita perfectly for an opening cut. Fluid motion creates "
                "a momentary opening to draw blood."
            ),
            "effects": [
                "<b>Trigger:</b> You use this ability as a Bonus Action.",
                "Move up to <b>10 feet</b> without provoking opportunity attacks.",
                "Your next weapon attack this turn applies <b>Bleed (potency 1, duration 1)</b>.",
                "If that attack already applies Bleed, increase its <b>duration by +1</b>."
            ],
            "tags": ["Mobility", "Bleed", "Bonus Action"]
        },

        {
            "name": "Sakura-mai — Cherryburst Spiral",
            "action_type": "Attack Action",
            "prerequisite": "Kurenai-ippo — Crimson Step",
            "incantation": "Scatter, petals… Sakura-mai!",
            "description": (
                "You whirl into a blooming spiral of drifting petals, striking twice in a graceful flurry that deepens "
                "the enemy’s bleeding wounds."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>two</b> weapon attacks instead of one.",
                "Each attack deals <b>+1 slashing damage</b>.",
                "If either attack hits a creature afflicted with <b>Bleed</b>, extend its <b>duration by +1</b>.",
                "If both attacks hit, deal an additional <b>1d8 slashing damage</b>."
            ],
            "tags": ["Bleed", "Multi-Hit", "Finisher", "Attack Action"]
        },
    ],

    "Mugetsu-no-Hamon — Moonless Blade Pattern": [
        {
            "name": "Mugetsu Hohō — Moonless Footwork",
            "action_type": "Bonus Action",
            "prerequisite": "Mugetsu-no-Hamon — Moonless Blade Pattern",
            "incantation": "A shadow without moonlight… Mugetsu Hohō!",
            "description": (
                "Through silent diagonal steps, you drift like a moonless shadow across the battlefield. This flowing "
                "footwork creates an unexpected opening to draw blood before your true technique begins."
            ),
            "effects": [
                "<b>Trigger:</b> You use this as a Bonus Action.",
                "Move up to <b>15 feet</b>, but every square moved must be <i>diagonal</i>.",
                "Your next weapon attack this turn applies <b>Bleed (potency 1, duration 2)</b>.",
                "If you did not enter the same square twice during this turn, the attack deals <b>+1 slashing damage</b>."
            ],
            "tags": ["Mobility", "Bleed", "Positioning", "Bonus Action"]
        },

        {
            "name": "Mugetsu Mai — Moonless Dance",
            "action_type": "Attack Action",
            "prerequisite": "Mugetsu Hohō — Moonless Footwork",
            "incantation": "Dance beneath a moonless sky… Mugetsu Mai!",
            "description": (
                "You weave in a silent dancing step around your foe, striking from an impossible diagonal angle. "
                "The flowing motion deepens their bleeding wound in a single, elegant execution."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>one</b> weapon attack.",
                "If you moved at least <b>15 feet diagonally</b> this turn, the attack gains <b>advantage</b>.",
                "On hit, if the target was already afflicted with <b>Bleed</b> at the start of your turn, "
                "deal additional slashing damage equal to <b>Bleed Potency × 2</b>.",
                "Then, you inflict <b>Bleed (potency 1, duration 1)</b>.",
                "You may remove Bleed from the target to deal <b>+1d6 slashing damage</b>.",
                "After the attack, you may move <b>5 feet</b> without provoking opportunity attacks."
            ],
            "tags": ["Bleed", "Finisher", "Positioning", "Attack Action"]
        },

        {
            "name": "Kage-sashi — Shadow-Piercing Step",
            "action_type": "Attack Action",
            "prerequisite": "Mugetsu-no-Hamon — Moonless Blade Pattern",
            "incantation": "A thrust from the unseen… Kage-sashi!",
            "description": (
                "You slip into an enemy’s blind angle and pierce with a shadowed thrust. The technique weakens their "
                "defenses for a decisive execution."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose <b>one</b> weapon attack this turn before you hit.",
                "If you are in a <b>flanking position</b>, the attack deals <b>+1d6 slashing damage</b>.",
                "If you are the <b>only creature</b> flanking the target, apply <b>Vulnerable (potency 1, duration 1)</b>.",
                "If the target already has Vulnerable, increase its <b>duration by +1</b> (respecting max duration)."
            ],
            "tags": ["Vulnerable", "Positioning", "Attack Action"]
        },

        {
            "name": "Getsumen-Sōkei — Moonshadow Twin Path",
            "action_type": "Attack Action",
            "prerequisite": "Kage-sashi — Shadow-Piercing Step",
            "incantation": "Two cuts under a moonless sky… Getsumen-Sōkei!",
            "description": (
                "You deliver a precise twin-path strike from the target’s blind angle, opening them to a devastating "
                "follow-up blow. A technique that perfectly complements Mugetsu’s spatial mastery."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>one</b> empowered weapon attack.",
                "If you strike from a <b>diagonal square</b>, the attack gains <b>advantage</b>.",
                "On hit, deal <b>+1d6 slashing damage</b>.",
                "If the target is afflicted with <b>Vulnerable</b>, deal an additional <b>+2d6 slashing damage</b>.",
                "If the target has <b>no adjacent allies</b>, increase Vulnerable’s <b>duration by +1</b>."
            ],
            "tags": ["Vulnerable", "Finisher", "Positioning", "Attack Action"]
        }
    ],

    "Mibu no Kurai": [
        {
            "name": "Osae Ippō — Guard Step",
            "action_type": "Bonus Action",
            "prerequisite": "Mibu no Kurai",
            "incantation": "Hold the line… Osae Ippō.",
            "description": (
                "You shift your stance by a single controlled step, lowering your center of gravity and tightening "
                "your guard without compromising your stillness."
            ),
            "effects": [
                "<b>Trigger:</b> You use this as a Bonus Action.",
                "Move <b>5 feet</b> forward.",
                "Gain <b>+1 AC</b> until the start of your next turn.",
                "Your next weapon attack this turn applies <b>Vulnerable (potency 1, duration 1)</b>."
            ],
            "tags": ["Vulnerable", "Defense", "Bonus Action", "Positioning"]
        },
        {
            "name": "Mibu Gyorin — Mibu Counter",
            "action_type": "Reaction",
            "prerequisite": "Osae Ippō — Guard Step",
            "incantation": "Read… and strike—Mibu Gyorin!",
            "description": (
                "You respond instantly to an opening created by your guarded stance. Your blade lashes out the moment "
                "your opponent overextends."
            ),
            "effects": [
                "<b>Trigger:</b> You used your reaction for Deflect and Pierce.",
                "This skill counts as a follow-up to the reaction.",
                "Make another weapon attack against the attacker after your first attack.",
                "On hit, deal <b>+2d6 piercing damage</b>.",
                "If the target is afflicted with <b>Vulnerable</b>, your attack's damage is increase by the <b>Vulnerable potency X 2</b>."
            ],
            "tags": ["Reaction", "Vulnerable", "Counter", "Defense"]
        },
        {
            "name": "Mikiri Ha — Reading Blade",
            "action_type": "Attack Action",
            "prerequisite": "Mibu no Kurai",
            "incantation": "I see through you… Mikiri Ha.",
            "description": (
                "You read the enemy’s stance, testing their guard with a quiet probing cut that exposes where they "
                "will falter next."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>one</b> weapon attack.",
                "On hit, apply <b>Vulnerable (potency 1, duration 1)</b>.",
                "If the enemy attacked you since the start of your last turn, increase Vulnerable’s duration by <b>+1</b>."
            ],
            "tags": ["Vulnerable", "Attack Action", "Insight"]
        },
        {
            "name": "Kanshi-zan — Insight Sever",
            "action_type": "Attack Action",
            "prerequisite": "Mikiri Ha — Reading Blade",
            "incantation": "Your weakness… revealed—Kanshi-zan!",
            "description": (
                "You strike at the exact flaw you predicted, severing the enemy’s stance and exposing their guard "
                "to an overwhelming finishing thrust."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>one empowered weapon attack</b>.",
                "On hit, deal <b>+1d8 piercing damage</b>.",
                "If the target is afflicted with <b>Vulnerable</b>, you may remove it to deal an additional <b>2d6 damage</b> "
                "of your weapon’s type.",
                "If the target attacked you since the start of your last turn, this attack gains <b>advantage</b>."
            ],
            "tags": ["Vulnerable", "Finisher", "Attack Action", "Insight"]
        }
    ],

    "Happa-zuki": [
        {
            "name": "Renda Ippō — Chain Step",
            "action_type": "Bonus Action",
            "prerequisite": "Happa-zuki",
            "incantation": "Drive forward—Renda Ippō!",
            "description": (
                "A sharp, decisive advance that initiates the rhythm of your chained thrusts. This opening step "
                "throws your weight forward, adding force to the first strike and setting the tempo for a relentless assault."
            ),
            "effects": [
                "<b>Trigger:</b> You use this as a Bonus Action.",
                "Move up to <b>10 feet</b> toward a creature you can see and use a weapon attack on that creature.",
                "If that attack hits the <b>same target</b> you damaged last turn, increase the damage to <b>+2d4</b>.",
                "If that attack reduces that target to <b>0 hit points</b>, you gain <b>+5 feet of movement</b>."
            ],
            "tags": ["Bonus Action", "Piercing", "Aggressive", "Positioning"]
        },
        {
            "name": "Renda-zan — Linked Slash Thrust",
            "action_type": "Attack Action",
            "prerequisite": "Renda Ippō — Chain Step",
            "incantation": "Break through—Renda-zan!",
            "description": (
                "A brutal follow-through thrust unleashed after your advancing step. Each consecutive strike in your "
                "assault compounds the force of this decisive finishing thrust."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>one</b> weapon attack.",
                "On hit, deal <b>+2d6 piercing damage</b>.",
                "If you have hit this target <b>once already</b> this turn, deal an additional <b>+2d4 piercing damage</b>.",
                "If you have hit this target <b>twice already</b> this turn, deal an additional <b>+1d8 piercing damage</b>.",
                "<b>Finisher:</b> If this attack reduces the target to <b>0 hit points</b>, you immediately "
                "regain your <b>Bonus Action</b>.",
            ],
            "tags": ["Finisher", "Multi-Hit", "Piercing", "Attack Action", "Aggressive"]
        },
        {
            "name": "Shigure-dan — Drizzle Burst",
            "action_type": "Attack Action",
            "prerequisite": "Happa-zuki",
            "incantation": "Rain down—Shigure-dan!",
            "description": (
                "You unleash several quick flicking thrusts, each light but relentlessly precise, like a sudden rainfall "
                "of piercing blows. This barrage creates an opening in the opponent’s stance."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose one weapon attack you make this turn before you hit.",
                "Make <b>two</b> weapon attacks instead of one.",
                "Each attack deals <b>-1 damage</b> (minimum 1).",
                "If both attacks hit the <b>same target</b>, apply <b>Vulnerable (potency 1, duration 1)</b>.",
                "If at least one attack hits and the target already has Vulnerable, increase its <b>duration by +1</b>."
            ],
            "tags": ["Multi-Hit", "Vulnerable", "Attack Action", "Aggressive"]
        },
        {
            "name": "Happa Kyōdan — Eightfold Break",
            "action_type": "Attack Action",
            "prerequisite": "Shigure-dan — Drizzle Burst",
            "incantation": "Shatter—Happa Kyōdan!",
            "description": (
                "You channel the full aggression of Happa-zuki into a devastating decisive thrust. The strike carries the "
                "momentum of eight symbolic blows, rupturing any weakness exposed by your earlier flurry."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose one weapon attack you make this turn before you hit.",
                "On hit, deal <b>+1d8 piercing damage</b>.",
                "If the target was hit <b>twice</b> by you this turn, deal an additional <b>+2d6 piercing damage</b>.",
                "If the target is afflicted with <b>Vulnerable</b>, you may remove it to deal <b>+1d8 damage</b> "
                "of your weapon’s type."
            ],
            "tags": ["Finisher", "Vulnerable", "Multi-Hit", "Attack Action"]
        }
    ],

    "Oni-Satsu": [
        {
            "name": "Oni Ippō — Demon Step Strike",
            "action_type": "Bonus Action",
            "prerequisite": "Oni-Satsu",
            "incantation": "One heavy step… Oni Ippō!",
            "description": (
                "You take a crushing step forward and swing with raw force, striking before your full attack begins."
            ),
            "effects": [
                "<b>Trigger:</b> You use this as a Bonus Action.",
                "Make <b>one weapon attack</b>.",
                "On hit, apply <b>Crush (potency 1, duration 1)</b>.",
                "If the target is already afflicted with Crush, this attack deals <b>+1d4 bludgeoning damage</b>."
            ],
            "tags": ["Bonus Action", "Crush", "Damage"]
        },
        {
            "name": "Oni Kōdan — Demon Beatdown",
            "action_type": "Attack Action",
            "prerequisite": "Oni Ippō — Demon Step Strike",
            "incantation": "Break them apart—Oni Kōdan!",
            "description": (
                "You follow up your opening blow with a brutal full-force strike, overwhelming your opponent with "
                "a two-hit crushing assault."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Choose <b>one</b> weapon attack you make this turn before you hit.",
                "On hit, deal <b>+1d8 bludgeoning damage</b>.",
                "If you hit the same target with <b>Oni Ippō</b> this turn, deal an additional <b>+2d6</b> damage.",
                "If the target is afflicted with <b>Crush</b>, increase its <b>duration by +1</b>."
            ],
            "tags": ["Finisher", "Crush", "Damage", "Attack Action"]
        },
        {
            "name": "Oni Kōsha — Demon Cleaver",
            "action_type": "Attack Action",
            "prerequisite": "Oni-Satsu",
            "incantation": "Split them—Oni Kōsha!",
            "description": (
                "A single overhead smash with the force of an oni-slayer, crushing armor and stunning foes."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>one heavy weapon attack</b>.",
                "On hit, deal <b>+1d6 bludgeoning damage</b>.",
                "Apply <b>Crush (potency 1, duration 1)</b>.",
                "If the target already has Crush, this attack gains <b>advantage</b>."
            ],
            "tags": ["Crush", "Damage", "Attack Action"]
        },
        {
            "name": "Oni Rekkazan — Rending Mountain Slash",
            "action_type": "Attack Action",
            "prerequisite": "Oni Kōsha — Demon Cleaver",
            "incantation": "Tear mountains—Oni Rekkazan!",
            "description": (
                "You unleash a devastating full-force swing, crashing down with enough power to split stone."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                "Make <b>one empowered weapon attack</b>.",
                "On hit, deal <b>+2d8 bludgeoning damage</b>.",
                "If the target is afflicted with <b>Crush</b>, deal an additional <b>+1d6</b> damage and increase "
                "Crush’s <b>duration by +1</b>.",
                "If you moved <b>5 feet or less</b> this turn, this attack has <b>advantage</b>."
            ],
            "tags": ["Finisher", "Crush", "Damage", "Attack Action"]
        }
    ],

    "Kuzushi-no-Kamae": [
        {
            "name": "Kuzushi Fumikomi — Crushing Step-In",
            "action_type": "Bonus Action",
            "prerequisite": "Kuzushi-no-Kamae",
            "incantation": "Stay down—Kuzushi Fumikomi!",
            "description": (
                "You burst forward with a crushing step-in shove. If the target stays standing, you sweep their legs with "
                "a judo-like foot reap, slamming them to the ground."
            ),
            "effects": [
                "<b>Trigger:</b> You use your Bonus Action to Shove a creature <i>and the shove does not knock it prone</i>.",
                
                "Immediately after <b>Shove Rush</b>, you may attempt a <b>second shove</b> against the same creature.",
                
                "This second shove can only attempt to <b>knock the target prone</b> as you attempt a Judo Sweep with your leg.",
                
                "For this shove attempt, you make the contested check with <b>advantage</b>.",
                
                "If the target is knocked prone by this effect, you fiercely step on them as they take <b>1d6 bludgeoning damage</b>.",
                
                "This follow-up shove does <b>not</b> trigger Shove Rush again."
            ],
            "tags": ["Bonus Action", "Shove", "Control", "Prone", "Combo"]
        },
        {
            "name": "Kuzushi Gashō — Crushing Impale",
            "action_type": "Attack Action",
            "prerequisite": "Kuzushi Fumikomi — Crushing Step-In",
            "incantation": "Hold still—Kuzushi Gashō!",
            "description": (
                "You follow your takedown with a brutal downward thrust, driving your blade into the prone enemy with "
                "unstoppable force."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action.",
                
                "Make <b>one</b> weapon attack.",
                
                "If the target is <b>prone</b>, this attack deals <b>+2d6 piercing damage</b>.",
                
                "If the target became prone <i>this turn</i> from your shove or your abilities, "
                "this attack applies <b>Crush (potency 1, duration 1)</b> on hit.",
                
                "If the prone target also collided with a wall or creature this turn, "
                "increase the bonus damage to <b>+2d8</b> instead."
            ],
            "tags": ["Finisher", "Prone", "Crush", "Damage", "Attack Action"]
        },
        {
            "name": "Kuzushi Kake-nuki — Pitfall Clinch",
            "action_type": "Attack Action",
            "prerequisite": "Kuzushi-no-Kamae",
            "incantation": "You're not getting up—Kuzushi Kake-nuki!",
            "description": (
                "You hurl yourself onto a prone enemy, locking their limbs in a crushing grounded clinch. "
                "Once you secure the hold, neither of you can freely move until one breaks the other."
            ),
            "effects": [
                "<b>Trigger:</b> When you take the Attack Action against a <b>prone creature</b>.",
                
                "Make <b>one</b> weapon attack.",
                
                "On hit, the creature takes normal damage and becomes <b>Grappled</b> by you.",
                
                "You and the grappled creature both become <b>Restrained</b> for the duration of the grapple.",
                
                "The grappled creature may attempt to escape as normal using its <b>Action</b> "
                "(contested Strength (Athletics) or Dexterity (Acrobatics) vs your Strength (Athletics)).",
                
                "You may release the grapple at any time (no action required).",
                
                "The target also gains <b>Crush (potency 1, duration 1)</b> when this grapple begins "
                "and that refreshes at the start of every turn of yours <b>while you're both restrained this way</b>."
            ],
            "tags": ["Prone", "Grapple", "Restrained", "Crush", "Control", "Attack Action"]
        },
        {
            "name": "Kuzushi Hazushi — Joint-Break Hold",
            "action_type": "Attack Action",
            "prerequisite": "Kuzushi Kake-nuki — Pitfall Clinch",
            "incantation": "Bones don't bend that way—Kuzushi Hazushi!",
            "description": (
                "With the enemy pinned beneath you, you torque their limb in a vicious lock, threatening to break it with "
                "a single brutal wrench."
            ),
            "effects": [
                "<b>Trigger:</b> While you are grappling a prone creature.",
                
                "Make <b>one</b> weapon attack with advantage.",
                
                "On hit, deal <b>+2d6 bludgeoning damage</b> as you torque the limb.",
                
                "If the target is afflicted with <b>Crush</b>, increase the bonus damage to <b>+3d6</b> "
                "and extend Crush’s duration by <b>+1</b>.",
                
                "If this reduces the creature to <b>0 HP</b>, the limb breaks with a loud snap and you may stand up "
                "without using movement."
            ],
            "tags": ["Finisher", "Prone", "Grapple", "Crush", "Damage", "Attack Action"]
        }
    ],
}
