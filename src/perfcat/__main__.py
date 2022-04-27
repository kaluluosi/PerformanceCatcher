import sys

# 把asset/放到搜索目录里，这样.ui文件里 import asset_rc 才能正常导入asset_rc
import pkg_resources

asset_dir = pkg_resources.resource_filename(__package__, "assets")
sys.path.append(asset_dir)

from . import logger
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGraphicsDropShadowEffect,
)
from PySide6.QtGui import QColor
from .ui.layout import MainWindow


app = QApplication(sys.argv)

with open(
    r"G:\projects\perfcat\src\perfcat\assets\css\default.css", encoding="utf-8"
) as f:
    sheet = f.read()

main_win = MainWindow()
main_win.setStyleSheet(sheet)
main_win.show()
sys.exit(app.exec())
