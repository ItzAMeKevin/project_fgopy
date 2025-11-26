from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

from skill_tree_widget import SkillTreeWidget
from servant_data import CHAR_ARMAMENTS, ARMAMENT_SKILLS


class CharacterPage(QWidget):
    def __init__(self, character_name, on_back):
        super().__init__()

        self.character = character_name
        self.on_back = on_back

        layout = QVBoxLayout(self)

        # Header bar
        top = QHBoxLayout()
        back_btn = QPushButton("← Back")
        back_btn.clicked.connect(self.on_back)
        top.addWidget(back_btn)

        title = QLabel(character_name)
        title.setStyleSheet("font-size: 28px; font-weight: bold; margin-left: 15px;")
        top.addWidget(title)
        top.addStretch()

        layout.addLayout(top)

        # Section Title
        label = QLabel(f"{character_name} — Armament Trees")
        label.setStyleSheet("font-size: 30px; font-weight: bold; margin-top: 10px; margin-bottom: 10px;")
        layout.addWidget(label)

        # Retrieve servant's armaments
        armaments = CHAR_ARMAMENTS.get(character_name, [])

        # Show each armament tree, one below another
        for arm in armaments:
            arm_name = arm["name"]
            arm_data = arm

            # Title for this armament
            arm_title = QLabel(f"⚔️ {arm_name}")
            arm_title.setStyleSheet("font-size: 28px; font-weight: bold; margin-top: 15px;")
            layout.addWidget(arm_title)

            # Skills for this armament
            skills = ARMAMENT_SKILLS.get(arm_name, [])

            # Create the tree widget
            tree = SkillTreeWidget(arm_name, skills, character_name, arm_data)
            tree.setMinimumHeight(450)  # Adjust if needed

            layout.addWidget(tree)

        layout.addStretch()
