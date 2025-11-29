from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt

from fgo_app.ui.SkillTree import SkillTreeWidget
from fgo_app.data.FgoGameData import CHAR_ARMAMENTS, ARMAMENT_SKILLS, getCharacter


class CharacterPage(QWidget):
    def __init__(self, character_name, on_back):
        super().__init__()
        all_armament_names = [a["name"] for a in CHAR_ARMAMENTS[character_name]]

        self.character_name = character_name
        self.character_data = getCharacter(self.character_name)
        self.on_back = on_back
        self.unlocked_state = SkillTreeWidget.load_progress_static(character_name)

        main_layout = QVBoxLayout(self)

        # Header bar
        top = QHBoxLayout()
        back_btn = QPushButton("← Back")
        back_btn.clicked.connect(self.on_back)
        top.addWidget(back_btn)

        title = QLabel(character_name)
        title.setStyleSheet("font-size: 34px; font-weight: bold; margin-left: 15px;")
        top.addWidget(title)
        top.addStretch()

        main_layout.addLayout(top)

        # Scroll Area

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scroll_container = QWidget()
        scroll_layout = QVBoxLayout(scroll_container)

        # Description Bar
        middle = QHBoxLayout()
        middle.setContentsMargins(10, 6, 10, 10)
        middle.setSpacing(10)
        description = QLabel()
        description.setObjectName("Description")
        description.setWordWrap(True)
        description.setTextFormat(Qt.RichText)
        description.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        description.setText(self.character_data["description"])
        middle.addWidget(description)
        scroll_layout.addLayout(middle)

        # Section Title
        label = QLabel(f"Armament Trees")
        label.setStyleSheet("font-size: 30px; font-weight: bold; margin-top: 10px; margin-bottom: 10px;")
        scroll_layout.addWidget(label)

        # Retrieve servant's armaments
        armaments = CHAR_ARMAMENTS.get(character_name, [])

        # Show each armament tree, one below another
        for arm in armaments:
            arm_name = arm["name"]
            arm_data = arm

            # Title for this armament
            arm_title = QLabel(f"⚔️ {arm_name}")
            arm_title.setStyleSheet("font-size: 28px; font-weight: bold; margin-top: 15px;")
            scroll_layout.addWidget(arm_title)

            # Skills for this armament
            skills = ARMAMENT_SKILLS.get(arm_name, [])

            # Create the tree widget
            tree = SkillTreeWidget(arm_name, skills, character_name, arm_data, all_armament_names, self.unlocked_state)
            tree.setMinimumHeight(450)  # Adjust if needed

            scroll_layout.addWidget(tree)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_container)

        main_layout.addWidget(scroll)