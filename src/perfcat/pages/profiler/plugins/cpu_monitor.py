#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   cpu_monitor.py
@Time    :   2022/05/09 18:20:33
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   emm...

获取cpu使用率和app cpu使用率的途径有很多
[1] 通过解析top命令
[2] 通过解析 proc/stat， top其实也是解析proc/stat
[2] 通过dumpsys cpuinfo，但是dumpsys不是实时的，他是间隔采样的

[1] github上的很多开源项目都是用top命令解析来获取cpu使用率，这个方法最简单，所以我还是决定用这个
"""

# here put the import lib

import logging

from perfcat.modules.profiler.cpu import get_all_cpu_cur_freq, normalize_factor, get_all_cpu_state
from ppadb.device import Device
from .base.chart import MonitorChart

from ppadb.device import Device
from ppadb.plugins.device.cpustat import TotalCPUStat

log = logging.getLogger(__name__)


def __cpu_max_freq(dev: Device) -> list:
    count = dev.cpu_count()
    freq = []
    for index in range(count):
        cmd_root = f"cat /sys/devices/system/cpu/cpu{index}/cpufreq"
        max = dev.shell(f"{cmd_root}/cpuinfo_max_freq")

        freq.append(int(max))

    return freq


class CpuMonitor(MonitorChart):
    def __init__(self, parent=None):
        super().__init__(
            series_names=["TotalCPU(标准化)", "AppCPU(标准化)"],
            formatter={"TotalCPU(标准化)": lambda v: f"{v}%", "AppCPU(标准化)": lambda v: f"{v}%"},
            y_axis_name="%",
            parent=parent,
        )
        self.setObjectName("CPU")
        self.pid = None
        self.last_total_cpu_state = None
        self.last_pid_cpu_state = None
        self.last_all_cpu_state = None
        
        self.cpu_count = None

        self._sample_data = {}

    def reset_series_data(self):
        self.pid = None
        self.last_total_cpu_state = None
        self.last_pid_cpu_state = None
        self.last_all_cpu_state = None
        self._sample_data = {}
        return super().reset_series_data()

    def sample(self, sec: int, device: Device, package_name: str):
        # 我们直接取top的数据，因此cpu占用是未规范化的
        # 为规范化的CPU占用值会导致一个问题：
        # 当你在A设备上测试采集到的峰值，跟B设备上测试采集到的峰值不一致。
        # 可能A设备的平均峰值更高

        pid_str = device.shell(f"pidof {package_name}")
        if pid_str:
            self.pid = int(pid_str)
        else:
            self.pid = None

        # 归一化因子，归一化CPU占用
        # 参考：https://blog.gamebench.net/measuring-cpu-usage-in-mobile-devices
        factor = normalize_factor(device)

        # 参考 SoloPi的算法

        # 采集cpu总占用
        total_cpu_usage = 0
        total_cpu_usage_normalized = 0
        if self.last_total_cpu_state is None:
            self.last_total_cpu_state = device.get_total_cpu()
        else:
            cur_total_cpu = device.get_total_cpu()
            cpu_diff:TotalCPUStat = cur_total_cpu - self.last_total_cpu_state
            total_cpu_usage = 100 * (cpu_diff.user + cpu_diff.system) / cpu_diff.total()
            total_cpu_usage = round(total_cpu_usage,2)
            self.last_total_cpu_state = cur_total_cpu

        total_cpu_usage_normalized = round(total_cpu_usage * factor,2)
        self.add_point("TotalCPU(标准化)", sec, total_cpu_usage_normalized)


        # 采集pid占用
        app_cpu_usage = 0
        app_cpu_usage_normalized = 0
        if self.pid is None:  # 如果app没启动，那么就记录0占用
            self.add_point("AppCPU(标准化)", sec, 0)
        else:
            # 启动了就从top里面找
            cur_pid_cpu = device.get_pid_cpu(self.pid)
            if self.last_pid_cpu_state is None:
                self.last_pid_cpu_state = cur_pid_cpu
            else:
                pid_diff = cur_pid_cpu - self.last_pid_cpu_state
                app_cpu_usage = 100 * pid_diff.total() / cpu_diff.total()
                app_cpu_usage = round(app_cpu_usage,2)
                self.last_pid_cpu_state = cur_pid_cpu
            app_cpu_usage_normalized = round(app_cpu_usage*factor,2)
            self.add_point("AppCPU(标准化)", sec, app_cpu_usage_normalized)

        # 采集所有cpu占用
        self.cpu_count = self.cpu_count or device.cpu_count()
        all_cpu_cur_freq = get_all_cpu_cur_freq(device)
        all_cpu_usage = {i:0 for i in range(self.cpu_count)}
        if self.last_all_cpu_state is None:
            self.last_all_cpu_state = get_all_cpu_state(device)
        else:
            all_cpu_state = get_all_cpu_state(device)
            for index, cpu_state in all_cpu_state.items():
                last_cpu_state = self.last_all_cpu_state[index]
                cpu_diff:TotalCPUStat = cpu_state-last_cpu_state
                cpu_usage = 100* (cpu_diff.user+cpu_diff.system)/cpu_diff.total()
                all_cpu_usage[index] = round(cpu_usage,2)
            self.last_all_cpu_state = all_cpu_state

        self._sample_data[sec] = {
            "AppCPU": app_cpu_usage,
            "TotalCPU":total_cpu_usage,
            "AppCPUNormalized":app_cpu_usage_normalized,
            "TotalCPUNormalized":total_cpu_usage_normalized,
            "AllCPUCurFreq": all_cpu_cur_freq,
            "AllCPUUsage":all_cpu_usage,
            "AllCPUUsageNormalized":{index:round(usage* factor,2) for index, usage in all_cpu_usage.items()}
        }



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
            app_cpu_value = data_table["AppCPUNormalized"]
            total_cpu_value = data_table["TotalCPUNormalized"]

            if app_cpu_value:
                self.add_point("AppCPU(标准化)", int(sec), app_cpu_value)

            if total_cpu_value:
                self.add_point("TotalCPU(标准化)", int(sec), total_cpu_value)

            self.flush()
