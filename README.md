📘 project_fgopy — FGO-Themed Servant Core Builder

A Fate/Grand Order–inspired desktop application built with Python + PyQt5.
This tool is designed for tabletop RPGs (like D&D 5E miniseries campaigns) where players unlock Servant abilities, skills, and armaments using a visual skill tree system.

The app provides:

* A servant selection screen

* Categories (Knights of the Round Table, Shinsengumi, etc.)

* Beautiful character cards

* Auto-layout FGO-style node trees

* Unlock system with prerequisites

* Save & load functionality

* Hover, highlight, and padlock icons for locked skills

* FGO-like UI styling via QSS themes

🌟 Features
🧬 Servant Selection

Browse servants grouped by categories. Each servant has:

* A character card

* Portrait image

* Category collapsible sections

* Smooth hover and glow effects

🌳 Armament & Skill Trees

Each servant has one or several Armaments, each containing a tree of unlockable Skills:

* Auto-centered tree layout

* Locked nodes show a padlock icon

* Hover highlight (blue border)

* Click to view detailed skill or armament descriptions

🔓 Unlock System

* Each node unlock requires explicit confirmation

* Unlock buttons are disabled unless prerequisites are met

* Built-in JSON save system preserving progress

* Nodes visually update on unlock

🎨 Theme System

Uses a full FGO-inspired QSS theme:

* Deep blues, gold borders, white typography

* Styled buttons, scrollbars, dialogs, cards

* Easy to modify