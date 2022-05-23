from PySide6.QtCore import *
import time

def time_calculate(func):
    def wapple(*arge):
        start_time = time.time()
        if len(arge) == 1:
            func(arge[0])
        elif len(arge) == 2:
            func(arge[0], arge[1])
        elif len(arge) == 3:
            func(arge[0], arge[1], arge[2])
        end_time = time.time()
        print("{}:{}".format(func.__name__, end_time - start_time))
    return wapple

class StringListModel(QAbstractTableModel):

    data_changed = Signal()

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
        # elif role == Qt.DecorationRole:
        #     pass
 
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
