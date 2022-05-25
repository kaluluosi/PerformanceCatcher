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

# # here put the import lib
# # 设置环境变量切换成生产模式
# import os
# os.environ["MODE"] = "production"

import sys
from perfcat.app import PerfcatApplication
from perfcat import asset_rc


def main():
    app = PerfcatApplication(sys.argv)
    return app.exec()


sys.exit(main())
