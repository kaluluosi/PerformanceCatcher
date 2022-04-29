# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_left_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import asset_rc

class Ui_LeftMenu(object):
    def setupUi(self, LeftMenu):
        if not LeftMenu.objectName():
            LeftMenu.setObjectName(u"LeftMenu")
        LeftMenu.resize(244, 732)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LeftMenu.sizePolicy().hasHeightForWidth())
        LeftMenu.setSizePolicy(sizePolicy)
        LeftMenu.setMinimumSize(QSize(50, 0))
        LeftMenu.setMaximumSize(QSize(244, 16777215))
        LeftMenu.setStyleSheet(u"#LeftMenu {\n"
"background-color: #1b1e23;\n"
"border-radius:8;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color:#1b1e23;\n"
"border-radius: 8;\n"
"height:40;\n"
"text-align:left;\n"
"padding-left:15;\n"
"padding-top:2;\n"
"padding-bottom:2;\n"
"color:#6b7884;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#21252d;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#2c313c;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:#2c313c;\n"
"}\n"
"\n"
"\n"
"#bottom{\n"
"border-top:1 solid #272c36;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"#nav_menu {\n"
"border-top:1 solid #272c36;\n"
"border-radius: 0\uff1b\n"
"}\n"
"\n"
"#LeftMenu #scrollArea,#scrollAreaWidgetContents_3{\n"
"background-color:#1b1e23;\n"
"border:none;\n"
"}\n"
"\n"
"#btn_toggle:checked{\n"
"background-color:#21252d;\n"
"}\n"
"\n"
"\n"
"QToolTip { \n"
"color:#6b7884;\n"
"background-color: #1b1e23; \n"
"border: 0px; \n"
"border-radius:8;\n"
"border-left: 2px solid #4f9fee;\n"
"}")
        self.verticalLayout = QVBoxLayout(LeftMenu)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(LeftMenu)
        self.bg.setObjectName(u"bg")
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setMinimumSize(QSize(240, 0))
        self.bg.setMaximumSize(QSize(240, 16777215))
        self.bg.setStyleSheet(u"")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bg)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.top = QFrame(self.bg)
        self.top.setObjectName(u"top")
        self.top.setMaximumSize(QSize(16777215, 46))
        self.top.setLayoutDirection(Qt.RightToLeft)
        self.top.setStyleSheet(u"")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.top.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.top)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.top)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/icon_w/svg_white/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon_b/svg_blue/circle-left.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(16, 16))
        self.btn_toggle.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_toggle)


        self.verticalLayout_6.addWidget(self.top)

        self.scrollArea = QScrollArea(self.bg)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 220, 553))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nav_menu = QFrame(self.scrollAreaWidgetContents_3)
        self.nav_menu.setObjectName(u"nav_menu")
        self.nav_menu.setLayoutDirection(Qt.LeftToRight)
        self.nav_menu.setStyleSheet(u"")
        self.nav_menu.setFrameShape(QFrame.StyledPanel)
        self.nav_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.nav_menu)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.btn_home = QPushButton(self.nav_menu)
        self.btn_home.setObjectName(u"btn_home")
        icon1 = QIcon()
        icon1.addFile(u":/icon_w/svg_white/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon_b/svg_blue/home.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_home.setIcon(icon1)
        self.btn_home.setCheckable(True)

        self.verticalLayout_5.addWidget(self.btn_home)


        self.verticalLayout_2.addWidget(self.nav_menu)

        self.verticalSpacer = QSpacerItem(20, 494, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.bottom = QFrame(self.bg)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setStyleSheet(u"")
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.bottom)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 6, 0, 0)
        self.btn_about = QPushButton(self.bottom)
        self.btn_about.setObjectName(u"btn_about")
        icon2 = QIcon()
        icon2.addFile(u":/icon_w/svg_white/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon_b/svg_blue/info.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_about.setIcon(icon2)
        self.btn_about.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btn_about)

        self.btn_setting = QPushButton(self.bottom)
        self.btn_setting.setObjectName(u"btn_setting")
        icon3 = QIcon()
        icon3.addFile(u":/icon_w/svg_white/wrench.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon_b/svg_blue/wrench.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_setting.setIcon(icon3)
        self.btn_setting.setCheckable(True)
        self.btn_setting.setChecked(False)

        self.verticalLayout_4.addWidget(self.btn_setting)


        self.verticalLayout_6.addWidget(self.bottom)


        self.verticalLayout.addWidget(self.bg)


        self.retranslateUi(LeftMenu)

        QMetaObject.connectSlotsByName(LeftMenu)
    # setupUi

    def retranslateUi(self, LeftMenu):
        LeftMenu.setWindowTitle(QCoreApplication.translate("LeftMenu", u"Form", None))
#if QT_CONFIG(tooltip)
        self.btn_toggle.setToolTip(QCoreApplication.translate("LeftMenu", u"<html><head/><body><p>\u9690\u85cf\u83dc\u5355</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_toggle.setWhatsThis(QCoreApplication.translate("LeftMenu", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_toggle.setText(QCoreApplication.translate("LeftMenu", u"    \u9690\u85cf\u83dc\u5355", None))
        self.btn_home.setText(QCoreApplication.translate("LeftMenu", u"    \u9996\u9875", None))
        self.btn_about.setText(QCoreApplication.translate("LeftMenu", u"    \u5173\u4e8e", None))
#if QT_CONFIG(tooltip)
        self.btn_setting.setToolTip(QCoreApplication.translate("LeftMenu", u"<html><head/><body><p>\u8bbe\u7f6e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setting.setText(QCoreApplication.translate("LeftMenu", u"    \u8bbe\u7f6e", None))
    # retranslateUi

