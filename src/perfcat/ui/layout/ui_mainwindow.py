# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLayout, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)
import asset_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 722)
        MainWindow.setMinimumSize(QSize(1200, 540))
        icon = QIcon()
        icon.addFile(u":/icon_b/svg_blue/xing.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"*{\n"
"border-radius:8;\n"
"}\n"
"\n"
"#window {\n"
"background-color:#2c313c;\n"
"}\n"
"\n"
"#left_menu_frame{\n"
"background-color:#1b1e23;\n"
"}\n"
"\n"
"#title_bar_frame{\n"
"background-color:#343b48;\n"
"}\n"
"\n"
"#status_bar_frame{\n"
"background-color:#343b48;\n"
"}\n"
"\n"
"#content_right_frame {\n"
"background-color:#343b48;\n"
"}\n"
"\n"
"#left_column_frame {\n"
"background-color:#343b48;\n"
"border-radius:0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(0, 0))
        self.container.setStyleSheet(u"")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.container.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.left_menu_frame = QFrame(self.container)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMinimumSize(QSize(50, 0))
        self.left_menu_frame.setMaximumSize(QSize(240, 16777215))
        self.left_menu_frame.setStyleSheet(u"")
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.left_menu_frame.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.left_menu_frame)

        self.left_column_frame = QFrame(self.container)
        self.left_column_frame.setObjectName(u"left_column_frame")
        self.left_column_frame.setMinimumSize(QSize(0, 0))
        self.left_column_frame.setMaximumSize(QSize(0, 16777215))
        self.left_column_frame.setFrameShape(QFrame.StyledPanel)
        self.left_column_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_column_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.left_column_frame)

        self.app_frame = QFrame(self.container)
        self.app_frame.setObjectName(u"app_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_frame.sizePolicy().hasHeightForWidth())
        self.app_frame.setSizePolicy(sizePolicy)
        self.app_frame.setFrameShape(QFrame.StyledPanel)
        self.app_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.app_frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar_frame = QFrame(self.app_frame)
        self.title_bar_frame.setObjectName(u"title_bar_frame")
        self.title_bar_frame.setMinimumSize(QSize(0, 40))
        self.title_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.title_bar_frame.setStyleSheet(u"")
        self.title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.title_bar_frame.setFrameShadow(QFrame.Raised)
        self.title_bar_frame.setLineWidth(8)
        self.title_bar_frame.setMidLineWidth(10)
        self.verticalLayout_4 = QVBoxLayout(self.title_bar_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.title_bar_frame)

        self.content_frame = QFrame(self.app_frame)
        self.content_frame.setObjectName(u"content_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.content_frame.sizePolicy().hasHeightForWidth())
        self.content_frame.setSizePolicy(sizePolicy1)
        self.content_frame.setStyleSheet(u"")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Plain)
        self.content_frame.setLineWidth(8)
        self.content_frame.setMidLineWidth(14)
        self.horizontalLayout_3 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.content_left_frame = QFrame(self.content_frame)
        self.content_left_frame.setObjectName(u"content_left_frame")
        self.content_left_frame.setFrameShape(QFrame.StyledPanel)
        self.content_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.content_left_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, -1, -1, -1)

        self.horizontalLayout_3.addWidget(self.content_left_frame)

        self.content_right_frame = QFrame(self.content_frame)
        self.content_right_frame.setObjectName(u"content_right_frame")
        self.content_right_frame.setMaximumSize(QSize(0, 16777215))
        self.content_right_frame.setBaseSize(QSize(0, 0))
        self.content_right_frame.setFrameShape(QFrame.StyledPanel)
        self.content_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.content_right_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.content_right_frame)


        self.verticalLayout.addWidget(self.content_frame)

        self.status_bar_frame = QFrame(self.app_frame)
        self.status_bar_frame.setObjectName(u"status_bar_frame")
        self.status_bar_frame.setMinimumSize(QSize(40, 26))
        self.status_bar_frame.setStyleSheet(u"")
        self.status_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.status_bar_frame.setFrameShadow(QFrame.Raised)
        self.status_bar_frame.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.status_bar_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.status_bar_frame)


        self.horizontalLayout.addWidget(self.app_frame)


        self.gridLayout.addWidget(self.container, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
    # retranslateUi

