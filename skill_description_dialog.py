from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class SkillDescriptionDialog(QDialog):
    def __init__(self, skill, tree_widget):
        super().__init__()

        self.tree = tree_widget
        self.data = skill

        self.setWindowTitle(skill["name"])
        self.setMinimumWidth(400)

        layout = QVBoxLayout(self)

        title = QLabel(f"<b>{skill['name']}</b>")
        layout.addWidget(title)

        desc = QLabel(f"<i>{skill['description']}</i>")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        layout.addSpacing(50)

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