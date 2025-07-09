import re
from nicegui import ui
from perfcat.components.profiler import ControlCard
from perfcat.services import AndroidProfielerService
from perfcat.utils import notify






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
        ip, port = self.input_address.value.split(":")
        res = await AndroidProfielerService.remote_connect(ip, int(port))
        if res:
            notify(f"连接成功: {ip}:{port}", color="green")
        else:
            notify(f"连接失败: {ip}:{port}", color="red")