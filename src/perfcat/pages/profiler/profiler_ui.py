# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profiler.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
    QHBoxLayout, QHeaderView, QPushButton, QScrollArea,
    QScrollBar, QSizePolicy, QSplitter, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
import asset_rc

class Ui_Profiler(object):
    def setupUi(self, Profiler):
        if not Profiler.objectName():
            Profiler.setObjectName(u"Profiler")
        Profiler.resize(1113, 795)
        icon = QIcon()
        icon.addFile(u":/icon_w/assets/svg_white/android.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon_b/assets/svg_blue/android.svg", QSize(), QIcon.Normal, QIcon.On)
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
"    image: url(:/icon/assets/svg/checkmark.svg);\n"
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
"QLine"
                        "Edit:focus{\n"
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
"    background-"
                        "color:none;\n"
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
"QScrollBar::sub-page:ve"
                        "rtical{\n"
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
"    border-radius: 8px;"
                        "\n"
"    background-color: #4f9fee;\n"
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
"QComboBox:"
                        ":down-arrow{\n"
"    image:url(:/icon_w/assets/svg_white/circle-down.svg);\n"
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
""
                        "	padding:5px;\n"
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
"QHeaderView::sect"
                        "ion:horizontal\n"
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
        self.cbx_app.setEditable(True)

        self.verticalLayout_3.addWidget(self.cbx_app)

        self.cbx_subprocess = QComboBox(self.frame_2)
        self.cbx_subprocess.setObjectName(u"cbx_subprocess")

        self.verticalLayout_3.addWidget(self.cbx_subprocess)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_connect = QPushButton(self.frame_2)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMaximumSize(QSize(16777215, 36))
        self.btn_connect.setStyleSheet(u"\\")
        icon1 = QIcon()
        icon1.addFile(u":/icon_w/assets/svg_white/power-cord.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/assets/svg/power-cord.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_connect.setIcon(icon1)
        self.btn_connect.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_connect)

        self.btn_open = QToolButton(self.frame_2)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMaximumSize(QSize(36, 36))
        icon2 = QIcon()
        icon2.addFile(u":/icon_w/assets/svg_white/folder-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon_b/assets/svg_blue/folder-open.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_open.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_open)

        self.btn_save = QToolButton(self.frame_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(False)
        self.btn_save.setMaximumSize(QSize(36, 36))
        icon3 = QIcon()
        icon3.addFile(u":/icon_w/assets/svg_white/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon_b/assets/svg_blue/save.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_save.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_record = QToolButton(self.frame_2)
        self.btn_record.setObjectName(u"btn_record")
        self.btn_record.setMaximumSize(QSize(36, 36))
        icon4 = QIcon()
        icon4.addFile(u":/icon_w/assets/svg_white/play2.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icon/assets/svg/pause.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_record.setIcon(icon4)
        self.btn_record.setIconSize(QSize(24, 24))
        self.btn_record.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_record)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tab_main = QTabWidget(self.frame_2)
        self.tab_main.setObjectName(u"tab_main")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.tb_device_info = QTableWidget(self.tab)
        if (self.tb_device_info.columnCount() < 2):
            self.tb_device_info.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_device_info.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_device_info.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tb_device_info.setObjectName(u"tb_device_info")
        self.tb_device_info.setEnabled(True)
        self.tb_device_info.setWordWrap(False)
        self.tb_device_info.setCornerButtonEnabled(True)
        self.tb_device_info.setColumnCount(2)
        self.tb_device_info.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_device_info.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_device_info.horizontalHeader().setStretchLastSection(True)
        self.tb_device_info.verticalHeader().setVisible(False)

        self.verticalLayout_7.addWidget(self.tb_device_info)

        self.btn_copy_info = QPushButton(self.tab)
        self.btn_copy_info.setObjectName(u"btn_copy_info")
        self.btn_copy_info.setEnabled(False)

        self.verticalLayout_7.addWidget(self.btn_copy_info)

        icon5 = QIcon()
        icon5.addFile(u":/icon_w/assets/svg_white/mobile2.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icon_b/assets/svg_blue/mobile2.svg", QSize(), QIcon.Normal, QIcon.On)
        self.tab_main.addTab(self.tab, icon5, "")

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
        self.splitter = QSplitter(self.right)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(1)
        self.frame_4 = QFrame(self.splitter)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.monitor_scollarea = QScrollArea(self.frame_4)
        self.monitor_scollarea.setObjectName(u"monitor_scollarea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(100)
        sizePolicy2.setHeightForWidth(self.monitor_scollarea.sizePolicy().hasHeightForWidth())
        self.monitor_scollarea.setSizePolicy(sizePolicy2)
        self.monitor_scollarea.setLayoutDirection(Qt.LeftToRight)
        self.monitor_scollarea.setStyleSheet(u"")
        self.monitor_scollarea.setWidgetResizable(True)
        self.monitor_scollarea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 849, 448))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents{\n"
"margin-right:5px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.monitor_scollarea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.monitor_scollarea)

        self.horizontalScrollBar = QScrollBar(self.frame_4)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalScrollBar)

        self.splitter.addWidget(self.frame_4)
        self.frame_3 = QFrame(self.splitter)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 400))
        self.frame_3.setSizeIncrement(QSize(0, 0))
        self.frame_3.setBaseSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_console = QTabWidget(self.frame_3)
        self.tab_console.setObjectName(u"tab_console")
        self.tab_console.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tab_console.sizePolicy().hasHeightForWidth())
        self.tab_console.setSizePolicy(sizePolicy4)
        self.tab_console.setMaximumSize(QSize(16777215, 16777215))
        self.tab_console.setElideMode(Qt.ElideLeft)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy5)
        self.verticalLayout_8 = QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        icon6 = QIcon()
        icon6.addFile(u":/icon_w/assets/svg_white/notification.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icon_b/assets/svg_blue/notification.svg", QSize(), QIcon.Normal, QIcon.On)
        self.tab_console.addTab(self.tab_3, icon6, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        icon7 = QIcon()
        icon7.addFile(u":/icon_w/assets/svg_white/terminal.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icon_b/assets/svg_blue/terminal.svg", QSize(), QIcon.Normal, QIcon.On)
        icon7.addFile(u":/icon_w/assets/svg_white/terminal.svg", QSize(), QIcon.Disabled, QIcon.Off)
        self.tab_console.addTab(self.tab_4, icon7, "")

        self.gridLayout.addWidget(self.tab_console, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame_3)

        self.verticalLayout_4.addWidget(self.splitter)


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
        Profiler.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cbx_device.setPlaceholderText(QCoreApplication.translate("Profiler", u"\u8bf7\u9009\u62e9\u8bbe\u5907", None))
        self.cbx_app.setPlaceholderText(QCoreApplication.translate("Profiler", u"\u9009\u62e9APP", None))
        self.btn_connect.setText(QCoreApplication.translate("Profiler", u"\u8fde\u63a5", None))
#if QT_CONFIG(tooltip)
        self.btn_open.setToolTip(QCoreApplication.translate("Profiler", u"<html><head/><body><p>\u8bfb\u53d6\u8bb0\u5f55</p><p>\u53ea\u6709\u65ad\u5f00\u8fde\u63a5\u7684\u60c5\u51b5\u4e0b\u624d\u53ef\u4ee5\u8bfb\u53d6\u8bb0\u5f55</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_open.setText(QCoreApplication.translate("Profiler", u"...", None))
#if QT_CONFIG(tooltip)
        self.btn_save.setToolTip(QCoreApplication.translate("Profiler", u"\u4fdd\u5b58\u8bb0\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save.setText(QCoreApplication.translate("Profiler", u"...", None))
        self.btn_record.setText(QCoreApplication.translate("Profiler", u"...", None))
        self.btn_record.setProperty("style", QCoreApplication.translate("Profiler", u"danger", None))
        ___qtablewidgetitem = self.tb_device_info.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Profiler", u"\u5c5e\u6027", None));
        ___qtablewidgetitem1 = self.tb_device_info.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Profiler", u"\u503c", None));
        self.btn_copy_info.setText(QCoreApplication.translate("Profiler", u"\u590d\u5236\u4fe1\u606f", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab), QCoreApplication.translate("Profiler", u"\u8bbe\u5907", None))
#if QT_CONFIG(tooltip)
        self.tab_console.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tab_console.setTabText(self.tab_console.indexOf(self.tab_3), QCoreApplication.translate("Profiler", u"LogCat", None))
        self.tab_console.setTabText(self.tab_console.indexOf(self.tab_4), QCoreApplication.translate("Profiler", u"Cmd", None))
    # retranslateUi

