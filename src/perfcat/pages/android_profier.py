import re
import random
from typing import cast
from nicegui import ui
from nicegui.observables import ObservableDict
from perfcat.components.layout import Page
from perfcat.components.profiler import ControlCard
from perfcat.components.profiler import Drawer
from perfcat.components.profiler import MonitorCard
from perfcat.services.android_profiler_service import AndroidProfielerService
from perfcat.utils import notify


class AndroidProfilerDrawer(Drawer):
    def __init__(self) -> None:
        super().__init__()

        with self:
            with self.create_tabs():
                self.tab_device = ui.tab("设备")
                self.tab_monitor = ui.tab("监控")

            with self.create_tab_panels():
                self.tab_panels.value = self.tab_device
                self.panel_device = DeviceTabPanel(self.tab_device)
                self.panel_monitor = MonitorTabPanel(self.tab_monitor)


class DeviceTabPanel(ui.tab_panel):
    def __init__(self, name: str | ui.tab) -> None:
        super().__init__(name)
        self.classes("w-full")
        with self:
            self.remote_connect_card = RemoteConnectCard()
            self.profiler_setting_card = ProfilerSettingCard()


class RemoteConnectCard(ControlCard):
    def __init__(self) -> None:
        super().__init__()
        with self:
            with self.session():
                self.input_address = (
                    ui.input(
                        "远程连接",
                        placeholder="e.g 192.168.1.100:5555",
                        validation=self._ip_port_validation,
                    )
                    .classes("flex-1")
                    .props("dense")
                )

                with self.input_address.add_slot("prepend"):
                    ui.icon("wifi")

                self.btn_connect = ui.button(icon="add").props("dense")

    def _ip_port_validation(self, v: str):
        pattern = re.compile(r"^((\d{1,3}\.){3}\d{1,3}|\blocalhost\b):(\d{1,5})$")
        if pattern.match(v):
            return None
        else:
            return "请输入正确的IP端口格式"


class ProfilerSettingCard(ControlCard):
    def __init__(self) -> None:
        super().__init__()
        with self:
            with self.session():
                self.device_select = (
                    ui.select([], label="选择设备")
                    .props("dense")
                    .classes("w-full flex-1")
                )

                with self.device_select.add_slot("prepend"):
                    ui.icon("adb")

                self.btn_tcpip = ui.button(icon="wifi").props("dense")

                with self.btn_tcpip:
                    ui.tooltip("开启无线连接\n(adb tcpip:5555)")

                self.app_select = (
                    ui.select([], label="选择APP", with_input=True)
                    .props("dense")
                    .classes("w-full")
                    .props("dense")
                )
                self.app_select.bind_enabled_from(
                    self.device_select, "value", backward=lambda v: v is not None
                )
                with self.app_select.add_slot("prepend"):
                    ui.icon("apps")

                self.process_select = (
                    ui.select([], label="选择进程").classes("w-full").props("dense")
                )
                self.process_select.bind_enabled_from(
                    self.app_select, "value", backward=lambda v: v is not None
                )
                with self.process_select.add_slot("prepend"):
                    ui.icon("wysiwyg")

                with ui.row().classes("items-center w-full justify-end"):
                    self.btn_record = (
                        ui.button("开始采集", icon="lens")
                        .props("dense color=red ")
                        .classes("p-2")
                    )


class FPSMonitorCard(MonitorCard):
    title = "FPS"
    description = "帧率"

    def __init__(self) -> None:
        super().__init__()

        self.craete_serie("FPS")
        self.craete_serie("Jank")
        self.update_chart()

    def sample(self):
        self._add_point("FPS", random.randrange(0, 60))
        self._add_point("Jank", random.randrange(0, 60))
        self.update_chart()


class CPUMonitorCard(MonitorCard):
    title = "CPU"
    description = "CPU使用率"

    def __init__(self) -> None:
        super().__init__()

        self.craete_serie("CPU")
        self.craete_serie("TotalCPU")
        self.update_chart()

    def sample(self):
        self._add_point("CPU", random.randrange(0, 100))
        self._add_point("TotalCPU", random.randrange(0, 100))
        self.update_chart()


class MemoryMonitorCard(MonitorCard):
    title = "Memory"
    description = "内存使用情况"

    def __init__(self) -> None:
        super().__init__()
        self.craete_serie("Memory")
        self.update_chart()

    def sample(self):
        self._add_point("Memory", random.randrange(0, 100))
        self.update_chart()


class TemperatureMonitorCard(MonitorCard):
    title = "Temperature"
    description = "设备温度情况"

    def __init__(self) -> None:
        super().__init__()
        self.craete_serie("体感温度")
        self.craete_serie("CPU温度")
        self.craete_serie("电池温度")
        self.update_chart()

    def sample(self):
        self._add_point("体感温度", random.randrange(0, 100))
        self._add_point("CPU温度", random.randrange(0, 100))
        self._add_point("电池温度", random.randrange(0, 100))
        self.update_chart()


class MonitorTabPanel(ui.tab_panel):
    def __init__(self, name: str | ui.tab) -> None:
        super().__init__(name)

        self._monitors_registers = ObservableDict()
        self._monitors_registers.on_change(self._on_monitors_registers_change)

        with self:
            with ControlCard().classes("p-4"):
                with ui.row().classes("items-center"):
                    ui.icon("info").props("size=xs color=blue")
                    ui.label("选择要监控采集的性能参数")

            self.create_table()  # type: ignore

    def _on_monitors_registers_change(self, e):
        self.create_table.refresh()

    def register_monitor(self, name: str, description: str):
        self._monitors_registers[name] = description

    @ui.refreshable
    def create_table(self):
        columns = [
            {
                "name": "name",
                "label": "名称",
                "field": "name",
                "required": True,
                "align": "left",
            },
            {
                "name": "description",
                "label": "描述",
                "field": "description",
                "required": True,
                "align": "left",
            },
        ]
        rows = [
            {"name": name, "description": description}
            for name, description in self._monitors_registers.items()
        ]
        self.table = (
            ui.table(columns=columns, rows=rows, row_key="name")
            .classes("w-full")
            .props("selection=multiple hide-selected-banner")
        )
        self.table.selected = rows

    def monitors(self):
        pass


class AndroidProfilerPage(Page):
    def __init__(self) -> None:
        super().__init__("/android_profiler", title="安卓性能")

        self.monitor_registers = {
            "FPS": FPSMonitorCard,
            "CPU": CPUMonitorCard,
            "Memory": MemoryMonitorCard,
            "Temperature": TemperatureMonitorCard,
        }

        self.monitors: list[MonitorCard] = []

    async def render(self):
        self.drawer = AndroidProfilerDrawer()

        self.drawer.panel_device.profiler_setting_card.btn_record.on_click(
            self.start_record
        )

        for name, monitor_card in self.monitor_registers.items():
            self.drawer.panel_monitor.register_monitor(name, monitor_card.description)

        await self.create_monitors()

    async def create_monitors(self):
        for name, monitor_card in self.monitor_registers.items():
            monitor: MonitorCard = monitor_card()
            self.monitors.append(monitor)
            monitor.bind_visibility_from(
                self.drawer.panel_monitor.table,
                "selected",
                backward=lambda selected, name=name: any(
                    [name == s["name"] for s in selected]
                ),
            )

    def start_record(self):
        ui.timer(1, self._on_sample)

    def _on_sample(self):
        for monitor in self.monitors:
            if monitor.visible:
                monitor.sample()


AndroidProfilerPage()
