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
from .. import utils


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

        # 删除掉设计时的首页按钮
        self.menu_group = QButtonGroup(self)
        self.menu.layout().removeWidget(self.btn_home)

        # 把关于和设置按钮放到按钮组里
        self.bottom_btn_group = QButtonGroup(self)
        self.bottom_btn_group.addButton(self.btn_about, 1)
        self.bottom_btn_group.addButton(self.btn_setting, 0)

    def add_menu(self, icon_name: str, name: str):
        normal_icon = f":/icon_w/svg_white/{icon_name}.svg"
        checked_icon = f":/icon_b/svg_blue/{icon_name}.svg"
        title = f"    {name}"

        icon = QIcon()
        icon.addPixmap(QPixmap(normal_icon), QIcon.Mode.Normal)
        icon.addPixmap(QPixmap(checked_icon), QIcon.Mode.Active)

        button = QPushButton(icon, title, self)
        button.setCheckable(True)
        self.menu_group.addButton(button)
        self.menu.layout().addWidget(button)
        return button

    def bottom_btn_group_reset(self):
        self.bottom_btn_group.setExclusive(False)
        for btn in self.bottom_btn_group.buttons():
            btn.setChecked(False)
        self.bottom_btn_group.setExclusive(True)

    def expand(self, checked):
        utils.set_h_expand_anim(self, checked, self.MAX_WIDTH, self.MIN_WIDTH)
