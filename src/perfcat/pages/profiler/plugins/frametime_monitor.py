# here put the import lib
from typing import Optional
from ppadb.device import Device
from .base.chart import MonitorChart
from perfcat.modules.profiler.fps import FpsSampler
from PySide6.QtCharts import QLineSeries

class FrameTimeMonitor(MonitorChart):
    def __init__(self, parent):
        super().__init__(
            parent,
            y_axis_name="FrameTime",
        )
        self.setObjectName("FrameTime")
        self.fps_sampler = None

        self._sample_data = {}

        self.create_series("FrameTime", QLineSeries(self), lambda v:f"{v}ms")

    def sample(self, sec: int, device: Device, package_name: str,subprocess:Optional[str]=None):
        if self.fps_sampler is None:
            self.fps_sampler = FpsSampler(device, package_name)

        data = self.fps_sampler.data
        frametimes = data["*frametimes"]
        frametime = sum(frametimes)/len(frametimes)

        self.add_point("FrameTime", sec, frametime)

    def reset_series_data(self):
        self.fps_sampler = None
        self._sample_data = {}
        return super().reset_series_data()

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
            frametimes = data_table["*frametimes"]
            frametime = sum(frametimes)/len(frametimes)
            self.add_point("FrameTime", int(sec), frametime)
            
            self.flush()
