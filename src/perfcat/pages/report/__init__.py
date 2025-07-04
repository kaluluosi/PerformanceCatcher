import json
import os
from nicegui import ui
from perfcat.components.layout import Page, Header
from perfcat.components.monitors import monitor_factory_map
from perfcat.components.profiler import MonitorCard


class ReportPage(Page):
    def __init__(self) -> None:
        @ui.page("/home/report/{filename}", title="性能报告")
        async def _(filename: str):
            # await self._frame()
            await self.render(filename)

    async def render(self, filename: str):
        Header()

        with open(os.path.join("records", filename), "r", encoding="utf-8") as f:
            lines = f.readlines()
            base_info = json.loads(lines[0])
            device_info = json.loads(lines[1])

        with ui.card().classes("w-full"):
            ui.label(f"{base_info['platform'].capitalize()}性能报告").classes(
                "text-2xl font-bold"
            )
            columns = [
                {
                    "name": "name",
                    "label": "名称",
                    "field": "name",
                    "required": True,
                    "align": "left",
                },
                {
                    "name": "value",
                    "label": "值",
                    "field": "value",
                    "required": True,
                    "align": "right",
                    "style": "overflow-wrap:anywhere",
                },
            ]
            rows = [
                {"name": "测试设备", "value": base_info.get("model", "unknown")},
                {"name": "包名", "value": base_info.get("app", "unknown")},
                {"name": "进程名", "value": base_info.get("process", "unknown")},
                {"name": "构建版本", "value": base_info.get("version", "unknown")},
                {"name": "安装日期", "value": base_info.get("install_time", "unknown")},
                {"name": "测试时间", "value": base_info.get("create_at", "unknown")},
            ]
            ui.label("基本信息")
            ui.table(columns=columns, rows=rows).classes("w-full").props(
                "hide-header dense"
            )

            ui.label("设备信息")
            rows = [{"name": key, "value": value} for key, value in device_info.items()]
            ui.table(columns=columns, rows=rows).classes("w-full").props(
                "hide-header dense"
            )

            monitors: dict[str, MonitorCard] = {}

            for line in lines[2:]:
                data: dict = json.loads(line)
                title = data["name"]
                if title not in monitors:
                    monitors[title] = monitor_factory_map[title](show_aggregate=True)
                    monitors[title].clear()

                for key, value in data.items():
                    if key == "name":
                        continue
                    monitors[title].add_point(key, value)

            for monitor in monitors.values():
                monitor.update_chart()


ReportPage()
