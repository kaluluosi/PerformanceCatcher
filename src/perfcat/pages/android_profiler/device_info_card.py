from perfcat.components.profiler import ControlCard
from perfcat.services import AndroidProfielerService
from perfcat.utils import notify


from nicegui import ui
from nicegui.events import ValueChangeEventArguments


class DeviceInfoCard(ControlCard):
    def __init__(self) -> None:
        super().__init__()

        with self:
            columns = [
                {
                    "name": "name",
                    "label": "名称",
                    "field": "name",
                    "align": "left",
                    "style": "width:120px",
                },
                {
                    "name": "value",
                    "label": "值",
                    "field": "value",
                    "style": "overflow-wrap:anywhere",
                },
            ]

            self._default_rows = [
                {"name": "品牌", "value": ""},
                {"name": "制造商", "value": ""},
                {"name": "型号", "value": ""},
                {"name": "名称", "value": ""},
                {"name": "系统版本", "value": ""},
                {"name": "SDK版本", "value": ""},
                {"name": "首选SDK版本", "value": ""},
                {"name": "CPU平台", "value": ""},
                {"name": "CPU名称", "value": ""},
                {"name": "CPU架构", "value": ""},
                {"name": "CPU核心", "value": ""},
                {"name": "CPU频率", "value": ""},
                {"name": "GPU型号", "value": ""},
                {
                    "name": "OpenGL",
                    "value": "",
                },
                {"name": "RAM", "value": ""},
                {"name": "SWAP", "value": ""},
                {"name": "ROOT", "value": ""},
                {"name": "Serial", "value": ""},
            ]

            self.table = ui.table(
                columns=columns, rows=self._default_rows, row_key="name"
            )
            self.table.props("dense wrap-cells bordered separator=cell")
            self.table.classes("w-full")

            with ui.card_actions().classes("w-full justify-end"):
                ui.button("复制到剪贴板", on_click=self._copy_to_clipboard)

    async def _copy_to_clipboard(self):
        rows = self.table.rows
        data = "\n".join([f"{row['name']}   {row['value']}" for row in rows])
        ui.clipboard.write(data)
        notify("已复制到剪贴板")

    async def load(self, args: ValueChangeEventArguments):
        if not args.value:
            self.table.rows = self._default_rows
            return

        serialno = args.value
        self.table.props("loading=true")
        device_info = await AndroidProfielerService.get_device_info(serialno)
        rows = [{"name": key, "value": value} for key, value in device_info.items()]
        self.table.rows = rows
        self.table.props("loading=false")