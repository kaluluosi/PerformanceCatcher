#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   app.py
@Time    :   2022/04/28 19:17:00
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   app全局对象
"""
# app 关于信息


# here put the import lib
import logging
from typing import Optional, Tuple, Union
import PySide6
import pkg_resources
from ctypes.wintypes import MSG
import win32con
from .ui.layout import MainWindow
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import (
    QAbstractNativeEventFilter,
    SignalInstance,
    Signal,
    QObject,
    QEvent,
)

from . import __version__, __author__, __author_email__
from .modules.hot_plug import HotPlugWatcher
from . import pages

log = logging.getLogger(__name__)


__doc__ = f"""
# Perfcat
**ver {__version__}**

### Meta

作者: {__author__}

邮件: {__author_email__}
"""


class PerfcatApplication(QApplication):
    """
    Perfcat App本体
    负责App框架管理

    _extended_summary_

    Args:
        QApplication (_type_): _description_
    """

    def __init__(self, *args):
        super().__init__(*args)

        self.load_stylesheet()

        self.main_win = MainWindow()
        self.main_win.set_about_info(__doc__)
        self.main_win.show()

        self._install_pages()

        HotPlugWatcher.install(self)

    @classmethod
    @property
    def instance(cls) -> "PerfcatApplication":
        return QApplication.instance()

    def load_stylesheet(self, path=None):
        if not path:
            stylesheet = pkg_resources.resource_string(
                __package__, "assets/css/default.css"
            ).decode("utf-8")
            log.debug("加载内置stylesheet")
        else:
            with open(path) as f:
                stylesheet = f.read()
            log.debug(f"加载stylesheet：{path}")

        self.setStyleSheet(stylesheet)
        log.debug("加载stylesheet")

    def _install_pages(self):
        w = self.main_win
        for page in pages.register:
            w.add_page(page(w))
