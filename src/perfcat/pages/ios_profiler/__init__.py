"""
author:        kaluluosi111 <kaluluosi@gmail.com>
date:          2025-07-06 12:17:16
Copyright © Kaluluosi All rights reserved
"""

from nicegui import ui
from nicegui.elements.tabs import Tab
from perfcat.components.layout import Page
from perfcat.components.profiler import Drawer

from .profiler_setting_card import ProfilerSettingCard

class IOSProfilerDrawer(Drawer):

    def __init__(self):
        super().__init__()

        with self:
            with self.create_tabs():
                self.tab_device = ui.tab("设备")
                self.tab_monitor = ui.tab("监控")

            with self.create_tab_panels():
                self.tab_panels.value = self.tab_device
                self.tab_device_panel = DeviceTabPanel("设备")

class DeviceTabPanel(ui.tab_panel):
    def __init__(self, name: Tab | str) -> None:
        super().__init__(name)
        self.classes("w-full")
        with self:
            self.profiler_setting_card = ProfilerSettingCard()


class IOSProfilerPage(Page):
    def __init__(self):
        super().__init__("/ios_profiler", title="iOS性能")

    
    async def render(self, *args, **kwargs):
        self.drawer = IOSProfilerDrawer()


IOSProfilerPage()