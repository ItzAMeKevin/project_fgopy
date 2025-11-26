from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class SkillDescriptionDialog(QDialog):
    def __init__(self, skill, tree_widget):
        super().__init__()

        self.tree = tree_widget
        self.data = skill

        self.setWindowTitle(skill["name"])
        self.setMinimumWidth(750)

        layout = QVBoxLayout(self)

        title = QLabel(f"<b>{skill['name']}</b>")
        layout.addWidget(title)

        incant = skill.get("incantation")
        if incant:
            incant_lbl = QLabel(f"<i>\"{incant}\"</i>")
            incant_lbl.setAlignment(Qt.AlignCenter)
            incant_lbl.setStyleSheet("font-size: 24px; color: #5599ff; margin-bottom: 8px;")
            incant_lbl.setWordWrap(True)
            layout.addWidget(incant_lbl)

        action_type = skill.get("action_type", None)
        if action_type:
            action_lbl = QLabel(f"<b>Action Type:</b> {action_type}")
            action_lbl.setWordWrap(True)
            layout.addWidget(action_lbl)

        if skill.get("description"):
            lore = QLabel(f"<i>{skill['description']}</i>")
            lore.setWordWrap(True)
            lore.setAlignment(Qt.AlignLeft)
            layout.addWidget(lore)
            layout.addSpacing(8)

        effects = skill.get("effects", [])
        if effects:
            layout.addSpacing(6)
            eff_title = QLabel("<b>Effects:</b>")
            layout.addWidget(eff_title)

            # Convert effects array into HTML bullet list
            bullets_html = "<ul>" + "".join(f"<li>{e}</li>" for e in effects) + "</ul>"
            eff_label = QLabel(bullets_html)
            eff_label.setWordWrap(True)
            layout.addWidget(eff_label)

        layout.addSpacing(15)

        prereq = skill.get("prerequisite")
        if prereq:
            prereq_lbl = QLabel(f"<b>Prerequisite:</b> {prereq}")
        else:
            prereq_lbl = QLabel("<b>Prerequisite:</b> None")

        layout.addWidget(prereq_lbl)

        layout.addStretch()

        unlock_btn = QPushButton("Unlock Skill")
        unlock_btn.setObjectName("unlock_btn")
        unlock_btn.clicked.connect(self.on_unlock)
        unlock_btn.setCursor(Qt.PointingHandCursor)

        already_unlocked = self.tree.is_unlocked[skill["name"]]
        prereq_missing = prereq is not None and not self.tree.is_unlocked.get(prereq, False)

        if already_unlocked or prereq_missing:
            unlock_btn.setEnabled(False)

        layout.addWidget(unlock_btn, alignment=Qt.AlignCenter)

    def on_unlock(self):
        self.tree.unlock(self.data["name"])
        self.accept()