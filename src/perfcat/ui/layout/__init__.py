#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/04/27 16:11:12
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   主体窗口

#todo:
[1] windows操作系统的窗口动画对无边窗口不起作用，所以放大缩小没有动画，也不能贴边触发分屏
目前还不知道怎么解决这个问题，用了win32api结果抽了
"""

# here put the import lib
import logging

from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtCore import Qt

from . import effects
from .ui_mainwindow import Ui_MainWindow

from .left_menu import LeftMenu
from .title_bar import TitleBar
from .left_column import LeftColumn

log = logging.getLogger(__name__)


class MainWindow(QMainWindow, Ui_MainWindow):

    LEFT_COLUMN_MAXWIDTH = 240
    LEFT_COLUMN_MINWIDTH = 0

    CONTENT_RIGHT_MAXWIDTH = 240
    CONTENT_RIGHT_MINWIDTH = 0

    def __init__(self) -> None:
        super().__init__()
        # 初始化ui文件
        self.setupUi(self)
        self.setStyleSheet("")  # 清空qt designer里写死的样式

        # 设置flag
        # 隐藏窗体边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 设置阴影（很淡……几乎看不见，有点感觉就行）
        effects.set_shadow_effect(self)
        effects.set_shadow_effect(self.content_right_frame)

        # 添加左导航菜单
        self._setup_leftmenu()

        # 添加标题栏
        self._setup_title_bar()

        # 添加状态栏
        self._setup_status_bar()

        # 添加左面板栏
        self._setup_left_column()

    def setWindowFilePath(self, filePath: str) -> None:
        super().setWindowFilePath(filePath)
        self.windowTitleChanged.emit(self.windowTitle())
        # return super().setWindowFilePath(filePath)

    def setWindowModified(self, arg__1: bool) -> None:
        super().setWindowModified(arg__1)
        self.windowTitleChanged.emit(self.windowTitle())
        # return super().setWindowModified(arg__1)

    def _setup_leftmenu(self):
        self.left_menu = LeftMenu(self)
        self.left_menu.setObjectName("LeftMenu")
        self.left_menu_frame.layout().addWidget(self.left_menu)

        # 添加阴影
        effects.set_shadow_effect(self.left_menu_frame)

        # 按钮组点击的时候触发展开左栏
        self.left_menu.bottom_btn_group.buttonToggled.connect(
            self._toggle_left_column_frame
        )

    def _setup_title_bar(self):
        # 添加标题栏
        self.title_bar = TitleBar(self)
        self.title_bar.setObjectName("TitleBar")
        self.title_bar_frame.layout().addWidget(self.title_bar)

        # 设置阴影
        effects.set_shadow_effect(self.title_bar_frame)

        # 页面设置按钮
        self.title_bar.btn_setting.toggled.connect(self.expand_content_right_frame)

    def _setup_status_bar(self):
        effects.set_shadow_effect(self.status_bar_frame)

    def _setup_left_column(self):
        self.left_column = LeftColumn(self)
        self.left_column_frame.layout().addWidget(self.left_column)

        self.left_column.btn_close.clicked.connect(
            lambda: self.expand_left_column_frame(False)
        )

    @property
    def left_column_visible(self) -> bool:
        return self.left_column_frame.maximumWidth() > 0

    @property
    def content_right_visible(self) -> bool:
        return self.content_right_frame.maximumWidth() > 0

    def _toggle_left_column_frame(self, button: QPushButton, checked: bool):

        if not self.left_column_visible:
            self.expand_left_column_frame(True)

    def expand_left_column_frame(self, checked: bool):
        effects.set_h_expand_anim(
            self.left_column_frame,
            checked,
            self.LEFT_COLUMN_MAXWIDTH,
            self.LEFT_COLUMN_MINWIDTH,
        )
        if not checked:
            # 折叠回去了，清除掉底部互斥选项卡的选中
            self.left_menu.bottom_btn_group_reset()

    def expand_content_right_frame(self, checked: bool):
        effects.set_h_expand_anim(
            self.content_right_frame,
            checked,
            self.CONTENT_RIGHT_MAXWIDTH,
            self.CONTENT_RIGHT_MINWIDTH,
        )
