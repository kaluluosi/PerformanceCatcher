from nicegui import ui, app
from perfcat.components.layout import Page


class HomePage(Page):
    def __init__(self) -> None:
        super().__init__("/", title="首页")

    async def render(self):
        ui.label("hello world")


HomePage()
