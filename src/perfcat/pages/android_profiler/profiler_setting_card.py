from perfcat.components.profiler import ControlCard
from perfcat.services import AndroidProfielerService
from perfcat.utils import notify


from nicegui import ui
from nicegui.events import ValueChangeEventArguments


class ProfilerSettingCard(ControlCard):
    def __init__(self) -> None:
        super().__init__()
        with self:
            with self.session():
                self.device_select = (
                    ui.select([], label="选择设备")
                    .props("dense spellcheck=false clearable")
                    .classes("w-full flex-1")
                )

                with self.device_select.add_slot("prepend"):
                    ui.icon("adb")

                self.btn_tcpip = ui.button(icon="wifi").props("dense")

                with self.btn_tcpip:
                    ui.tooltip("开启无线连接\n(adb tcpip:5555)")

                self.app_select = (
                    ui.select([], label="选择APP", with_input=True)
                    .props("dense spellcheck=false clearable")
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
                    .props("dense spellcheck=false clearable")
                )
                self.process_select.bind_enabled_from(
                    self.app_select, "value", backward=lambda v: v is not None
                )
                with self.process_select.add_slot("prepend"):
                    ui.icon("wysiwyg")

                with ui.row().classes("items-center w-full justify-between"):
                    self.btn_record = (
                        ui.button("开始采集", icon="lens")
                        .props("dense color=red ")
                        .classes("p-2")
                    )

                    self.btn_restart_adb = (
                        ui.button("重启ADB服务", icon="restart_alt",color="red")
                        .props("dense color=red ")
                        .classes("p-2")
                    )

        AndroidProfielerService.on_device_connected.subscribe(
            lambda device: notify(
                f"设备连接: {device}",
                type="positive",
                position="top-right",
                color="green",
            )
        )

        AndroidProfielerService.on_device_disconnected.subscribe(
            lambda device: notify(
                f"设备断开: {device}",
                type="negative",
                position="top-right",
                color="red",
            )
        )

        AndroidProfielerService.on_devices_changed.subscribe(self._on_device_changed)

        self.device_select.on_value_change(self._on_device_select_changed)
        self.app_select.on_value_change(self._on_app_select_changed)
        self.btn_tcpip.on_click(self._on_btn_tcpip_click)

        self._refresh_devices()


    def _refresh_devices(self):
        self.device_select.set_options(list(AndroidProfielerService.devices))

    def _on_device_changed(self, devices: set[str]):
        self.device_select.set_options(list(devices))

    async def _on_device_select_changed(self, value: ValueChangeEventArguments):
        if not value.value:
            self.app_select.set_options([])
            return
        apps = await AndroidProfielerService.get_device_apps(value.value)
        self.app_select.set_options(apps)

    async def _on_app_select_changed(self, value: ValueChangeEventArguments):
        if not value.value or not self.device_select.value:
            self.process_select.set_options([])
            return
        processes = await AndroidProfielerService.get_device_processes(
            self.device_select.value,
            value.value,  # type: ignore
        )
        self.process_select.set_options(processes)

    async def _on_btn_tcpip_click(self):
        self.btn_tcpip.props("loading=true")
        serialno = self.device_select.value
        if not serialno:
            notify("请先选择设备", color="red")
            return
        dev = await AndroidProfielerService.get_device(serialno)
        ip = await dev.shell("ip route | awk '{print $9}'")

        await AndroidProfielerService.adb_tcpip_enable(serialno)
        res = await AndroidProfielerService.remote_connect(ip.strip(), 5555)
        if res:
            notify(f"开启无线连接成功: {ip.strip()}:5555", color="green")
        else:
            notify(f"开启无线连接失败: {ip.strip()}:5555", color="red")
        self.btn_tcpip.props("loading=false")