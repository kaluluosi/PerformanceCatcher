import sys
import logging
from typing import Optional
from ppadb.device import Device

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QSortFilterProxyModel
from .ui_logcat import Ui_Logcat
from .log_model import LogModel, LogSortFilterProxyModel

log = logging.getLogger(__name__)


class LogcatWidget(QWidget, Ui_Logcat):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._device: Device = None

        self.btn_start.setEnabled(False)

        self.origin_model = LogModel(self)
        self.origin_model.rowsInserted.connect(self._on_scroll_to_bottom)

        self.proxy_model = LogSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.origin_model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        # 过滤内容列
        self.proxy_model.setFilterKeyColumn(-1)

        self.tbv_logs.setModel(self.proxy_model)
        self.btn_start.toggled.connect(self.on_start)

        self._auto_scroll_to_bottom = True
        vsbar = self.tbv_logs.verticalScrollBar()
        vsbar.valueChanged.connect(self._on_vsbar_value_changed)

        # 固定字符匹配
        self.le_search.editingFinished.connect(
            lambda: self.proxy_model.set_filter_by_column(
                self.le_search.text(), LogModel.COL_CONTENT
            )
        )
        self.le_tag.editingFinished.connect(
            lambda: self.proxy_model.set_filter_by_column(
                self.le_tag.text(), LogModel.COL_TAG
            )
        )
        self.cbx_priority.activated.connect(
            lambda: self.proxy_model.set_filter_by_column(
                self.cbx_priority.currentText(), LogModel.COL_LEVEL
            )
        )

        # 列表右键菜单
        self.tbv_logs.addAction(self.action_copy)
        self.action_copy.triggered.connect(self._on_log_copy)

        # 保存内容
        self.btn_save.clicked.connect(self._on_btn_save)
        
        # 清空内容
        self.btn_clear.clicked.connect(self.origin_model.clear)

        # 初始化前5列的列宽
        self.tbv_logs.setColumnWidth(0, 40)
        self.tbv_logs.setColumnWidth(1, 80)
        self.tbv_logs.setColumnWidth(2, 45)
        self.tbv_logs.setColumnWidth(3, 45)
        self.tbv_logs.setColumnWidth(4, 45)

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, value: Device):
        self._device = value
        if value == None:
            self.btn_start.setEnabled(False)
        else:
            self.btn_start.setEnabled(True)

    def _on_tag_text_changed(self, text: str):
        self.proxy_model.setFilterKeyColumn(self.origin_model.COL_TAG)
        self.proxy_model.setFilterFixedString(text)

    def _on_log_copy(self):
        selection = self.tbv_logs.selectedIndexes()
        text = self.origin_model.get_text_by_indexes(selection)
        QApplication.clipboard().setText(text)

    def _on_vsbar_value_changed(self, value):
        vsbar = self.tbv_logs.verticalScrollBar()
        maximun = vsbar.maximum()
        self._auto_scroll_to_bottom = value == maximun
        # log.debug(f"自动滚动 {self._auto_scroll_to_bottom}")

    def on_start(self, checked):
        if checked:
            self.origin_model.start(self.device.serial)
        else:
            self.origin_model.stop()

    def _on_scroll_to_bottom(self, index, first, last):
        # 可能有性能问题，但是要观察
        self.tbv_logs.setUpdatesEnabled(False)
        for i in range(first, last):
            self.tbv_logs.resizeRowToContents(i)
        self.tbv_logs.setUpdatesEnabled(True)
        if self._auto_scroll_to_bottom:
            self.tbv_logs.scrollToBottom()

    def _on_btn_save(self):
        text = self.origin_model.log_text()
        try:
            filepath, type = QFileDialog.getSaveFileName(
                self, "文件保存", "/", "log(*.log)"
            )
            file = open(filepath, "w", encoding="utf-8")
            log.debug(f"保存的文件路径：{filepath}")
            file.writelines(text)
            file.close()
        except Exception:
            QMessageBox.critical(self, "错误", "没有指定保存的文件名")

        

if __name__ == "__main__":

    app = QApplication()
    win = LogcatWidget()
    win.show()
    sys.exit(app.exec())
