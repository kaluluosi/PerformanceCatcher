from PySide6.QtCore import Qt, QSortFilterProxyModel

class SortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, data, parent=None):
        super(SortFilterProxyModel, self).__init__(parent)
        self.role = Qt.DisplayRole

        self.column = 0     # 最后操作过滤的列号
        self.filter_list = {2:"", 3:"", 4:"", 5:""}   # 各列正在使用的正则表达式
        self.filter6 = ""

    def filterAcceptsRow(self, sourceRow, sourceParent):
        '''
        sourceRow : 行数
        sourceParent ：
        第7列（下标是6，消息内容）特殊处理，按照输入半匹配
        '''
        _reg_exp = self.filterRegularExpression().pattern()  # 当前正则
        # text = self.sourceModel().data(index2, self.role)   # 单元格的内容
        index6 = self.sourceModel().index(sourceRow, 6, sourceParent)
        text6 = self.sourceModel().data(index6, self.role)
        for i in self.filter_list:
            index = self.sourceModel().index(sourceRow, i, sourceParent)
            text = self.sourceModel().data(index, self.role)        # 单元格的内容
            if i == self.column:
                self.filter_list[i] = _reg_exp
            # 多列过滤规则
            if self.filter_list[i] != "" and self.filter_list[i] != text:
                return False
        if self.column == 6 and _reg_exp != "":
            self.filter6 = _reg_exp
        if self.filter6 != "":
            if self.filter6 not in text6:
                return False
        return True

    def setFilterKeyColumn(self, column):
        self.column = column
        return column