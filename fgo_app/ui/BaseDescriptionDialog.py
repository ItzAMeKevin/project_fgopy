# base_description_dialog.py

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton,
    QWidget, QScrollArea, QHBoxLayout
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
        parent=None
    ):
        super().__init__(parent)
        self.setWindowTitle(title)

        # ---- WIDTH RESTORED ----
        self.setMinimumWidth(720)

        main_layout = QVBoxLayout(self)

        # ---- Title ----
        title_label = QLabel(f"<h1 style='text-align:center'>{title}</h1>")
        main_layout.addWidget(title_label)

        # ---- Scroll Area ----
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        scroll_layout = QVBoxLayout(content)
        scroll.setWidget(content)
        main_layout.addWidget(scroll)

        # ---- DESCRIPTION (now in italic & BEFORE fields) ----
        if description:
            desc_html = f"<p><i>{description}</i></p>"
            desc_label = QLabel(desc_html)
            desc_label.setWordWrap(True)
            scroll_layout.addWidget(desc_label)

        # ---- EXTRA FIELDS (Type, Action Type, Incantation, Prerequisite) ----
        if extra_fields:
            for label, value in extra_fields.items():
                if value is None:
                    continue
                field = QLabel(f"<b>{label}:</b> {value}")
                field.setWordWrap(True)
                scroll_layout.addWidget(field)

        # ---- EFFECTS (bullet list) ----
        if effects:
            html_list = "<ul>" + "".join([f"<li>{e}</li>" for e in effects]) + "</ul>"
            effects_label = QLabel(html_list)
            effects_label.setWordWrap(True)
            scroll_layout.addWidget(effects_label)

        # ---- UNLOCK BUTTON SUPPORT ----
        self.unlock_btn = None
        if can_unlock and unlock_callback:
            self.unlock_btn = QPushButton("Unlock")

            def do_unlock():
                unlock_callback()          # perform unlock
                self.unlock_btn.setDisabled(True)   # disable button
                self.unlock_btn.setText("Unlocked") # optional, looks good

            self.unlock_btn.clicked.connect(do_unlock)
            scroll_layout.addWidget(self.unlock_btn)

        elif unlock_callback:
            self.unlock_btn = QPushButton("Unlocked")
            self.unlock_btn.setDisabled(True)
            scroll_layout.addWidget(self.unlock_btn)
