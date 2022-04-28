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
    QLayout, QMainWindow, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
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
        MainWindow.setStyleSheet(u"#container {\n"
"background-color:#2c313c;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#left_menu_frame{\n"
"background-color:#1b1e23;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#title_bar_frame{\n"
"background-color:#343b48;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#status_bar_frame{\n"
"background-color:#343b48;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#content_right_frame {\n"
"background-color:#343b48;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#left_column_frame {\n"
"background-color:#343b48;\n"
"}\n"
"\n"
"/* \u4fa7\u8fb9\u83dc\u5355\u680f\u6837\u5f0f */\n"
"\n"
"#LeftMenu {\n"
"background-color: #005dfd;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#LeftMenu QPushButton {\n"
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
"#LeftMenu QPushButton:hover{\n"
"background-color:#21252d;\n"
"}\n"
"\n"
"#LeftMenu QPushButton:pressed{\n"
"background-color:#2c313c;\n"
"}\n"
"\n"
"#LeftMenu QPushButton:checked{\n"
"backgrou"
                        "nd-color:#2c313c;\n"
"}\n"
"\n"
"\n"
"#LeftMenu #bottom{\n"
"border-top:1 solid #272c36;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"#LeftMenu #menu {\n"
"border-top:1 solid #272c36;\n"
"border-radius: 0\uff1b\n"
"}\n"
"\n"
"#LeftMenu #btn_toggle:checked{\n"
"background-color:#21252d;\n"
"}\n"
"\n"
"\n"
"#LeftMenu QToolTip { \n"
"color:#6b7884;\n"
"background-color: #1b1e23; \n"
"border: 0px; \n"
"border-radius:8;\n"
"border-left: 2px solid #4f9fee;\n"
"}\n"
"\n"
"/* \u6807\u9898\u680f\u6837\u5f0f */\n"
"\n"
"#TitleBar #bg{\n"
"background-color:#343b48;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#TitleBar #logo {\n"
"border: 1px solid #3c4454;\n"
"padding-right:10px;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"border-left:none;\n"
"margin-right:5px;\n"
"border-radius:0;\n"
"}\n"
"\n"
"#TitleBar  #logo_title{\n"
"color:#77b3f1;\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"#TitleBar  #lb_title{\n"
"font-size:14px;\n"
"color:#6c7c96;\n"
"}\n"
"\n"
"#TitleBar  QToolButton{\n"
"background-color:#343b48;\n"
"bord"
                        "er:none;\n"
"border-radius:4;\n"
"padding: 4;\n"
"}\n"
"\n"
"#TitleBar QToolButton:hover,\n"
"#TitleBar QToolButton:checked{\n"
"background-color:#3c4454;\n"
"}\n"
"\n"
"\n"
"#TitleBar QToolButton:pressed{\n"
"background-color:#e2e9f7;\n"
"}\n"
"\n"
"#TitleBar #tool{\n"
"border:1px solid #3c4454;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"margin-right:5px;\n"
"border-radius:0;\n"
"}\n"
"\n"
"\n"
"#LeftColumn{\n"
"background-color:#343b48;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#LeftColumn #top{\n"
"background-color: #3c4454;\n"
"border-radius:8;\n"
"}\n"
"\n"
"#LeftColumn #title{\n"
"color:#6c7c96;\n"
"}\n"
"\n"
"#LeftColumn QToolButton{\n"
"border-radius:8;\n"
"border:none;\n"
"padding:4;\n"
"}\n"
"\n"
"#LeftColumn #btn_close:hover{\n"
"background-color:#343b48;\n"
"}\n"
"\n"
"#LeftColumn #btn_close:pressed{\n"
"background-color:#1b1e23;\n"
"}\n"
"")
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
        self.content_left_stacked = QStackedWidget(self.content_frame)
        self.content_left_stacked.setObjectName(u"content_left_stacked")
        sizePolicy.setHeightForWidth(self.content_left_stacked.sizePolicy().hasHeightForWidth())
        self.content_left_stacked.setSizePolicy(sizePolicy)
        self.content_left_stacked.setMaximumSize(QSize(16777215, 16777215))
        self.content_left_stacked.setFrameShape(QFrame.StyledPanel)
        self.content_left_stacked.setFrameShadow(QFrame.Raised)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.content_left_stacked.addWidget(self.page)

        self.horizontalLayout_3.addWidget(self.content_left_stacked)

        self.content_right_frame = QFrame(self.content_frame)
        self.content_right_frame.setObjectName(u"content_right_frame")
        self.content_right_frame.setMinimumSize(QSize(0, 0))
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

