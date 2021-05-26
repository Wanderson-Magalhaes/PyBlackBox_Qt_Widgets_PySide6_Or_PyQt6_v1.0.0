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

# DEFAULT PACKAGES
# ///////////////////////////////////////////////////////////////
import sys
import os

# IMPORT / GUI, SETTINGS AND WIDGETS
# ///////////////////////////////////////////////////////////////
# Packages
from app.packages.pyside_or_pyqt import * # Qt
from app.packages.widgets import * # Widgets
# GUIs
from app.uis.login.ui_login import Ui_Login # Login / Splash Screen
from app.uis.main_window.ui_main import Ui_MainWindow # MainWindow
from app.uis.chat.page_messages import Chat # Chat Widget
# Modules
import app.modules.ui_functions.functions as ui_functions
from app.modules.app_settings.settings import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
counter = 0

# LOGIN
# ///////////////////////////////////////////////////////////////
class LoginWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_login.py"
        # Load widgets inside LoginWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        # ///////////////////////////////////////////////////////////////
        self.progress = CircularProgress()
        self.progress.width = 240
        self.progress.height = 240
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 4
        self.progress.progress_color = QColor("#bdff00")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()

        # ADD DROP SHADOW
        # ///////////////////////////////////////////////////////////////
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(self.shadow)

        # QTIMER
        # ///////////////////////////////////////////////////////////////
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        self.ui.username.keyReleaseEvent = self.check_login
        self.ui.password.keyReleaseEvent = self.check_login

        self.show()

    # CHECK LOGIN
    # ///////////////////////////////////////////////////////////////
    def check_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()

            def open_main():
                # SHOW MAIN WINDOW
                self.main = MainWindow()
                self.main.top_user.label_user.setText(username.capitalize())
                self.main.show()                
                self.close()

            if username and password == "123456":
                self.ui.user_description.setText(f"Welcome {username}!")
                self.ui.user_description.setStyleSheet("#user_description { color: #bdff00 }")
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid #bdff00; }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid #bdff00; }")
                QTimer.singleShot(1200, lambda: open_main())
            else:
                # SET STYLESHEET
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(255, 0, 127); }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(255, 0, 127); }")
                self.shacke_window()
            

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    # UPDATE PROGRESS BAR
    # ///////////////////////////////////////////////////////////////
    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            self.animation_login()

        # INCREASE COUNTER
        counter += 1

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_main.py"
        # Load widgets inside MainWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SET DEFAULT PAGE
        # ///////////////////////////////////////////////////////////////
        self.ui.app_pages.setCurrentWidget(self.ui.home)

        # LOAD DICT SETTINGS FROM "settings.json" FILE
        # ///////////////////////////////////////////////////////////////
        self.settings = Settings()

        self.custom_btn_top = LeftMenuButton(
            self,
            "custom_btn_top",
            "images/icons_svg/icon_add_user.svg",
            "Add new friend"
        )
        self.custom_btn_bottom_1 = LeftMenuButton(
            self,
            "custom_btn_bottom_1",
            "images/icons_svg/icon_more_options.svg",
            "More options, test with many words"
        )
        self.custom_btn_bottom_2 = LeftMenuButton(
            self,
            "custom_btn_bottom_2",
            "images/icons_svg/icon_settings.svg",
            "Open settings"
        )
        self.ui.top_menus_layout.addWidget(self.custom_btn_top)
        self.ui.bottom_menus_layout.addWidget(self.custom_btn_bottom_1)
        self.ui.bottom_menus_layout.addWidget(self.custom_btn_bottom_2)

        # DEBUG
        self.custom_btn_top.clicked.connect(lambda: print(f"{self.settings['app_name']}: clicked"))
        self.custom_btn_top.released.connect(lambda: print(f"{self.custom_btn_top.objectName()}: released"))
        self.custom_btn_bottom_1.clicked.connect(lambda: print(f"{self.custom_btn_bottom_1.objectName()}: clicked"))
        self.custom_btn_bottom_1.released.connect(lambda: print(f"{self.custom_btn_bottom_1.objectName()}: released"))

        
        # TOP USER BOX
        # Add widget to App
        # ///////////////////////////////////////////////////////////////
        self.top_user = TopUserInfo(self.ui.left_messages, 8, 64, "wanderson", "Writing python codes")
        self.top_user.setParent(self.ui.top_user_frame)
        self.top_user.status.connect(self.status_change)

        # SET UI DEFINITIONS
        # Run set_ui_definitions() in the ui_functions.py
        # ///////////////////////////////////////////////////////////////
        ui_functions.UiFunctions.set_ui_definitions(self)

        # ADD MESSAGE BTNS / FRIEND MENUS
        # Add btns to page
        # ///////////////////////////////////////////////////////////////
        add_user = [
            {
                "user_image" : "images/users/cat.png",
                "user_name" : "Tom",
                "user_description" : "Did you see a mouse?",
                "user_status" : "online",
                "unread_messages" : 2,
                "is_active" : False
            },
            {
                "user_image" : "images/users/mouse.png",
                "user_name" : "Jerry",
                "user_description" : "I think I saw a cat...",
                "user_status" : "busy",
                "unread_messages" : 1,
                "is_active" : False
            },
            {
                "user_image" : "images/users/me.png",
                "user_name" : "Me From The Future",
                "user_description" : "Lottery result...",
                "user_status" : "invisible",
                "unread_messages" : 0,
                "is_active" : False
            }
        ]
        self.menu = FriendMessageButton
        def add_menus(self, parameters):
            id = 0
            for parameter in parameters:
                
                user_image = parameter['user_image']
                user_name = parameter['user_name']
                user_description = parameter['user_description']
                user_status = parameter['user_status']
                unread_messages = parameter['unread_messages']
                is_active = parameter['is_active']
                
                self.menu = FriendMessageButton(
                    id, user_image, user_name, user_description, user_status, unread_messages, is_active
                )
                self.menu.clicked.connect(self.btn_clicked)
                self.menu.released.connect(self.btn_released)
                self.ui.messages_layout.addWidget(self.menu)
                id += 1

        add_menus(self, add_user)


        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # SET USERNAME TO MAIN WINDOW
    # ///////////////////////////////////////////////////////////////
    def set_user_and_description(self, username):
        self.top_user.user_name = username
        print(f"User: {username} are logged!")

    # PRINT STATUS
    # ///////////////////////////////////////////////////////////////
    def status_change(self, status):
        print(f"send signal: {status}")
        
    # GET BTN CLICKED
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = self.sender()
        
        # UNSELECT CHATS
        ui_functions.UiFunctions.deselect_chat_message(self, btn.objectName())

        # SELECT CLICKED
        if btn.objectName():
            btn.reset_unread_message()
            ui_functions.UiFunctions.select_chat_message(self, btn.objectName())

        # LOAD CHAT PAGE
        if btn.objectName():
            # REMOVE CHAT
            for chat in reversed(range(self.ui.chat_layout.count())):
                self.ui.chat_layout.itemAt(chat).widget().deleteLater()
            self.chat = None

            # SET CHAT WIDGET
            self.chat = Chat(btn.user_image, btn.user_name, btn.user_description, btn.objectName(), self.top_user.user_name)

            # ADD WIDGET TO LAYOUT
            self.ui.chat_layout.addWidget(self.chat)

            # JUMP TO CHAT PAGE
            self.ui.app_pages.setCurrentWidget(self.ui.chat)

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # GET BTN RELEASED
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = self.sender()
        print(F"Button {btn.objectName()}, released!")


    # RESIZE EVENT
    # Whenever the window is resized, this event will be triggered
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        ui_functions.UiFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = LoginWindow()
    sys.exit(app.exec_())