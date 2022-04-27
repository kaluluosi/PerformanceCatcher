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


from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QButtonGroup
from PySide6.QtCore import Slot, QPropertyAnimation, QEasingCurve
from .ui_left_menu import Ui_LeftMenu
from .. import effects


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

        self.bottom_btn_group = QButtonGroup(self)
        self.bottom_btn_group.addButton(self.btn_setting)
        self.bottom_btn_group.addButton(self.btn_about)

    def bottom_btn_group_reset(self):
        self.bottom_btn_group.setExclusive(False)
        for btn in self.bottom_btn_group.buttons():
            btn.setChecked(False)
        self.bottom_btn_group.setExclusive(True)

    def expand(self, checked):
        effects.set_h_expand_anim(self, checked, self.MAX_WIDTH, self.MIN_WIDTH)

    def add_bottom_entry(self):
        pass
