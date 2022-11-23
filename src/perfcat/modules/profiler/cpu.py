#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   cpu.py
@Time    :   2022/05/10 10:33:37
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   emm...
参考：
    [1] https://blog.gamebench.net/measuring-cpu-usage-in-mobile-devices
    [2] https://github.com/alipay/SoloPi/blob/master/src/shared/src/main/cpp/cpu_usage.c
"""

# here put the import lib

import re
from ppadb.device import Device
from ppadb.plugins.device.cpustat import TotalCPUStat
from ppadb.client import Client




def get_all_cpu_freq(dev:Device, filename) -> list:
    count = dev.cpu_count()
    values = {}

    for index in range(count):
        CMD_ROOT = f"cat /sys/devices/system/cpu/cpu{index}/cpufreq"
        value = dev.shell(f"{CMD_ROOT}/{filename}")
        values[index] = int(value)/1024

    return values

def get_all_cpu_max_freq(dev: Device) -> list:
    return get_all_cpu_freq(dev, "cpuinfo_max_freq")

def get_all_cpu_cur_freq(dev:Device) -> list:
    return get_all_cpu_freq(dev, "scaling_cur_freq")

def normalize_factor(device: Device):

    # 合计所有CPU最大频率
    max_freq = get_all_cpu_max_freq(device)
    total_max_freq = sum(max_freq.values())

    # 找出所有在在线的CPU
    online_cmd = "cat /sys/devices/system/cpu/online"
    online = device.shell(online_cmd)
    count = int(online.strip().split("-")[1])

    # 合计所有在线CPU的当前频率
    cur_freq_sum = 0
    all_cur_freq = get_all_cpu_cur_freq(device)
    cur_freq_sum = sum([all_cur_freq[i] for i in range(count)])

    return cur_freq_sum / total_max_freq



def get_all_cpu_state(device:Device) -> list[TotalCPUStat]:
    pattern = re.compile(
        "cpu(\d)\s+([\d]+)\s([\d]+)\s([\d]+)\s([\d]+)\s([\d]+)\s([\d]+)\s([\d]+)\s([\d]+)\s([\d]+)\s([\d]+)\s"
    )
    cpu_state_info = device.shell("cat /proc/stat")
    matches = pattern.findall(cpu_state_info)

    all_cpu_state = {
        int(group[0]):TotalCPUStat(*map(lambda x:int(x),group[1:])) for group in matches
    }

    return all_cpu_state
