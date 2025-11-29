# ArchetypeInfoPanel.py
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from fgo_app.data.FgoGameData import ARCHETYPES

class ArchetypeInfoPanel(QFrame):
    def __init__(self, archetype_name, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)

        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(10, 10, 10, 10)

        label = QLabel()
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        if archetype_name in ARCHETYPES:
            label.setText(ARCHETYPES[archetype_name])
        else:
            # Fallback message
            label.setText(
                f"<h2>{archetype_name}</h2>"
                "<p>No archetype information available yet.</p>"
            )

        layout.addWidget(label)
