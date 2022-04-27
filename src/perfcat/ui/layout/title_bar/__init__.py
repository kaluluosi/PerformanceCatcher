#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/04/27 23:57:16
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   
windows平台可以用win32api的方式来移动窗口
其他系统就用Qt的解决方法了

PS:
[1] 其实直接用通用Tilebar就好了……目前来讲就只有移动方案分家了
[2] 不过我保留两种方案，供其他人学习
"""

# here put the import lib


import sys
import logging

log = logging.getLogger(__name__)

if sys.platform == "win32":
    log.debug("使用 win titlebar")
    from .win_title_bar import WinTitleBar as TitleBar
else:
    log.debug("使用 通用 titlebar")
    from .comm_title_bar import CommTitleBar as TitleBar
