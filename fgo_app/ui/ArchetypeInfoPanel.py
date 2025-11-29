# ArchetypeInfoPanel.py
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

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

        if "Knights" in archetype_name:
            label.setText("""
            <h2>Knight's Resolve</h2>
            <p>Knights wield elemental power through martial discipline, gaining Resolve as they act with chivalry on the battlefield.</p>

            <h3>Gaining Resolve</h3>
            <ul>
                <li>Hit a target afflicted by your Primary Element</li>
                <li>Reduce a creature to 0 HP</li>
                <li>Protect an ally</li>
                <li>Apply your Primary Element for the first time in a round</li>
            </ul>
            <h3>Spending 3 Resolve — Knight's Valor</h3>
            <ul>
                <li><b>Elemental Edge:</b> Empower your next attack by consuming your element.</li>
                <li><b>Chivalric Defense:</b> Gain resistance to your Primary Element.</li>
                <li><b>Hero's Surge:</b> Make one additional weapon attack.</li>
                <li><b>Radiant Shield:</b> Gain temporary HP.</li>
            </ul>
            <h3>Spending 6 Resolve — Critical Exploit</h3>
            <p>A devastating elemental finisher unique to each Knight. See an individual character page for details.</p>
            """)
        elif "Shinsengumi" in archetype_name:
            label.setText("""
                <h2>Shinsengumi Archetype — Overview</h2>
                <p>Shinsengumi excel at swift, precise strikes and battlefield repositioning, rewarding decisive aggression and discipline.</p>
                <p><i>(Detailed mechanics TBD.)</i></p>
            """)
        elif "Argonauts" in archetype_name:
            label.setText("""
                <h2>Argonauts Archetype — Overview</h2>
                <p>Argonauts embody heroic momentum and mythic synergy, growing stronger as the party overcomes adversity together.</p>
                <p><i>(Detailed mechanics TBD.)</i></p>
            """)
        else:
            label.setText(f"<h2>{archetype_name}</h2><p>No archetype information available yet.</p>")

        layout.addWidget(label)
