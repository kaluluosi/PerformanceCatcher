#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   comm_title_bar.py
@Time    :   2022/04/27 18:54:24
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   通用标题栏，完全用PySide6实现窗体移动
"""

# here put the import lib

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QCursor
from .base_title_bar import BaseTitleBar


class CommTitleBar(BaseTitleBar):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)
        self._handle_move_window()

    def _handle_move_window(self):
        main_win: QMainWindow = self.window()

        def moveWindow(event: QMouseEvent):
            if main_win.isMaximized():
                main_win.showNormal()
                cur_x = main_win.pos().x()
                cur_y = event.globalPos().y() - QCursor.pos().y()
                main_win.move(cur_x, cur_y)

            if event.buttons() == Qt.LeftButton:
                main_win.move(main_win.pos() + event.globalPos() - self._dragPos)
                self._dragPos = event.globalPos()
                event.accept()

        self.logo.mouseMoveEvent = moveWindow
        self.lb_title.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self._dragPos = event.globalPos()
        return super().mousePressEvent(event)
