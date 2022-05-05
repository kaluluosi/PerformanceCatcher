"""
@File    :   __init__.py
@Time    :   2022/04/27 16:11:12
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   主体窗口

#todo:
设备观察器基类
只产生拔插事件
"""


from typing import Optional, Union
import PySide6

from PySide6.QtCore import QCoreApplication,QObject, QAbstractNativeEventFilter,SignalInstance,Signal


class BaseHotPlugNativeEventFilter(QObject, QAbstractNativeEventFilter):
    
    device_changed: SignalInstance = Signal()
    device_added: SignalInstance = Signal()
    device_removed: SignalInstance = Signal()

    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = None) -> None:
        super().__init__(parent)    
        super(QObject, self).__init__()
        
    def install(self, app:QCoreApplication):
        self.setParent(app)
        app.installNativeEventFilter(self)
        
    def uninstall(self, app:QCoreApplication):
        self.setParent(None)
        app.removeNativeEventFilter(self)