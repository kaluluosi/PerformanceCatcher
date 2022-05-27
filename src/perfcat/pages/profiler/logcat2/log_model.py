import logging
from typing import Any, Optional, Union
from PySide6.QtCore import (
    QAbstractTableModel,
    QObject,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)
from PySide6.QtGui import QColor
from perfcat.ui.constant import Color
from .log_provider import LogProvider

log = logging.getLogger(__name__)


class LogModel(QAbstractTableModel):
    COL_DATE = 0
    COL_TIME = 1
    COL_PID = 2
    COL_TID = 3
    COL_LEVEL = 4
    COL_TAG = 5
    COL_CONTENT = 6

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.log_provider = LogProvider(self)
        self.log_provider.new_log_added.connect(self.on_new_log_added)
        self._logs = []
        self._headers = ["日期", "时间", "PID", "TID", "优先级", "标签", "消息"]

    def start(self, serial: str):
        self.log_provider.start(serial)

    def stop(self):
        self.log_provider.exit()

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = None) -> int:
        return len(self._logs)

    def on_new_log_added(self, msg: list):
        row = self.rowCount()
        length = len(msg)
        self.beginInsertRows(QModelIndex(), row, row + length - 1)
        self._logs += msg
        self.endInsertRows()

    def data(
        self, index: Union[QModelIndex, QPersistentModelIndex], role: int = ...
    ) -> Any:
        if role == Qt.DisplayRole:
            return self._logs[index.row()][index.column()]
        elif role == Qt.EditRole:  # 编辑时
            return self._logs[index.row()][index.column()]
        if role == Qt.ForegroundRole:
            level = self._logs[index.row()][self.COL_LEVEL]
            if "E" == level:
                return QColor(Color["danger"])
            elif "W" == level:
                return QColor(Color["warning"])
            elif "D" == level:
                return QColor(Color["success"])
            elif "I" == level:
                return QColor(Color["info"])

    def columnCount(
        self, parent: Union[QModelIndex, QPersistentModelIndex] = ...
    ) -> int:
        return len(self._headers)

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: int = ...
    ) -> Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]

    def clear(self):
        self.beginResetModel()
        self._logs = []
        self.endResetModel()

    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]) -> Qt.ItemFlags:
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def get_text_by_indexes(self, indexes: list[QModelIndex]):
        lines = []
        row = None

        line = []
        for index in indexes:
            if row is None:
                row = index.row()
            elif index.row() != row:
                lines.append("  ".join(line))
                line.clear()
                row = index.row()
            line.append(index.data())

        lines.append("  ".join(line))

        return "\n".join(lines)
