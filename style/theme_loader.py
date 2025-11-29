import os
import configparser
from PyQt5.QtGui import QColor
from fgo_app.utils import resource_path

class ThemeLoader:
    """Loads color + theme data from an INI file."""

    def __init__(self, theme_file_path):
        self.theme_file_path = theme_file_path
        self.config = configparser.ConfigParser()
        self.loaded = False
        self.theme = {}

    def load(self):
        """Load theme file the first time it is requested."""
        if self.loaded:
            return self.theme

        if not os.path.exists(self.theme_file_path):
            raise FileNotFoundError(f"Theme file not found: {self.theme_file_path}")

        self.config.read(self.theme_file_path)

        # Parse all sections and keys into a dict of QColor or raw values
        for section in self.config.sections():
            self.theme[section] = {}

            for key, value in self.config[section].items():
                value = value.split(";")[0].strip()

                # Try to convert hex colors to QColor automatically
                if value.startswith("#") and len(value) in (7, 9):
                    qcol = QColor(value)
                    if not qcol.isValid():
                        print(f"[ThemeLoader] Warning: invalid color '{value}' in {key}")
                    self.theme[section][key] = qcol
                else:
                    # raw text or numeric value
                    self.theme[section][key] = value

        self.loaded = True
        return self.theme

    def get_color(self, section, key, fallback="#ffffff"):
        """Safe QColor fetch with fallback."""
        theme = self.load()
        try:
            val = theme[section][key]
            if isinstance(val, QColor):
                return val
            else:
                return QColor(val)
        except KeyError:
            print(f"[ThemeLoader] Missing {section}:{key}, using fallback {fallback}")
            return QColor(fallback)


# GLOBAL THEME INSTANCE
# You can import this anywhere:
#
#     from style.theme_loader import theme
#
theme = ThemeLoader(resource_path("style/fgo_colors.ini"))
