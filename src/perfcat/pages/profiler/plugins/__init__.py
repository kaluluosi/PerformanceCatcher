from .base import MonitorChart
from .cpu_monitor import CpuMonitor

register: list[MonitorChart] = [CpuMonitor]
