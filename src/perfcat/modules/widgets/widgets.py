from PySide6.QtWidgets import QWidget, QPushButton
from perfcat.ui.page import Page
from .ui_widgets import Ui_Widgets
from PySide6.QtCore import Qt


class Widgets(Page, Ui_Widgets):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setupUi(self)
        self.clear_stylesheet()

        self.comboBox.addItem("x10")

        self.btn_reload.clicked.connect(self.reload_stylesheet)

    def reload_stylesheet(self):
        from perfcat.app import PerfcatApplication

        PerfcatApplication.instance.load_stylesheet()
        self.repaint()
        self.adjustSize()
