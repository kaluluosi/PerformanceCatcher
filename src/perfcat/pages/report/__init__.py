import asyncio
import os
import json
import webview
import base64
import logging
from typing import cast
from collections import defaultdict
from nicegui import app, ui,events
from perfcat.components.layout import Page
from perfcat.components.monitors import monitor_factory_map

logger = logging.getLogger(__name__)

class ReportPage(Page):
    def __init__(self) -> None:
        self.filename:str = ""

        @ui.page("/home/report", title="性能报告")
        async def _(filename: str):
            await self._frame()
            await self.render(filename)

    async def render(self, filename: str):
        self.filename = filename
        ui.query("html").style("overflow:auto")
        ui.add_head_html("<script src='/static/js/html2canvas.min.js'></script>")

        self.header.btn_browser.classes(remove="hidden")
        self.header.btn_browser.on_click(self._to_browser)

        self.header.btn_screenshot.classes(remove="hidden")
        self.header.btn_screenshot.on_click(self._on_screenshot)

        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            base_info = json.loads(lines[0])
            device_info = json.loads(lines[1])

        # with ui.column().classes("w-full p-2 scroll h-[90vh]"):

        self._create_monitors(lines, base_info, device_info)

    def _create_monitors(self, lines, base_info, device_info):
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
                {"name": "测试时间", "value": base_info.get("created_at", "unknown")},
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

            monitor_seires: dict[str, list] = defaultdict(list) 

            for line in lines[2:]:
                try:
                    data: dict = json.loads(line)
                    title = data["name"]
                    monitor_seires[title].append(data)
                except Exception as e:
                    logger.error(f"解析数据失败: {e}")
                    logger.error(line)
                    raise e
            
            for moinitor_name,monitor_class in monitor_factory_map.items():
                if moinitor_name in monitor_seires:
                    monitor = monitor_class(show_aggregate=True)
                    monitor.clear()
                    for data in monitor_seires[moinitor_name]:
                        for serie_name, data_value in data.items():
                            if serie_name != "name":
                                monitor.add_point(serie_name, data_value)
                    monitor.update_chart()

            ui.run_javascript("echarts.connect('monitor')")

    async def _to_browser(self):
        url = await app.native.main_window.get_current_url() # type: ignore
        ui.navigate.to(url,True)

    async def _on_screenshot(self,args:events.ClickEventArguments):
        ui.run_javascript(
            '''
            scrollTo({
            top: 0,
            left: 0,
            behavior: 'instant',
            });
        ''')

        nav_show = self.navigationbar.value
        self.navigationbar.value = False
        await asyncio.sleep(0.5)
        try:
            args.sender.props("loading")
            base_name = os.path.basename(self.filename).replace(".pcat",".jpg")
            url = await ui.run_javascript(
                f'''
                let canvas = await html2canvas(document.body);
                let imgData = canvas.toDataURL("image/jpg");
                const link = document.createElement('a');
                link.download = '{base_name}';
                link.href = imgData;
                link.click();
                return ;
                ''',
                timeout=60
            )
            args.sender.props(remove="loading")
            self.navigationbar.value = nav_show
        except Exception as e:
            logger.error(f"截图失败: {e}")
            ui.notify("截图失败")
            self.navigationbar.value = nav_show
            args.sender.props(remove="loading")
            return
    
        # user_agent = ui.context.client.request.headers['user-agent'] # type: ignore
        # base_name = os.path.basename(self.filename)
        # if "Edg/138.0.0.0" in user_agent:
        #     save_to = await app.native.main_window.create_file_dialog( # type: ignore
        #         webview.SAVE_DIALOG,directory="./",
        #         save_filename=base_name.replace(".pcat",".png"),
        #         file_types=("PNG (*.png)",)
        #         )
        #     save_to = cast(str,save_to)
        #     with open(save_to,"wb") as f:
        #         b64_data = url.split(",")[1]
        #         f.write(base64.b64decode(b64_data))

        #     logger.info(f"save screenshot to {save_to}")
        #     ui.notify(f"截图已保存为 {save_to}")
        # else:
        #     ui.download(url,base_name.replace(".pcat",".png"),media_type="image/png")

        
ReportPage()
