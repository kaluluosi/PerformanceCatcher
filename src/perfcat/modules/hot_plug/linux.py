#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/04/29 12:12:58
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   

linux系统下的 热拔插监控实现

用pyudev的observer来实现
"""

# here put the import lib

import pyudev

from PySide6.QtCore import QCoreApplication
from pyudev.monitor import MonitorObserver
from .base import BaseHotPlugNativeEventFilter


class LinuxHotPlugNatvieEventFilter(BaseHotPlugNativeEventFilter):
    def _action_handler(self, action, device):
        if action == 'add':
            self.device_added.emit()
            self.device_changed.emit()        
        elif action == 'remove':
            self.device_removed.emit()
            self.device_changed.emit()        
            

    def install(self, app: QCoreApplication):
        self.context = pyudev.Context()
        self.observer = MonitorObserver(self.context, self._action_handler)
        self.observer.start()
        return super().install(app)
    
    def uninstall(self, app: QCoreApplication):
        self.observer.stop()
        return super().uninstall(app)