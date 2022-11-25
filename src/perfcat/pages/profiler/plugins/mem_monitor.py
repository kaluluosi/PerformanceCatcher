from ppadb.device import Device
from .base.chart import MonitorChart
from PySide6.QtCharts import QLineSeries

class MemMonitor(MonitorChart):
    def __init__(self, parent=None):
        super().__init__(
            y_axis_name="MEM",
            parent=parent,
        )
        self.setObjectName("Memory")

        self._sample_data ={}

        self.create_series("PSS", QLineSeries(self),lambda v: f"{v}MB")
        self.create_series("PrivateDirty", QLineSeries(self),lambda v: f"{v}MB")
        self.create_series("PrivateClean", QLineSeries(self),lambda v: f"{v}MB")
        self.create_series("SwappedDirty", QLineSeries(self),lambda v: f"{v}MB")
        self.create_series("HeapSize", QLineSeries(self),lambda v: f"{v}MB")
        self.create_series("HeapAlloc", QLineSeries(self),lambda v: f"{v}MB")
        self.create_series("HeapFree", QLineSeries(self),lambda v: f"{v}MB")

    def reset_series_data(self):
        self._sample_data = {}
        return super().reset_series_data()


    def sample(self, sec: int, device: Device, package_name: str):

        mem_info = device.get_meminfo(package_name)

        self._sample_data[sec] = {
            "PSS":round(mem_info.pss / 1024,2),
            "PrivateDirty":round(mem_info.private_dirty / 1024,2),
            "PrivateClean": round(mem_info.private_clean/ 1024,2),
            "SwappedDirty": round(mem_info.swapped_dirty/ 1024,2),
            "HeapSize": round(mem_info.heap_size / 1024,2),
            "HeapAlloc": round(mem_info.heap_alloc / 1024,2),
            "HeapFree": round(mem_info.heap_free / 1024,2),
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
                self.add_point(k,int(sec),v)
            self.flush()
