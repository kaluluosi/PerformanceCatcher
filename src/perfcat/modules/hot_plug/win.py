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

win系统下的 热拔插监控实现

Qt默认的nativeEvent下，WM_DEVICECHANGE的msg.wParam永远是7，这意味着你只能得到设备变更事件，无法得知是插还是拔。
想要wParam的值正常，你需要win32gui.RegisterDeviceNotification注册系统设备通知。
注册过后WM_DEVICECHANGE的msg.wParam就会在插拔的时候为 win32con.DBT_DEVICEARRIVAL 或  win32con.DBT_DEVICEREMOVECOMPLETE了。
"""

# here put the import lib

import ctypes
from ctypes.wintypes import MSG
import PySide6
import logging
import win32gui_struct
import win32gui, win32con

from typing import Tuple, Union
from PySide6.QtCore import QCoreApplication, QTimer
from PySide6.QtGui import QWindow
from .base import BaseHotPlugNativeEventFilter

log = logging.getLogger(__name__)

# These device GUIDs are from Ioevent.h in the Windows SDK.  Ideally they
# could be collected somewhere for pywin32...
GUID_DEVINTERFACE_USB_DEVICE = "{A5DCBF10-6530-11D2-901F-00C04FB951ED}"


class WinHotPlugNativeEventFilter(BaseHotPlugNativeEventFilter):
    def nativeEventFilter(
        self, eventType: Union[PySide6.QtCore.QByteArray, bytes], message: int
    ) -> Tuple[object, int]:
        if eventType == b"windows_generic_MSG":
            msg = MSG.from_address(int(message))
            if msg.message == win32con.WM_DEVICECHANGE:
                # log.debug(f"设备变更 {msg.message} {msg.wParam} {msg.lParam}")
                # info = win32gui_struct.UnpackDEV_BROADCAST(msg.lParam)
                timer = QTimer(self)
                timer.setSingleShot(True)
                timer.setInterval(1000)
                timer.timeout.connect(lambda: self.device_changed.emit())

                if msg.wParam == win32con.DBT_DEVICEARRIVAL:
                    log.debug("设备插入")
                    timer.timeout.connect(lambda: self.device_added.emit())
                    timer.start()

                if msg.wParam == win32con.DBT_DEVICEREMOVECOMPLETE:
                    log.debug("设备移除")
                    timer.timeout.connect(lambda: self.device_removed.emit())
                    timer.start()

        return False

    def install(self, app: QCoreApplication):

        # 创建一个看不见的窗口用来RegisterDeviceNotification
        # 我们无法从app中获取其主窗口
        self._watcher = QWindow()
        hwnd = self._watcher.winId()

        filter = win32gui_struct.PackDEV_BROADCAST_DEVICEINTERFACE(
            GUID_DEVINTERFACE_USB_DEVICE
        )

        self.h_notify = win32gui.RegisterDeviceNotification(
            hwnd, filter, win32con.DEVICE_NOTIFY_WINDOW_HANDLE
        )

        if self.h_notify == 0:
            log.error(f"RegisterDeviceNotification {ctypes.FormatError()}")

        return super().install(app)

    def uninstall(self, app: QCoreApplication):
        win32gui.UnregisterDeviceNotification(self.h_notify)
        return super().uninstall(app)
