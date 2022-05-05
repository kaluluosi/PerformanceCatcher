from PySide6.QtWidgets import QWidget, QPushButton
from perfcat.ui.page import Page
from .ui_home import Ui_Home


class Home(Page, Ui_Home):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setupUi(self)
