from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton,
    QWidget, QScrollArea, QHBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt

class BaseDescriptionDialog(QDialog):
    def __init__(
        self,
        title,
        description,
        effects,
        extra_fields=None,
        unlock_callback=None,
        can_unlock=False,
        is_unlocked=False,
        parent=None
    ):
        super().__init__(parent)
        self.setWindowTitle(title)

        # ---- DIMENSIONS ----
        self.setMinimumWidth(720)
        self.setMaximumHeight(700)

        main_layout = QVBoxLayout(self)

        # ============================================================
        #  TOP: TITLE
        # ============================================================
        title_label = QLabel(f"<h1 style='text-align:center'>{title}</h1>")
        main_layout.addWidget(title_label)

        # ============================================================
        #  MIDDLE: SCROLLABLE CONTENT
        # ============================================================
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        scroll_layout = QVBoxLayout(content)
        scroll.setWidget(content)

        # Expand scroll to fill space but not overflow past max height
        scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(scroll)

        # ---- DESCRIPTION ----
        if description:
            desc_label = QLabel(f"<p><i>{description}</i></p>")
            desc_label.setWordWrap(True)
            scroll_layout.addWidget(desc_label)

        # ---- EXTRA FIELDS ----
        if extra_fields:
            for label, value in extra_fields.items():
                if value is None:
                    continue
                field = QLabel(f"<b>{label}:</b> {value}")
                field.setWordWrap(True)
                scroll_layout.addWidget(field)

        # ---- EFFECTS ----
        if effects:
            html_list = "<ul>" + "".join([f"<li>{e}</li>" for e in effects]) + "</ul>"
            effects_label = QLabel(html_list)
            effects_label.setWordWrap(True)
            scroll_layout.addWidget(effects_label)

        scroll_layout.addStretch()

        # ============================================================
        #  BOTTOM: FIXED FOOTER WITH BUTTON
        # ============================================================
        footer = QHBoxLayout()
        footer.setAlignment(Qt.AlignCenter)

        self.unlock_btn = QPushButton()
        footer.addWidget(self.unlock_btn)

        main_layout.addLayout(footer)

        # ============================================================
        #  BUTTON LOGIC
        # ============================================================
        # State 1: Already unlocked
        if is_unlocked:
            self.unlock_btn.setText("Unlocked")
            self.unlock_btn.setDisabled(True)

        # State 2: Unlockable
        elif can_unlock and unlock_callback:
            self.unlock_btn.setText("Unlock")

            def do_unlock():
                unlock_callback()
                self.unlock_btn.setDisabled(True)
                self.unlock_btn.setText("Unlocked")

            self.unlock_btn.clicked.connect(do_unlock)

        # State 3: Locked
        else:
            self.unlock_btn.setText("Locked")
            self.unlock_btn.setDisabled(True)

        # Let Qt compute the correct initial dialog size
        self.adjustSize()

        # But do not exceed the allowed maximum height
        if self.height() > 700:
            self.resize(self.width(), 700)
