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
# Modules
import os

# FRIEND MENU MESSAGE / MESSAGE BUTTON
# Friends messages with name and status
class FriendMessageButton(QWidget):
    # SIGNALS
    # ///////////////////////////////////////////////////////////////
    clicked = Signal()
    released = Signal()

    def __init__(
        self,
        id,
        user_image,
        user_name,
        user_descrition,
        user_status,
        unread_messages,
        is_active
    ):
        QWidget.__init__(self)

        # ICON PATH
        # ///////////////////////////////////////////////////////////////
        image = user_image
        app_path = os.path.abspath(os.getcwd())
        image_path = os.path.join(app_path, image)

        # CUSTOM PARAMETERS
        # ///////////////////////////////////////////////////////////////
        self.user_image = image_path
        self.user_name = user_name
        self.user_description = user_descrition
        self.user_status = user_status
        self.unread_messages = unread_messages
        self.is_active = is_active
        self._status_color = "#46b946"
        self.bg_color_entered = "#22CCCCCC"
        self.bg_color_leave = "#00000000"
        self.bg_color_active = "#33CCCCCC"
        self._bg_color = self.bg_color_leave      


        # SETUP
        self.setFixedSize(240, 50)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(str(id))
        self.setup_ui()

        # SHOW UNREAD MESSAGES
        if self.unread_messages > 0:
            self.label_messages.show()
            self.label_messages.setText(str(self.unread_messages))
        
        # CHANGE COLOR
        if self.user_status == "online":
            self._status_color = "#46b946"
        elif self.user_status == "ilde":
            self._status_color = "#ff9955"
        elif self.user_status == "busy":
            self._status_color = "#a02c2c"
        elif self.user_status == "invisible":
            self._status_color = "#808080"
        
        # CHANGE OPACITY
        if self.user_status == "invisible":
            self.opacity = QGraphicsOpacityEffect()
            self.opacity.setOpacity(0.4)
            self.setGraphicsEffect(self.opacity)

    def reset_unread_message(self):
        self.unread_messages = 0
        self.label_messages.hide()
        self.repaint()

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # EMIT SIGNAL
            self.clicked.emit()

    # MOUSE RELEASE
    # Event fired when the mouse leaves the BTN
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.released.emit()

    # MOUSE ENTER
    # Event fired when the mouse enter
    def enterEvent(self, event):
        if not self.is_active:
            self._bg_color = self.bg_color_entered
            self.repaint()

    # MOUSE LEAVE
    # Event fired when the mouse leave
    def leaveEvent(self, event):
        if not self.is_active:
            self._bg_color = self.bg_color_leave
            self.repaint()

    def set_active(self, active):
        if active:
            self.is_active = active
        else:
            self.is_active = active 
            self._bg_color = self.bg_color_leave
        self.repaint()

    # SETUP WIDGETS
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # FRAME TEXT
        self.text_frame = QFrame(self)
        self.text_frame.setGeometry(60, 0, 170, 50)

        # USER NAME
        self.label_user = QLabel(self.text_frame)
        self.label_user.setGeometry(0, 8, self.text_frame.width(), 20)
        self.label_user.setAlignment(Qt.AlignVCenter)        
        self.label_user.setText(self.user_name.capitalize())
        self.label_user.setStyleSheet("color: #e7e7e7; font: 700 10pt 'Segoe UI';")

        # USER STATUS
        self.label_description = QLabel(self.text_frame)
        self.label_description.setGeometry(0, 22, self.text_frame.width(), 18)
        self.label_description.setAlignment(Qt.AlignVCenter)        
        self.label_description.setText(self.user_description)
        self.label_description.setStyleSheet("color: #A6A6A6; font: 9pt 'Segoe UI';")

        # USER STATUS
        self.label_messages = QLabel(self)
        self.label_messages.setFixedSize(35, 20)
        self.label_messages.setAlignment(Qt.AlignCenter)
        self.label_messages.setStyleSheet("""
            background-color: #1e2021;
            padding-left: 5px;
            padding-right: 5px;
            color: #bdff00;
            border-radius: 10px;
            border: 3px solid #333;
            font: 9pt 'Segoe UI';
        """)
        self.label_messages.move(self.width() - 45, 16)
        self.label_messages.hide()

    # PAINT EVENT
    # PAINT USER IMAGE EVENTS
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        # PAINTER USER IMAGE
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # RECT
        rect = QRect(10, 5, 40, 40)

        # DRAW BG
        if self.is_active:
            painter.setBrush(QBrush(QColor(self.bg_color_active)))            
        else:
            painter.setBrush(QBrush(QColor(self._bg_color)))
        painter.drawRoundedRect(5, 0, 230, 50, 25, 25)

        # CIRCLE        
        painter.setBrush(QBrush(QColor("#000000")))
        painter.drawEllipse(rect)

        # DRAW USER IMAGE
        self.draw_user_image(painter, self.user_image, rect)        

        painter.end()

        # DRAW USER IMAGE
        if self.user_status != "invisible":
            self.draw_status(self.user_image, rect)

    # DRAW USER IMAGE
    # ///////////////////////////////////////////////////////////////
    def draw_user_image(self, qp, image, rect):
        user_image = QImage(image)
        path = QPainterPath()
        path.addEllipse(rect)
        qp.setClipPath(path)
        qp.drawImage(rect, user_image)

    # DRAW STATUS
    # ///////////////////////////////////////////////////////////////
    def draw_status(self, status, rect):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # PEN
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("#151617"))
        painter.setPen(pen)

        # BRUSH/STATUS COLOR
        painter.setBrush(QBrush(QColor(self._status_color)))

        # DRAW
        painter.drawEllipse(rect.x() + 27, rect.y() + 27, 13, 13)
        painter.end()
        