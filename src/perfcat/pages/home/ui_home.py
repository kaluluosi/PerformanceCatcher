# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
import asset_rc

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(500, 336)
        icon = QIcon()
        icon.addFile(u":/icon_w/assets/svg_white/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon_b/assets/svg_blue/home.svg", QSize(), QIcon.Normal, QIcon.On)
        Home.setWindowIcon(icon)
        Home.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Home)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"background-image: url(:/images/assets/images/logo_sws_10.png);\n"
"background-repeat: no;\n"
"background-position:center;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"\u9996\u9875", None))
    # retranslateUi

