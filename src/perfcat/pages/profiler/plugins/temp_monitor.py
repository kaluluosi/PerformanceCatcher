#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   temp_monitor.py
@Time    :   2022/05/10 12:16:47
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   emm...
温度采集

"""

# here put the import lib
from ppadb.device import Device
from perfcat.modules.profiler.temp import MarkTemp
from .base.chart import MonitorChart


class TempMonitor(MonitorChart):
    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            series_names=["整体温度", "CPU温度", "GPU温度", "NPU温度", "电池温度"],
            formatter={
                "整体温度": lambda v: f"{v}℃",
                "CPU温度": lambda v: f"{v}℃",
                "GPU温度": lambda v: f"{v}℃",
                "NPU温度": lambda v: f"{v}℃",
                "电池温度": lambda v: f"{v}℃",
            },
            y_axis_name="℃",
            parent=parent,
        )
        self.setToolTip("不少设备无法获得温度，会显示为-1")
        self.mark_temp = None

    def sample(self, sec: int, device: Device, package_name: str):

        if self.mark_temp is None:
            self.mark_temp = MarkTemp(device)

        temp_data = self.mark_temp.get_temp()

        self.add_point("整体温度", sec, temp_data["total"])
        self.add_point("CPU温度", sec, temp_data["cpu"])
        self.add_point("GPU温度", sec, temp_data["gpu"])
        self.add_point("NPU温度", sec, temp_data["npu"])
        self.add_point("电池温度", sec, temp_data["battery"])

    def reset_series_data(self):
        self.mark_temp = None
        return super().reset_series_data()
