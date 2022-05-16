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
from ppadb.device import Device
from .base.chart import MonitorChart
from perfcat.modules.profiler.fps import FpsSampler


class FpsMonitor(MonitorChart):
    def __init__(self, parent):
        super().__init__(
            parent,
            series_names=["FPS", "Jank-卡顿", "BigJank-大卡顿"],
            formatter={
                "Jank-卡顿": lambda v: f"{v}次",
                "BigJank-大卡顿": lambda v: f"{v}次",
            },
            y_axis_name="FPS",
        )
        self.fps_sampler = None

    def sample(self, sec: int, device: Device, package_name: str):
        if self.fps_sampler is None:
            self.fps_sampler = FpsSampler(device, package_name)
        data = self.fps_sampler.data
        self.add_point("FPS", sec, data["fps"])
        self.add_point("Jank-卡顿", sec, data["jank"])
        self.add_point("BigJank-大卡顿", sec, data["big_jank"])

    def reset_series_data(self):
        self.fps_sampler = None
        return super().reset_series_data()
