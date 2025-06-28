import reactivex as rx
from asyncio import Task
from nicegui import ui, background_tasks
from async_adbc import ADBClient, Device, Status


class _AndroidProfilerService:
    on_devices_changed: rx.Subject[list[str]] = rx.Subject()
    on_device_connected: rx.Subject[str] = rx.Subject()
    on_device_disconnected: rx.Subject[str] = rx.Subject()

    def __init__(self) -> None:
        self.adbc = ADBClient()
        self._timer_scan_device = None

    @property
    async def devices(self):
        devices = await self.adbc.devices()
        return [dev.serialno for dev in devices]

    async def get_device(self, serialno: str):
        dev = await self.adbc.device(serialno)
        return dev

    async def get_device_apps(self, serialno: str):
        dev = await self.get_device(serialno)
        return await dev.pm.list_packages()

    async def get_device_processes(self, serialno: str, app_name: str):
        dev = await self.get_device(serialno)
        res = await dev.shell(f"ps -A|grep {app_name}|grep -v grep|awk '{{print $9}}'")
        return res.strip().splitlines()

    async def remote_connect(self, ip: str, port: int):
        res = await self.adbc.remote_connect(ip, port)
        if res:
            self.on_devices_changed.on_next(await self.devices)
            self.on_device_connected.on_next(":".join([ip, str(port)]))
        return res

    async def remote_adb_enable(self, serialno: str):
        dev = await self.get_device(serialno)
        res = await dev.adbd_tcpip(5555)
        print(res)

    def start_scan_devices(self):
        self._timer_scan_device = ui.timer(1, self._scan_devices, once=True)

    def stop_scan_devices(self):
        if self._timer_scan_device:
            self._timer_scan_device.cancel()

    async def _scan_devices(self):
        async for dev in self.adbc.devices_track():
            if dev.status == Status.DEVICE:
                print(f"Device {dev.serialno} connected")
                self.on_devices_changed.on_next(await self.devices)
                self.on_device_connected.on_next(dev.serialno)
            elif dev.status == Status.OFFLINE:
                print(f"Device {dev.serialno} {dev.status} disconnected")
                self.on_devices_changed.on_next(await self.devices)
                self.on_device_disconnected.on_next(dev.serialno)


AndroidProfielerService = _AndroidProfilerService()
