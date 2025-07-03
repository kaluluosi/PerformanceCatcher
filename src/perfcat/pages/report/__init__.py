from nicegui import ui
from perfcat.components.layout import Page, Header


class ReportPage(Page):
    def __init__(self) -> None:
        @ui.page("/home/report/{filename}", title="性能报告")
        async def _(filename: str):
            # await self._frame()
            await self.render(filename)

    async def render(self, filename: str):
        Header()

        with ui.card().classes("w-full"):
            ui.label("Android性能报告").classes("text-2xl font-bold")
            with ui.row():
                ui.label("日志文件:")
                ui.link(filename, filename).classes("text-blue-500")


ReportPage()
