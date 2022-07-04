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

# 把asset/放到搜索目录里，这样.ui文件里 import asset_rc 才能正常导入asset_rc
import logging
import sys
import pkg_resources
from email import message_from_string
from importlib.metadata import metadata
from webob.multidict import MultiDict

log = logging.getLogger(__name__)

asset_dir = pkg_resources.resource_filename(__package__, ".")
sys.path.append(asset_dir)


try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

# 读取和设置包的元信息
__version__ = "1.0.2"
__author__ = "dengxuan"
__author_email__ = "dengxuan@xinyuanstu.com"
__meta__ = {}

try:
    METADATA = pkg_resources.get_distribution("perfcat").get_metadata("METADATA")
    msg = message_from_string(METADATA)
    __meta__ = MultiDict(msg)
    __version__ = __meta__["Version"]
    __author__ = __meta__["Author"]
    __author_email__ = __meta__["Author-email"]
except Exception as e:
    log.exception(e)
