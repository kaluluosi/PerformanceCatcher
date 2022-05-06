#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   profiler.py
@Time    :   2022/05/05 20:16:06
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :  
todo:
[1] 如果需要设备选择和app选择体验更好点就要重新实现model和itemdelegate了。目前暂时这样吧。
[2] 最好还是开一个线程去采集性能数据，不然会阻塞主线程。

"""

# here put the import lib


import io
import PySide6
import logging
import csv
from ppadb.client import Client as adb
from ppadb.device import Device
from PySide6.QtWidgets import QCompleter, QTableWidgetItem, QApplication
from perfcat.ui.constant import ButtonStyle
from perfcat.ui.page import Page
from PySide6.QtCore import Qt, Signal, SignalInstance, QThread
from perfcat.modules.hot_plug import HotPlugWatcher


from .ui_profiler import Ui_Profiler
from .util import device_info

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

        self.adb = adb()
        self.tick_timer_id = -1
        self._device_info = {}

        self.btn_connect.toggled.connect(self._connect_device)

        # 默认是没选中任何设备和app，此时连接和录制置灰
        self.btn_connect.setEnabled(False)
        self.btn_record.setEnabled(False)

        # 复制设备信息
        self.btn_copy_info.clicked.connect(self._copy_info)

        # 档设备选择改变的时候更新连接按钮状态
        self.cbx_device.currentIndexChanged.connect(self._update_btn_status)  # 设备切换时更新
        self.cbx_device.currentIndexChanged.connect(
            self._update_device_info
        )  # 读取显示设备信息
        self.cbx_app.currentIndexChanged.connect(self._update_btn_status)  # app切换时更新
        self.cbx_app.editTextChanged.connect(self._update_btn_status)  # app名修改的时候更新

        self.cbx_device.currentIndexChanged.connect(self._update_app_list)

    @property
    def current_device(self) -> Device:
        """
        返回当前选中的设备

        Returns:
            Device: _description_
        """
        return self.cbx_device.currentData(Qt.UserRole)

    @property
    def device_info(self) -> dict[str, str]:
        if self.current_device is None:
            return {}

        return self._device_info

    def _update_btn_status(self):
        valid_device = self.cbx_device.currentIndex() > -1
        valid_app = (
            self.cbx_app.currentIndex() > -1 and self.cbx_app.currentText() != ""
        )

        log.debug(f"更新按钮状态 valid_device:{valid_device} valid_app:{valid_app}")
        self.btn_connect.setEnabled(valid_device and valid_app)

    def _copy_info(self):
        """
        把设备信息复制到剪贴板

        """
        if self.current_device:
            device_info = self._device_info
            clipboard = QApplication.clipboard()
            output = io.StringIO()
            writer = csv.writer(output, csv.get_dialect("excel-tab"))
            for k, v in device_info.items():
                writer.writerow([k, v])
            text = output.getvalue()
            clipboard.setText(text)
            self.notify("复制设备信息到剪贴板", ButtonStyle.success)

    def _update_device_info(self):
        """
        更新设备信息

        _extended_summary_
        """
        thread = QThread(self)

        def run():
            # 缓存到成员变量里免得每次都重新获取阻塞UI
            if self.current_device:
                dev_info = self._device_info = device_info(self.current_device)
            else:
                dev_info = self._device_info = {}

            # 清空数据
            self.tb_device_info.clear()
            # 重新设置表头
            prop_header = QTableWidgetItem("属性")
            value_header = QTableWidgetItem("值")
            self.tb_device_info.setHorizontalHeaderItem(0, prop_header)
            self.tb_device_info.setHorizontalHeaderItem(1, value_header)

            if not dev_info:
                self.btn_copy_info.setEnabled(False)
                return

            # 设置行数
            self.tb_device_info.setRowCount(len(dev_info))

            # 填写数据
            index = 0
            for prop, value in dev_info.items():
                prop_item = QTableWidgetItem(prop)
                prop_item.setFlags(prop_item.flags() ^ Qt.ItemIsEditable)
                self.tb_device_info.setItem(index, 0, prop_item)
                value_item = QTableWidgetItem(value)
                value_item.setToolTip(value)
                value_item.setFlags(prop_item.flags() ^ Qt.ItemIsEditable)
                self.tb_device_info.setItem(index, 1, value_item)
                index += 1
            self.btn_copy_info.setEnabled(True)

        thread.run = run
        thread.start()

    def _update_app_list(self, index: int):
        if not self.current_device:
            self.cbx_app.clear()
            return
        packages = self.current_device.list_packages()
        self.cbx_app.clear()
        items = packages
        self.cbx_app.addItems(items)
        completer = QCompleter(items, self.cbx_app)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.cbx_app.setCompleter(completer)

    def _update_devices_list(self):
        devices: list[Device] = self.adb.devices()
        pre_selected = self.cbx_device.currentText()
        self.cbx_device.clear()
        for dev in devices:
            model = dev.get_properties()["ro.product.model"]
            self.cbx_device.addItem(f"[{dev.serial}] {model}", dev)

        self.cbx_device.setCurrentText(pre_selected)
        # 这一段检查当前选中的设备是不是断开了
        if self.cbx_device.currentIndex() == -1 and pre_selected != "":
            self.notify("当前选择的设备已经断开！", ButtonStyle.danger)
            # 如果断开了不管是不是正在连接都强制断开
            self._connect_device(False)

    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:

        # 这种神奇的用法……用monkeypatch的方式强行把run方法替换成内部函数，就不用派生了
        # 这样可以快速的编写异步代码，防止阻塞UI线程
        # 如果不需要维护和释放thread，那么就不需要self里声明一个变量来保存了
        # 这样写用完就抛，python会帮我们释放这个thread对象
        thread = QThread(self)

        def run():
            HotPlugWatcher.device_added.connect(self._on_device_add)
            HotPlugWatcher.device_removed.connect(self._on_device_removed)

            self.devices = set(self.adb.devices())

            self._update_devices_list()
            log.debug(f"刷新设备列表 {self.devices}")

        thread.run = run
        thread.start()

        return super().showEvent(event)

    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None:
        HotPlugWatcher.device_added.disconnect(self._on_device_add)
        HotPlugWatcher.device_removed.disconnect(self._on_device_removed)
        return super().hideEvent(event)

    def _on_device_add(self):
        self.notify("发现新设备！", ButtonStyle.success)
        # todo: 添加新设备item
        self._update_devices_list()

    def _on_device_removed(self):
        self.notify("设备被移除！", ButtonStyle.warning)
        # todo: 移除旧设备item，如果旧设备的serial正好是当前连接中设备，那么就置空currentIndex
        self._update_devices_list()

    def start_tick(self):
        log.debug("开启tick定时器 开始采集")
        self.tick_timer_id = self.startTimer(1000, Qt.VeryCoarseTimer)

    def stop_tick(self):
        log.debug("停止tick定时器 停止采集")
        self.killTimer(self.tick_timer_id)

    def timerEvent(self, event: PySide6.QtCore.QTimerEvent) -> None:

        try:
            log.info(f"cpu:{self.current_device.cpu_percent()}")
        except Exception as e:
            log.warning(e)

        return super().timerEvent(event)

    def _connect_device(self, enable: bool = True):
        """
        连接设备

        这个方法说是连接设备，其实只是开启tick定时器来轮询设备而已

        Args:
            enable (bool, optional): True开始轮询，False结束轮询. Defaults to True.
        """

        if enable:
            log.debug(f"连接设备 {self.current_device.serial}")
            self.notify(f"连接设备 {self.current_device.serial}", ButtonStyle.success)
            self.start_tick()
        else:
            if self.current_device:  # current_device非none就是还连着usb
                log.debug(f"断开设备 {self.current_device.serial}")
                self.notify(f"断开设备 {self.current_device.serial}", ButtonStyle.warning)
            else:
                self.notify(f"当前设备异常断开，可能被直接拔了！", ButtonStyle.danger)

            self.stop_tick()

        self.cbx_device.setDisabled(enable)
        self.cbx_app.setDisabled(enable)

        # 先拦截信号防止setchecked的时候发出toggled信号导致执行两次
        self.btn_connect.blockSignals(True)
        self.btn_connect.setChecked(enable)
        self.btn_connect.blockSignals(False)

        self.btn_record.setEnabled(enable)
