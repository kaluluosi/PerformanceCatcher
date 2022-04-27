#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   win_title_bar.py
@Time    :   2022/04/27 18:55:33
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   windows系统下的标题栏，用到win32 api去实现窗体移动
"""

# here put the import lib

import win32api
import win32gui
import win32con

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QCursor
from .base_title_bar import BaseTitleBar


class WinTitleBar(BaseTitleBar):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent) -> None:

        if self.rect().contains(event.pos()):
            win32gui.ReleaseCapture()
            win32api.SendMessage(
                self.window().winId(),
                win32con.WM_SYSCOMMAND,
                win32con.SC_MOVE | win32con.HTCAPTION,
                0,
            )
            event.ignore()
        return super().mousePressEvent(event)
