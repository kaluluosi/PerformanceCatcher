# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widgets.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLineEdit, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QScrollBar,
    QSizePolicy, QSlider, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)
import asset_rc

class Ui_Widgets(object):
    def setupUi(self, Widgets):
        if not Widgets.objectName():
            Widgets.setObjectName(u"Widgets")
        Widgets.resize(1253, 742)
        icon = QIcon()
        icon.addFile(u":/icon_w/svg_white/stack.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon_b/svg_blue/stack.svg", QSize(), QIcon.Normal, QIcon.On)
        Widgets.setWindowIcon(icon)
        Widgets.setStyleSheet(u"*{\n"
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
"")
        self.verticalLayout = QVBoxLayout(Widgets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 645, 191, 51))
        self.gridLayout_2 = QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_reload = QPushButton(self.horizontalLayoutWidget)
        self.btn_reload.setObjectName(u"btn_reload")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_reload.sizePolicy().hasHeightForWidth())
        self.btn_reload.setSizePolicy(sizePolicy)
        self.btn_reload.setMinimumSize(QSize(40, 0))

        self.gridLayout_2.addWidget(self.btn_reload, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(230, 10, 220, 291))
        self.groupBox_2.setMinimumSize(QSize(220, 0))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolButton_4 = QToolButton(self.groupBox_2)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icon_w/svg_white/IcoMoon.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/svg/IcoMoon.svg", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setCheckable(True)
        self.toolButton_4.setChecked(True)

        self.gridLayout.addWidget(self.toolButton_4, 0, 1, 1, 1)

        self.toolButton = QToolButton(self.groupBox_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(40, 40))
        self.toolButton.setIcon(icon1)

        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)

        self.toolButton_3 = QToolButton(self.groupBox_2)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(40, 40))
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setChecked(True)

        self.gridLayout.addWidget(self.toolButton_3, 1, 1, 1, 1)

        self.toolButton_2 = QToolButton(self.groupBox_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(40, 40))
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setChecked(True)

        self.gridLayout.addWidget(self.toolButton_2, 2, 0, 1, 1)

        self.toolButton_6 = QToolButton(self.groupBox_2)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setMinimumSize(QSize(40, 40))
        self.toolButton_6.setIcon(icon1)
        self.toolButton_6.setCheckable(True)

        self.gridLayout.addWidget(self.toolButton_6, 1, 0, 1, 1)

        self.toolButton_5 = QToolButton(self.groupBox_2)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icon_w/svg_white/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/svg/heart.svg", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_5.setIcon(icon2)
        self.toolButton_5.setCheckable(True)
        self.toolButton_5.setChecked(True)

        self.gridLayout.addWidget(self.toolButton_5, 2, 1, 1, 1)

        self.toolButton_7 = QToolButton(self.groupBox_2)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setEnabled(False)
        self.toolButton_7.setMinimumSize(QSize(40, 40))
        self.toolButton_7.setIcon(icon1)

        self.gridLayout.addWidget(self.toolButton_7, 3, 0, 1, 1)

        self.toolButton_8 = QToolButton(self.groupBox_2)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setMinimumSize(QSize(40, 40))
        self.toolButton_8.setIcon(icon1)
        self.toolButton_8.setCheckable(True)
        self.toolButton_8.setChecked(True)

        self.gridLayout.addWidget(self.toolButton_8, 3, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(470, 10, 471, 291))
        self.groupBox_3.setMinimumSize(QSize(220, 0))
        self.horizontalScrollBar = QScrollBar(self.groupBox_3)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(30, 30, 181, 8))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.verticalScrollBar = QScrollBar(self.groupBox_3)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(110, 70, 8, 181))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.horizontalSlider = QSlider(self.groupBox_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(260, 30, 160, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.verticalSlider = QSlider(self.groupBox_3)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(330, 70, 22, 160))
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 310, 220, 128))
        self.groupBox_4.setMinimumSize(QSize(220, 0))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.checkBox)

        self.radioButton = QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.radioButton)

        self.groupBox_5 = QGroupBox(self.frame)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(230, 310, 491, 321))
        self.lineEdit = QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 30, 141, 40))
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.textEdit = QTextEdit(self.groupBox_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 100, 104, 71))
        self.plainTextEdit = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(40, 200, 104, 71))
        self.lineEdit_2 = QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 30, 141, 40))
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.textEdit_2 = QTextEdit(self.groupBox_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(180, 100, 104, 71))
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(180, 200, 104, 71))
        self.lineEdit_3 = QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(320, 30, 141, 40))
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setReadOnly(True)
        self.textEdit_3 = QTextEdit(self.groupBox_5)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(330, 100, 104, 71))
        self.textEdit_3.setReadOnly(True)
        self.plainTextEdit_3 = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(330, 200, 104, 71))
        self.plainTextEdit_3.setReadOnly(True)
        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(720, 310, 171, 321))
        self.progressBar_2 = QProgressBar(self.groupBox_6)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(70, 120, 21, 151))
        self.progressBar_2.setValue(50)
        self.progressBar_2.setOrientation(Qt.Vertical)
        self.progressBar = QProgressBar(self.groupBox_6)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 50, 118, 23))
        self.progressBar.setValue(50)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(11, 11, 220, 291))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/icon_w/svg_white/IE.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/svg/IE.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(True)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_5.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(920, 330, 131, 36))
        self.comboBox.setMinimumSize(QSize(0, 36))
        self.comboBox.setEditable(False)
        self.comboBox.setModelColumn(0)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Widgets)

        QMetaObject.connectSlotsByName(Widgets)
    # setupUi

    def retranslateUi(self, Widgets):
        Widgets.setWindowTitle(QCoreApplication.translate("Widgets", u"\u63a7\u4ef6\u53c2\u8003", None))
        self.btn_reload.setText(QCoreApplication.translate("Widgets", u"\u5237\u65b0\u6837\u5f0f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widgets", u"ToolButton", None))
        self.toolButton_4.setText(QCoreApplication.translate("Widgets", u"...", None))
        self.toolButton_4.setProperty("style", QCoreApplication.translate("Widgets", u"success", None))
        self.toolButton.setText(QCoreApplication.translate("Widgets", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("Widgets", u"...", None))
        self.toolButton_3.setProperty("style", QCoreApplication.translate("Widgets", u"warning", None))
        self.toolButton_2.setText(QCoreApplication.translate("Widgets", u"...", None))
        self.toolButton_6.setText(QCoreApplication.translate("Widgets", u"...", None))
        self.toolButton_5.setText(QCoreApplication.translate("Widgets", u"...", None))
        self.toolButton_5.setProperty("style", QCoreApplication.translate("Widgets", u"danger", None))
        self.toolButton_7.setText(QCoreApplication.translate("Widgets", u"...", None))
        self.toolButton_8.setText(QCoreApplication.translate("Widgets", u"...", None))
        self.toolButton_8.setProperty("style", QCoreApplication.translate("Widgets", u"info", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widgets", u"Bar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widgets", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("Widgets", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("Widgets", u"RadioButton", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Widgets", u"TextEdit", None))
        self.lineEdit.setText(QCoreApplication.translate("Widgets", u"hello world", None))
        self.textEdit.setHtml(QCoreApplication.translate("Widgets", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hello<span style=\" font-size:14pt;\"> world</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Widgets", u"hello world", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Widgets", u"place holder", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("Widgets", u"place holder", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("Widgets", u"placeholder", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Widgets", u"hello world", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("Widgets", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hello<span style=\" font-size:14pt;\"> world</span></p></body></html>", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("Widgets", u"hello world", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Widgets", u"ProgressBar", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widgets", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widgets", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Widgets", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widgets", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widgets", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widgets", u"PushButton", None))
        self.comboBox.setCurrentText("")
    # retranslateUi

