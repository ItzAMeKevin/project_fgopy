from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QScrollArea, QGridLayout, QSizePolicy
)
from PyQt5.QtGui import QPixmap
import sys, os

from fgo_app.ui.Category import CollapsibleCategory
from fgo_app.ui.CharacterPage import CharacterPage
from fgo_app.data.FgoGameData import CHARACTERS


class MainWindow(QWidget):
    CARD_IMG_W = 256
    CARD_IMG_H = 362

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fate Grand Order - Servant Core")
        self.resize(1600, 900)

        self.main_layout = QVBoxLayout(self)
        self.build_main_page()

    def build_main_page(self):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        header = QWidget()
        header.setObjectName("main-header")   # for QSS styling
        header_layout = QVBoxLayout(header)
        header_layout.setContentsMargins(20, 12, 20, 12)

        title = QLabel("Choose your Servant Core")
        title.setObjectName("main-header-title")
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        header_layout.addWidget(title)

        self.main_layout.addWidget(header)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()
        vbox = QVBoxLayout(container)

        # Create collapsible categories
        for category_name, character_list in CHARACTERS.items():
            col = CollapsibleCategory(category_name)
            grid = QGridLayout()
            grid.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            col.setContentLayout(grid)

            # Insert characters
            for i, ch in enumerate(character_list):
                r, c = divmod(i, 5)

                # Card widget
                card = QWidget()
                card.setObjectName("character-card")
                card.setProperty("class", "character-card")
                card.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                card_layout = QVBoxLayout(card)
                card_layout.setContentsMargins(6, 6, 6, 6)
                card_layout.setSpacing(6)

                # Load thumbnail
                if os.path.exists(ch["image"]):
                    pixmap = QPixmap(ch["image"]).scaled(
                        self.CARD_IMG_W, self.CARD_IMG_H, Qt.KeepAspectRatio, Qt.SmoothTransformation
                    )
                else:
                    pixmap = QPixmap(self.CARD_IMG_W, self.CARD_IMG_H)
                    pixmap.fill(Qt.gray)

                img_label = QLabel()
                img_label.setPixmap(pixmap)
                card_layout.addWidget(img_label)

                name_label = QLabel(ch["name"])
                name_label.setStyleSheet("font-weight: bold; margin-top: 6px;")
                name_label.setObjectName("character-card")
                name_label.setAlignment(Qt.AlignCenter)
                card_layout.addWidget(name_label)

                # OPEN BUTTON
                btn = QPushButton("Select")
                btn.setObjectName("open_button_" + ch["name"])
                btn.clicked.connect(lambda _, n=ch["name"]: self.open_character_page(n))
                card_layout.addWidget(btn)

                grid.addWidget(card, r, c)

            vbox.addWidget(col)

        vbox.addStretch()
        scroll.setWidget(container)
        self.main_layout.addWidget(scroll)

    def open_character_page(self, character_name):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        page = CharacterPage(character_name, self.build_main_page)
        self.main_layout.addWidget(page)

if __name__ == "__main__":
    with open("style/fgo_theme.qss", "r") as f:
        style = f.read()
    app = QApplication(sys.argv)
    app.setStyleSheet(style)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
