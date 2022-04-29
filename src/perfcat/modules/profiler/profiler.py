from PySide6.QtWidgets import QWidget, QPushButton
from perfcat.ui.page import Page
from .ui_profiler import Ui_Profiler


class Setting(Page):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setWindowTitle("性能>设置")

        btn = QPushButton("性能 设置", self)


class Profiler(Page, Ui_Profiler):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setupUi(self)

        self._setting_widget = Setting(self)
