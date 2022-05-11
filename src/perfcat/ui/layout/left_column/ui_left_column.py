# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_left_column.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QStackedWidget, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)
import asset_rc

class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 549)
        LeftColumn.setMaximumSize(QSize(240, 16777215))
        LeftColumn.setStyleSheet(u"* {\n"
"    border-radius:8;\n"
"    color:#6c7c96;\n"
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
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(LeftColumn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top = QFrame(LeftColumn)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 32))
        self.top.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.icon = QToolButton(self.top)
        self.icon.setObjectName(u"icon")
        self.icon.setEnabled(True)
        self.icon.setMinimumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/icon_w/svg_white/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon1)
        self.icon.setAutoRaise(False)

        self.horizontalLayout.addWidget(self.icon)

        self.title = QLabel(self.top)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title)

        self.btn_close = QToolButton(self.top)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 32))
        self.btn_close.setMaximumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/icon_w/svg_white/cross.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon_b/svg_blue/cross.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.top)

        self.stacked = QStackedWidget(LeftColumn)
        self.stacked.setObjectName(u"stacked")
        self.stacked.setMinimumSize(QSize(220, 0))
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_2 = QVBoxLayout(self.page_setting)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stacked.addWidget(self.page_setting)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.verticalLayout_3 = QVBoxLayout(self.page_about)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.te_about = QTextBrowser(self.page_about)
        self.te_about.setObjectName(u"te_about")
        self.te_about.setStyleSheet(u"QTextEdit{\n"
"    background-color:#3c4454;\n"
"	padding:8px;\n"
"}\n"
"")
        self.te_about.setReadOnly(True)
        self.te_about.setAcceptRichText(True)

        self.verticalLayout_3.addWidget(self.te_about)

        self.stacked.addWidget(self.page_about)

        self.verticalLayout.addWidget(self.stacked)


        self.retranslateUi(LeftColumn)

        self.stacked.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"\u4fa7\u8fb9\u680f", None))
        self.icon.setText(QCoreApplication.translate("LeftColumn", u"PushButton", None))
        self.title.setText(QCoreApplication.translate("LeftColumn", u"\u8bbe\u7f6e", None))
        self.btn_close.setText("")
        self.te_about.setMarkdown(QCoreApplication.translate("LeftColumn", u"**Perfcat**\n"
"\n"
"v 1.0.1\n"
"\n"
"", None))
        self.te_about.setHtml(QCoreApplication.translate("LeftColumn", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Perfcat</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">v 1.0.1</span></p></body></html>", None))
    # retranslateUi

