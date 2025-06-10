#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   fps_monitor.py
@Time    :   2022/05/13 16:58:00
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   emm...
fps采样
"""

# here put the import lib
from typing import Optional
from ppadb.device import Device
from .base.chart import MonitorChart
from PySide6.QtCharts import QScatterSeries,QLineSeries
from perfcat.modules.profiler.fps import FpsSampler


class FpsMonitor(MonitorChart):
    def __init__(self, parent):
        super().__init__(
            parent,
            y_axis_name="FPS",
        )
        self.setObjectName("FPS")

        series = QLineSeries(self)
        self.create_series("FPS", series, lambda v:f"{v}")

        series = QScatterSeries(self)
        self.create_series("Jank-卡顿", series, lambda v:f"{v}次")

        series = QScatterSeries(self)
        self.create_series("BigJank-大卡顿", series, lambda v:f"{v}次")

        self.fps_sampler = None

        self._sample_data = {}

    def sample(self, sec: int, device: Device, package_name: str,subprocess:Optional[str]=None):
        if self.fps_sampler is None:
            self.fps_sampler = FpsSampler(device, package_name)
        data = self.fps_sampler.data
        self.add_point("FPS", sec, data["fps"])
        if data["jank"] > 0:
            self.add_point("Jank-卡顿", sec, data["jank"])

        if data["big_jank"] > 0:
            self.add_point("BigJank-大卡顿", sec, data["big_jank"])

        self._sample_data[sec] = data

    def reset_series_data(self):
        self.fps_sampler = None
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
        for sec, data_table in data.items():
            fps = data_table["fps"]
            jank_value = data_table['jank']
            big_jank_value = data_table['big_jank']

            if fps:
                self.add_point("FPS", int(sec), fps)

            if jank_value:
                self.add_point("Jank-卡顿", int(sec), jank_value)

            if big_jank_value:
                self.add_point("BigJank-大卡顿", int(sec), big_jank_value)

            self.flush()
