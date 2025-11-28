from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class CharacterIntroPanel(QFrame):
    def __init__(self, servant_data, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)

        name = servant_data["name"]
        element = servant_data["primary"]
        description = servant_data.get("intro", "")

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        html = f"""
        <h2>{name} — Knight of {element}</h2>
        <p>{description}</p>

        <h3>Critical Exploit</h3>
        <p>{servant_data.get("critical_exploit_summary", "A powerful finisher unique to this Knight.")}</p>
        """
        label = QLabel(html)
        label.setWordWrap(True)
        layout.addWidget(label)

        self.setLayout(layout)
