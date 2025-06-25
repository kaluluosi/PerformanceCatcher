import asyncio
import datetime
import re
from typing import cast
from nicegui import Client, ui
from nicegui.events import ValueChangeEventArguments, ClickEventArguments
from nicegui.observables import ObservableDict
from perfcat.components.layout import Page
from perfcat.components.profiler import ControlCard
from perfcat.components.profiler import Drawer
from perfcat.components.profiler import MonitorCard
from perfcat.pages.android_profiler.cpu_monitor import CPUMonitorCard
from perfcat.pages.android_profiler.memery_monitor import MemoryTotalPSSMonitorCard
from perfcat.pages.android_profiler.temperature_monitor import TemperatureMonitorCard
from perfcat.pages.android_profiler.fps_monitor import FPSMonitorCard
from perfcat.services import AndroidProfielerService,RecordService
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

                self.btn_connect.on_click(self._on_btn_connect_click)

    def _ip_port_validation(self, v: str):
        pattern = re.compile(r"^((\d{1,3}\.){3}\d{1,3}|\blocalhost\b):(\d{1,5})$")
        if pattern.match(v):
            return None
        else:
            return "请输入正确的IP端口格式"
        
    async def _on_btn_connect_click(self):
        ip,port = self.input_address.value.split(":")
        res = await AndroidProfielerService.remote_connect(ip,int(port))
        if res:
            notify(f"连接成功: {ip}:{port}", color="green")
        else:
            notify(f"连接失败: {ip}:{port}", color="red")


class ProfilerSettingCard(ControlCard):
    def __init__(self) -> None:
        super().__init__()
        with self:
            with self.session():
                self.device_select = (
                    ui.select([], label="选择设备")
                    .props("dense spellcheck=false")
                    .classes("w-full flex-1")
                )

                with self.device_select.add_slot("prepend"):
                    ui.icon("adb")

                self.btn_tcpip = ui.button(icon="wifi").props("dense")

                with self.btn_tcpip:
                    ui.tooltip("开启无线连接\n(adb tcpip:5555)")

                self.app_select = (
                    ui.select([], label="选择APP", with_input=True)
                    .props("dense spellcheck=false")
                    .classes("w-full")
                )
                self.app_select.bind_enabled_from(
                    self.device_select, "value", backward=lambda v: v is not None
                )
                with self.app_select.add_slot("prepend"):
                    ui.icon("apps")

                self.process_select = (
                    ui.select([], label="选择进程")
                    .classes("w-full")
                    .props("dense spellcheck=false")
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

        AndroidProfielerService.on_device_connected.subscribe(
            lambda device:notify(f"设备连接成功: {device}",type='positive',position='bottom-right', color="green")
        )

        AndroidProfielerService.on_device_disconnected.subscribe(
            lambda device: notify(f"设备断开连接: {device}",type='negative',position='bottom-right', color="red")
        )

        AndroidProfielerService.on_devices_changed.subscribe(
            self._on_device_changed
        )

        self.device_select.on_value_change(self._on_device_select_changed)
        self.app_select.on_value_change(self._on_app_select_changed)
        self.btn_tcpip.on_click(self._on_btn_tcpip_click)

    def _on_device_changed(self, devices: list[str]):
        self.device_select.set_options(devices)

    async def _on_device_select_changed(self, value:ValueChangeEventArguments):
        if not value.value:
            self.app_select.set_options([])
            return
        apps = await AndroidProfielerService.get_device_apps(value.value)
        self.app_select.set_options(apps)

    async def _on_app_select_changed(self, value:ValueChangeEventArguments):
        if not value.value:
            self.process_select.set_options([])
            return
        processes = await AndroidProfielerService.get_device_processes(
            self.device_select.value, value.value # type: ignore
        )
        self.process_select.set_options(processes)

    async def _on_btn_tcpip_click(self):
        serialno = self.device_select.value
        if not serialno:
            notify("请先选择设备", color="red")
            return
        dev = await AndroidProfielerService.get_device(serialno)
        ip = await dev.shell("ip route | awk '{print $9}'")

        await AndroidProfielerService.remote_adb_enable(serialno)
        res = await AndroidProfielerService.remote_connect(ip.strip(), 5555)
        if res:
            notify(f"开启无线连接成功: {ip.strip()}:5555", color="green")
        else:
            notify(f"开启无线连接失败: {ip.strip()}:5555", color="red")


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



class AndroidProfilerPage(Page):
    def __init__(self) -> None:
        super().__init__("/android_profiler", title="安卓性能")

        self.monitor_registers = {
            "FPS": FPSMonitorCard,
            "CPU": CPUMonitorCard,
            "Memory": MemoryTotalPSSMonitorCard,
            "Temperature": TemperatureMonitorCard,
        }

        self.serialno: str = ""
        self.app: str = ""
        self.process: str = ""
        self.timer_sampler: ui.timer|None = None

        self.setting_card_enable: bool = True

        self.monitors: list[MonitorCard] = []
       

    async def render(self):
        AndroidProfielerService.start_scan_devices()

        AndroidProfielerService.on_device_disconnected.subscribe(self._on_device_disconnected)

        self.drawer = AndroidProfilerDrawer()

        self.drawer.panel_device.profiler_setting_card.device_select.bind_value(self, "serialno")
        self.drawer.panel_device.profiler_setting_card.app_select.bind_value(self, "app")
        self.drawer.panel_device.profiler_setting_card.process_select.bind_value(self, "process")

        self.drawer.panel_device.profiler_setting_card.device_select.bind_enabled(self, "setting_card_enable")
        self.drawer.panel_device.profiler_setting_card.app_select.bind_enabled(self, "setting_card_enable")
        self.drawer.panel_device.profiler_setting_card.process_select.bind_enabled(self, "setting_card_enable")



        self.drawer.panel_device.profiler_setting_card.btn_record.on_click(
            self.toggle_record
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

    async def toggle_record(self,event:ClickEventArguments):
        if not self.serialno or not self.app or not self.process:
            notify("请先选择设备、应用和进程", color="red")
            return
        if event.sender.props["icon"] == "lens":
            await self.start_record(event)
        else:
            await self.stop_record()

    async def start_record(self, event):
        self.drawer.panel_device.profiler_setting_card.btn_record.props("icon=stop color=green")
        self._clear_monitors()
        self.setting_card_enable = False
        self.drawer.panel_device.profiler_setting_card.btn_record.set_text("停止采集")
        self.timer_sampler = ui.timer(1,self._on_sample, active=True)
        await RecordService.init_logger(self.serialno, self.app, self.process)
        ui.notify(
                f"开始采集: {self.serialno} - {self.app} - {self.process}",
                color="green",
                position="top",
            )
    
    async def stop_record(self):
        self.drawer.panel_device.profiler_setting_card.btn_record.props("icon=lens color=red")
        self.setting_card_enable = True
        self.drawer.panel_device.profiler_setting_card.btn_record.set_text("开始采集")
        self.timer_sampler.cancel() if self.timer_sampler else None
        await RecordService.save_record(
            f"{self.app}-{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        ui.notify(
            f"停止采集: {self.serialno} - {self.app} - {self.process}",
            color="red",
            position="top"
        )

    async def _on_sample(self):
        if not self.serialno or not self.app or not self.process:
            return

        for monitor in self.monitors:
            if monitor.visible:
                await monitor.sample(self.serialno, self.app, self.process)

    def _clear_monitors(self):
        for monitor in self.monitors:
            monitor.clear()

    def _on_device_disconnected(self, serialno:str):
        if not self.serialno:
            self.setting_card_enable = True
            self.timer_sampler.cancel() if self.timer_sampler else None
            ui.notify(
                f"设备 {serialno} 断开连接，停止采集",
                color="red",
                position="top",
                type='negative'
            )
            with ui.dialog().props('backdrop-filter="blur(8px) brightness(40%)"') as dialog:
                ui.label('设备断开连接，停止采集').classes('text-3xl text-white')

AndroidProfilerPage()
