from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import Slot, QPropertyAnimation, QEasingCurve
from .ui_left_column import Ui_LeftColumn


class LeftColumn(QWidget, Ui_LeftColumn):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("")
