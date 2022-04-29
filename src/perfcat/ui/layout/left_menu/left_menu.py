#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   left_menu.py
@Time    :   2022/04/27 14:39:00
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   侧边导航栏组件
"""

# here put the import lib


import textwrap
from PySide6.QtWidgets import (
    QWidget,
    QGraphicsDropShadowEffect,
    QButtonGroup,
    QVBoxLayout,
    QPushButton,
)
from PySide6.QtCore import Slot, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QPixmap
from .ui_left_menu import Ui_LeftMenu
from .. import util


class LeftMenu(QWidget, Ui_LeftMenu):

    # 展开最大宽度，收起最小宽度，目前只能写死了
    MAX_WIDTH = 240
    MIN_WIDTH = 50

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("")  # 清空qt designer里写死的样式

        # 菜单展开和收起功能
        self.btn_toggle.setChecked(True)
        self.btn_toggle.toggled.connect(self.expand)

        # 清空掉nav_menu设计时按钮
        util.clear_layout(self.nav_menu)
        self.btn_home.deleteLater()
        self.nav_menu_group = QButtonGroup(self)

        # 把关于和设置按钮放到按钮组里
        self.bottom_btn_group = QButtonGroup(self)
        self.bottom_btn_group.addButton(self.btn_setting, 0)
        self.bottom_btn_group.addButton(self.btn_about, 1)

    def add_nav_menu(self, icon, text, binding_page_name):
        text = textwrap.indent(text, " " * 4)  # 缩进4格用来适配按钮样式
        btn_menu = QPushButton(icon, text, self)
        btn_menu.setCheckable(True)
        btn_menu.setObjectName(binding_page_name)
        self.nav_menu.layout().addWidget(btn_menu)
        self.nav_menu_group.addButton(btn_menu)
        if self.nav_menu.layout().count() == 1:
            btn_menu.setChecked(True)

    def bottom_btn_group_reset(self):
        self.bottom_btn_group.setExclusive(False)
        for btn in self.bottom_btn_group.buttons():
            btn.setChecked(False)
        self.bottom_btn_group.setExclusive(True)

    def expand(self, checked):
        util.set_h_expand_anim(
            self.parentWidget(), checked, self.MAX_WIDTH, self.MIN_WIDTH
        )
