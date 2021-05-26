import sys
import os
from cx_Freeze import setup, Executable
# Packages
from app.packages.pyside_or_pyqt import * # Qt
from app.packages.widgets import * # Widgets
# GUIs
from app.uis.login.ui_login import Ui_Login # Login / Splash Screen
from app.uis.main_window.ui_main import Ui_MainWindow # MainWindow
from app.uis.chat.page_messages import Chat # Chat Widget
# Modules
import app.modules.ui_functions.functions as ui_functions
import app.modules.app_settings.settings as app_settings

# ADD FILES/FOLDERS
files = ['icon.ico', 'settings.json','images/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "PyBlackBOX",
    version = "1.0",
    description = "Modern GUI for desktop chat",
    author = "Wanderson M. Pimenta",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]    
)
