from PySide6.QtCore import Qt, QSortFilterProxyModel, QDate, QDateTime
import re

class MultiFilterMode:
    AND = 0
    OR = 1

class SortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, data, parent=None):
        super(SortFilterProxyModel, self).__init__(parent)
        self.role = Qt.DisplayRole
        self.minDate = QDate()
        self.maxDate = QDate()
        self.__data = data

    def setFilterMinimumDate(self, date):
        self.minDate = date
        self.invalidateFilter()

    def filterMinimumDate(self):
        return self.minDate

    def setFilterMaximumDate(self, date):
        self.maxDate = date
        self.invalidateFilter()

    def filterMaximumDate(self):
        return self.maxDate

    def filterAcceptsRow(self, sourceRow, sourceParent):
        # index0 = self.sourceModel().index(sourceRow, 0, sourceParent)
        # index1 = self.sourceModel().index(sourceRow, 1, sourceParent)
        index2 = self.sourceModel().index(sourceRow, 2, sourceParent)
        index3 = self.sourceModel().index(sourceRow, 3, sourceParent)
        index4 = self.sourceModel().index(sourceRow, 4, sourceParent)
        index5 = self.sourceModel().index(sourceRow, 5, sourceParent)
        print("index2", index2, self.filterRegExp().indexIn(self.sourceModel().data(index2, self.role)))
        print("index3", index3, self.filterRegExp().indexIn(self.sourceModel().data(index3, self.role)))
        print("index4", index4, self.filterRegExp().indexIn(self.sourceModel().data(index4, self.role)))
        print("index5", index5, self.filterRegExp().indexIn(self.sourceModel().data(index5, self.role)))
        return ((
                self.filterRegExp().indexIn(self.sourceModel().data(index2, self.role)) >= 0
                and self.filterRegExp().indexIn(self.sourceModel().data(index3, self.role)) >= 0
                and self.filterRegExp().indexIn(self.sourceModel().data(index4, self.role)) >= 0
                and self.filterRegExp().indexIn(self.sourceModel().data(index5, self.role)) >= 0
        ))

    def lessThan(self, left, right):
        leftData = self.sourceModel().data(left, self.role)
        rightData = self.sourceModel().data(right, self.role)

        if not isinstance(leftData, QDate):
            emailPattern = QRegExp("([\\w\\.]*@[\\w\\.]*)")

            if left.column() == 1 and emailPattern.indexIn(leftData) != -1:
                leftData = emailPattern.cap(1)

            if right.column() == 1 and emailPattern.indexIn(rightData) != -1:
                rightData = emailPattern.cap(1)

        return leftData < rightData

    def dateInRange(self, date):
        if isinstance(date, QDateTime):
            date = date.date()

        return ((not self.minDate.isValid() or date >= self.minDate)
                and (not self.maxDate.isValid() or date <= self.maxDate))