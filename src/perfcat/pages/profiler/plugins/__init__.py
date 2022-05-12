from .base import MonitorChart
from .cpu_monitor import CpuMonitor
from .mem_monitor import MemMonitor
from .temp_monitor import TempMonitor

register: list[MonitorChart] = [CpuMonitor, MemMonitor, TempMonitor]
