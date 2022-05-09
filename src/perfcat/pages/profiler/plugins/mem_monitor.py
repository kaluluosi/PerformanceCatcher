from ppadb.device import Device
from .base.chart import MonitorChart
from .top_util import top_to_dict
from .cpu_normalize import normalize


class MemMonitor(MonitorChart):
    def __init__(self, parent=None):
        super().__init__(
            series_names=["Total Mem", "App Mem"],
            formatter={},
            y_axis_name="MEM",
            parent=parent,
        )
        self.pid = None

    def tick(self, sec: int, device: Device, package_name: str):
        pass
