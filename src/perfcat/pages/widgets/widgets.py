import logging
from perfcat.ui.constant import ButtonStyle
from perfcat.ui.page import Page
from perfcat.ui.widgets import notification
from .ui_widgets import Ui_Widgets
from PySide6.QtCore import Qt
from perfcat.ui.widgets.notification import Notification

log = logging.getLogger(__name__)

class Widgets(Page, Ui_Widgets):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setupUi(self)
        self.clear_stylesheet()

        self.comboBox.addItem("x10")

        self.btn_reload.clicked.connect(self.reload_stylesheet)
        
        self.btn_notify.clicked.connect(self.notify)
        self.btn_notify_2.clicked.connect(self.notify_2)

    def reload_stylesheet(self):
        from perfcat.app import PerfcatApplication

        PerfcatApplication.instance.load_stylesheet()
        self.repaint()
        self.adjustSize()

    def notify_2(self):
        log.debug("弹出提示！")
        Notification(self, msg="这是样式2", style=ButtonStyle.success).show()