from perfcat.components.profiler import ControlCard
from perfcat.services.ios_profiler_service import IOSProfilerService

from nicegui import ui


class ProfilerSettingCard(ControlCard):
    def __init__(self) -> None:
        super().__init__()

        with self:

            with self.session():
                self.device_select = (
                    ui.select([],label="选择设备")
                    .props("dense spellcheck=false clearable")
                    .classes("w-full flex-1")
                )

                with self.device_select.add_slot("prepend"):
                    ui.icon("apple")

        self._refresh_devices()


    def _refresh_devices(self):
        self.device_select.set_options(IOSProfilerService.devices)