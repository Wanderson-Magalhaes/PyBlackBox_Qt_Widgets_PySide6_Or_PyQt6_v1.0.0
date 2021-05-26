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

# TOP USER BOX
# Top box with name, description and status
# ///////////////////////////////////////////////////////////////
class TopUserInfo(QWidget):
    status = Signal(str)
    def __init__(self, parent, left, top, my_name, my_description):
        QWidget.__init__(self)

        # ICON PATH
        # ///////////////////////////////////////////////////////////////
        image = "images/users/me.png"
        icon_settings = "images/icons_svg/icon_settings.svg"
        app_path = os.path.abspath(os.getcwd())
        image_path = os.path.join(app_path, image)
        icon_settings_path = os.path.join(app_path, icon_settings)

        # INITIAL SETUP
        # ///////////////////////////////////////////////////////////////
        self.setGeometry(0, 0, 240, 60)
        self.setObjectName("top_text_box")
        self.setStyleSheet("#top_text_box { background-color: #F00000 }")

        # CUSTOM PARAMETERS
        # ///////////////////////////////////////////////////////////////
        self.user_name = my_name
        self.user_description = my_description
        self.user_status = "online"
        self.user_image = image_path
        self.icon_settings = icon_settings
        self._status_color = "#46b946"

        # DRAW BASE FRAME
        # ///////////////////////////////////////////////////////////////
        self.setup_ui()

        # IMAGE FRAME EVENTS
        # ///////////////////////////////////////////////////////////////
        self.user_overlay.mousePressEvent = self.mouse_press
        self.user_overlay.enterEvent = self.mouse_enter
        self.user_overlay.leaveEvent = self.mouse_leave

        # SETUP STATUS BOX
        # ///////////////////////////////////////////////////////////////
        self.status_box = _ChangeStatus(parent)
        self.status_box.move(left, top)
        self.status_box.focusOutEvent = self.lost_focus_status_box
        self.status_box.line_edit.focusOutEvent = self.lost_focus_line_edit
        self.status_box.line_edit.keyReleaseEvent = self.change_description
        self.status_box.hide()
        self.status_box.status.connect(self.change_status)       
        
    # CHANGE USER STATUS
    # Change when is connected with status signal
    # ///////////////////////////////////////////////////////////////
    def change_status(self, status):
        # CHANGE STATUS
        if status == "online":
            self._status_color = "#46b946"
            self.repaint()
        elif status == "idle":
            self._status_color = "#ff9955"
            self.repaint()
        elif status == "busy":
            self._status_color = "#a02c2c"
            self.repaint()
        elif status == "invisible":
            self._status_color = "#808080"
            self.repaint()
        # EMIT SIGNAL
        self.status.emit(status)

    # CHANGE TEXT DESCRIPTION
    # ///////////////////////////////////////////////////////////////
    def change_description(self, event):        
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.label_description.setText(self.status_box.line_edit.text())
            self.status_box.line_edit.setText("")
            self.status_box.hide()
        
    # SHO HIDE DIALOP POPUP
    # ///////////////////////////////////////////////////////////////
    # HIDE LINE EDIT WHEN LOST FOCUS
    def lost_focus_status_box(self, event):
        if not self.status_box.line_edit.hasFocus():
            self.status_box.hide()
            self.status_box.line_edit.setText("")

    # HIDE WHEN LOST FOCUS
    def lost_focus_line_edit(self, event):
        if not self.status_box.hasFocus():
            self.status_box.hide()
            self.status_box.line_edit.setText("")

    # OPEN STATUS BOX POPUP
    # ///////////////////////////////////////////////////////////////
    def mouse_press(self, event):
        if self.status_box.isVisible():
            self.status_box.hide()
            self.status_box.line_edit.setText("")
        else:
            self.status_box.show()
            self.status_box.line_edit.setFocus()

    # SHOW ICON
    # ///////////////////////////////////////////////////////////////
    def mouse_enter(self, event):
        self.user_overlay.setPixmap(self.icon_settings)

    # HIDE ICON
    # ///////////////////////////////////////////////////////////////
    def mouse_leave(self, event):
        self.user_overlay.setPixmap(None)

    # SETUP WIDGETS
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # LAYOUT AND BORDER
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10,10,10,0)
        self.border = QFrame(self)
        self.layout.addWidget(self.border)
        
        # FRAME IMAGE
        self.user_overlay = QLabel(self.border)
        self.user_overlay.setGeometry(0, 5, 40, 40)
        self.user_overlay.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_overlay.setAlignment(Qt.AlignCenter)
        opacity = QGraphicsOpacityEffect(self)
        opacity.setOpacity(0.75)
        self.user_overlay.setGraphicsEffect(opacity)

        # FRAME TEXT
        self.text_frame = QFrame(self.border)
        self.text_frame.setGeometry(50, 0, 170, 50)

        # USER NAME
        self.label_user = QLabel(self.text_frame)
        self.label_user.setGeometry(0, 8, self.text_frame.width(), 20)
        self.label_user.setAlignment(Qt.AlignVCenter)        
        self.label_user.setText(self.user_name.capitalize())
        self.label_user.setStyleSheet("color: #bdff00; font: 700 10pt 'Segoe UI';")

        # USER STATUS
        self.label_description = QLabel(self.text_frame)
        self.label_description.setGeometry(0, 22, self.text_frame.width(), 18)
        self.label_description.setAlignment(Qt.AlignVCenter)        
        self.label_description.setText(self.user_description)
        self.label_description.setStyleSheet("color: #A6A6A6; font: 9pt 'Segoe UI';")

    # PAINT USER IMAGE EVENTS
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        # PAINTER USER IMAGE
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # RECT
        rect = QRect(10, 15, 40, 40)

        # CIRCLE
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor("#000000")))
        painter.drawEllipse(rect)

        # DRAW USER IMAGE
        self.draw_user_image(painter, self.user_image, rect)        

        # PAINT END
        painter.end()

        # DRAW USER IMAGE
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

# SET STYLE TO POPUP
# ///////////////////////////////////////////////////////////////
style = """
/* QFrame */
QFrame {
    background: #333436; border-radius: 10px;
}
/* Search Message */
.QLineEdit {
	border: 2px solid rgb(47, 48, 50);
	border-radius: 15px;
	background-color: rgb(47, 48, 50);
	color: rgb(121, 121, 121);
	padding-left: 10px;
	padding-right: 10px;
}
.QLineEdit:hover {
	color: rgb(230, 230, 230);
	border: 2px solid rgb(62, 63, 66);
}
.QLineEdit:focus {
	color: rgb(230, 230, 230);
	border: 2px solid rgb(53, 54, 56);
	background-color: rgb(14, 14, 15);
}
/* QPushButton */
.QPushButton{
    background-color: transparent;
    border: none;
    border-radius: 10px;
    background-repeat: no-repeat;
    background-position: left center;
    text-align: left;
    color: #999999;
    padding-left: 38px;
}
.QPushButton:hover{
    background-color: #151617;
    color: #CCCCCC;
}

"""
# CHAN STATUS POPUP
# # ///////////////////////////////////////////////////////////////
class _ChangeStatus(QFrame):
    status = Signal(str)
    def __init__(self, parent):
        QFrame.__init__(self)

        # SETUP
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(230, 205)
        self.setStyleSheet(style)
        self.setParent(parent)

        # LAYOUT AND BORDER
        # ///////////////////////////////////////////////////////////////
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10,10,10,10)
        self.border = QFrame(self)
        self.layout.addWidget(self.border)

        # LINEEDIT AND BTNS BOX
        # ///////////////////////////////////////////////////////////////
        self.layout_content = QVBoxLayout(self.border)
        self.layout_content.setContentsMargins(0,0,0,0)
        self.layout_content.setSpacing(1)

        # CHANGE DESCRIPTION
        # ///////////////////////////////////////////////////////////////
        self.line_edit = QLineEdit()
        self.line_edit.setMinimumHeight(30)
        self.line_edit.setPlaceholderText("Write what you are doing...")

        # TOP LABEL
        # ///////////////////////////////////////////////////////////////
        self.label = QLabel("Change status:")
        self.label.setStyleSheet("padding-top: 5px; padding-bottom: 5px; color: rgb(121, 121, 121);")

        # BTN ONLINE
        # ///////////////////////////////////////////////////////////////
        self.btn_online = QPushButton()
        self.btn_online.setText("Online")
        self.btn_online.setMinimumHeight(30)
        self.btn_online.setStyleSheet("background-image: url(:/icons_svg/images/icons_svg/icon_online.svg)")
        self.btn_online.clicked.connect(lambda: self.send_signal("online"))
        self.btn_online.setCursor(Qt.PointingHandCursor)

        # BTNL ILDE
        # ///////////////////////////////////////////////////////////////
        self.btn_idle = QPushButton()
        self.btn_idle.setText("Idle")
        self.btn_idle.setMinimumHeight(30)
        self.btn_idle.setStyleSheet("background-image: url(:/icons_svg/images/icons_svg/icon_idle.svg)")
        self.btn_idle.clicked.connect(lambda: self.send_signal("idle"))
        self.btn_idle.setCursor(Qt.PointingHandCursor)

        # BTN BUSE
        # ///////////////////////////////////////////////////////////////
        self.btn_busy = QPushButton()
        self.btn_busy.setText("Do not disturb")
        self.btn_busy.setMinimumHeight(30)
        self.btn_busy.setStyleSheet("background-image: url(:/icons_svg/images/icons_svg/icon_busy.svg)")
        self.btn_busy.clicked.connect(lambda: self.send_signal("busy"))
        self.btn_busy.setCursor(Qt.PointingHandCursor)

        # BTN INVISIBLE
        self.btn_invisible = QPushButton()
        self.btn_invisible.setText("Invisible")
        self.btn_invisible.setMinimumHeight(30)
        self.btn_invisible.setStyleSheet("background-image: url(:/icons_svg/images/icons_svg/icon_invisible.svg)")
        self.btn_invisible.clicked.connect(lambda: self.send_signal("invisible"))
        self.btn_invisible.setCursor(Qt.PointingHandCursor)

        # ADD WIDGETS TO LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.layout_content.addWidget(self.line_edit)
        self.layout_content.addWidget(self.label)
        self.layout_content.addWidget(self.btn_online)
        self.layout_content.addWidget(self.btn_idle)
        self.layout_content.addWidget(self.btn_busy)
        self.layout_content.addWidget(self.btn_invisible)

        # SET DROP SHADOW
        # ///////////////////////////////////////////////////////////////
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(self.shadow)
    
    # SEND SIGNAL TO TOP USER WIDGET
    # ///////////////////////////////////////////////////////////////
    def send_signal(self, status):
        self.status.emit(status)