from logging.handlers import RotatingFileHandler
from PySide6.QtCore import *

class StractViewModel(QAbstractListModel):
    
    def __init__(self, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self._data = ["ALL"]

    # 更新单个数据
    def update_one_data(self, data):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        if data not in self._data and data != "":
            self._data.append(data)
        self.endInsertRows()

    def rowCount(self, parent=None, *args, **kwargs):
        """
        行数
        """
        return len(self._data)

    def data(self, index, role):
        if role in [Qt.DisplayRole,Qt.EditRole]:
            return self._data[index.row()]

