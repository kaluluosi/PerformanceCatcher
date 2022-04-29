from typing import List
import PySide6
from ppadb.client import Client as adb
from ppadb.device import Device
from PySide6.QtWidgets import QWidget, QPushButton
from perfcat.ui.page import Page
from PySide6.QtCore import Qt
from .ui_profiler import Ui_Profiler


class Setting(Page):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setWindowTitle("性能>设置")

        btn = QPushButton("性能 设置", self)


class Profiler(Page, Ui_Profiler):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setupUi(self)
        self.clear_stylesheet()

        self.verticalLayout_6.setAlignment(Qt.AlignTop)

        self._setting_widget = Setting(self)

        self.adb = adb()
        self.current_device = None

        self.startTimer(1000, Qt.VeryCoarseTimer)

        self.btn_connect.toggled.connect(self.connect_device)

    def timerEvent(self, event: PySide6.QtCore.QTimerEvent) -> None:
        self.detect_device()
        return super().timerEvent(event)

    def connect_device(self, checked):
        self.cbx_device.setDisabled(checked)
        self.cbx_app.setDisabled(checked)
        # todo：连接设备
        if checked:
            self.current_device = self.adb.devices()[self.cbx_device.currentIndex()]
        else:
            self.current_device = None

    def detect_device(self):

        if self.current_device:
            # 当前连着设备，所以不检测设备
            return

        devices: List[Device] = self.adb.devices()
        for d in devices:
            serial_no = d.get_serial_no()
            model = d.get_properties()["ro.product.model"]
            if self.cbx_device.findText(model) != -1:
                continue
            self.cbx_device.addItem(f"{model}")
