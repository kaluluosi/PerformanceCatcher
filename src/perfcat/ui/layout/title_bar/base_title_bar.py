#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   title_bar.py
@Time    :   2022/04/27 17:09:08
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :
标题栏组件，本身没有包含具体逻辑，具体按钮逻辑由使用它的模块来去实现
"""

# here put the import lib
import logging

from PySide6.QtWidgets import QWidget, QMainWindow, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QCursor, QColor
from .ui_title_bar import Ui_TitleBar

log = logging.getLogger(__name__)


class BaseTitleBar(QWidget, Ui_TitleBar):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)
        self.setupUi(self)
        # 清空qt designer写死的qss
        self.setStyleSheet("")
        # 清空qt designer设计时的文本
        self.lb_title.setText("")

        self.window().windowTitleChanged.connect(self._handle_window_title)

        self._setup_control_buttons()

    def _handle_window_title(self, title: str):
        file_path = self.window().windowFilePath()
        modified = self.window().isWindowModified()
        title_str = f"{file_path}{'*' if modified else ''}"
        self.lb_title.setText(title_str)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()
        return super().mouseDoubleClickEvent(event)

    def _setup_control_buttons(self):
        main_win: QMainWindow = self.window()

        self.btn_min.clicked.connect(self.parent().showMinimized)
        self.btn_close.clicked.connect(self.parent().close)

        # MonkeyPath掉主窗口的最大最小化方法，这样被系统最大最小化时候
        # 最大最小化按钮的状态也会正确
        def showNormal():
            log.debug("窗口最大化恢复")
            self.btn_max.setChecked(False)
            super(QMainWindow, main_win).showNormal()

        def showMaximized():
            log.debug("窗口最大化")
            self.btn_max.setChecked(True)
            super(QMainWindow, main_win).showMaximized()

        main_win.showNormal = showNormal
        main_win.showMaximized = showMaximized

        self.btn_max.toggled.connect(self._toggle_maximized)

    def _toggle_maximized(self, checked):
        if checked:
            self.window().showMaximized()
        else:
            self.window().showNormal()

    @property
    def title(self):
        return self.lb_title.text()

    @title.setter
    def title(self, value: str):
        self.lb_title.setText(value)
