# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMcMyCG.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 720)
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"/* DEFAULT */\n"
"QWidget {\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(230, 230, 230);\n"
"	selection-background-color: rgb(86, 115, 0);\n"
"}\n"
"/* Bg App */\n"
"#bg_app {	\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(30, 32, 33);\n"
"}\n"
"\n"
"/* Left Menu */\n"
"#left_menu {\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"/* Logo Top */\n"
"#logo_top {\n"
"	background-image: url(:/images_svg/images/images_svg/logo_symbol_top.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* Buttons */\n"
"#left_menu QPushButton {\n"
"	border: none;	\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"#left_menu QPushButton:hover {\n"
"	background-color: rgb(21, 22, 23);\n"
"}\n"
"#left_menu QPushButton:pressed {\n"
"	background-color: rgb(172, 229, 0);\n"
"}\n"
"#add_user_btn {	\n"
"	background-image: url(:/icons_svg/images/icons_svg/ico"
                        "n_add_user.svg);\n"
"}\n"
"#settings_btn {	\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_settings.svg);\n"
"}\n"
"\n"
"/* Left Messages */\n"
"#left_messages {\n"
"	background-color: rgb(21, 22, 23);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(30, 32, 33);\n"
"}\n"
"\n"
"/* Top */\n"
"#top_messages {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(47, 48, 50);\n"
"}\n"
"\n"
"/* Search Message */\n"
"#search_sms_frame .QLineEdit {\n"
"	border: 2px solid rgb(47, 48, 50);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 30px;\n"
"	padding-right: 10px;\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_search.svg);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"#search_sms_frame .QLineEdit:hover {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(62, 63, 66);\n"
"}\n"
"#search_sms_frame .QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(53, 54"
                        ", 56);\n"
"	background-color: rgb(14, 14, 15);\n"
"}\n"
"\n"
"/* Menus Scroll Area */\n"
"#left_messages_scroll, #messages_scroll {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/* Bottom / Signal */\n"
"#bottom_messages {	\n"
"	background-color: rgb(30, 32, 33);\n"
"}\n"
"#signal_icon { \n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_signal.svg);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"#label_top{	\n"
"	font: 800 10pt \"Segoe UI\";\n"
"	color: rgb(189, 255, 0);\n"
"}\n"
"#label_bottom {	\n"
"	color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"/* Right Content */\n"
"#right_content {\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"/* Top Bar */\n"
"#top_bar {\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"/* Title Bar */\n"
"#title_bar {\n"
"	background-image: url(:/images_svg/images/images_svg/text_logo.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	border-left: 15px solid trans"
                        "parent;\n"
"}\n"
"\n"
"/* Top BTNs */\n"
"#top_btns {  }\n"
"#top_btns .QPushButton {	\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	outline: none;\n"
"	border-radius: 8px;\n"
"	text-align: left;\n"
"}\n"
"#top_btns .QPushButton:hover { background-color: rgb(21, 22, 23); }\n"
"#top_btns .QPushButton:pressed { background-color: rgb(172, 229, 0); }\n"
"#top_btns #close_app_btn:hover { background-color: rgb(255, 0, 127); }\n"
"#top_btns #close_app_btn:pressed { background-color: rgb(172, 229, 0); }\n"
"\n"
"/* Content / Pages */\n"
"#app_pages {\n"
"	background-color: transparent;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(47, 48, 50);\n"
"    min-widt"
                        "h: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(47, 48"
                        ", 50);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: transparent;\n"
"     height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"")
        self.margins_app = QVBoxLayout(self.stylesheet)
        self.margins_app.setSpacing(0)
        self.margins_app.setObjectName(u"margins_app")
        self.margins_app.setContentsMargins(10, 10, 10, 10)
        self.bg_app = QFrame(self.stylesheet)
        self.bg_app.setObjectName(u"bg_app")
        self.bg_app.setStyleSheet(u"#bg_app { border-radius: 10px; }")
        self.bg_app.setFrameShape(QFrame.NoFrame)
        self.bg_app.setFrameShadow(QFrame.Raised)
        self.bg_app.setLineWidth(0)
        self.base_Layout = QVBoxLayout(self.bg_app)
        self.base_Layout.setSpacing(0)
        self.base_Layout.setObjectName(u"base_Layout")
        self.base_Layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_Layout = QHBoxLayout()
        self.horizontal_Layout.setSpacing(0)
        self.horizontal_Layout.setObjectName(u"horizontal_Layout")
        self.left_menu = QFrame(self.bg_app)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(50, 0))
        self.left_menu.setMaximumSize(QSize(50, 16777215))
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.left_menu.setLineWidth(0)
        self.vertical_left_menu_layout = QVBoxLayout(self.left_menu)
        self.vertical_left_menu_layout.setSpacing(0)
        self.vertical_left_menu_layout.setObjectName(u"vertical_left_menu_layout")
        self.vertical_left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_top = QLabel(self.left_menu)
        self.logo_top.setObjectName(u"logo_top")
        self.logo_top.setMinimumSize(QSize(50, 50))
        self.logo_top.setMaximumSize(QSize(50, 50))

        self.vertical_left_menu_layout.addWidget(self.logo_top)

        self.top_menus = QFrame(self.left_menu)
        self.top_menus.setObjectName(u"top_menus")
        self.top_menus.setMinimumSize(QSize(0, 50))
        self.top_menus.setFrameShape(QFrame.NoFrame)
        self.top_menus.setFrameShadow(QFrame.Raised)
        self.top_menus_layout = QVBoxLayout(self.top_menus)
        self.top_menus_layout.setSpacing(5)
        self.top_menus_layout.setObjectName(u"top_menus_layout")
        self.top_menus_layout.setContentsMargins(5, 5, 5, 5)

        self.vertical_left_menu_layout.addWidget(self.top_menus)

        self.spacer_vertical_menu = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_left_menu_layout.addItem(self.spacer_vertical_menu)

        self.bottom_menus = QFrame(self.left_menu)
        self.bottom_menus.setObjectName(u"bottom_menus")
        self.bottom_menus.setMinimumSize(QSize(0, 50))
        self.bottom_menus.setFrameShape(QFrame.NoFrame)
        self.bottom_menus.setFrameShadow(QFrame.Raised)
        self.bottom_menus_layout = QVBoxLayout(self.bottom_menus)
        self.bottom_menus_layout.setSpacing(5)
        self.bottom_menus_layout.setObjectName(u"bottom_menus_layout")
        self.bottom_menus_layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.bottom_menus_layout.setContentsMargins(5, 5, 5, 5)

        self.vertical_left_menu_layout.addWidget(self.bottom_menus)


        self.horizontal_Layout.addWidget(self.left_menu)

        self.left_messages = QFrame(self.bg_app)
        self.left_messages.setObjectName(u"left_messages")
        self.left_messages.setMinimumSize(QSize(243, 0))
        self.left_messages.setMaximumSize(QSize(243, 16777215))
        self.left_messages.setFrameShape(QFrame.NoFrame)
        self.left_messages.setFrameShadow(QFrame.Raised)
        self.left_messages.setLineWidth(0)
        self.left_box_layout = QVBoxLayout(self.left_messages)
        self.left_box_layout.setSpacing(0)
        self.left_box_layout.setObjectName(u"left_box_layout")
        self.left_box_layout.setContentsMargins(0, 0, 0, 0)
        self.top_messages = QFrame(self.left_messages)
        self.top_messages.setObjectName(u"top_messages")
        self.top_messages.setMinimumSize(QSize(0, 105))
        self.top_messages.setMaximumSize(QSize(16777215, 105))
        self.top_messages.setFrameShape(QFrame.NoFrame)
        self.top_messages.setFrameShadow(QFrame.Raised)
        self.top_messages_layout = QVBoxLayout(self.top_messages)
        self.top_messages_layout.setSpacing(0)
        self.top_messages_layout.setObjectName(u"top_messages_layout")
        self.top_messages_layout.setContentsMargins(0, 0, 0, 0)
        self.top_user_frame = QFrame(self.top_messages)
        self.top_user_frame.setObjectName(u"top_user_frame")
        self.top_user_frame.setMinimumSize(QSize(0, 60))
        self.top_user_frame.setMaximumSize(QSize(16777215, 60))
        self.top_user_frame.setFrameShape(QFrame.NoFrame)
        self.top_user_frame.setFrameShadow(QFrame.Raised)

        self.top_messages_layout.addWidget(self.top_user_frame)

        self.search_sms_frame = QFrame(self.top_messages)
        self.search_sms_frame.setObjectName(u"search_sms_frame")
        self.search_sms_frame.setMinimumSize(QSize(0, 40))
        self.search_sms_frame.setMaximumSize(QSize(16777215, 40))
        self.search_sms_frame.setFrameShape(QFrame.NoFrame)
        self.search_sms_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.search_sms_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.search_line_edit = QLineEdit(self.search_sms_frame)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setMinimumSize(QSize(0, 30))
        self.search_line_edit.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_6.addWidget(self.search_line_edit, 0, Qt.AlignVCenter)


        self.top_messages_layout.addWidget(self.search_sms_frame)


        self.left_box_layout.addWidget(self.top_messages)

        self.left_messages_scroll = QScrollArea(self.left_messages)
        self.left_messages_scroll.setObjectName(u"left_messages_scroll")
        self.left_messages_scroll.setFrameShape(QFrame.NoFrame)
        self.left_messages_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.left_messages_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.left_messages_scroll.setWidgetResizable(True)
        self.messages_scroll = QWidget()
        self.messages_scroll.setObjectName(u"messages_scroll")
        self.messages_scroll.setGeometry(QRect(0, 0, 240, 524))
        self.messages_layout_base = QVBoxLayout(self.messages_scroll)
        self.messages_layout_base.setSpacing(0)
        self.messages_layout_base.setObjectName(u"messages_layout_base")
        self.messages_layout_base.setContentsMargins(0, 5, 0, 5)
        self.messages_frame = QFrame(self.messages_scroll)
        self.messages_frame.setObjectName(u"messages_frame")
        self.messages_frame.setFrameShape(QFrame.NoFrame)
        self.messages_frame.setFrameShadow(QFrame.Raised)
        self.messages_layout = QVBoxLayout(self.messages_frame)
        self.messages_layout.setSpacing(5)
        self.messages_layout.setObjectName(u"messages_layout")
        self.messages_layout.setContentsMargins(0, 0, 0, 0)

        self.messages_layout_base.addWidget(self.messages_frame, 0, Qt.AlignTop)

        self.left_messages_scroll.setWidget(self.messages_scroll)

        self.left_box_layout.addWidget(self.left_messages_scroll)

        self.bottom_messages = QFrame(self.left_messages)
        self.bottom_messages.setObjectName(u"bottom_messages")
        self.bottom_messages.setMinimumSize(QSize(0, 65))
        self.bottom_messages.setMaximumSize(QSize(16777215, 65))
        self.bottom_messages.setFrameShape(QFrame.NoFrame)
        self.bottom_messages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.bottom_messages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, 0, 10, 0)
        self.signal_frame = QFrame(self.bottom_messages)
        self.signal_frame.setObjectName(u"signal_frame")
        self.signal_frame.setMinimumSize(QSize(0, 35))
        self.signal_frame.setMaximumSize(QSize(16777215, 35))
        self.signal_frame.setFrameShape(QFrame.NoFrame)
        self.signal_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.signal_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.signal_icon = QFrame(self.signal_frame)
        self.signal_icon.setObjectName(u"signal_icon")
        self.signal_icon.setMaximumSize(QSize(30, 16777215))
        self.signal_icon.setFrameShape(QFrame.NoFrame)
        self.signal_icon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.signal_icon)

        self.signal_text = QFrame(self.signal_frame)
        self.signal_text.setObjectName(u"signal_text")
        self.signal_text.setFrameShape(QFrame.NoFrame)
        self.signal_text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.signal_text)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 2, 0, 2)
        self.label_top = QLabel(self.signal_text)
        self.label_top.setObjectName(u"label_top")

        self.verticalLayout_7.addWidget(self.label_top)

        self.label_bottom = QLabel(self.signal_text)
        self.label_bottom.setObjectName(u"label_bottom")

        self.verticalLayout_7.addWidget(self.label_bottom)


        self.horizontalLayout_2.addWidget(self.signal_text)


        self.verticalLayout_5.addWidget(self.signal_frame, 0, Qt.AlignVCenter)


        self.left_box_layout.addWidget(self.bottom_messages)


        self.horizontal_Layout.addWidget(self.left_messages)

        self.right_content = QFrame(self.bg_app)
        self.right_content.setObjectName(u"right_content")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.right_content.setFont(font)
        self.right_content.setFrameShape(QFrame.NoFrame)
        self.right_content.setFrameShadow(QFrame.Raised)
        self.right_content.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.right_content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.right_content)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 45))
        self.top_bar.setMaximumSize(QSize(16777215, 45))
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.top_bar.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QLabel(self.top_bar)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setLineWidth(0)

        self.horizontalLayout.addWidget(self.title_bar)

        self.top_btns = QFrame(self.top_bar)
        self.top_btns.setObjectName(u"top_btns")
        self.top_btns.setMaximumSize(QSize(100, 16777215))
        self.top_btns.setFrameShape(QFrame.NoFrame)
        self.top_btns.setFrameShadow(QFrame.Raised)
        self.top_btns.setLineWidth(0)
        self.top_btn_layout = QHBoxLayout(self.top_btns)
        self.top_btn_layout.setSpacing(4)
        self.top_btn_layout.setObjectName(u"top_btn_layout")
        self.top_btn_layout.setContentsMargins(0, 0, 0, 0)
        self.minimize_app_btn = QPushButton(self.top_btns)
        self.minimize_app_btn.setObjectName(u"minimize_app_btn")
        self.minimize_app_btn.setMinimumSize(QSize(28, 28))
        self.minimize_app_btn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.NoAntialias)
        self.minimize_app_btn.setFont(font1)
        self.minimize_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_app_btn.setStyleSheet(u"background-image: url(:/icons_svg/images/icons_svg/icon_minimize.svg);")
        self.minimize_app_btn.setIconSize(QSize(20, 20))

        self.top_btn_layout.addWidget(self.minimize_app_btn)

        self.maximize_restore_app_btn = QPushButton(self.top_btns)
        self.maximize_restore_app_btn.setObjectName(u"maximize_restore_app_btn")
        self.maximize_restore_app_btn.setMinimumSize(QSize(28, 28))
        self.maximize_restore_app_btn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximize_restore_app_btn.setFont(font2)
        self.maximize_restore_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize_restore_app_btn.setStyleSheet(u"background-image: url(:/icons_svg/images/icons_svg/icon_maximize.svg);")
        self.maximize_restore_app_btn.setIconSize(QSize(20, 20))

        self.top_btn_layout.addWidget(self.maximize_restore_app_btn)

        self.close_app_btn = QPushButton(self.top_btns)
        self.close_app_btn.setObjectName(u"close_app_btn")
        self.close_app_btn.setMinimumSize(QSize(28, 28))
        self.close_app_btn.setMaximumSize(QSize(28, 28))
        self.close_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_app_btn.setStyleSheet(u"background-image: url(:/icons_svg/images/icons_svg/icon_close.svg);")
        self.close_app_btn.setIconSize(QSize(20, 20))

        self.top_btn_layout.addWidget(self.close_app_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_btn_layout.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.top_btns)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.right_content)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.content.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.app_pages = QStackedWidget(self.content)
        self.app_pages.setObjectName(u"app_pages")
        self.app_pages.setStyleSheet(u"background-color: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"#home {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/images_svg/images/images_svg/logo_home.svg);\n"
"}")
        self.app_pages.addWidget(self.home)
        self.chat = QWidget()
        self.chat.setObjectName(u"chat")
        self.chat_layout = QVBoxLayout(self.chat)
        self.chat_layout.setSpacing(0)
        self.chat_layout.setObjectName(u"chat_layout")
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.app_pages.addWidget(self.chat)

        self.verticalLayout_4.addWidget(self.app_pages)


        self.verticalLayout.addWidget(self.content)


        self.horizontal_Layout.addWidget(self.right_content)


        self.base_Layout.addLayout(self.horizontal_Layout)


        self.margins_app.addWidget(self.bg_app)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.app_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search messages", None))
        self.label_top.setText(QCoreApplication.translate("MainWindow", u"Signal 80%", None))
        self.label_bottom.setText(QCoreApplication.translate("MainWindow", u"PyBlackBOX server signal", None))
        self.title_bar.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_app_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_app_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_restore_app_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_restore_app_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_app_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_app_btn.setText("")
    # retranslateUi

