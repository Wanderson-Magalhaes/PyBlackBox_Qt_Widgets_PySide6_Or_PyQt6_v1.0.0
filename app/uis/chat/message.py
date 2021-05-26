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
import os

# IMPORT / GUI, SETTINGS AND WIDGETS
# ///////////////////////////////////////////////////////////////
# Packages
from datetime import datetime
from app.packages.pyside_or_pyqt import * # Qt

# GLOBALS
send_by = None

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class Message(QWidget):
    def __init__(self, message, me_send):
        QWidget.__init__(self)
        global send_by
        send_by = me_send

        self.setMinimumHeight(20)
        self.setup_ui()
        self.setFixedHeight(self.layout.sizeHint().height())

        # SET MESSAGE
        self.message.setText(message)

        # SET DATE TIME
        date_time = datetime.now()
        date_time_format = date_time.strftime("%m/%d/%Y %H:%M")
        self.data_message.setText(str(date_time_format))

    def setup_ui(self):
        # LAYOUT
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)

        # FRAME BG
        self.bg = QFrame()
        if send_by:
            self.bg.setStyleSheet("#bg {background-color: #0e0e0f; border-radius: 10px; margin-left: 150px; } #bg:hover { background-color: #252628; }")
        else:
            self.bg.setStyleSheet("#bg {background-color: #28282b; border-radius: 10px; margin-right: 150px; } #bg:hover { background-color: #252628; }")
        self.bg.setObjectName("bg")

        # FRAME BG
        self.btn = QPushButton()
        self.btn.setMinimumSize(40, 40)
        self.btn.setMaximumSize(40, 40)
        self.btn.setStyleSheet("""
        QPushButton {
            background-color: transparent;
            border-radius: 20px;
            background-repeat: no-repeat;
            background-position: center;
            background-image: url(:/icons_svg/images/icons_svg/icon_more_options.svg);
        }
        QPushButton:hover {
            background-color: rgb(61, 62, 65);
        }
        QPushButton:pressed {
            background-color: rgb(16, 17, 18);
        }        
        """)

        if send_by:
            self.layout.addWidget(self.bg)
            self.layout.addWidget(self.btn)
        else:
            self.layout.addWidget(self.btn)
            self.layout.addWidget(self.bg)

        # LAYOUT INSIDE
        self.layout_inside = QVBoxLayout(self.bg)
        self.layout.setContentsMargins(10,10,10,10)

        # LABEL MESSAGE 
        self.message = QLabel()
        self.message.setText("message test")
        self.message.setStyleSheet("font: 500 11pt 'Segoe UI'")
        self.message.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard)

        # LABEL MESSAGE 
        self.data_message = QLabel()
        self.data_message.setText("date")
        self.data_message.setStyleSheet("font: 8pt 'Segoe UI'; color: #4c5154")
        if send_by:
            self.data_message.setAlignment(Qt.AlignRight)
        else:
            self.data_message.setAlignment(Qt.AlignLeft)

        self.layout_inside.addWidget(self.message)
        self.layout_inside.addWidget(self.data_message)
