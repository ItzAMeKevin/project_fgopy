import json
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget, QHBoxLayout
)
from PyQt5.QtCore import Qt

class StatusEffectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Status Effects")
        self.setMinimumWidth(780)
        self.setMinimumHeight(980)

        # Load JSON
        with open("fgo_app/resources/status_effects.json", "r") as f:
            self.effects = json.load(f)

        # --------- MAIN LAYOUT ----------
        layout = QVBoxLayout(self)

        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)

        container = QWidget()
        scroll_layout = QVBoxLayout(container)
        scroll.setWidget(container)

        # --------- LIST ALL EFFECTS ----------
        for name, data in self.effects.items():
            item = self.build_effect_item(name, data)
            scroll_layout.addWidget(item)

        scroll_layout.addStretch()

    # ----------------------------------------
    def build_effect_item(self, name, data):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(2)

        # Title
        title = QLabel(f"<h2>{name}</h2>")
        layout.addWidget(title)

        # Type badge (color-coded)
        type_color = {
            "positive": "#4CAF50",
            "negative": "#E53935",
            "neutral": "#FFB300"
        }.get(data["type"], "#AAAAAA")

        type_label = QLabel(
            f"<b>Type:</b> <span style='color:{type_color}'>{data['type'].capitalize()}</span>"
        )
        layout.addWidget(type_label)

        # Description
        desc = QLabel(f"<i>{data['description']}</i>")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        # Potency
        potency = data.get("potency", None)
        max_potency = data.get("max_potency", None)
        layout.addWidget(QLabel(f"<b>Potency:</b> {potency}"))
        layout.addWidget(QLabel(f"<b>Max Potency:</b> {max_potency if max_potency is not None else 'No Limit'}"))

        # Duration
        duration = data.get("duration", None)
        max_duration = data.get("max_duration", None)
        layout.addWidget(QLabel(f"<b>Duration:</b> {duration}"))
        layout.addWidget(QLabel(f"<b>Max Duration:</b> {max_duration}"))

        # Spacing line
        separator = QLabel("<hr>")
        layout.addWidget(separator)

        return widget
