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
import app.modules.ui_functions.functions as ui_functions
from app.modules.app_settings.settings import *
import os

# TOOLTIP / LABEL StyleSheet
style_tooltip = """ 
QLabel {		
	background-color: #0b0b0c;	
	color: rgb(230, 230, 230);
	padding-left: 10px;
	padding-right: 10px;
	border-radius: 17px;
    border: 1px solid #2f3032;
    border-left: 3px solid #bdff00;
    font: 800 9pt "Segoe UI";
}
"""

# CUSTOM LEFT MENU
class LeftMenuButton(QWidget):
    # SIGNALS
    clicked = Signal()
    released = Signal()

    def __init__(self, parent, name, icon, tooltip):
        QWidget.__init__(self)
        # APP PATH
        app_path = os.path.abspath(os.getcwd())
        icon_path = os.path.join(app_path, icon)

        # GET SETTINGS
        settings = Settings()
        self.settings = settings.items

        # DEFAULT PARAMETERS
        self.width = 40
        self.height = 40
        self.pos_x = 0
        self.pos_y = 0
        self.border_radius = 10
        self.parent = parent
        self.setGeometry(0, 0, self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(name)
        
        # BG COLORS
        self.color_default = QColor(self.settings["left_menu"]["color"])
        self.color_hover = QColor(self.settings["left_menu"]["color_hover"])
        self.color_pressed = QColor(self.settings["left_menu"]["color_pressed"])
        self._set_color = self.color_default

        # ICON
        self.icon_color = QColor(0xE6E6E6)
        self.icon_color_pressed = QColor(0x151617)
        self._set_icon_path = icon_path        
        self._set_icon_color = self.icon_color

        # TOOLTIP
        self.tooltip_text = tooltip
        self.tooltip = _ToolTip(parent, tooltip)
        self.tooltip.hide()

    # PAINT EVENT
    # Responsible for painting the button, as well as the icon
    def paintEvent(self, event):
        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # BRUSH
        brush = QBrush(self._set_color)

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.setBrush(brush)
        paint.drawRoundedRect(rect, self.border_radius, self.border_radius)

        # DRAW ICONS
        self.icon_paint(paint, self._set_icon_path, rect)

        # END PAINTER
        paint.end()

    # DRAW ICON WITH COLORS
    def icon_paint(self, qp, image, rect):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._set_icon_color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2, 
            (rect.height() - icon.height()) / 2,
            icon
        )        
        painter.end()

    # REPAINT BTN
    # Reaload/Repaint BTN
    def repaint_btn(self, event):
        if event == QEvent.Enter:            
            self.repaint()
        if event == QEvent.Leave:            
            self.repaint()
        if event == QEvent.MouseButtonPress:
            self.repaint()
        if event == QEvent.MouseButtonRelease:            
            self.repaint()

    # CHANGE STYLES
    # Functions with custom styles
    def change_style(self, event):
        if event == QEvent.Enter:
            self._set_color = self.color_hover
            self.repaint_btn(event)          
        elif event == QEvent.Leave:
            self._set_color = self.color_default
            self.repaint_btn(event) 
        elif event == QEvent.MouseButtonPress:            
            self._set_color = self.color_pressed
            self._set_icon_color = self.icon_color_pressed
            self.repaint_btn(event) 
        elif event == QEvent.MouseButtonRelease:
            self._set_color = self.color_hover
            self._set_icon_color = self.icon_color
            self.repaint_btn(event) 

    # MOVE TOOLTIP
    def move_tooltip(self):
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSTION
        # Return absolute position of widget inside app
        pos = self.parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        pos_x = pos.x() + self.width + 12
        pos_y = pos.y() + (self.width - self.tooltip.height()) // 2

        # SET POSITION TO WIDGET
        # Move tooltip position
        self.tooltip.move(pos_x, pos_y)      

    # MOUSE OVER
    # Event triggered when the mouse is over the BTN
    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        self.move_tooltip()
        self.tooltip.show()

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        self.move_tooltip()
        self.tooltip.hide()

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            # EMIT SIGNAL
            self.clicked.emit()
            # SET FOCUS
            self.setFocus()

    # MOUSE RELEASED
    # Event triggered after the mouse button is released
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            # EMIT SIGNAL
            self.released.emit()

class _ToolTip(QLabel):
    def __init__(self, parent, tooltip):
        QLabel.__init__(self)

        # LABEL SETUP
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style_tooltip)
        self.setMinimumHeight(36)
        self.setParent(parent)
        self.setText(tooltip)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(self.shadow)

        # SET OPACITY
        self.opacity = QGraphicsOpacityEffect(self)
        self.opacity.setOpacity(0.85)
        self.setGraphicsEffect(self.opacity)

    
