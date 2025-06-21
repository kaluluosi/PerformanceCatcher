import re
import random
from contextlib import contextmanager
from typing import cast
from nicegui import app, ui
from pydantic import BaseModel, Field, RootModel
from perfcat.components.layout import Page
from perfcat.services.android_profiler_service import AndroidProfielerService
from perfcat.utils import notify


class Drawer(ui.drawer):
    def __init__(self) -> None:
        super().__init__(side="right", value=True, elevated=True)
        self.bind_value(app.storage.general, "android_profiler_drawer_expand")
        self.classes("p-0")
        self.props("width=400")

        with ui.page_sticky(position="top-right", y_offset=100).style("z-index:2000"):
            self.btn_expand = ui.button(
                icon="arrow_left", on_click=lambda: self.toggle()
            )
            self.btn_expand.classes("pl-2 pr-2 pt-8 pb-8 w-1")
            self.btn_expand.style("border-radius:3px 0px 0px 3px;")

        with self:
            with ui.tabs() as tabs:
                self.device_panel = ui.tab("设备面板")
                self.monitor_panel = ui.tab("监控面板")

            with ui.tab_panels(tabs, value=self.device_panel).classes("w-full"):
                self.device_tab_panel = DeviceTabPanel(self.device_panel)
                self.monitor_tab_panel = MonitorTabPanel(self.monitor_panel)


class DeviceTabPanel(ui.tab_panel):
    def __init__(self, name: str | ui.tab) -> None:
        super().__init__(name)
        self.classes("w-full")
        with self:
            self.remote_connect_card = RemoteConnectCard()
            self.profiler_setting_card = ProfilerSettingCard()

    @contextmanager
    def _create_card(self):
        with ui.card().tight().classes("w-full"):
            with ui.card_section().classes("w-full"):
                with ui.row().classes("items-center w-full"):
                    yield

    def _ip_port_validation(self, v: str):
        # 正则表达式来识别 ip:port 格式，要兼容localhost:port
        pattern = re.compile(r"^((\d{1,3}\.){3}\d{1,3}|\blocalhost\b):(\d{1,5})$")
        if pattern.match(v):
            return None
        else:
            return "请输入正确的IP端口格式"


class ControlCard(ui.card):
    def __init__(self) -> None:
        super().__init__()
        self.tight()
        self.classes("w-full")

    @contextmanager
    def session(self):
        with ui.card_section().classes("w-full"):
            with ui.row().classes("items-center w-full"):
                yield

    @contextmanager
    def actions(self):
        with ui.card_actions().classes("w-full"):
            yield


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


class MonitorTabPanel(ui.tab_panel):
    def __init__(self, name: str | ui.tab) -> None:
        super().__init__(name)
        self.classes("w-full")


class SerieData(BaseModel):
    name: str
    type: str = "line"
    data: list[float] = Field(default_factory=list)


Series = RootModel[list[SerieData]]


class MonitorCard(ui.card):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.classes("w-full")

        self.title = title

        self._series: list[SerieData] = []

        with self:
            with ui.card_section().classes("w-full"):
                self.label_title = ui.label(title)
                ui.separator()

            with self:
                self.chart = ui.echart(
                    {
                        "legend": {"data": [], "orient": "vertical", "left": 10},
                        "grid": {
                            "left": "100px",
                            "right": "4%",
                            "top": "3%",
                            "bottom": "10%",
                            "containLabel": True,
                        },
                        "xAxis": {"type": "category"},
                        "yAxis": {"type": "value"},
                        "series": [],
                    }
                )

    @contextmanager
    def session(self):
        with ui.card_section().classes("w-full"):
            yield

    def craete_serie(self, name: str, type: str = "line"):
        seire = SerieData(name=name, type=type, data=[])
        self._series.append(seire)

    def _add_point(self, serie_name: str, value: float, type: str = "line"):
        for serie in self._series:
            if serie.name == serie_name:
                serie.data.append(value)
                return

        new_series = SerieData(name=serie_name, data=[value], type=type)
        self._series.append(new_series)

    def update_chart(self):
        self.chart.options["series"] = Series(self._series).model_dump()
        self.chart.options["legend"]["data"] = [serie.name for serie in self._series]
        self.chart.update()


class FPSMonitorCard(MonitorCard):
    def __init__(self) -> None:
        super().__init__("FPS")

        self.craete_serie("FPS")
        self.craete_serie("Jank")
        self.update_chart()

    def sample(self):
        self._add_point("FPS", random.randrange(0, 60))
        self._add_point("Jank", random.randrange(0, 60))
        self.update_chart()


class CPUMonitorCard(MonitorCard):
    def __init__(self) -> None:
        super().__init__("CPU")

        self.craete_serie("CPU")
        self.craete_serie("TotalCPU")
        self.update_chart()


class MemoryMonitorCard(MonitorCard):
    def __init__(self) -> None:
        super().__init__("Memory")
        self.craete_serie("Memory")
        self.update_chart()


class TemperatureMonitorCard(MonitorCard):
    def __init__(self) -> None:
        super().__init__("Temperature")
        self.craete_serie("体感温度")
        self.craete_serie("CPU温度")
        self.craete_serie("电池温度")
        self.update_chart()


class AndroidProfilerPage(Page):
    def __init__(self) -> None:
        super().__init__("/android_profiler", title="安卓性能")

        self.monitor_list = [
            {"name": "FPS", "description": "帧率情况"},
            {"name": "CPU", "description": "CPU使用情况"},
            {"name": "MEMORY", "description": "内存使用情况"},
            {"name": "TEMPERATURE", "description": "温度情况"},
        ]

        self.monitor_register = {
            "FPS": FPSMonitorCard,
            "CPU": CPUMonitorCard,
            "MEMORY": MemoryMonitorCard,
            "TEMPERATURE": TemperatureMonitorCard,
        }

        self.monitors = {}

    async def render(self):
        self.drawer = Drawer()
        with self.drawer.monitor_tab_panel:
            with ui.card().classes("w-full"):
                with ui.row().classes("items-center"):
                    ui.icon("info").props("size=xs color=blue")
                    ui.label("选择要监控采集的性能参数")
            self.table_monitor = (
                ui.table(
                    columns=[
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
                    ],
                    rows=self.monitor_list,
                    row_key="name",
                )
                .classes("w-full")
                .props("selection=multiple hide-selected-banner")
            )
            self.table_monitor.selected[:] = self.monitor_list[:4]

        self.monitor_view()

    def monitor_view(self):
        for monitor_data in self.table_monitor.selected:
            monitor: MonitorCard = self.monitor_register[monitor_data["name"]]()
            monitor.bind_visibility_from(
                self.table_monitor,
                "selected",
                backward=lambda e, monitor_data=monitor_data: monitor_data in e,
            )
            self.monitors[monitor_data["name"]] = monitor

    def selected_monitors(self):
        return self.table_monitor.selected


AndroidProfilerPage()
