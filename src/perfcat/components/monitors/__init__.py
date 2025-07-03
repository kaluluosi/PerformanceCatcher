"""
author:        kaluluosi111 <kaluluosi@gmail.com>
date:          2025-07-04 00:15:39
Copyright © Kaluluosi All rights reserved
"""

from perfcat.components.profiler import MonitorCard
from .cpu_monitor import CPUMonitorCard
from .memery_monitor import MemoryTotalPSSMonitorCard
from .battery_monitor import BatteryLevelMonitorCard, BatterymAhMonitorCard
from .fps_monitor import FPSMonitorCard
from .temperature_monitor import TemperatureMonitorCard
from .traffic_monitor import TrafficMonitorCard

__all__ = [
    "CPUMonitorCard",
    "MemoryTotalPSSMonitorCard",
    "BatteryLevelMonitorCard",
    "BatterymAhMonitorCard",
    "FPSMonitorCard",
    "TemperatureMonitorCard",
    "TrafficMonitorCard",
]

monitor_factory_map: dict[str, type[MonitorCard]] = {
    CPUMonitorCard.title: CPUMonitorCard,
    MemoryTotalPSSMonitorCard.title: MemoryTotalPSSMonitorCard,
    BatteryLevelMonitorCard.title: BatteryLevelMonitorCard,
    BatterymAhMonitorCard.title: BatterymAhMonitorCard,
    FPSMonitorCard.title: FPSMonitorCard,
    TemperatureMonitorCard.title: TemperatureMonitorCard,
    TrafficMonitorCard.title: TrafficMonitorCard,
}
