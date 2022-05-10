from .base import MonitorChart
from .cpu_monitor import CpuMonitor
from .mem_monitor import MemMonitor

register: list[MonitorChart] = [CpuMonitor, MemMonitor]
