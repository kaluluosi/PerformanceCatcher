# here put the import lib
from ppadb.device import Device
from .base.chart import MonitorChart
from perfcat.modules.profiler.fps import FpsSampler


class FrameTimeMonitor(MonitorChart):
    def __init__(self, parent):
        super().__init__(
            parent,
            series_names=["FrameTime"],
            formatter={"FrameTime": lambda v: f"{v}ms"},
            y_axis_name="FrameTime",
        )
        self.fps_sampler = None

    def sample(self, sec: int, device: Device, package_name: str):
        if self.fps_sampler is None:
            self.fps_sampler = FpsSampler(device, package_name)

        self.add_point("FrameTime", sec, self.fps_sampler.data["frametime"])

    def reset_series_data(self):
        self.fps_sampler = None
        return super().reset_series_data()
