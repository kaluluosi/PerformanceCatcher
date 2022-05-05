# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_profiler.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)
import asset_rc

class Ui_Profiler(object):
    def setupUi(self, Profiler):
        if not Profiler.objectName():
            Profiler.setObjectName(u"Profiler")
        Profiler.resize(1113, 795)
        icon = QIcon()
        icon.addFile(u":/icon_w/svg_white/android.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon_b/svg_blue/android.svg", QSize(), QIcon.Normal, QIcon.On)
        Profiler.setWindowIcon(icon)
        Profiler.setStyleSheet(u"*{\n"
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
        self.verticalLayout = QVBoxLayout(Profiler)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Profiler)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.left = QFrame(self.frame)
        self.left.setObjectName(u"left")
        self.left.setMaximumSize(QSize(240, 16777215))
        self.left.setFrameShape(QFrame.StyledPanel)
        self.left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.left)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cbx_device = QComboBox(self.frame_2)
        self.cbx_device.setObjectName(u"cbx_device")
        self.cbx_device.setEnabled(True)
        self.cbx_device.setMinimumSize(QSize(0, 36))

        self.verticalLayout_3.addWidget(self.cbx_device)

        self.cbx_app = QComboBox(self.frame_2)
        self.cbx_app.setObjectName(u"cbx_app")
        self.cbx_app.setEnabled(True)
        self.cbx_app.setMinimumSize(QSize(0, 36))

        self.verticalLayout_3.addWidget(self.cbx_app)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_connect = QPushButton(self.frame_2)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMaximumSize(QSize(16777215, 36))
        self.btn_connect.setStyleSheet(u"\\")
        icon1 = QIcon()
        icon1.addFile(u":/icon_w/svg_white/power-cord.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/svg/power-cord.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_connect.setIcon(icon1)
        self.btn_connect.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_connect)

        self.btn_record = QToolButton(self.frame_2)
        self.btn_record.setObjectName(u"btn_record")
        self.btn_record.setMaximumSize(QSize(36, 36))
        icon2 = QIcon()
        icon2.addFile(u":/icon_w/svg_white/play2.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon_b/svg_blue/stop.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_record.setIcon(icon2)
        self.btn_record.setIconSize(QSize(24, 24))
        self.btn_record.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_record)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tab_main = QTabWidget(self.frame_2)
        self.tab_main.setObjectName(u"tab_main")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        icon3 = QIcon()
        icon3.addFile(u":/icon_w/svg_white/mobile2.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon_b/svg_blue/mobile2.svg", QSize(), QIcon.Normal, QIcon.On)
        self.tab_main.addTab(self.tab, icon3, "")

        self.verticalLayout_3.addWidget(self.tab_main)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left)

        self.right = QFrame(self.frame)
        self.right.setObjectName(u"right")
        self.right.setFrameShape(QFrame.StyledPanel)
        self.right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.right)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 841, 978))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents{\n"
"margin-right:5px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 240))

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 240))

        self.verticalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 240))

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 240))

        self.verticalLayout_6.addWidget(self.pushButton_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.right)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 240))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_console = QTabWidget(self.frame_3)
        self.tab_console.setObjectName(u"tab_console")
        self.tab_console.setElideMode(Qt.ElideLeft)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        icon4 = QIcon()
        icon4.addFile(u":/icon_w/svg_white/notification.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icon_b/svg_blue/notification.svg", QSize(), QIcon.Normal, QIcon.On)
        self.tab_console.addTab(self.tab_3, icon4, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        icon5 = QIcon()
        icon5.addFile(u":/icon_w/svg_white/terminal.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icon_b/svg_blue/terminal.svg", QSize(), QIcon.Normal, QIcon.On)
        icon5.addFile(u":/icon_w/svg_white/terminal.svg", QSize(), QIcon.Disabled, QIcon.Off)
        self.tab_console.addTab(self.tab_4, icon5, "")

        self.gridLayout.addWidget(self.tab_console, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.right)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Profiler)

        self.tab_main.setCurrentIndex(0)
        self.tab_console.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Profiler)
    # setupUi

    def retranslateUi(self, Profiler):
        Profiler.setWindowTitle(QCoreApplication.translate("Profiler", u"\u5b89\u5353\u6027\u80fd", None))
#if QT_CONFIG(tooltip)
        Profiler.setToolTip(QCoreApplication.translate("Profiler", u"\u5b89\u5353\u6027\u80fd\u6d4b\u8bd5\u8f85\u52a9\u5de5\u5177", None))
#endif // QT_CONFIG(tooltip)
        self.btn_connect.setText(QCoreApplication.translate("Profiler", u"\u8fde\u63a5", None))
        self.btn_record.setText(QCoreApplication.translate("Profiler", u"...", None))
        self.btn_record.setProperty("style", QCoreApplication.translate("Profiler", u"danger", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab), QCoreApplication.translate("Profiler", u"\u8bbe\u5907", None))
        self.pushButton_2.setText(QCoreApplication.translate("Profiler", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Profiler", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Profiler", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Profiler", u"PushButton", None))
#if QT_CONFIG(tooltip)
        self.tab_console.setToolTip(QCoreApplication.translate("Profiler", u"\u53cc\u51fb\u6807\u7b7e\u9690\u85cf", None))
#endif // QT_CONFIG(tooltip)
        self.tab_console.setTabText(self.tab_console.indexOf(self.tab_3), QCoreApplication.translate("Profiler", u"LogCat", None))
        self.tab_console.setTabText(self.tab_console.indexOf(self.tab_4), QCoreApplication.translate("Profiler", u"Cmd", None))
    # retranslateUi

