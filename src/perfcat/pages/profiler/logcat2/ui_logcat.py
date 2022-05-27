# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_logcat.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import asset_rc

class Ui_Logcat(object):
    def setupUi(self, Logcat):
        if not Logcat.objectName():
            Logcat.setObjectName(u"Logcat")
        Logcat.resize(652, 455)
        Logcat.setStyleSheet(u"*{\n"
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
"QLineEdit:"
                        "focus{\n"
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
"    background-color"
                        ":none;\n"
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
"    /* subcontrol-position:right; */\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"    background-color:#272c36;\n"
"    border:none;\n"
"    width:0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    /* subcontrol-position:right; */\n"
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
"QScrollBar::sub-pa"
                        "ge:vertical{\n"
"    background-color:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    background-color:#272c36;\n"
"    border:none;\n"
"    width:0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-top-left-radius: 4px;\n"
"    /* subcontrol-position:right; */\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"    background-color:#272c36;\n"
"    border:none;\n"
"    width:0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-top-left-radius: 4px;\n"
"    /* subcontrol-position:right; */\n"
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
"    bord"
                        "er-radius: 8px;\n"
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
"QComboBox:disabled{\n"
"    background-color: #272c36;\n"
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
""
                        "QComboBox::drop-down:disabled{\n"
"    background-color: #272c36;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover{\n"
"    background-color:black;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
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
"    /* background: #1b1e23;\n"
"    border-bottom-color: #1b1e23;  */\n"
"    background:#2c313c;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    min-width: 8ex;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    backgroun"
                        "d: #1b1e23;\n"
"    /* color:black; */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"\n"
"QScrollArea{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollArea #scrollAreaWidgetContents *{\n"
"    margin-right:5px;\n"
"}\n"
"\n"
"\n"
"\n"
"#Notification QToolButton{\n"
"    padding-left:20px;\n"
"    padding-right:20px;\n"
"    color:black;\n"
"}\n"
"\n"
"QSplitter::handle{\n"
"    background-color: #2c313c;\n"
"    margin-top:5px;\n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"\n"
"QTableWidget, QTableView{\n"
"	background-color:#343b48;\n"
"	/* padding:5px; */\n"
"gridline-color:#2c313c;\n"
"}\n"
"\n"
"QTableWidget::item,\n"
"QTableView::item{\n"
"border-color:none;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"gridline-color:rgb(44, 49, 60);\n"
"border-bottom: 1px solid #3c4454;\n"
"}\n"
"\n"
"QTableWidget::item:selected,\n"
"QTableView::item:selected{\n"
"	background-color: #568af2;\n"
"}\n"
"\n"
"QHeaderView::section{"
                        "\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader,\n"
"QTableView::horizontalHeader {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section,\n"
"QTableView QTableCornerButton::section\n"
" {\n"
"    border: none;\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"    border-top-left-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: none;\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
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
"\n"
"\n"
"QHeaderView {\n"
"    background-color: #21252b;\n"
"}\n"
"\n"
"QHeaderView::section:"
                        "horizontal:first\n"
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
"QTableWidget QLineEdit,\n"
"QTableView QLineEdit{\n"
"	padding:2px;\n"
"background-color:#568af2;\n"
"color:black;\n"
"}\n"
"\n"
"\n"
"/* profiler */\n"
"\n"
"Monitor QFrame {\n"
"background-color: #1b1e23;\n"
"}\n"
"\n"
"\n"
"Logcat #container {\n"
"    background-color: #343b48;\n"
"}\n"
"")
        self.action_copy = QAction(Logcat)
        self.action_copy.setObjectName(u"action_copy")
        self.verticalLayout_3 = QVBoxLayout(Logcat)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.container = QFrame(Logcat)
        self.container.setObjectName(u"container")
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_search = QLineEdit(self.container)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout.addWidget(self.le_search)

        self.le_tag = QLineEdit(self.container)
        self.le_tag.setObjectName(u"le_tag")
        self.le_tag.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout.addWidget(self.le_tag)

        self.btn_start = QPushButton(self.container)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMaximumSize(QSize(36, 36))
        icon = QIcon()
        icon.addFile(u":/icon_w/assets/svg_white/play2.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon/assets/svg/play2.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_start.setIcon(icon)
        self.btn_start.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_start)

        self.btn_save = QPushButton(self.container)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMaximumSize(QSize(36, 36))
        icon1 = QIcon()
        icon1.addFile(u":/icon_w/assets/svg_white/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/assets/svg/save.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_save.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_clear = QPushButton(self.container)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMaximumSize(QSize(36, 36))
        icon2 = QIcon()
        icon2.addFile(u":/icon_w/assets/svg_white/bin.svg", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u":/icon/assets/svg/bin.svg", QSize(), QIcon.Disabled, QIcon.Off)
        self.btn_clear.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_clear)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tbv_logs = QTableView(self.container)
        self.tbv_logs.setObjectName(u"tbv_logs")
        self.tbv_logs.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tbv_logs.setDefaultDropAction(Qt.IgnoreAction)
        self.tbv_logs.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tbv_logs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbv_logs.setCornerButtonEnabled(False)
        self.tbv_logs.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbv_logs.horizontalHeader().setStretchLastSection(True)
        self.tbv_logs.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tbv_logs)


        self.verticalLayout_3.addWidget(self.container)


        self.retranslateUi(Logcat)

        QMetaObject.connectSlotsByName(Logcat)
    # setupUi

    def retranslateUi(self, Logcat):
        Logcat.setWindowTitle(QCoreApplication.translate("Logcat", u"Form", None))
        self.action_copy.setText(QCoreApplication.translate("Logcat", u"\u590d\u5236", None))
        self.btn_start.setText("")
        self.btn_save.setText("")
        self.btn_clear.setText("")
    # retranslateUi

