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


class TempMonitor(MonitorChart):
    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            series_names=["CPU温度"], formatter={}, y_axis_name="℃", parent=parent
        )

    def sample(self, sec: int, device: Device, package_name: str):

        c_temp = int(device.shell("cat /sys/class/thermal/thermal_zone0/temp")) / 1000
        self.add_point("CPU温度", sec, c_temp)
