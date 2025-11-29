from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from fgo_app.ui.SkillDialog import SkillDescriptionDialog
from fgo_app.ui.ArmamentDialog import ArmamentDescriptionDialog
from fgo_app.data.FgoGameData import ARMAMENT_SKILLS, CHAR_ARMAMENTS, ARCHETYPES, get_archetype_for_character
from fgo_app.data.FgoGameData import getCharacter
from fgo_app.ui.StatusEffectDialog import StatusEffectDialog


class FinalChoicePage(QWidget):
    def __init__(self, character_name, unlocked, on_back):
        super().__init__()

        self.character_name = character_name
        self.unlocked_nodes = unlocked
        self.on_back = on_back

        self.character_data = getCharacter(character_name)

        main_layout = QVBoxLayout(self)

        # Scroll Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        main_layout.addWidget(scroll)

        scroll_contents = QFrame()
        scroll_layout = QVBoxLayout(scroll_contents)
        scroll.setWidget(scroll_contents)

        # Back button
        back_button = QPushButton("Back")
        back_button.setFixedWidth(100)
        back_button.clicked.connect(self.on_back)
        scroll_layout.addWidget(back_button, alignment=Qt.AlignLeft)

        # Title
        title = QLabel(f"<h1>{character_name}</h1>")
        title.setAlignment(Qt.AlignCenter)
        scroll_layout.addWidget(title)

        # Archetype Row
        archetype_name = get_archetype_for_character(self.character_name)
        if archetype_name and archetype_name in ARCHETYPES:

            archetype_section = QWidget()
            archetype_layout = QVBoxLayout(archetype_section)
            archetype_layout.setContentsMargins(10, 10, 10, 10)

            archetype_label = QLabel()
            archetype_label.setTextFormat(Qt.RichText)
            archetype_label.setWordWrap(True)
            archetype_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            archetype_label.setText(
                f"<h2>{archetype_name}</h2>" + ARCHETYPES[archetype_name]
            )

            archetype_layout.addWidget(archetype_label)
        else:
            # If no archetype found, add empty stretch for spacing
            archetype_layout.addStretch()
        scroll_layout.addWidget(archetype_section)

        # Portrait + description
        row = QHBoxLayout()

        portrait_label = QLabel()
        pixmap = QPixmap(self.character_data["image"])
        portrait_label.setPixmap(pixmap.scaledToWidth(300, Qt.SmoothTransformation))
        row.addWidget(portrait_label)

        desc_label = QLabel(self.character_data["description"]["mini_ult"])
        desc_label.setWordWrap(True)
        row.addWidget(desc_label)

        scroll_layout.addLayout(row)

        # BOTTOM: Section separated in two

        bottom_row = QHBoxLayout()
        scroll_layout.addLayout(bottom_row)

        # LEFT: Unlocked nodes section
        unlocked_section = QVBoxLayout()
        bottom_row.addLayout(unlocked_section)

        unlocked_title = QLabel("<h2>Unlocked Armament & Skills</h2>")
        unlocked_section.addWidget(unlocked_title)

        skills_list_widget = QWidget()
        skills_list_layout = QVBoxLayout(skills_list_widget)
        skills_list_layout.setContentsMargins(0, 0, 0, 0)
        skills_list_layout.setSpacing(6)

        if self.unlocked_nodes:
            for name in self.unlocked_nodes:
                btn = QPushButton(name)
                btn.setObjectName("FinalPageNode")
                btn.clicked.connect(lambda _, n=name: self.open_description(n))
                skills_list_layout.addWidget(btn)
        else:
            skills_list_layout.addWidget(QLabel("No skills unlocked yet."))

        skills_list_layout.addStretch()
        unlocked_section.addWidget(skills_list_widget, stretch=3)

        # RIGHT: Helper section
        helper_column = QVBoxLayout()
        helper_column.setAlignment(Qt.AlignTop)

        helper_title = QLabel("<h2>Help & Tips</h2>")
        helper_column.addWidget(helper_title)
        status_btn = QPushButton("Status Effects")
        status_btn.setObjectName("FinalPageNode")
        status_btn.setFixedWidth(160)
        status_btn.clicked.connect(self.show_status_effects)

        helper_column.addWidget(status_btn)
        helper_column.addStretch()

        bottom_row.addLayout(helper_column, stretch=0)

        scroll_layout.addStretch()


    def show_status_effects(self):
        dlg = StatusEffectDialog(self)
        dlg.exec_()


    def open_description(self, name):
        # First check if it's an armament
        armaments = CHAR_ARMAMENTS.get(self.character_name, [])
        for arm in armaments:
            if arm["name"] == name:
                dialog = ArmamentDescriptionDialog(
                    data=arm,
                    unlock_callback= None,
                    can_unlock=False
                )
                dialog.exec_()
                return

        # Otherwise it must be a skill (if it exists)
        for arm in armaments:
            arm_name = arm["name"]
            for sk in ARMAMENT_SKILLS.get(arm_name, []):
                if sk["name"] == name:
                    dlg = SkillDescriptionDialog(
                        data=sk,            # NOTE: parameter is "data", not "skill_data"
                        unlock_callback=None,
                        can_unlock=False,
                        parent=self
                    )
                    dlg.exec_()
                    return

        # Fallback
        print(f"No description found for {name}")
