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
from .base.chart import MonitorChart
from perfcat.modules.profiler.temp import MarkTempSampler


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
        self.setObjectName("Temperature")
        self.setToolTip("不少设备无法获得温度，会显示为-1")
        self.mark_temp = None

        self._sample_data = {}

    def sample(self, sec: int, device: Device, package_name: str):

        if self.mark_temp is None:
            self.mark_temp = MarkTempSampler(device)

        temp_data = self.mark_temp.get_temp()

        self._sample_data[sec] = {
            "整体温度": temp_data["total"],
            "CPU温度":temp_data["cpu"],
            "GPU温度": temp_data["gpu"],
            "NPU温度": temp_data["npu"],
            "电池温度": temp_data["battery"]
        }

        for k,v in self._sample_data[sec].items():
            self.add_point(k, sec, v)

    def reset_series_data(self):
        self.mark_temp = None
        self._sample_data = {}
        return super().reset_series_data()

    def to_dict(self, all: bool = True) -> dict:
        if all:
            return self._sample_data
        else:
            start = self.record_range[0]
            end = self.record_range[1]

            data = {}
            for k,v in self._sample_data.items():
                if start <= k <= end:
                    data[k] = v
            return data

    def from_dict(self, data: dict):
        for sec, data_table in data:
            for k, v in data_table.items():
                self.add_point(k,sec, v)
