from ast import Set
from os import stat
from tkinter import Button, EventType
import PySide6
import logging
from typing import List, Optional, Sequence, Tuple, Union
from ppadb.client import Client as adb
from ppadb.device import Device
from PySide6.QtWidgets import QWidget, QPushButton, QErrorMessage, QApplication
from perfcat.ui.constant import ButtonStyle
from perfcat.ui.page import Page
from PySide6.QtCore import (
    Qt,
    Signal,
    SignalInstance,
)
from perfcat.modules.hot_plug import HotPlugWatcher


from .ui_profiler import Ui_Profiler

log = logging.getLogger(__name__)


class Profiler(Page, Ui_Profiler):

    # 当系统设备插拔的时候发出信号
    device_changed: SignalInstance = Signal()

    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setupUi(self)
        self.clear_stylesheet()

        # 让监视器layout顶部对齐（designer里无法做到只能代码设置）
        self.verticalLayout_6.setAlignment(Qt.AlignTop)

        self.devices:Set = set()
        self.current_device: Device = None

        self.adb = adb()
        
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        HotPlugWatcher.device_added.connect(self._on_device_add)
        HotPlugWatcher.device_removed.connect(self._on_device_removed)
        
        self.devices = set(self.adb.devices())
        
        for d in self.devices:
            self.cbx_device.addItem(d.serial)
        
        return super().showEvent(event)
    
    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None:
        HotPlugWatcher.device_added.disconnect(self._on_device_add)
        HotPlugWatcher.device_removed.disconnect(self._on_device_removed)
        return super().hideEvent(event)

    def _on_device_add(self):
        self.notify("发现新设备！",ButtonStyle.success)
        device_list = set(self.adb.devices())
        log.debug(self.devices)
        log.debug(device_list)


    def _on_device_removed(self):
        self.notify("设备被移除！",ButtonStyle.warning)
        
        log.debug(self.devices)
        


    def start_tick(self):
        log.debug("开启tick定时器 开始采集")
        self.tick_timer_id = self.startTimer(1000, Qt.VeryCoarseTimer)

    def stop_tick(self):
        log.debug("停止tick定时器 停止采集")
        self.killTimer(self.tick_timer_id)

