# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cpu_monitor.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CPUMonitor(object):
    def setupUi(self, CPUMonitor):
        if not CPUMonitor.objectName():
            CPUMonitor.setObjectName(u"CPUMonitor")
        CPUMonitor.resize(824, 240)
        CPUMonitor.setMinimumSize(QSize(0, 240))
        CPUMonitor.setMaximumSize(QSize(16777215, 16777215))
        CPUMonitor.setStyleSheet(u"*{\n"
"    border-radius:8;\n"
"    color:#6c7c96;\n"
"}\n"
"\n"
"#container {\n"
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
"#content_frame{\n"
"background-color:#343b48;\n"
"}\n"
"\n"
"#setting_frame {\n"
"background-color:#3c4454;\n"
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
"}\n"
"\n"
"#LeftMenu QPushButton {\n"
"background-color:#1b1e23;\n"
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
"background-color:#2c313c;\n"
"}\n"
""
                        "\n"
"#LeftMenu QPushButton:focus{\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"#LeftMenu #bottom{\n"
"border-top:1 solid #272c36;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"#LeftMenu #nav_menu {\n"
"border-top:1 solid #272c36;\n"
"border-radius: 0\uff1b\n"
"}\n"
"\n"
"#LeftMenu #scrollArea,#scrollAreaWidgetContents_3{\n"
"background-color:#1b1e23;\n"
"border:none;\n"
"}\n"
"\n"
"#LeftMenu #btn_toggle:checked{\n"
"background-color:#21252d;\n"
"}\n"
"\n"
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
"border:none;\n"
""
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
"}\n"
"\n"
"#LeftColumn #top{\n"
"background-color: #3c4454;\n"
"}\n"
"\n"
"#leftColumn #icon{\n"
"\n"
"}\n"
"\n"
"#LeftColumn #title{\n"
"color:#6c7c96;\n"
"}\n"
"\n"
"#LeftColumn QToolButton{\n"
"border:none;\n"
"padding:4;\n"
"background-color: #3c4454;\n"
"}\n"
"\n"
"#LeftColumn #btn_close:hover{\n"
"background-color:#343b48;\n"
"}\n"
"\n"
"#LeftColumn #btn_close:pressed{\n"
"background-color:#1b1e23;\n"
"}\n"
"\n"
"\n"
"/* \u901a\u7528\u63a7\u4ef6 */\n"
"\n"
"QToolTip { \n"
"color:#6b7884;\n"
"background-color: #1b1e23; \n"
"border-left: 2px solid #4f9fee;\n"
"border-radius:"
                        " 8px;\n"
"}\n"
"\n"
"QGroupBox{\n"
"	border: 2px solid gray; \n"
"    border-radius: 3px; \n"
"    margin:10;\n"
"}\n"
"\n"
"QGroupBox::title { \n"
"    subcontrol-position: center top; /* position at the top left*/ \n"
"	subcontrol-origin: border;\n"
"	margin-top:-20px;\n"
"\n"
"}\n"
"\n"
"/* Button */\n"
"QAbstractButton{\n"
"background-color:#1b1e23;\n"
"border:none;\n"
"border-radius:4;\n"
"padding: 4;\n"
"outline:none;\n"
"width:36;\n"
"height:36;\n"
"}\n"
"\n"
"QAbstractButton:hover,\n"
"QAbstractButton:checked{\n"
"background-color:#21252d;\n"
"}\n"
"\n"
"\n"
"QAbstractButton:pressed{\n"
"background-color:#272c36;\n"
"}\n"
"\n"
"QAbstractButton:disabled{\n"
"background-color: #272c36;\n"
"}\n"
"\n"
"QAbstractButton:checked{\n"
"background-color:#568af2;\n"
"color:black;\n"
"}\n"
"\n"
"QAbstractButton:focus{\n"
"border: 2px solid #568af2;\n"
"}\n"
"\n"
"QAbstractButton[style~='success']:checked{\n"
"    background-color: #67c23a;\n"
"}\n"
"QAbstractButton[style~='warning']:checked{\n"
"    background-col"
                        "or: #e6a23c;\n"
"}\n"
"QAbstractButton[style~='danger']:checked{\n"
"    background-color: #f56c6c;\n"
"}\n"
"QAbstractButton[style~='info']:checked{\n"
"    background-color: #909399;\n"
"}\n"
"\n"
"\n"
"/* CheckBox */\n"
"\n"
"QCheckBox::indicator{\n"
"    border:2px solid #6c7c96;\n"
"    border-radius: 2px;\n"
"    width:10px;\n"
"    height:10px;\n"
"    margin-left:8px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    border:2px solid black;\n"
"    image: url(:/icon/svg/checkmark.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"    border:1px solid #6c7c96;\n"
"    background-color:#6c7c96;\n"
"    border-radius: 4px;\n"
"    width:10px;\n"
"    height:10px;\n"
"    margin-left:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked{\n"
"    border:1px solid #fff;\n"
"    background-color:black;\n"
"}\n"
"\n"
"/* TextEdit */\n"
"QPlainTextEdit,\n"
"QTextEdit,\n"
"QLineEdit{\n"
"    background-color: #1b1e23;\n"
"    padding:8px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus,\n"
"QTextEdit:focus,\n"
"QLineEdit:fo"
                        "cus{\n"
"    border: 2px solid #568af2;\n"
"}\n"
"\n"
"QPlainTextEdit:read-only,\n"
"QTextEdit:read-only,\n"
"QLineEdit:read-only{\n"
"    border:none;\n"
"}\n"
"\n"
"/* ProgressBar */\n"
"QProgressBar{\n"
"    background-color: #1b1e23;\n"
"    text-align:center;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal{\n"
"    background-color: #4f9fee;\n"
"    border-radius: 8px;\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius:0;\n"
"}\n"
"QProgressBar::chunk:vertical{\n"
"    background-color: #4f9fee;\n"
"    border-radius: 8px;\n"
"    border-top-left-radius: 0;\n"
"    border-top-right-radius:0;\n"
"}\n"
"\n"
"\n"
"/* ScrollBar */\n"
"QScrollBar:horizontal{\n"
"    background-color: #2c313c;\n"
"    border-radius: 0;\n"
"    border:none;\n"
"    max-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"    background-color:#568af2;\n"
"    border-radius:4px;\n"
"    min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal{\n"
"    background-color:n"
                        "one;\n"
"}\n"
"QScrollBar::sub-page:horizontal{\n"
"    background-color:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"    background-color:#272c36;\n"
"    border:none;\n"
"    width:0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-posistion:right;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"    background-color:#272c36;\n"
"    border:none;\n"
"    width:0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-posistion:right;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"\n"
"/* Vertical */\n"
"QScrollBar:vertical{\n"
"    background-color: #2c313c;\n"
"    border-radius: 0;\n"
"    border:none;\n"
"    max-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color:#568af2;\n"
"    border-radius:4px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical{\n"
"    background-color:none;\n"
"}\n"
"QScrollBar::sub-page:vertical{"
                        "\n"
"    background-color:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    background-color:#272c36;\n"
"    border:none;\n"
"    width:0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-top-left-radius: 4px;\n"
"    subcontrol-posistion:right;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"    background-color:#272c36;\n"
"    border:none;\n"
"    width:0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-top-left-radius: 4px;\n"
"    subcontrol-posistion:right;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"\n"
"\n"
"/* Slider */\n"
"\n"
"QSlider:horizontal{\n"
"    margin:8;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"    background-color: #1b1e23;\n"
"    border-radius: 4px;\n"
"    margin:0px;\n"
"    height: 10px;\n"
"}\n"
"QSlider::groove:horizontal:hover{\n"
"    background-color: #21252d;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"    border:none;\n"
"    height:16px;\n"
"    width:16px;\n"
"    margin: -3px;\n"
"    border-radius: 8px;\n"
"  "
                        "  background-color: #4f9fee;\n"
"}\n"
"\n"
"QSlider:vertical{\n"
"    margin:8;\n"
"}\n"
"\n"
"QSlider::groove:vertical{\n"
"    background-color: #1b1e23;\n"
"    border-radius: 4px;\n"
"    margin:0px;\n"
"    width: 10px;\n"
"}\n"
"QSlider::groove:vertical:hover{\n"
"    background-color: #21252d;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"    border:none;\n"
"    height:16px;\n"
"    width:16px;\n"
"    margin: -3px;\n"
"    border-radius: 8px;\n"
"    background-color: #4f9fee;\n"
"}\n"
"\n"
"\n"
"/* ComboBox */\n"
"\n"
"QComboBox{\n"
"    background-color: #1b1e23;\n"
"    padding:8px;\n"
"    selection-background-color:transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    subcontrol-origin:padding;\n"
"    subcontrol-position:center right;\n"
"    background-color:#1b1e23;\n"
"    width:10px;\n"
"    padding:10px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover{\n"
"    background-color:black;\n"
"}\n"
"\n"
"QComboBox::down-a"
                        "rrow{\n"
"    image:url(:/icon_w/svg_white/circle-down.svg);\n"
"    width: 18px;\n"
"    height:18px;\n"
"}\n"
"\n"
"\n"
"/* TabWidget */\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #1b1e23;\n"
"    background-color:#1b1e23;\n"
"    border-radius: 8px;\n"
"    border-top-left-radius:0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: #1b1e23;\n"
"    border-bottom-color: #1b1e23; \n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    min-width: 8ex;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #568af2;\n"
"    color:black;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:#343b48;\n"
"	padding:5"
                        "px;\n"
"gridline-color:#2c313c;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"border-color:none;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"gridline-color:rgb(44, 49, 60);\n"
"border-bottom: 1px solid #3c4454;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"	background-color: #568af2;\n"
"}\n"
"\n"
"QTableWidget QLineEdit{\n"
"	padding:2px;\n"
"background-color:#568af2;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QTableWidget::verticalHeader{\n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    border: none;\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"    border-top-left-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section:horizo"
                        "ntal\n"
"{\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:first\n"
"{\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"border-top-left-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:last\n"
"{\n"
"\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"border-top-right-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: none;\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border-bottom: 1px solid #3c4454;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: #21252b;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(CPUMonitor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CPUMonitor)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(CPUMonitor)

        QMetaObject.connectSlotsByName(CPUMonitor)
    # setupUi

    def retranslateUi(self, CPUMonitor):
        CPUMonitor.setWindowTitle(QCoreApplication.translate("CPUMonitor", u"Form", None))
    # retranslateUi

