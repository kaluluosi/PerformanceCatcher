from typing import List
from .base import MonitorChart
from .cpu_monitor import CpuMonitor
from .mem_monitor import MemMonitor
from .temp_monitor import TempMonitor
from .fps_monitor import FpsMonitor
from .frametime_monitor import FrameTimeMonitor

register: List[MonitorChart] = [
    FpsMonitor,
    CpuMonitor,
    MemMonitor,
    FrameTimeMonitor,
    TempMonitor,
]
