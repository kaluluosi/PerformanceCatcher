import asyncio
import datetime
from nicegui import app, ui
from nicegui.events import (
    ClickEventArguments,
    TableSelectionEventArguments,
)
from nicegui.observables import ObservableDict
from perfcat.components.layout import Page
from perfcat.components.profiler import ControlCard, Drawer, MonitorCard
from perfcat.pages.android_profiler.device_info_card import DeviceInfoCard
from perfcat.pages.android_profiler.profiler_setting_card import ProfilerSettingCard
from perfcat.pages.android_profiler.remote_connect_card import RemoteConnectCard
from perfcat.services import AndroidProfielerService, RecordService
from perfcat.utils import notify, set_navigation_disable
from perfcat.components.monitors import monitor_factory_map,FPSMonitorCard,CPUMonitorCard,MemoryTotalPSSMonitorCard


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
            self.device_info_card = DeviceInfoCard()


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
                "style": "overflow-wrap:anywhere",
            },
        ]
        rows = [
            {"name": name, "description": description}
            for name, description in self._monitors_registers.items()
        ]
        self.table = (
            ui.table(
                columns=columns,
                rows=rows,
                row_key="name",
                on_select=self._on_select,
            )
            .classes("w-full")
            .props("selection=multiple dense hide-selected-banner")
        )
        self.table.selected = app.storage.general.get(
            "android_profiler_monitors_selection", []
        )

    def _on_select(self, e: TableSelectionEventArguments):
        app.storage.general["android_profiler_monitors_selection"] = e.selection


class AndroidProfilerPage(Page):
    def __init__(self) -> None:
        super().__init__("/android_profiler", title="安卓性能")

        self.serialno: str = ""
        self.app: str = ""
        self.process: str = ""
        self.timer_sampler: ui.timer | None = None

        if "android_profiler_monitors_selection" not in app.storage.general:
            app.storage.general["android_profiler_monitors_selection"] = [
                {"name":FPSMonitorCard.title,"description":FPSMonitorCard.description},
                {"name":CPUMonitorCard.title,"description":CPUMonitorCard.description},
                {"name":MemoryTotalPSSMonitorCard.title,"description":MemoryTotalPSSMonitorCard.description},   
            ]

        self.setting_card_enable: bool = True

        self.monitors: list[MonitorCard] = []

        AndroidProfielerService.on_device_disconnected.subscribe(
            self._on_device_disconnected
        )

    @property
    def is_recording(self):
        return self.timer_sampler.active if self.timer_sampler else False

    async def render(self):
        ui.timer(0,self.start_adb_server,once=True)

        self.setting_card_enable = True

        self.monitors.clear()

        self.drawer = AndroidProfilerDrawer()

        self.drawer.panel_device.profiler_setting_card.device_select.bind_value(
            self, "serialno"
        )
        self.drawer.panel_device.profiler_setting_card.app_select.bind_value(
            self, "app"
        )
        self.drawer.panel_device.profiler_setting_card.process_select.bind_value(
            self, "process"
        )

        self.drawer.panel_device.profiler_setting_card.device_select.bind_enabled_from(
            self, "setting_card_enable"
        )
        self.drawer.panel_device.profiler_setting_card.app_select.bind_enabled_from(
            self, "setting_card_enable"
        )
        self.drawer.panel_device.profiler_setting_card.process_select.bind_enabled_from(
            self, "setting_card_enable"
        )

        self.drawer.panel_device.profiler_setting_card.device_select.on_value_change(
            self.drawer.panel_device.device_info_card.load
        )

        self.drawer.panel_device.profiler_setting_card.btn_record.on_click(
            self.toggle_record
        )
        self.drawer.panel_device.profiler_setting_card.btn_restart_adb.on_click(
            self.restart_adb_server
        )

        for monitor_card in monitor_factory_map.values():
            self.drawer.panel_monitor.register_monitor(
                monitor_card.title, monitor_card.description
            )

        with ui.column().classes("w-full p-2 scroll h-[90vh]"):
            await self.create_monitors()


    async def start_adb_server(self):
        n = ui.notification("正在启动adb服务", position="bottom",spinner=True,timeout=None)
        ret = await AndroidProfielerService.start_adb_server()
        
        if ret == 0:
            n.message = "adb服务启动成功"
            n.type = "positive"
        else:
            n.message = "adb服务启动失败"
            n.type = "negative"
        n.spinner = False
        await asyncio.sleep(2)
        n.dismiss()

    async def restart_adb_server(self):
        n = ui.notification("正在重启adb服务", position="bottom",spinner=True,timeout=None)
        ret = await AndroidProfielerService.stop_adb_server()
        ret = await AndroidProfielerService.start_adb_server()
        
        if ret == 0:
            n.message = "adb服务启动成功"
            n.type = "positive"
        else:
            n.message = "adb服务启动失败"
            n.type = "negative"
        n.spinner = False
        await asyncio.sleep(2)
        n.dismiss()


    async def create_monitors(self):
        for monitor_card in monitor_factory_map.values():
            monitor: MonitorCard = monitor_card()
            self.monitors.append(monitor)

            monitor.bind_visibility_from(
                app.storage.general,
                "android_profiler_monitors_selection",
                backward=lambda selection, name=monitor_card.title: any(
                    [name == select["name"] for select in selection]
                ),
            )

        ui.run_javascript("echarts.connect('monitor')")

    def _make_log_filename(self):
        return f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"

    async def toggle_record(self, event: ClickEventArguments):
        if not self.serialno or not self.app or not self.process:
            notify("请先选择设备、应用和进程", color="red")
            return
        if event.sender.props["icon"] == "lens":
            await self.start_record(event)
        else:
            await self.stop_record()

    async def start_record(self, event):
        set_navigation_disable(True)
        self.drawer.panel_device.profiler_setting_card.btn_record.props(
            "icon=stop color=green"
        )
        self._clear_monitors()
        await RecordService.init_logger(self.serialno, self.app, self.process)
        self.setting_card_enable = False
        self.drawer.panel_device.profiler_setting_card.btn_record.set_text("停止采集")
        self.timer_sampler = ui.timer(1, self._on_sample, active=True)
        ui.notify(
            "开始采集",
            type="positive",
            position="bottom",
        )

    async def stop_record(self):
        set_navigation_disable(False)
        self.drawer.panel_device.profiler_setting_card.btn_record.props(
            "icon=lens color=red"
        )
        self.setting_card_enable = True
        self.drawer.panel_device.profiler_setting_card.btn_record.set_text("开始采集")
        self.timer_sampler.deactivate() if self.timer_sampler else None
        ui.notify(
            "停止采集",
            type="positive",
            position="bottom",
        )

        self._show_save_record_dialog()

    def _show_save_record_dialog(self):
        def _on_ok():
            RecordService.save_record(input_filename.value)
            dialog.close()
            notify("日志保存成功", type="positive")

        with ui.dialog(value=True) as dialog, ui.card():
            with ui.card_section().style("width:400px"):
                ui.label("日志保存为").classes("text-h6")
                input_filename = (
                    ui.input(value=self._make_log_filename())
                    .classes("w-full")
                    .props("hint=日志将保存到records目录下")
                )

            with ui.card_actions().classes("w-full justify-end"):
                ui.button(
                    "确认",
                    color="primary",
                    on_click=_on_ok,
                )
                ui.button("取消", color="secondary", on_click=dialog.close)

    async def _on_sample(self):
        if not self.serialno or not self.app or not self.process:
            return

        for monitor in self.monitors:
            if monitor.visible:
                await monitor.sample(self.serialno, self.app, self.process)

    def _clear_monitors(self):
        for monitor in self.monitors:
            monitor.clear()

    def _on_device_disconnected(self, serialno: str):
        if not self.is_recording:
            return

        if self.serialno:
            return

        self.setting_card_enable = True
        self.timer_sampler.cancel() if self.timer_sampler else None

        with ui.context.client.content:
            with ui.dialog(value=True).props(
                'backdrop-filter="blur(8px) brightness(40%)"'
            ) as dialog:
                ui.label("设备断开连接，停止采集").classes("text-3xl text-white")

            dialog.on("hide", self._show_save_record_dialog)


AndroidProfilerPage()
