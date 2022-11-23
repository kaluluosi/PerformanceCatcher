from ppadb.device import Device
from .base.chart import MonitorChart


class MemMonitor(MonitorChart):
    def __init__(self, parent=None):
        super().__init__(
            series_names=[
                "PSS",
                "PrivateDirty",
                "PrivateClean",
                "SwappedDirty",
                "HeapSize",
                "HeapAlloc",
                "HeapFree",
            ],
            formatter={
                "PSS": lambda v: f"{v}MB",
                "PrivateDirty": lambda v: f"{v}MB",
                "PrivateClean": lambda v: f"{v}MB",
                "SwappedDirty": lambda v: f"{v}MB",
                "HeapSize": lambda v: f"{v}MB",
                "HeapAlloc": lambda v: f"{v}MB",
                "HeapFree": lambda v: f"{v}MB",
            },
            y_axis_name="MEM",
            parent=parent,
        )
        self.setObjectName("Memory")

        self._sample_data ={}

    def reset_series_data(self):
        self._sample_data = {}
        return super().reset_series_data()


    def sample(self, sec: int, device: Device, package_name: str):

        mem_info = device.get_meminfo(package_name)

        self._sample_data[sec] = {
            "PSS":mem_info.pss / 1024,
            "PrivateDirty":mem_info.private_dirty / 1024,
            "PrivateClean": mem_info.private_clean/ 1024,
            "SwappedDirty": mem_info.swapped_dirty/ 1024,
            "HeapSize": mem_info.heap_size / 1024,
            "HeapAlloc": mem_info.heap_alloc / 1024,
            "HeapFree": mem_info.heap_free / 1024,
        }

        for k,v in self._sample_data[sec].items():
            self.add_point(k, sec, v)

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
            for k, v in data_table.items():
                self.add_point(k,sec,v)
