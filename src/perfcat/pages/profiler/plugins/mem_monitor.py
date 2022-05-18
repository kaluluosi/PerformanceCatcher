from ppadb.device import Device
from .base.chart import MonitorChart


class MemMonitor(MonitorChart):
    def __init__(self, parent=None):
        super().__init__(
            series_names=[
                "pss",
                "private dirty",
                "private clean",
                "swapped dirty",
                "heap size",
                "heap alloc",
                "heap free",
            ],
            formatter={
                "pss": lambda v: f"{v}MB",
                "private dirty": lambda v: f"{v}MB",
                "private clean": lambda v: f"{v}MB",
                "swapped dirty": lambda v: f"{v}MB",
                "heap size": lambda v: f"{v}MB",
                "heap alloc": lambda v: f"{v}MB",
                "heap free": lambda v: f"{v}MB",
            },
            y_axis_name="MEM",
            parent=parent,
        )
        self.setObjectName("Memory")

    def sample(self, sec: int, device: Device, package_name: str):

        mem_info = device.get_meminfo(package_name)

        self.add_point("pss", sec, mem_info.pss / 1024)
        self.add_point("private dirty", sec, mem_info.private_dirty / 1024)
        self.add_point("private clean", sec, mem_info.private_clean / 1024)
        self.add_point("swapped dirty", sec, mem_info.swapped_dirty / 1024)
        self.add_point("heap size", sec, mem_info.heap_size / 1024)
        self.add_point("heap alloc", sec, mem_info.heap_alloc / 1024)
        self.add_point("heap free", sec, mem_info.heap_free / 1024)
