#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/04/29 15:16:47
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   页面基类
"""

# here put the import lib
from typing import Optional
from PySide6.QtWidgets import QWidget
from perfcat.ui.constant import ButtonStyle

from perfcat.ui.widgets import notification


class Page(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._setting_widget = None

    def clear_stylesheet(self):
        self.setStyleSheet("")

    @property
    def setting_widget(self) -> Optional["Page"]:
        """
        返回设置页widget

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return self._setting_widget

    def notify(self, msg:str="警告", style:ButtonStyle=ButtonStyle.warning):
        notification.Notification(self, msg, style).show()