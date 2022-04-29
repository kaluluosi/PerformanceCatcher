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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import asset_rc

class Ui_Profiler(object):
    def setupUi(self, Profiler):
        if not Profiler.objectName():
            Profiler.setObjectName(u"Profiler")
        Profiler.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/icon_w/svg_white/address-book.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon_b/svg_blue/address-book.svg", QSize(), QIcon.Normal, QIcon.On)
        Profiler.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Profiler)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Profiler)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 30, 151, 41))

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Profiler)

        QMetaObject.connectSlotsByName(Profiler)
    # setupUi

    def retranslateUi(self, Profiler):
        Profiler.setWindowTitle(QCoreApplication.translate("Profiler", u"\u6027\u80fd", None))
        self.pushButton.setText(QCoreApplication.translate("Profiler", u"profiler", None))
    # retranslateUi

