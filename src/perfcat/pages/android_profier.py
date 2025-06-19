from contextlib import contextmanager
import re
from typing import cast
from nicegui import app, ui, events
from perfcat.components.layout import Page
from perfcat.services.android_profiler_service import AndroidProfielerService
from perfcat.utils import notify

columns = [
    {
        "name": "name",
        "label": "属性",
        "field": "name",
        "required": True,
        "align": "left",
    },
    {"name": "value", "label": "值", "field": "value", "sortable": False},
]
rows = [
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 21},
    {"name": "Carol", "age": None},  # 假设 Carol 的年龄未知，可以设置为 None
]


class AndroidProfilerPage(Page):
    def __init__(self) -> None:
        super().__init__("/android_profiler", title="安卓性能")

    async def render(self):
        self.drawer = Drawer()


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
            self.btn_expand.classes("pl-4 pr-4 pt-4 pb-4 w-1")
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
    def sessions(self):
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
            with self.sessions():
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
            with self.sessions():
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
        with self:
            ui.label("敬请期待")


AndroidProfilerPage()
