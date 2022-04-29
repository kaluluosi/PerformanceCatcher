#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/04/29 12:12:58
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   __version__ 会作为包版本
"""

# here put the import lib


import sys
import pkg_resources

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

# 读取和设置包的元信息
metadata = importlib_metadata.metadata(__package__)
__version__ = pkg_resources.get_distribution(__package__).version
__author__ = metadata["Author"]
__author_email__ = metadata["Author-email"]

# 把asset/放到搜索目录里，这样.ui文件里 import asset_rc 才能正常导入asset_rc
asset_dir = pkg_resources.resource_filename(__package__, "assets")
sys.path.append(asset_dir)