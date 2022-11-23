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


from ppadb.device import Device
from perfcat.logger.get_time import get_time
from .base.chart import MonitorChart

from ppadb.device import Device
from ppadb.client import Client
import time
import logging

log = logging.getLogger(__name__)


def __cpu_max_freq(dev: Device) -> list:
    count = dev.cpu_count()
    freq = []
    for index in range(count):
        cmd_root = f"cat /sys/devices/system/cpu/cpu{index}/cpufreq"
        max = dev.shell(f"{cmd_root}/cpuinfo_max_freq")

        freq.append(int(max))

    return freq


def normalize(device: Device) -> float:
    """
    获取设备的CPU归一化因子

    Args:
        device (Device): 设备对象

    Returns:
        float : 因子
    """

    # 合计所有CPU最大频率
    max_freq = __cpu_max_freq(device)
    total_max_freq = sum(max_freq)

    # 找出所有在在线的CPU
    online_cmd = "cat /sys/devices/system/cpu/online"
    online = device.shell(online_cmd)
    count = int(online.strip().split("-")[1])

    # 合计所有在线CPU的当前频率
    cur_freq_sum = 0
    for index in range(count):
        cmd_cur_freq = (
            f"cat /sys/devices/system/cpu/cpu{index}/cpufreq/scaling_cur_freq"
        )
        cur_freq = device.shell(cmd_cur_freq)
        cur_freq_sum += int(cur_freq)

    return cur_freq_sum / total_max_freq


class CpuMonitor(MonitorChart):
    def __init__(self, parent=None):
        super().__init__(
            series_names=["CPU", "AppCPU"],
            formatter={"CPU": lambda v: f"{v}%", "AppCPU": lambda v: f"{v}%"},
            y_axis_name="%",
            parent=parent,
        )
        self.setObjectName("CPU")
        self.pid = None
        self.last_total_cpu = None
        self.last_pid_cpu = None

    def reset_series_data(self):
        self.pid = None
        self.last_total_cpu = None
        self.last_pid_cpu = None
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
        factor = normalize(device)

        # 参考 SoloPi的算法

        # 采集cpu总占用
        total_cpu = 0
        if self.last_total_cpu is None:
            self.last_total_cpu = device.get_total_cpu()
        else:
            cur_total_cpu = device.get_total_cpu()
            cpu_diff = cur_total_cpu - self.last_total_cpu
            total_cpu = 100 * (cpu_diff.total() - cpu_diff.idle) / cpu_diff.total()
            self.last_total_cpu = cur_total_cpu

        self.add_point("CPU", sec, total_cpu * factor)

        # 采集pid占用
        if self.pid is None:  # 如果app没启动，那么就记录0占用
            self.add_point("AppCPU", sec, 0)
        else:
            # 启动了就从top里面找
            pid_cpu = 0
            cur_pid_cpu = device.get_pid_cpu(self.pid)
            if self.last_pid_cpu is None:
                self.last_pid_cpu = cur_pid_cpu
            else:
                pid_diff = cur_pid_cpu - self.last_pid_cpu
                pid_cpu = 100 * pid_diff.total() / cpu_diff.total()
                self.last_pid_cpu = cur_pid_cpu
            self.add_point("AppCPU", sec, pid_cpu * factor)
