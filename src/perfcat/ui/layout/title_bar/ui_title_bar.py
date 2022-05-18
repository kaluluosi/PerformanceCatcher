# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_title_bar.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
import asset_rc
import asset_rc


class Ui_TitleBar(object):
    def setupUi(self, TitleBar):
        if not TitleBar.objectName():
            TitleBar.setObjectName("TitleBar")
        TitleBar.resize(722, 40)
        TitleBar.setMinimumSize(QSize(0, 40))
        TitleBar.setMaximumSize(QSize(16777215, 40))
        TitleBar.setStyleSheet(
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
            "}"
        )
        self.verticalLayout = QVBoxLayout(TitleBar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(TitleBar)
        self.bg.setObjectName("bg")
        self.bg.setMinimumSize(QSize(0, 40))
        self.bg.setMaximumSize(QSize(16777215, 40))
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.logo = QFrame(self.bg)
        self.logo.setObjectName("logo")
        self.logo.setMaximumSize(QSize(130, 16777215))
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.logo)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo_icon = QLabel(self.logo)
        self.logo_icon.setObjectName("logo_icon")
        self.logo_icon.setPixmap(QPixmap(":/icon_b/assets/svg_blue/xing.svg"))

        self.horizontalLayout_2.addWidget(self.logo_icon)

        self.logo_title = QLabel(self.logo)
        self.logo_title.setObjectName("logo_title")

        self.horizontalLayout_2.addWidget(self.logo_title)

        self.horizontalLayout.addWidget(self.logo)

        self.lb_title = QLabel(self.bg)
        self.lb_title.setObjectName("lb_title")

        self.horizontalLayout.addWidget(self.lb_title)

        self.tool = QFrame(self.bg)
        self.tool.setObjectName("tool")
        self.tool.setMaximumSize(QSize(80, 16777215))
        self.tool.setFrameShape(QFrame.StyledPanel)
        self.tool.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.tool)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_search = QToolButton(self.tool)
        self.btn_search.setObjectName("btn_search")
        icon = QIcon()
        icon.addFile(
            ":/icon_w/assets/svg_white/search.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        icon.addFile(
            ":/icon_b/assets/svg_blue/search.svg", QSize(), QIcon.Normal, QIcon.On
        )
        self.btn_search.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btn_search)

        self.btn_setting = QToolButton(self.tool)
        self.btn_setting.setObjectName("btn_setting")
        icon1 = QIcon()
        icon1.addFile(
            ":/icon_w/assets/svg_white/cog.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        icon1.addFile(
            ":/icon_b/assets/svg_blue/cog.svg", QSize(), QIcon.Normal, QIcon.On
        )
        self.btn_setting.setIcon(icon1)
        self.btn_setting.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btn_setting)

        self.horizontalLayout.addWidget(self.tool)

        self.control_btn = QFrame(self.bg)
        self.control_btn.setObjectName("control_btn")
        self.control_btn.setMaximumSize(QSize(94, 16777215))
        self.control_btn.setFrameShape(QFrame.StyledPanel)
        self.control_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.control_btn)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_min = QToolButton(self.control_btn)
        self.btn_min.setObjectName("btn_min")
        self.btn_min.setLayoutDirection(Qt.LeftToRight)
        self.btn_min.setStyleSheet("")
        icon2 = QIcon()
        icon2.addFile(
            ":/icon_w/assets/svg_white/minus.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        icon2.addFile(
            ":/icon_b/assets/svg_blue/minus.svg", QSize(), QIcon.Normal, QIcon.On
        )
        self.btn_min.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.btn_min)

        self.btn_max = QToolButton(self.control_btn)
        self.btn_max.setObjectName("btn_max")
        self.btn_max.setLayoutDirection(Qt.LeftToRight)
        self.btn_max.setStyleSheet("")
        icon3 = QIcon()
        icon3.addFile(
            ":/icon_w/assets/svg_white/checkbox-unchecked.svg",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        icon3.addFile(
            ":/icon_b/assets/svg_blue/checkbox-unchecked.svg",
            QSize(),
            QIcon.Normal,
            QIcon.On,
        )
        self.btn_max.setIcon(icon3)
        self.btn_max.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btn_max)

        self.btn_close = QToolButton(self.control_btn)
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setLayoutDirection(Qt.LeftToRight)
        self.btn_close.setStyleSheet("")
        icon4 = QIcon()
        icon4.addFile(
            ":/icon_w/assets/svg_white/cross.svg", QSize(), QIcon.Normal, QIcon.On
        )
        icon4.addFile(
            ":/icon_b/assets/svg_blue/cross.svg", QSize(), QIcon.Disabled, QIcon.Off
        )
        self.btn_close.setIcon(icon4)
        self.btn_close.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_4.addWidget(self.btn_close)

        self.horizontalLayout.addWidget(self.control_btn)

        self.verticalLayout.addWidget(self.bg)

        self.retranslateUi(TitleBar)

        QMetaObject.connectSlotsByName(TitleBar)

    # setupUi

    def retranslateUi(self, TitleBar):
        TitleBar.setWindowTitle(QCoreApplication.translate("TitleBar", "Form", None))
        self.logo_icon.setText("")
        self.logo_title.setText(QCoreApplication.translate("TitleBar", "Perfcat", None))
        self.lb_title.setText(
            QCoreApplication.translate(
                "TitleBar", "\u5c0f\u82f1\u96c4-xxx-\u6027\u80fd\u6d4b\u8bd5", None
            )
        )
        self.btn_search.setText("")
        self.btn_setting.setText("")
        self.btn_min.setText(QCoreApplication.translate("TitleBar", "...", None))
        self.btn_max.setText(QCoreApplication.translate("TitleBar", "...", None))
        self.btn_close.setText(QCoreApplication.translate("TitleBar", "...", None))

    # retranslateUi
