from PySide6.QtCore import *
from PySide6.QtGui import QColor
from perfcat.ui.constant import Color

class StringListModel(QAbstractTableModel):

    data_changed = Signal()

    COL_DATE = 0
    COL_TIME = 1
    COL_LEVEL = 4
    COL_TAG = 5

    def __init__(self, data, HEADERS):
        super(StringListModel, self).__init__()
        self._data = data       # model使用的数据
        self.headers = HEADERS  # 标题（列表形式）
        self.count = 0          # 表格更新的标记
        self._data_dict = {0:[], 2:[], 3:[], 4:[], 5:[]}    # 标题菜单页签
        self.operate_column = self._data_dict.keys()
        self.table_refresh = 20        # 用于判定表格添加多少数据才刷新一次（实时添加数据但表格不实时刷新）

    def updateData(self, data):
        """
        (自定义)更新数据
        """
        # self.beginResetModel()
        # 开始插入行(最后一行插入)
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        
        self._data.append(data)
        self.column_list(data)
        self.count+=1
        # 每20行才触发滚动底部的信号
        if self.count >= self.table_refresh:
            self.count = 0
            if self.rowCount() % 10000 == 0:
                self.table_refresh = 40
            self.data_changed.emit()

        # 插入行数数据结束（必须有该方法，不然不会进入model）
        self.endInsertRows()

    def column_list(self, data):
        '''
        更新页签的列表(前2列不更新)
        '''
        for i in self.operate_column:
            if data[i] not in self._data_dict[i]:
                self._data_dict[i].append(data[i])

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        elif role == Qt.EditRole:   # 编辑时
            return self._data[index.row()][index.column()]
        if role == Qt.ForegroundRole:
            # if index.column() == self.COL_PRIORITY:
            level = self._data[index.row()][self.COL_LEVEL]
            if "E" == level:
                return QColor(Color['danger'])
            elif "W" == level:
                return QColor(Color['warning'])
            elif "D" == level:
                return QColor(Color['success'])
            elif "I" == level:
                return QColor(Color['info'])
 
    def rowCount(self, parent=None, *args, **kwargs):
        """
        行数
        """
        return len(self._data)
 
    def columnCount(self, parent=None, *args, **kwargs):
        """
        列数
        """
        return len(self.headers)
 
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """
        标题定义
        """
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.headers[section]

    def column_menu(self, columnvalue=0):
        '''
        返回页签对象
        '''
        return self._data_dict[columnvalue]

    def removeRows(self):
        '''
        清空model的所有数据
        '''
        self.beginResetModel()
        self._data = []
        self.endResetModel()

    def setData(self, index, value, role):
        '''
        设置单元格数据
        '''
        if role == Qt.EditRole:
            value = self._data[index.row()][index.column()]
            return True
        return False

    def flags(self, index):
        '''
        单元格的可操作性标志位，如可编辑，可选中等
        '''
        # if index.isValid():
        #     return Qt.NoItemFlags
        return Qt.ItemIsEnabled|Qt.ItemIsEditable
