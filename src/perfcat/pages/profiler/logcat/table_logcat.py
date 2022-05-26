
from perfcat.pages.profiler.logcat.view_model import StractViewModel
from perfcat.pages.profiler.logcat.ui_logtable import Ui_Logcat
from PySide6.QtWidgets import *
from perfcat.pages.profiler.logcat.table_model import StringListModel
from PySide6.QtCore import *
from PySide6.QtGui import *
from perfcat.pages.profiler.logcat.filter_proxy_model import SortFilterProxyModel
import subprocess
import re
import logging

log = logging.getLogger(__name__)


class WorkThread(QThread):
    # 实例化一个信号对象，类变量，需要定义在函数体外
    trigger = Signal(object)

    def __int__(self, model):
        super(WorkThread, self).__init__()

    def run(self):
        subprocess.call("adb -s {} logcat -c".format(self.serial), shell=True)
        self.process = subprocess.Popen(
            "adb -s {} logcat".format(self.serial),
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            encoding="utf-8",
        )
        self.fal = True
        self.log_gain()

    def log_gain(self):
        while self.process.poll() is None:
            if not self.fal:
                break
            try:
                data = self.process.stdout.readline()
            except Exception:
                data = "异常输出"
            if data == b"":
                if self.process.poll() is not None:
                    break
            else:
                self.trigger.emit(data)

    def stop(self):
        try:
            self.fal = False
            self.process.kill()
        except Exception:
            log.exception("未启动就关闭的日志线程！")

    # 用正则取出对应的数据
    def filter_rule(self, message):
        try:
            r = re.search("(.*[0-9\s][VISFEWD]\s.*?):\s(.*)", message)
            try:
                _data_list = r.group(1).split(" ")
            except Exception:
                return ["", "", "", "", "", "", message]
            while "" in _data_list:
                _data_list.remove("")
            _content = r.group(2)
            _date = _data_list[0]
            _time = _data_list[1]
            _pid = _data_list[2]
            _tid = _data_list[3]
            _priority = _data_list[4]
            try:
                _tag = _data_list[5]
            except Exception:
                _tag = ""
            return [_date, _time, _pid, _tid, _priority, _tag, _content]
        except Exception as e:
            log.exception(message)
            return -1

    # 把数据插入交给线程来做
    def insert_data(self, model, message):
        # message = self.filter_rule(message)
        # if message != -1:
        model.updateData(message)


class LogCat(QWidget, Ui_Logcat):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.log_list_gain = []  # 全部日志记录（列表）
        self.str_list = ""  # 全部日志记录（字符串）

        self.tableView.wordWrap = True
        # 表格model
        self.model = StringListModel([], ["日期", "时间", "PID", "TID", "优先级", "标签", "消息"])
        self.tableView.setModel(self.model)

        # 下拉框列表model
        self.drop_down = StractViewModel()
        self.cbx_tag.setModel(self.drop_down)
        completer = QCompleter(self.drop_down, self.cbx_tag)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.cbx_tag.setCompleter(completer)

        # 显示最后一行
        self.model.data_changed.connect(self.last_line)

        self.btn_empty.clicked.connect(self.remove_content)
        self.btn_save.clicked.connect(self.save_log)
        self.le_search.editingFinished.connect(lambda: self.on_tableview_content(self.le_search.text()))
        self.cbx_tag.editTextChanged.connect(self.on_tableview_tag)

        # 标记选中的图标
        self.pick_on = QIcon()
        self.pick_on.addFile(
            ":/icon/assets/svg/checkmark.svg", QSize(), QIcon.Normal, QIcon.Off
        )

        # 初始化列宽
        self.tableView.setColumnWidth(0, 40)
        self.tableView.setColumnWidth(1, 80)
        self.tableView.setColumnWidth(2, 45)
        self.tableView.setColumnWidth(3, 45)
        self.tableView.setColumnWidth(4, 45)

        # 创建线程
        self.threads = WorkThread(self)
        self.threads.trigger.connect(self.update_text)  # 当信号接收到消息时，更新数据
        # 过滤模型
        self.proxy = SortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)  # 传入需要处理的模型
        self.tableView.setModel(self.proxy)

        # 设置自动换行
        self.tableView.setWordWrap(True)
        # 隐藏行号
        self.tableView.verticalHeader().hide()

        # 点击标题时，发送一个信号
        self.horizontalHeader = self.tableView.horizontalHeader()
        self.horizontalHeader.sectionClicked.connect(
            self.on_view_horizontalHeader_sectionClicked
        )

    # 启动函数（跟随设备启动）
    def start_catch(self, serial):
        self.threads.serial = serial
        self.threads.start()

    # 关闭日志（跟随设备）
    def stop_catch(self):
        self.threads.stop()

    def update_text(self, message):
        self.str_list += message
        _message = self.threads.filter_rule(message)
        if _message != -1:
            self.threads.insert_data(self.model, _message)
            # 自适应宽度
            self.tableView.resizeRowToContents(self.model.rowCount() - 1)
            # 更新标签过滤的列表
            self.drop_down.update_one_data(_message[5])

    # 重写键盘监听事件
    def keyPressEvent(self, event):
        # 监听 CTRL+C 组合键，实现复制数据到粘贴板
        if (
            event.key() == Qt.Key_C
        ) and QApplication.keyboardModifiers() == Qt.ControlModifier:
            text = self.selected_tb_text(self.tableView)  # 获取当前表格选中的数据
            if text:
                QApplication.clipboard().setText(text)  # 复制数据到粘贴板

    # 处理选择的表格数据
    def selected_tb_text(self, table_view):
        try:
            indexes = table_view.selectedIndexes()  # 获取表格对象中被选中的数据索引列表
            text = ""
            indexes_dict = {}
            for index in indexes[::]:  # 遍历每个单元格
                row, column = index.row(), index.column()  # 获取单元格的行号，列号

                # 同一行则拼接字符串（暂时用空格拼接）
                if row in indexes_dict.keys():
                    indexes_dict[row] = (
                        indexes_dict[row]
                        + " "
                        + table_view.model().index(row, column).data()
                    )
                else:
                    indexes_dict[row] = table_view.model().index(row, column).data()

            for i in indexes_dict:
                text += indexes_dict[i] + "\n"
            return text
        except BaseException as e:
            log.exception(e)
            return ""

    def last_line(self):
        _visible_first = self.tableView.verticalScrollBar().value()     # 表格可见的第一行行号
        # _visible_total = self.tableView.verticalScrollBar().pageStep()  # 表格可见的行数范围
        maxium = self.tableView.verticalScrollBar().maximum()
        print(_visible_first, maxium)
        # 滚动条在底部某个范围时才触发实时显示底部内容
        # if _visible_first + _visible_total >= self.tableView.model().rowCount() - 10:
        #     # 保持滚动条在底部
        # self.tableView.scrollToBottom()
        if abs(maxium - _visible_first) < 2:
            QTimer.singleShot(0, self.tableView.scrollToBottom)

    # 清空列表（删除所有行，除了标题）
    def remove_content(self):
        # self.model.removeRows(0, self.model.rowCount())
        self.model.removeRows()

    def icon_show(self, column, menu_con):
        """
        传入2个参数（列数和菜单字符），返回需要创建的菜单图标

        根据过滤model存储的对应列数传入的正则进行判断的
        """
        if menu_con == self.proxy.filter_list[column]:
            return self.pick_on
        else:
            return QIcon()

    # 文件保存
    def save_log(self):
        _log = self.str_list
        try:
            filepath, type = QFileDialog.getSaveFileName(
                self, "文件保存", "/", "log(*.log)"
            )
            file = open(filepath, "w", encoding="utf-8")
            print(filepath)
            file.write(_log)
            file.close()
        except Exception:
            QMessageBox.critical(self, "错误", "没有指定保存的文件名")

    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        self.logicalIndex = logicalIndex  # 标题所在的列号下标
        if logicalIndex in [0, 1, 5, 6]:
            return
        self.menuValues = QMenu(self)
        self.signalMapper = QSignalMapper(self)

        # 获取当前列所有的数据
        valuesUnique = self.model.column_menu(self.logicalIndex)
        # 创建菜单（也就是点击标题后生成的）
        actionAll = QAction("显示全部", self)
        actionAll.triggered.connect(self.on_actionAll_triggered)  # 菜单选项绑定函数
        self.menuValues.addAction(actionAll)
        self.menuValues.addSeparator()

        # 根据获得的列数据批量创建菜单
        for actionNumber, actionName in enumerate(sorted(valuesUnique)):
            if actionName == "":
                continue
            action = QAction(actionName, self)
            action.setIcon(self.icon_show(self.logicalIndex, actionName))
            # 设置转发规则，转发 QAction 类型的信号，并把对应的菜单列号作为实参传递
            self.signalMapper.setMapping(action, actionNumber)
            action.triggered.connect(
                self.signalMapper.map
            )  # 将菜单发送的原始信号传递给 signalmapper
            self.menuValues.addAction(action)

        # 将转发的信号连接到最终的槽函数
        self.signalMapper.mappedInt.connect(self.on_signalMapper_mapped)

        headerPos = self.tableView.mapToGlobal(self.horizontalHeader.pos())

        posY = headerPos.y() + self.horizontalHeader.height()
        posX = headerPos.x() + self.horizontalHeader.sectionPosition(self.logicalIndex)
        # 循环执行（点击标题的坐标弹出菜单）
        self.menuValues.exec(QPoint(posX, posY))

    def on_actionAll_triggered(self):
        filterColumn = self.logicalIndex
        # 过滤规则
        filterString = QRegularExpression("")  # 正则表达式（空字符则默认匹配全部）

        self.proxy.setFilterKeyColumn(filterColumn)  # 过滤规则生效的列数
        self.proxy.setFilterRegularExpression(filterString)  # 传入过滤规则

    def on_signalMapper_mapped(self, i):
        stringAction = self.signalMapper.mapping(i).text()  # 获取对应菜单列号的列名称
        filterColumn = self.logicalIndex
        filterString = QRegularExpression(stringAction)
        self.proxy.setFilterKeyColumn(filterColumn)
        self.proxy.setFilterRegularExpression(filterString)

    def on_tableview_content(self, text):
        search = QRegularExpression(text)
        self.proxy.setFilterKeyColumn(6)
        self.proxy.setFilterRegularExpression(search)

    def on_tableview_tag(self, text):
        _tag = text
        if _tag == "ALL" or _tag == "":
            _tag = ""
        search = QRegularExpression(_tag)
        self.proxy.setFilterKeyColumn(5)
        self.proxy.setFilterRegularExpression(search)
