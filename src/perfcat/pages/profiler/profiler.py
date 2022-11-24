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


import PySide6
import logging
import csv
import time
import json
import io
import os
import subprocess
import pkg_resources
from shutil import which

from perfcat.pages.profiler.plugins.base import MonitorChart
from . import plugins
from ppadb.client import Client as adb
from ppadb.device import Device
from PySide6.QtWidgets import (
    QCompleter,
    QTableWidgetItem,
    QApplication,
    QMessageBox,
    QFileDialog,
)
from PySide6.QtCore import (
    Qt,
    Signal,
    QRunnable,
    SignalInstance,
    QThread,
    QTimer,
    QElapsedTimer,
    QThreadPool,
)
from perfcat.modules.hot_plug import HotPlugWatcher
from perfcat.modules.reporter import export
from perfcat.settings import settings

from ...ui.constant import ButtonStyle
from ...ui.page import Page
from .plugins import register
from .ui_profiler import Ui_Profiler
from ...modules.profiler.device import device_info
from .logcat2 import LogcatWidget

log = logging.getLogger(__name__)


class Worker(QRunnable):
    def __init__(self, func, *args, **kwargs) -> None:
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func(*self.args, **self.kwargs)


class Profiler(Page, Ui_Profiler):

    # 当系统设备插拔的时候发出信号
    device_changed: SignalInstance = Signal()
    # 初始化adb-server信号
    adb_server_starting: SignalInstance = Signal()

    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setupUi(self)
        self.clear_stylesheet()

        # 让监视器layout顶部对齐（designer里无法做到只能代码设置）
        self.verticalLayout_6.setAlignment(Qt.AlignTop)

        self.adb = adb()
        self._device_info = {}

        self.plugins: list[MonitorChart] = []

        self.sample_thread: QThread = QThread(self)
        self.tick_count = 0
        self.record_range = [0, 0]

        self.btn_connect.toggled.connect(self._connect_device)

        # 默认是没选中任何设备和app，此时连接和录制置灰
        self.btn_connect.setEnabled(False)
        self.btn_record.setEnabled(False)

        # 复制设备信息
        self.btn_copy_info.clicked.connect(self._copy_info)

        # 日志logcat模块
        self.logcat = LogcatWidget(self)
        self.verticalLayout_8.addWidget(self.logcat)

        # 当设备选择改变的时候更新连接按钮状态
        self.cbx_device.currentIndexChanged.connect(self._update_btn_status)  # 设备切换时更新
        self.cbx_device.currentIndexChanged.connect(
            self._update_device_info
        )  # 读取显示设备信息
        self.cbx_app.currentIndexChanged.connect(self._update_btn_status)  # app切换时更新
        self.cbx_app.editTextChanged.connect(self._update_btn_status)  # app名修改的时候更新

        self.cbx_device.currentIndexChanged.connect(self._update_app_list)

        # 按钮处理
        self.btn_save.clicked.connect(self._save_file)
        self.btn_open.clicked.connect(self._open_file)
        self.btn_record.toggled.connect(self._on_toggled_record)

        self._init_plugins()
        self._update_btn_status()

        self.adb_server_starting.connect(
            lambda: self.notify("adb server 启动中...", ButtonStyle.warning)
        )

    def _init_plugins(self):
        self.reset_h_scrollbar()
        for plugin_cls in register:
            plugin: MonitorChart = plugin_cls(self)
            self.scrollAreaWidgetContents.layout().addWidget(plugin)

            self.plugins.append(plugin)

            self.horizontalScrollBar.valueChanged.connect(plugin.set_x_offset)  # 水平滚动同步
            plugin.axis_range_size_changed.connect(self._sync_plugin_range_size)  # 缩放同步
            plugin.mark_line_changed.connect(self._sync_mark_line)  # 标线位置同步
            plugin.x_max_offset_changed.connect(self._sync_scroll_max)  # 滚动条同步最大x轴

    def start_adb_server(self):
        path = which("adb")
        default_adb_path = pkg_resources.resource_filename("perfcat", "adb/adb.exe")
        log.debug(f"系统adb:{path} 内置adb:{default_adb_path}")
        path = path or default_adb_path
        try:
            self.adb.version()
        except RuntimeError:
            self.adb_server_starting.emit()
            log.debug(f"启动adb命令:{[path, 'start-server']}")
            subprocess.call([path, "start-server"], shell=True)
            log.debug(f"测试adb server:{self.adb.version()}")

    def reset_h_scrollbar(self):
        self.horizontalScrollBar.setMaximum(0)
        self.horizontalScrollBar.setValue(0)

    def _sync_mark_line(self, pos):
        sender: MonitorChart = self.sender()
        for p in self.plugins:
            if p == sender:
                continue
            p.mark_line = sender.mark_line

    def _sync_plugin_range_size(self):
        sender: MonitorChart = self.sender()
        axis_range_size = sender.axis_range_size
        for p in self.plugins:
            if p == sender:
                continue
            p.axis_range_size = axis_range_size

    def _sync_scroll_max(self, value):
        if self.horizontalScrollBar.value() == self.horizontalScrollBar.maximum():
            self.horizontalScrollBar.setMaximum(value)
            self.horizontalScrollBar.setValue(value)
        else:
            self.horizontalScrollBar.setMaximum(value)

    def clear_all_data(self):
        for p in self.plugins:
            p.reset_series_data()

        self.reset_h_scrollbar()

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
        self.btn_save.setEnabled(valid_device and valid_app)

        self.logcat.device = self.current_device

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
            self.tb_device_info.clearContents()

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
        devices: list[Device] = self.adb.devices(state="device")
        pre_selected = self.cbx_device.currentText()
        self.cbx_device.clear()
        for dev in devices:
            model = dev.get_properties()["ro.product.model"]
            name = dev.get_properties()["ro.product.name"]
            self.cbx_device.addItem(f"[{dev.serial}] {model}-{name}", dev)

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
            self.start_adb_server()
            # self.devices = set(self.adb.devices(state="device"))
            self._update_devices_list()
            # log.debug(f"刷新设备列表 {self.devices}")

        thread.run = run
        thread.start()

        return super().showEvent(event)

    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None:
        HotPlugWatcher.device_added.disconnect(self._on_device_add)
        HotPlugWatcher.device_removed.disconnect(self._on_device_removed)

        self._connect_device(False)
        return super().hideEvent(event)

    def _on_device_add(self):
        devices: list[Device] = self.adb.devices(state="device")
        count = len(devices)
        if self.cbx_device.count() != count:
            self.notify("发现新设备！", ButtonStyle.success)
            # todo: 添加新设备item
            self._update_devices_list()

    def _on_device_removed(self):
        devices: list[Device] = self.adb.devices(state="device")
        count = len(devices)
        if self.cbx_device.count() != count:
            self.notify("设备被移除！", ButtonStyle.warning)
            # todo: 移除旧设备item，如果旧设备的serial正好是当前连接中设备，那么就置空currentIndex
            self._update_devices_list()

    def timerEvent(self, event: PySide6.QtCore.QTimerEvent) -> None:
        return super().timerEvent(event)

    def start_tick(self):
        log.debug("开始采样")
        self.tick_count = 0

        def _run():
            # 先采样缓存采样点，然后再统一刷入可以保证多个monitor同步刷新
            # 统一采样
            pool = QThreadPool.globalInstance()
            while not self.sample_thread.isInterruptionRequested():

                # 记录这次采样耗时
                time_counter = QElapsedTimer()
                time_counter.start()

                for p in self.plugins:
                    # 用线程池来启动每一个monitor的采样方法
                    # 测试发现 adb的每次命令调用耗时大概0.01ms
                    # 如果采样的实现方式有多次命令调用，那么采样耗时会累积的很高
                    # 如果每个monitor的采样采用遍历切同步的方式去处理就会很容易累计超过1s采样间隔
                    # 导致采样间隔不固定
                    # 现在改为用线程池开worker去并发处理每个monitor的sample
                    # 然后线程池等待所有worker结束再进入下一轮采样
                    workder = Worker(
                        p.sample,
                        self.tick_count,
                        self.current_device,
                        self.cbx_app.currentText(),
                    )

                    pool.start(workder)

                pool.waitForDone()

                # 统一刷入系列，让图标绘制折线
                for p in self.plugins:
                    p.flush()

                # 获取采样耗时
                take_sec = time_counter.elapsed()
                # 如果采样时间不足1s，那么剩下空闲时间让采样tick线程把这段时间睡过去
                if take_sec < 1000:
                    self.sample_thread.msleep(1000 - take_sec)
                self.tick_count += 1
            log.debug("采样线程退出")

        self.sample_thread.run = _run
        self.sample_thread.start()

    def stop_tick(self):
        log.debug("停止采样")
        if self.sample_thread.isRunning():
            self.sample_thread.requestInterruption()  # 中断线程
            self.sample_thread.wait()  # 主线程同步等待线程退出

    def destroy(self, destroyWindow: bool = ..., destroySubWindows: bool = ...) -> None:
        self.stop_tick()
        return super().destroy(destroyWindow, destroySubWindows)

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
            self.clear_all_data()
            self.start_tick()
            self.btn_open.setEnabled(False)
        else:
            if self.current_device:  # current_device非none就是还连着usb
                log.debug(f"断开设备 {self.current_device.serial}")
                self.notify(f"断开设备 {self.current_device.serial}", ButtonStyle.warning)

            self.stop_tick()
            self.btn_record.setChecked(False)
            self.btn_open.setEnabled(True)
            self.record_range = [0, 0]

        self.cbx_device.setDisabled(enable)
        self.cbx_app.setDisabled(enable)

        # 先拦截信号防止setchecked的时候发出toggled信号导致执行两次
        self.btn_connect.blockSignals(True)
        self.btn_connect.setChecked(enable)
        self.btn_connect.blockSignals(False)

        self.btn_record.setEnabled(enable)

    def _save_file(self):

        device_name = self._device_info["型号"]
        app_name = self.cbx_app.currentText()

        result = QMessageBox.question(
            self,
            "保存全部?",
            "是:保存全部数据\n否:仅保存录制的那部分",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
            QMessageBox.Yes,
        )
        if result == QMessageBox.Cancel:
            return

        if result == QMessageBox.Yes:
            data = self._get_data()
        elif result == QMessageBox.No:
            data = self._get_data(False)

        date_str = time.strftime("%Y-%m-%d_%H-%M-%S")
        last_dir = settings.value("profiler/last_dir", "")

        file_name = QFileDialog.getSaveFileName(
            self,
            "保存记录",
            os.path.join(last_dir, f"{device_name}_{app_name}_{date_str}"),
            "perfcat(*.pc);;excel(*.xlsx)",
        )
        if file_name[0]:
            if file_name[1] == "perfcat(*.pc)":
                self.btn_record.setChecked(False)
                self.update()
                with open(file_name[0], "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    self.notify(f"保存到 {file_name[0]}", ButtonStyle.success)
                last_dir = os.path.dirname(file_name[0])
                settings.setValue("profiler/last_dir", last_dir)
            elif file_name[1] == "excel(*.xlsx)":
                export(app_name,data, file_name[0])


    def _open_file(self):
        last_dir = settings.value("profiler/last_dir", "")
        file_name = QFileDialog.getOpenFileName(self, "保存记录", last_dir, "perfcat(*.pc)")

        if file_name[0]:
            with open(file_name[0], "r", encoding="utf-8") as f:
                data = json.load(f)
                data = data["data"]

                for plugin in self.plugins:
                    if plugin.objectName() in data:
                        plugin.from_dict(data[plugin.objectName()])

                self.notify(f"打开:{file_name[0]}", ButtonStyle.success)

    def _get_data(self, all: bool = True):
        data = {"data": {}}
        for plugin in self.plugins:
            if all:
                _p_data = plugin.to_dict()
            elif not all:
                # todo: 根据record切割数据
                _p_data = plugin.to_dict(False)

            data["data"][plugin.objectName()] = _p_data
        data["device_info"] = self.device_info
        data["tick_count"] = self.tick_count
        return data

    def _on_toggled_record(self, checked: bool):
        if checked:
            self.record_range[0] = self.tick_count
            self.notify("开始记录", ButtonStyle.info)
            # 遍历插件开启记录线绘制（就是画条线来显示从哪到哪是记录的）
            # 记录的截取则是在这里加工处理，插件不负责截取区间数据
            for p in self.plugins:
                p.record_enable(True, self.tick_count)
        else:
            self.record_range[1] = self.tick_count
            # 遍历插件关闭记录线绘制（就是画条线来显示从哪到哪是记录的）
            for p in self.plugins:
                p.record_enable(False)
            log.debug(f"结束录制，录制的时间范围是 {self.record_range}")
            self.notify("结束记录", ButtonStyle.info)
            # todo: 结束记录后要做什么，比如直接复制剪贴板？保存报告？可以在这后面处理
