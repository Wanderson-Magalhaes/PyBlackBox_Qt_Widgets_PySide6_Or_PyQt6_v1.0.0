# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_messagesEjpDxJ.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_chat_page(object):
    def setupUi(self, chat_page):
        if not chat_page.objectName():
            chat_page.setObjectName(u"chat_page")
        chat_page.resize(880, 616)
        chat_page.setStyleSheet(u"QWidget { color: rgb(165, 165, 165); }\n"
"#chat_page{\n"
"	background-color: rgb(0, 0, 0);	\n"
"}\n"
"/* TOP */\n"
"#top {\n"
"	background-color: rgb(30, 32, 33);\n"
"	border-radius: 10px;\n"
"}\n"
"#user_name { \n"
"	color: rgb(179, 179, 179);\n"
"	font: 600 12pt \"Segoe UI\";\n"
"}\n"
"#user_image {\n"
"	border: 1px solid rgb(30, 32, 33);\n"
"	background-color: rgb(47, 48, 50);\n"
"	border-radius: 20px;\n"
"}\n"
"#top QPushButton {\n"
"	background-color: rgb(47, 48, 50);\n"
"	border-radius: 20px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"#top QPushButton:hover {\n"
"	background-color: rgb(61, 62, 65);\n"
"}\n"
"#top QPushButton:pressed {\n"
"	background-color: rgb(16, 17, 18);\n"
"}\n"
"#btn_attachment_top {	\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_attachment.svg);\n"
"}\n"
"#btn_more_top {	\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_more_options.svg);\n"
"}\n"
"/* BOTTOM */\n"
"#bottom QPushButton {\n"
"	background-color: rgb(47, 4"
                        "8, 50);\n"
"	border-radius: 20px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"#bottom QPushButton:hover {\n"
"	background-color: rgb(61, 62, 65);\n"
"}\n"
"#bottom QPushButton:pressed {\n"
"	background-color: rgb(16, 17, 18);\n"
"}\n"
"#send_message_frame { \n"
"	background-color: rgb(47, 48, 50);\n"
"	border-radius: 20px;\n"
"}\n"
"#send_message_frame QPushButton {\n"
"	background-color: rgb(76, 77, 80);\n"
"	border-radius: 15px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"#send_message_frame QPushButton:hover {\n"
"	background-color: rgb(81, 82, 86);\n"
"}\n"
"#send_message_frame QPushButton:pressed {\n"
"	background-color: rgb(16, 17, 18);\n"
"}\n"
"#line_edit_message {\n"
"	background-color: transparent;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(149, 199, 0);\n"
"	border: none;\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	"
                        "font: 10pt \"Segoe UI\";\n"
"	color: rgb(94, 96, 100);\n"
"}\n"
"#line_edit_message:focus {\n"
"	color: rgb(165, 165, 165);\n"
"}\n"
"#btn_emoticon{\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_emoticons.svg);\n"
"}\n"
"#btn_send_message{	\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_send.svg);\n"
"}\n"
"#btn_attachment_bottom{	\n"
"	\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_more_options.svg);\n"
"}")
        self.verticalLayout = QVBoxLayout(chat_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top = QFrame(chat_page)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 60))
        self.top.setMaximumSize(QSize(16777215, 60))
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.user_image = QLabel(self.top)
        self.user_image.setObjectName(u"user_image")
        self.user_image.setMinimumSize(QSize(40, 40))
        self.user_image.setMaximumSize(QSize(40, 40))
        self.user_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.user_image)

        self.user_information_frame = QFrame(self.top)
        self.user_information_frame.setObjectName(u"user_information_frame")
        self.user_information_frame.setFrameShape(QFrame.NoFrame)
        self.user_information_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.user_information_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.user_name = QLabel(self.user_information_frame)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setMinimumSize(QSize(0, 22))
        self.user_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.user_name)

        self.user_description = QLabel(self.user_information_frame)
        self.user_description.setObjectName(u"user_description")
        self.user_description.setStyleSheet(u"background: transparent;")

        self.verticalLayout_2.addWidget(self.user_description)


        self.horizontalLayout.addWidget(self.user_information_frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.last_time_connected = QLabel(self.top)
        self.last_time_connected.setObjectName(u"last_time_connected")

        self.horizontalLayout.addWidget(self.last_time_connected)

        self.btn_attachment_top = QPushButton(self.top)
        self.btn_attachment_top.setObjectName(u"btn_attachment_top")
        self.btn_attachment_top.setMinimumSize(QSize(40, 40))
        self.btn_attachment_top.setMaximumSize(QSize(40, 40))
        self.btn_attachment_top.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_attachment_top)

        self.btn_more_top = QPushButton(self.top)
        self.btn_more_top.setObjectName(u"btn_more_top")
        self.btn_more_top.setMinimumSize(QSize(40, 40))
        self.btn_more_top.setMaximumSize(QSize(40, 40))
        self.btn_more_top.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_more_top)


        self.verticalLayout.addWidget(self.top)

        self.chat_messages = QScrollArea(chat_page)
        self.chat_messages.setObjectName(u"chat_messages")
        self.chat_messages.setStyleSheet(u"background: transparent")
        self.chat_messages.setFrameShape(QFrame.NoFrame)
        self.chat_messages.setFrameShadow(QFrame.Raised)
        self.chat_messages.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chat_messages.setWidgetResizable(True)
        self.chat_messages.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.messages_widget = QWidget()
        self.messages_widget.setObjectName(u"messages_widget")
        self.messages_widget.setGeometry(QRect(0, 0, 862, 486))
        self.messages_widget.setStyleSheet(u"background: transparent")
        self.chat_layout = QVBoxLayout(self.messages_widget)
        self.chat_layout.setSpacing(0)
        self.chat_layout.setObjectName(u"chat_layout")
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.chat_layout.addItem(self.verticalSpacer)

        self.messages_frame = QFrame(self.messages_widget)
        self.messages_frame.setObjectName(u"messages_frame")
        self.messages_frame.setFrameShape(QFrame.NoFrame)
        self.messages_frame.setFrameShadow(QFrame.Raised)
        self.chat_messages_layout = QVBoxLayout(self.messages_frame)
        self.chat_messages_layout.setSpacing(0)
        self.chat_messages_layout.setObjectName(u"chat_messages_layout")
        self.chat_messages_layout.setContentsMargins(0, 0, 0, 0)

        self.chat_layout.addWidget(self.messages_frame)

        self.chat_messages.setWidget(self.messages_widget)

        self.verticalLayout.addWidget(self.chat_messages)

        self.bottom = QFrame(chat_page)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 40))
        self.bottom.setMaximumSize(QSize(16777215, 40))
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.send_message_frame = QFrame(self.bottom)
        self.send_message_frame.setObjectName(u"send_message_frame")
        self.send_message_frame.setFrameShape(QFrame.StyledPanel)
        self.send_message_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.send_message_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.btn_emoticon = QPushButton(self.send_message_frame)
        self.btn_emoticon.setObjectName(u"btn_emoticon")
        self.btn_emoticon.setMinimumSize(QSize(30, 30))
        self.btn_emoticon.setMaximumSize(QSize(30, 30))
        self.btn_emoticon.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btn_emoticon)

        self.line_edit_message = QLineEdit(self.send_message_frame)
        self.line_edit_message.setObjectName(u"line_edit_message")
        self.line_edit_message.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_3.addWidget(self.line_edit_message)

        self.btn_send_message = QPushButton(self.send_message_frame)
        self.btn_send_message.setObjectName(u"btn_send_message")
        self.btn_send_message.setMinimumSize(QSize(30, 30))
        self.btn_send_message.setMaximumSize(QSize(30, 30))
        self.btn_send_message.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btn_send_message)


        self.horizontalLayout_2.addWidget(self.send_message_frame)

        self.btn_attachment_bottom = QPushButton(self.bottom)
        self.btn_attachment_bottom.setObjectName(u"btn_attachment_bottom")
        self.btn_attachment_bottom.setMinimumSize(QSize(40, 40))
        self.btn_attachment_bottom.setMaximumSize(QSize(40, 40))
        self.btn_attachment_bottom.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_attachment_bottom)


        self.verticalLayout.addWidget(self.bottom)


        self.retranslateUi(chat_page)

        QMetaObject.connectSlotsByName(chat_page)
    # setupUi

    def retranslateUi(self, chat_page):
        chat_page.setWindowTitle(QCoreApplication.translate("chat_page", u"Form", None))
        self.user_image.setText("")
        self.user_name.setText(QCoreApplication.translate("chat_page", u"User name", None))
        self.user_description.setText(QCoreApplication.translate("chat_page", u"User description", None))
        self.last_time_connected.setText(QCoreApplication.translate("chat_page", u"connected last time 24h ago", None))
        self.btn_attachment_top.setText("")
        self.btn_more_top.setText("")
        self.btn_emoticon.setText("")
        self.line_edit_message.setPlaceholderText(QCoreApplication.translate("chat_page", u"Message #user", None))
        self.btn_send_message.setText("")
        self.btn_attachment_bottom.setText("")
    # retranslateUi

