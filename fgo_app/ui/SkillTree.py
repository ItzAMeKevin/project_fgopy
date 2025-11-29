from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PyQt5.QtGui import QPen, QBrush, QPainter, QColor
from PyQt5.QtCore import Qt, QRectF, QPointF

from fgo_app.ui.SkillDialog import SkillDescriptionDialog
from fgo_app.ui.ArmamentDialog import ArmamentDescriptionDialog
from style.theme_loader import theme
from fgo_app.utils import resource_path

import json
import os

# ============================================================
#  OVERRIDDEN COLORS (better locked/unlocked clarity)
# ============================================================

# Armament colors
ARMAMENT_UNLOCKED_FILL  = QColor("#ffe9a3")     # bright gold
ARMAMENT_UNLOCKED_BORDER = QColor("#d8ad2f")

ARMAMENT_LOCKED_FILL    = QColor("#cec6a4")
ARMAMENT_LOCKED_BORDER  = QColor("#8b835e")

# Skill colors
UNLOCKED_FILL           = QColor("#bde2ff")     # bright blue
UNLOCKED_BORDER         = QColor("#2c7ad1")

UNLOCKABLE_BORDER       = QColor("#6fa9ff")

LOCKED_FILL             = QColor("#c4c7d1")     # locked (prereq unmet)
LOCKED_BORDER           = QColor("#80838d")

# Hover
HOVER_BORDER            = QColor("#00b4ff")

CONNECTION_COLOR        = theme.get_color("Tree", "connection_line")
SAVE_FILE = "fgo_app/saves/servant_progress.json"


# ============================================================
#  SKILL TREE WIDGET
# ============================================================

class SkillTreeWidget(QGraphicsView):
    def __init__(self, armament_name, skills, servant_name, armament_data, all_armament_names, shared_unlocked):
        super().__init__()

        self.armament_name = armament_name
        self.skills = skills
        self.servant_name = servant_name
        self.armament_data = armament_data
        self.all_armament_names = all_armament_names

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)

        # Storage
        self.node_items = {}
        self.node_rectangles = {}
        self.original_brush = {}
        self.original_pen = {}

        self.hovered_node = None
        self.clicked_node = None

        # Unlock state
        self.is_unlocked = shared_unlocked
        self.prereq_map = {}

        # Armament starts LOCKED
        self.is_unlocked[self.armament_name] = False
        self.prereq_map[self.armament_name] = None

        # Skills start locked
        for sk in skills:
            name = sk["name"]
            prereq = sk["prerequisite"]
            self.prereq_map[name] = prereq
            self.is_unlocked[name] = False

        self.setMouseTracking(True)
        self.load_progress(servant_name)
        self.draw_tree()

    # ---------------------------------------------------------
    # UNLOCK NODE PROGRAMMATICALLY + SAVE PROGRESS
    # ---------------------------------------------------------

    def can_unlock_armament(self):
        for name in self.all_armament_names:
            if self.is_unlocked.get(name, False):
                return False
        return True

    def unlock(self, name):
        """Unlock a node programmatically after confirmation."""
        if name in self.all_armament_names:
            for other in self.all_armament_names:
                self.is_unlocked[other] = (other == name)
        else:
            self.is_unlocked[name] = True

        rect = self.node_rectangles[name]
        self.apply_node_colors(name, rect)

        # Save progress
        self.save_progress(self.servant_name)
        self.load_progress(self.servant_name)
        for node, rect in self.node_rectangles.items():
            self.apply_node_colors(node, rect)
    
    @staticmethod
    def load_progress_static(servant_name):
        try:
            with open(resource_path(SAVE_FILE)) as f:
                data = json.load(f)
                return {name: True for name in data.get(servant_name, {}).get("unlocked", [])}
        except:
            return {}
    
    def load_progress(self, servant_name):
        """Load saved unlocked skills for this servant."""
        if not os.path.exists(resource_path(SAVE_FILE)):
            return

        with open(resource_path(SAVE_FILE)) as f:
            data = json.load(f)

        if servant_name not in data:
            return

        saved = data[servant_name]["unlocked"]
        for name in saved:
            self.is_unlocked[name] = True

    def save_progress(self, servant_name):
        os.makedirs(resource_path(os.path.dirname(SAVE_FILE)), exist_ok=True)
        data = {}
        if os.path.exists(resource_path(SAVE_FILE)):
            try:
                with open(resource_path(SAVE_FILE), "r") as f:
                    data = json.load(f)
            except:
                data = {}

        data[self.servant_name] = {
            "unlocked": [name for name, value in self.is_unlocked.items() if value]
        }

        with open(resource_path(SAVE_FILE), "w") as f:
            json.dump(data, f, indent=4)

    # ---------------------------------------------------------
    # CLICK LOGIC
    # ---------------------------------------------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = self.mapToScene(event.pos())
            item = self.scene.itemAt(pos, self.transform())

            if item in self.node_items:
                data = self.node_items[item]
                name = data["name"]

                # Check pre-req
                prereq = self.prereq_map[name]
                if prereq is not None and not self.is_unlocked.get(prereq, False):
                    from PyQt5.QtWidgets import QMessageBox
                    box = QMessageBox()
                    box.setWindowTitle("Locked Skill")
                    box.setText(f"You must unlock **{prereq}** first.")
                    box.exec_()
                    return

                # Check if it is an Armament
                if name == self.armament_name:
                    dlg = ArmamentDescriptionDialog(
                        data=data,
                        unlock_callback=lambda: self.unlock(name),
                        can_unlock=self.can_unlock_armament(),
                        parent=self
                    )
                    dlg.exec_()
                    return

                dlg = SkillDescriptionDialog(
                    data=data,
                    unlock_callback=lambda: self.unlock(name),
                    can_unlock=not self.is_unlocked.get(name, False),
                    parent=self
                )
                dlg.exec_()

        super().mousePressEvent(event)


    # ---------------------------------------------------------
    # HOVER LOGIC
    # ---------------------------------------------------------
    def mouseMoveEvent(self, event):
        pos = self.mapToScene(event.pos())
        item = self.scene.itemAt(pos, self.transform())

        # Restore previous node
        if self.hovered_node and self.hovered_node in self.node_rectangles:
            rect = self.node_rectangles[self.hovered_node]
            self.apply_node_colors(self.hovered_node, rect)
            self.hovered_node = None

        # New hover
        if item in self.node_items:
            data = self.node_items[item]
            name = data["name"]
            self.hovered_node = name
            rect = self.node_rectangles[name]

            # Hover = lighter version of its current color
            rect.setPen(QPen(HOVER_BORDER, 3))
            rect.setBrush(QBrush(self.get_base_color(name).lighter(110)))

        super().mouseMoveEvent(event)


    # ---------------------------------------------------------
    # DETERMINE NODE BASE COLOR (locked / unlockable / unlocked)
    # ---------------------------------------------------------
    def get_base_color(self, name):
        # Armament
        if name == self.armament_name:
            return ARMAMENT_UNLOCKED_FILL if self.is_unlocked[name] else ARMAMENT_LOCKED_FILL

        # Skill
        if self.is_unlocked[name]:
            return UNLOCKED_FILL

        return LOCKED_FILL


    def get_base_border(self, name):
        if name == self.armament_name:
            return ARMAMENT_UNLOCKED_BORDER if self.is_unlocked[name] else ARMAMENT_LOCKED_BORDER

        if self.is_unlocked[name]:
            return UNLOCKED_BORDER

        prereq = self.prereq_map[name]
        if prereq is not None and self.is_unlocked.get(prereq, False):
            return UNLOCKABLE_BORDER

        return LOCKED_BORDER


    # ---------------------------------------------------------
    # APPLY COLORS TO A NODE RECTANGLE
    # ---------------------------------------------------------
    def apply_node_colors(self, name, rect):
        rect.setBrush(QBrush(self.get_base_color(name)))
        rect.setPen(QPen(self.get_base_border(name), 2))


    # ---------------------------------------------------------
    # BUILD TREE STRUCTURE
    # ---------------------------------------------------------
    def build_tree(self):
        self.children = {self.armament_name: []}

        for sk in self.skills:
            prereq = sk["prerequisite"]
            if prereq is None:
                self.children[self.armament_name].append(sk["name"])
            else:
                self.children.setdefault(prereq, []).append(sk["name"])


    # ---------------------------------------------------------
    # WIDTH COMPUTATION
    # ---------------------------------------------------------
    def compute_subtree_width(self, node, node_w, spacing_x):
        if node in self._width_cache:
            return self._width_cache[node]

        kids = self.children.get(node, [])
        if not kids:
            w = node_w + 40
            self._width_cache[node] = w
            return w

        widths = [self.compute_subtree_width(child, node_w, spacing_x) for child in kids]
        total = sum(widths) + spacing_x * (len(widths) - 1)

        self._width_cache[node] = total
        return total


    # ---------------------------------------------------------
    # POSITION ASSIGNMENT
    # ---------------------------------------------------------
    def assign_positions(self, node, cx, depth, node_w, spacing_x, spacing_y):
        y = 60 + depth * spacing_y
        self.positions[node] = QPointF(cx, y)

        kids = self.children.get(node, [])
        if not kids:
            return

        widths = [self.compute_subtree_width(child, node_w, spacing_x) for child in kids]
        total = sum(widths) + spacing_x * (len(widths) - 1)

        start = cx - total / 2

        for child, w in zip(kids, widths):
            center = start + w / 2
            self.assign_positions(child, center, depth + 1, node_w, spacing_x, spacing_y)
            start += w + spacing_x


    # ---------------------------------------------------------
    # DRAW TREE
    # ---------------------------------------------------------
    def draw_tree(self):
        self.scene.clear()
        self.node_items.clear()
        self.node_rectangles.clear()

        node_w = 300
        spacing_x = 120
        spacing_y = 120

        self.positions = {}
        self._width_cache = {}

        # Build
        self.build_tree()
        total_w = self.compute_subtree_width(self.armament_name, node_w, spacing_x)
        root_center = total_w / 2 + 100
        self.assign_positions(self.armament_name, root_center, 0, node_w, spacing_x, spacing_y)

        def draw_node(name, skill=None):
            pos = self.positions[name]
            base_h = 50
            fill_color = self.get_base_color(name)

            # ---- Text with wrapping ----
            text_item = QGraphicsTextItem()
            text_item.setPlainText(name)
            text_item.setTextWidth(node_w - 20)
            self.scene.addItem(text_item)
            current_font = text_item.font()
            current_font.setPointSize(10)
            current_font.setFamily("Arial")
            current_font.setBold(True)
            text_item.setFont(current_font)

            text_rect = text_item.boundingRect()
            node_h = max(base_h, text_rect.height() + 20)

            x = pos.x() - node_w / 2
            y = pos.y() - node_h / 2

            rect_item = self.scene.addRect(
                QRectF(x, y, node_w, node_h),
                QPen(self.get_base_border(name)),
                QBrush(fill_color)
            )

            text_item.setPos(
                x + 10,
                y + (node_h - text_rect.height()) / 2
            )
            text_item.setZValue(1)

            # Register items
            if skill:
                data = skill
            else:
                data = {
                    "name": self.armament_data["name"],
                    "description": self.armament_data["description"],
                    "type": self.armament_data["type"],
                    "effects": self.armament_data["effects"],
                    "prerequisite": None
                }

            self.node_rectangles[name] = rect_item
            self.node_items[rect_item] = data
            self.node_items[text_item] = data

            return node_h

        root_h = draw_node(self.armament_name)

        heights = {}
        for sk in self.skills:
            heights[sk["name"]] = draw_node(sk["name"], sk)

        # Connections
        for sk in self.skills:
            parent = sk["prerequisite"] or self.armament_name
            p = self.positions[parent]
            c = self.positions[sk["name"]]

            parent_h = heights.get(parent, root_h)
            child_h = heights[sk["name"]]

            self.scene.addLine(
                p.x(), p.y() + parent_h / 2,
                c.x(), c.y() - child_h / 2,
                QPen(CONNECTION_COLOR, 2)
            )

        self.setSceneRect(self.scene.itemsBoundingRect().adjusted(-60, -60, 60, 60))
