# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT
# ///////////////////////////////////////////////////////////////
# Packages
from app.packages.pyside_or_pyqt import *
from app.packages.widgets import *
# Modules
import app.modules.app_settings.settings as app_settings

# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class AppFunctions:
    def __init__(self):
        # GET WIDGETS FROM "ui_main.py"
        # Load widgets inside App Functions
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def change_placeholder(self):
        self.ui.search_line_edit.setPlaceholderText("teste")