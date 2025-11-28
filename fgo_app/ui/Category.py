import os
from PyQt5.QtWidgets import (
    QWidget, QLabel, QToolButton, QVBoxLayout, QHBoxLayout,
    QFrame
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from fgo_app.ui.ArchetypeInfoPanel import ArchetypeInfoPanel


# =============================================================
#  Image cropping utility (unchanged)
# =============================================================

def load_and_crop(path, target_w, target_h):
    """Center-crop + resize image (Qt version)."""
    img = QImage(path)
    if img.isNull():
        fallback = QImage(target_w, target_h, QImage.Format_RGBA8888)
        fallback.fill(Qt.darkGray)
        return QPixmap.fromImage(fallback)

    src_w, src_h = img.width(), img.height()
    scale = max(target_w / src_w, target_h / src_h)
    new_w = int(src_w * scale)
    new_h = int(src_h * scale)

    scaled = img.scaled(new_w, new_h, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2

    cropped = scaled.copy(left, top, target_w, target_h)
    return QPixmap.fromImage(cropped)


# =============================================================
#  Collapsible Category (Option B: QToolButton with indicator)
# =============================================================

class CollapsibleCategory(QWidget):

    def __init__(self, title="", parent=None, start_expanded=False):
        super().__init__(parent)

        self._expanded = start_expanded

        # Main container layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header frame
        header_frame = QWidget()
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(6, 4, 6, 4)
        header_layout.setSpacing(8)

        # =========================================================
        #  QToolButton (REAL arrow indicator)
        # =========================================================

        self.toggle_btn = QToolButton()
        self.toggle_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toggle_btn.setArrowType(Qt.DownArrow if self._expanded else Qt.RightArrow)
        self.toggle_btn.setText(title)
        self.toggle_btn.setCheckable(True)
        self.toggle_btn.setChecked(self._expanded)
        self.toggle_btn.setObjectName("CategoryButton")  # QSS styling
        self.toggle_btn.clicked.connect(self.toggle)

        header_layout.addWidget(self.toggle_btn)
        header_layout.addStretch()

        main_layout.addWidget(header_frame)

        # Content area
        self.content_area = QFrame()
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(10, 6, 10, 10)

        main_layout.addWidget(self.content_area)

        # Initial state
        if not self._expanded:
            self.content_area.hide()

    # Allow MainWindow to inject an external layout
    def setContentLayout(self, layout):
        # Replace previous layout safely
        QWidget().setLayout(self.content_layout)
        self.content_layout = layout
        self.content_area.setLayout(layout)

    # Expand/collapse logic
    def toggle(self):
        self._expanded = not self._expanded

        if self._expanded:
            self.content_area.show()
            self.toggle_btn.setArrowType(Qt.DownArrow)
        else:
            self.content_area.hide()
            self.toggle_btn.setArrowType(Qt.RightArrow)

        self.toggle_btn.setChecked(self._expanded)
