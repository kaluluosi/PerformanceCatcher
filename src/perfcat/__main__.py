#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __main__.py
@Time    :   2022/04/28 06:13:15
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   主启动文件
"""

# here put the import lib
import sys
from .app import PerfcatApplication

from PySide6.QtGui import QWindow


def main():
    app = PerfcatApplication(sys.argv)
    return app.exec()


sys.exit(main())
