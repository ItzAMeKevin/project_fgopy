from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class ArmamentDescriptionDialog(QDialog):
    def __init__(self, armament_data, tree_widget):
        super().__init__()
        self.tree = tree_widget
        self.data = armament_data

        self.setWindowTitle(armament_data["name"])

        layout = QVBoxLayout()

        name = QLabel(f"<b>{armament_data['name']}</b>")
        name.setAlignment(Qt.AlignCenter)
        layout.addWidget(name)

        desc = QLabel(f"<i>{armament_data['description']}</i>")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        type_label = QLabel(f"<b>Type:</b> {armament_data['type']}")
        layout.addWidget(type_label)

        # Unlock button
        unlock_btn = QPushButton("Unlock Armament")
        unlock_btn.setObjectName("unlock_btn")
        unlock_btn.clicked.connect(self.on_unlock)
        unlock_btn.setCursor(Qt.PointingHandCursor)

        if self.tree.is_unlocked[self.data["name"]]:
            unlock_btn.setEnabled(False)
        
        layout.addWidget(unlock_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.setMinimumWidth(320)

    def on_unlock(self):
        self.tree.unlock(self.data["name"])
        self.accept()