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
# GUI
from app.uis.main_window.ui_main import Ui_MainWindow # MainWindow
from app.modules.app_settings.settings import *

# GLOBAL VARS
# ///////////////////////////////////////////////////////////////
_is_maximized = False

# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class UiFunctions:

    def __init__(self):
        super(UiFunctions, self).__init__()
        # GET WIDGETS FROM "ui_main.py"
        # Load widgets inside App Functions
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # SET UI DEFINITIONS
    # Set ui definitions before "self.show()" in main.py
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global _is_maximized
        
        # CHANGE UI AND RESIZE GRIP
        def change_ui():
            if not _is_maximized:
                self.resize(self.width()+1, self.height()+1)
                self.ui.margins_app.setContentsMargins(10, 10, 10, 10)
                self.ui.maximize_restore_app_btn.setToolTip("Restore")
                self.ui.maximize_restore_app_btn.setStyleSheet("background-image: url(:/icons_svg/images/icons_svg/icon_maximize.svg);")
                self.ui.bg_app.setStyleSheet("#bg_app { border-radius: 10px; border: 2px solid rgb(30, 32, 33); }")
                self.left_grip.show()
                self.right_grip.show()
                self.top_grip.show()
                self.bottom_grip.show()
                
            else:
                self.ui.margins_app.setContentsMargins(0, 0, 0, 0)
                self.ui.maximize_restore_app_btn.setToolTip("Restore")
                self.ui.maximize_restore_app_btn.setStyleSheet("background-image: url(:/icons_svg/images/icons_svg/icon_restore.svg);")
                self.ui.bg_app.setStyleSheet("#bg_app { border-radius: 0px; border: none; }")
                self.left_grip.hide()
                self.right_grip.hide()
                self.top_grip.hide()
                self.bottom_grip.hide()

        # CHECK EVENT
        if self.isMaximized():
            _is_maximized = False
            self.showNormal()
            change_ui()
        else:
            _is_maximized = True
            self.showMaximized()
            change_ui()

    # START CHAT SELECTION
    # ///////////////////////////////////////////////////////////////
    def select_chat_message(self, widget):
        for w in self.ui.messages_frame.findChildren(QWidget):
            if w.objectName() == widget:
                w.set_active(True)

    # RESET CHAT SELECTION
    # ///////////////////////////////////////////////////////////////
    def deselect_chat_message(self, widget):
        for w in self.ui.messages_frame.findChildren(QWidget):
            if w.objectName() != widget:
                if hasattr(w, 'set_active'):
                    w.set_active(False)

    # SET UI DEFINITIONS
    # Set ui definitions before "self.show()" in main.py
    # ///////////////////////////////////////////////////////////////
    def set_ui_definitions(self):

        # GET SETTINGS FROM JSON DESERIALIZED
        settings = Settings()
        self.settings = settings.items

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if self.isMaximized():
                UiFunctions.maximize_restore(self)
                curso_x = self.pos().x()
                curso_y = event.globalPos().y() - QCursor.pos().y()
                self.move(curso_x, curso_y)
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.logo_top.mouseMoveEvent = moveWindow
        self.ui.title_bar.mouseMoveEvent = moveWindow

        # DOUBLE CLICK MAXIMIZE / RESTORE
        def maximize_restore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                UiFunctions.maximize_restore(self)
        self.ui.title_bar.mouseDoubleClickEvent = maximize_restore

        # TOP BTNS
        self.ui.minimize_app_btn.clicked.connect(lambda: self.showMinimized())        
        self.ui.maximize_restore_app_btn.clicked.connect(lambda: UiFunctions.maximize_restore(self))
        self.ui.close_app_btn.clicked.connect(lambda: self.close())
        

        
        # DEFAULT PARAMETERS
        self.setWindowTitle(self.settings["app_name"])
        self.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        self.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

        # APPLY DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(25)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.stylesheet.setGraphicsEffect(self.shadow)

        # CUSTOM GRIPS
        # Create grips to resize window
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

    # RESIZE GRIPS
    # This function should be called whenever "MainWindow/main.py" has its window resized.
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)
