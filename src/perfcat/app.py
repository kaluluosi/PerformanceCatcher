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
from . import __version__, __author__, __author_email__

__doc__ = f"""
# Perfcat
**ver {__version__}**

### Meta

作者: {__author__}

邮件: {__author_email__}
"""
import logging
from .ui.layout import MainWindow

# here put the import lib
from PySide6.QtWidgets import QWidget, QApplication

from . import modules

log = logging.getLogger(__name__)


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

    @classmethod
    @property
    def instance(cls) -> "PerfcatApplication":
        return QApplication.instance()

    def load_stylesheet(self):
        with open(
            r"G:\projects\perfcat\src\perfcat\assets\css\default.css", encoding="utf-8"
        ) as f:
            sheet = f.read()

        self.setStyleSheet(sheet)
        log.debug("加载stylesheet")

    def _install_pages(self):
        w = self.main_win
        for page in modules.register:
            w.add_page(page(w))
