#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Chart.py
@Time    :   2022/05/07 16:18:16
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   

[1] 画出每个系列的最大值水位线
"""

# here put the import lib


import logging
import math
import PySide6

from typing import Union
from ppadb.device import Device
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QDateTimeAxis,
    QLegendMarker,
    QLineSeries,
    QValueAxis,
    QAbstractSeries,
    QAreaSeries,
)
from PySide6.QtCore import (
    QDateTime,
    QPoint,
    QPointF,
    QRect,
    QRectF,
    Qt,
    Signal,
    SignalInstance,
    QTimer,
    QThread,
)
from PySide6.QtGui import QBrush, QColor, QMouseEvent, QPainter, QPen, QWheelEvent
from PySide6.QtWidgets import QScrollBar


log = logging.getLogger(__name__)


class MonitorChart(QChartView):

    series_changed: SignalInstance = Signal()
    x_offset_changed: SignalInstance = Signal(int)
    x_max_offset_changed: SignalInstance = Signal(int)
    axis_range_size_changed: SignalInstance = Signal(int)
    mark_line_changed: SignalInstance = Signal(QPoint)

    INIT_RANGE_SIZE = 30

    def __init__(
        self,
        parent,
        series_names: list[str] = [],
        formatter: dict = {},
        y_axis_name="%",
    ):
        super().__init__(parent)
        self.setToolTip("")

        self.setMaximumHeight(300)
        self.setMinimumHeight(240)
        self.setStyleSheet("background-color:transparent;")

        _chart: QChart = QChart()
        _chart.layout().setContentsMargins(0, 0, 4, 0)
        _chart.legend().setMinimumWidth(150)
        _chart.legend().setMaximumWidth(150)

        self.device = None
        self.package_name = None
        self.sample_points = {}

        self.series_map: dict[str, QLineSeries] = {}
        self.formatter: dict[str, str] = formatter  # 值格式化
        self._mark_line: QPoint = QPoint()  # 标线坐标

        self.tick_count = 0

        self.total_x = 0  # x轴序列最大值
        self._axis_range_size = self.INIT_RANGE_SIZE  # 区间大小
        self._x_offset = 0  # 区间整体偏移

        self.recording = False
        self.record_range = [-1, -1]

        _chart.setTheme(QChart.ChartThemeDark)
        _chart.legend().setAlignment(Qt.AlignRight)
        # self.setRubberBand(QChartView.HorizontalRubberBand)
        # _chart.setAnimationOptions(QChart.SeriesAnimations)

        self.setRenderHint(QPainter.Antialiasing)

        # 时间轴坐标用一个比较笨的方法去实现
        # 开始时间直接选择0时间戳时间，也就是1970年8:00:00
        # 之后采集到的数据以这个时间为基准+秒
        self.axis_x = QDateTimeAxis(self)
        self.update_range()
        self.axis_x.setFormat("mm:ss")
        _chart.addAxis(self.axis_x, Qt.AlignBottom)

        self.axis_y = QValueAxis(self)
        self.axis_y.setRange(0, 100)
        self.axis_y.setTitleText(y_axis_name)
        _chart.addAxis(self.axis_y, Qt.AlignLeft)

        self.axis_x.rangeChanged.connect(self.update_x_offset)

        # 创建并装载系列
        for s_name in series_names:
            series = QLineSeries(self)
            series.setName(s_name)
            self.series_map[s_name] = series
            _chart.addSeries(series)

            pen = series.pen()
            pen.setWidth(1)
            series.setPen(pen)

            _chart.setAxisX(self.axis_x, series)
            _chart.setAxisY(self.axis_y, series)

        self.setChart(_chart)

        for mk in _chart.legend().markers():
            mk.clicked.connect(self._on_marker_clicked)

    def reset_series_data(self):
        """
        清空系列数据
        """
        for s in self.series_map.values():
            s.clear()

        self.total_x = 0
        self.record_range = [-1, -1]

    def sample(self, sec: int, device: Device, package_name: str):
        """每一tick更新数据，自己实现，然后通过addpoint添加数据点"""
        raise NotImplementedError

    def flush(self):
        """
        刷入采样数据

        _extended_summary_
        """
        for s_name, p in self.sample_points.items():
            self.series_map[s_name].append(*p)
        self.sample_points.clear()
        self.update()
        self.series_changed.emit()

    def _base_time(self) -> QDateTime:
        return QDateTime.fromMSecsSinceEpoch(0)

    def update_x_offset(self, min_d: QDateTime, max_d: QDateTime):
        offset = min_d.toSecsSinceEpoch() - self._base_time().toSecsSinceEpoch()
        self._x_offset = max(offset, 0)
        self._axis_range_size = max_d.toSecsSinceEpoch() - min_d.toSecsSinceEpoch()
        self.update_range()

    def axis_x_min(self):
        return self._base_time().addSecs(self._x_offset)

    def axis_x_max(self):
        return self.axis_x_min().addSecs(self._axis_range_size)

    def x_max_offset(self):
        return max(0, self.total_x - self._axis_range_size)

    @property
    def axis_range_size(self):
        """
        这个值是区间范围，每次缩放的时候会改变
        """
        return self._axis_range_size

    @axis_range_size.setter
    def axis_range_size(self, value):
        self._axis_range_size = max(self.INIT_RANGE_SIZE, value)
        self.update_range()

    @property
    def x_offset(self):
        return self._x_offset

    @x_offset.setter
    def x_offset(self, value):
        """
        通过修改这个值平移
        """
        self._x_offset = value
        self.update_range()
        self.x_offset_changed.emit(value)

    def set_x_offset(self, value):
        self.x_offset = value

    def update_range(self):
        self.axis_x.setRange(self.axis_x_min(), self.axis_x_max())

    @property
    def mark_line(self) -> QPoint:
        """
        获取标线坐标

        _extended_summary_

        Returns:
            QPoint: _description_
        """
        return self._mark_line

    @mark_line.setter
    def mark_line(self, point: QPoint):
        # refer to https://stackoverflow.com/a/44078533/9758790
        scene_position = self.mapToScene(point)
        chart_position = self.chart().mapFromScene(scene_position)
        value_at_position = self.chart().mapToValue(chart_position)

        if (
            self.axis_x.min().toMSecsSinceEpoch()
            < value_at_position.x()
            < self.axis_x.max().toMSecsSinceEpoch()
        ):
            self._mark_line = scene_position.toPoint()

        self.update()

    def _on_marker_clicked(self):
        mk: QLegendMarker = self.sender()
        mk.series().setVisible(not mk.series().isVisible())
        mk.setVisible(True)
        log.debug(f"设置图例显隐：{mk.series().name()} {mk.series().isVisible()}")

        # 隐藏系列的时候对图例样式做个表现
        # 参考自官方：https://doc.qt.io/qt-5/qtcharts-legendmarkers-example.html

        alpha = 1.0
        if not mk.series().isVisible():
            alpha = 0.5

        brush = mk.labelBrush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        mk.setLabelBrush(brush)

        brush = mk.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        mk.setBrush(brush)

        brush = mk.pen()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        mk.setPen(brush)

    def add_point(self, s_name: str, x: float, y: float):
        """
        加数据点
        """

        # series: QLineSeries = self.series_map.get(s_name)
        time = self._base_time().addSecs(x)
        # series.append(time.toMSecsSinceEpoch(), y)

        pre_total_x = self.total_x
        self.total_x = max(self.total_x, x)
        if pre_total_x != self.total_x:
            self.x_max_offset_changed.emit(self.x_max_offset())

        y_max = max(self.axis_y.max(), y)
        self.axis_y.setMax(y_max)

        self.sample_points[s_name] = (time.toMSecsSinceEpoch(), y)

        self.tick_count = x

        if self.recording:
            self.record_range[1] = self.tick_count

    def drawForeground(
        self,
        painter: QPainter,
        rect: Union[QRectF, QRect],
    ) -> None:
        painter.save()

        # 绘制标线
        _start = self._base_time().addSecs(self.record_range[0])
        _end = self._base_time().addSecs(self.record_range[1])

        _start: QDateTime = max(self.axis_x_min(), min(_start, self.axis_x_max()))
        _end: QDateTime = max(self.axis_x_min(), min(_end, self.axis_x_max()))

        start = (
            self.chart().mapToPosition(QPointF(_start.toMSecsSinceEpoch(), 0)).toPoint()
        )
        end = self.chart().mapToPosition(QPointF(_end.toMSecsSinceEpoch(), 0)).toPoint()
        color = QColor("#007acc")
        color.setAlphaF(0.8)
        pen = QPen(color)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.setBrush(QBrush(color, Qt.SolidPattern))
        painter.drawRect(start.x(), start.y() + 1, end.x() - start.x(), 3)

        if self.mark_line.x() == 0:
            painter.restore()
            return

        # 绘制标线
        pen = QPen(QColor("white"))
        pen.setWidth(1)
        painter.setPen(pen)

        area_rect = self.chart().plotArea()

        p1 = QPointF(self.mark_line.x(), area_rect.top())
        p2 = QPointF(self.mark_line.x(), area_rect.bottom())

        painter.drawLine(p1, p2)

        chart_position = self.chart().mapFromScene(self.mark_line)
        value_at_position = self.chart().mapToValue(chart_position)

        points = {}

        # 绘制值点
        for name, series in self.series_map.items():
            pen2 = QPen(series.color())
            pen2.setWidth(10)
            painter.setPen(pen2)

            # 找到最近的点

            # 遍历所有点

            nearest_left = None
            nearest_right = None
            exact_point = None
            last_diff = 0  # 上次的差值

            for p in series.pointsVector():

                if nearest_left is None:
                    # 如果最左为空，那么先设置最左为p
                    nearest_left = p
                    last_diff = p.x() - value_at_position.x()
                    continue

                if p.x() == value_at_position.x():
                    # 鼠标所在横坐标正好有一个点，就直接退出了
                    exact_point = p
                    nearest_left = None
                    nearest_right = None
                    break

                # 不然就逼近
                diff = p.x() - value_at_position.x()
                if math.copysign(1, diff) + math.copysign(1, last_diff) == 0:
                    nearest_right = p
                    break
                else:
                    nearest_left = p
                    last_diff = diff

            if exact_point:
                painter.drawPoint(
                    self.chart().mapToScene(self.chart().mapToPosition(exact_point))
                )
                points[series.name()] = exact_point
            elif nearest_left and nearest_right:
                # 斜率
                k = (nearest_right.y() - nearest_left.y()) / (
                    nearest_right.x() - nearest_left.x()
                )
                # 插值点
                point_interp_y = nearest_left.y() + k * (
                    value_at_position.x() - nearest_left.x()
                )
                # print(point_interp_y)
                point_interp_x = value_at_position.x()
                point_intrep = QPoint(point_interp_x, point_interp_y)

                painter.drawPoint(self.chart().mapToPosition(point_intrep))
                points[series.name()] = point_intrep

        # 绘制信息label
        painter.setPen(QPen(QColor("white")))
        scene_rect = self.sceneRect()
        text_rect = QRectF(
            p1.x() + 10, p1.y() + 10, scene_rect.width(), scene_rect.height()
        )

        lines = []
        time = self._base_time().addMSecs(int(value_at_position.x()))
        lines.append(time.toString("mm:ss"))
        for name, point in points.items():
            if not self.series_map[name].isVisible():
                continue
            format = self.formatter.get(name, lambda v: v)
            lines.append(f"{name}: {format(point.y())}")
        text = "\n".join(lines)

        painter.drawText(text_rect, Qt.AlignLeft, text)

        painter.restore()
        return super().drawForeground(painter, rect)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.mark_line = event.pos()
        self.mark_line_changed.emit(event.pos())
        return super().mouseMoveEvent(event)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if self.chart().plotArea().contains(event.position()):
            sign = int(math.copysign(1, event.angleDelta().y()))
            self.axis_range_size += sign * 10
            self.axis_range_size_changed.emit(self.axis_range_size)
            self.x_max_offset_changed.emit(self.x_max_offset())
        else:
            # 莫名其妙的会上下滚动，找不到原因，暂时屏蔽掉基类的滚动
            # return super().wheelEvent(event)
            event.ignore()  #  event传进来的时候默认是setaccept(True)的，因此我们要ignore掉让其传递到父widget去处理，比如滚动

    def to_dict(self) -> dict:
        """
        series 转字典

        _extended_summary_

        Returns:
            dict: _description_
        """
        data = {}

        for s_name, s in self.series_map.items():
            if s_name not in data:
                data[s_name] = []

            for p in s.points():
                data[s_name].append((p.x(), p.y()))

        return data

    def from_dict(self, data: dict):
        """
        把字典的值读取转series

        _extended_summary_

        Args:
            value (_type_): _description_
        """
        for s_name, s in self.series_map.items():
            if s_name not in data:
                log.error(f"data里没有 {s_name}系列的数据")
                continue

            for p in data[s_name]:
                s.append(p[0], p[1])

    def record_enable(self, enable: bool):
        self.recording = enable
        if enable:
            self.record_range = [self.tick_count, self.tick_count]


if __name__ == "__main__":
    import random
    import sys

    from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
    from PySide6.QtCore import Qt, QThread, QTimer, Signal, SignalInstance
    from PySide6.QtGui import QPainter
    from PySide6.QtWidgets import (
        QApplication,
        QHBoxLayout,
        QMainWindow,
        QPushButton,
        QSlider,
        QScrollBar,
        QVBoxLayout,
        QWidget,
    )

    class Win(QWidget):
        def __init__(self, parent=None) -> None:
            super().__init__(parent)
            # self.setStyleSheet("background-color:red")

            self.chart_view1 = MonitorChart(parent, ["CPU"])
            self.chart_view1.setObjectName("c1")
            self.chart_view2 = MonitorChart(parent, ["GPU"])
            self.chart_view2.setObjectName("c2")
            self.chart_views = [self.chart_view1, self.chart_view2]
            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(0, 0, 0, 0)
            self.layout.addWidget(self.chart_view1)
            self.layout.addWidget(self.chart_view2)

            for i in range(1000):
                self.chart_view1.add_point("CPU", i, random.randrange(150))
            for i in range(1000):
                self.chart_view2.add_point("GPU", i, random.randrange(150))

            self.h_scrollbar = QScrollBar(Qt.Horizontal, self)
            self.h_scrollbar.setMaximum(self.chart_view1.x_max_offset())
            self.layout.addWidget(self.h_scrollbar)

            self.v = 0

            self.h_scrollbar.valueChanged.connect(self.scroll_changed)
            for c in self.chart_views:
                c.axis_range_size_changed.connect(self.range_size_changed)
                c.mark_line_changed.connect(self.on_mark_line_changed)
            self.startTimer(1000)

        def timerEvent(self, event: PySide6.QtCore.QTimerEvent) -> None:
            return super().timerEvent(event)

        def on_mark_line_changed(self, point):
            sender = self.sender()
            for chartview in self.chart_views:
                if chartview == sender:
                    continue
                chartview.mark_line = sender.mark_line
                print(chartview.objectName(), chartview.mark_line)

        def range_size_changed(self, size):
            sender = self.sender()
            for chartview in self.chart_views:
                if chartview == sender:
                    continue
                chartview.axis_range_size = size

        def scroll_changed(self, v):
            self.chart_view1.set_x_offset = v
            self.chart_view2.set_x_offset = v

    app = QApplication(sys.argv)

    widget = Win()

    widget.resize(800, 400)
    widget.show()
    sys.exit(app.exec())
