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

# here put the import lib
from PySide6.QtWidgets import QWidget, QApplication


class PerfcatApplication(QApplication):
    """
    Perfcat App本体
    负责App框架管理

    _extended_summary_

    Args:
        QApplication (_type_): _description_
    """

    def __init__(self, *args):
        super().__init__(args)
