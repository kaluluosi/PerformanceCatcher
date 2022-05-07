import logging
from typing import Union
import PySide6
import math

from PySide6.QtCharts import (
    QChart,
    QLineSeries,
    QLegendMarker,
    QChartView,
    QValueAxis,
    QDateTimeAxis,
)
from PySide6.QtCore import Qt, QDateTime, QPoint, QRectF, QRect, QPointF
from PySide6.QtGui import QPainter, QMouseEvent, QPen, QBrush, QColor, QTextItem

log = logging.getLogger(__name__)


class MonitorChart(QChartView):
    def __init__(self, series_names: list[str] = [], parent=None):
        super().__init__(parent)

        _chart: QChart = QChart()
        self.series: dict[str, QLineSeries] = {}
        self.series_value_format: dict[str, str] = {}  # 值格式化
        self._mark_line: QPoint = QPoint()  # 标线坐标
        self._show_mark_line = True

        _chart.setTheme(QChart.ChartThemeDark)
        # self.chart.setBackgroundVisible(False)
        _chart.legend().setAlignment(Qt.AlignRight)
        _chart.setAnimationOptions(QChart.SeriesAnimations)

        self.setRenderHint(QPainter.Antialiasing)

        # 时间轴坐标用一个比较笨的方法去实现
        # 开始时间直接选择0时间戳时间，也就是1970年8:00:00
        # 之后采集到的数据以这个时间为基准+秒
        start_time = self._base_time()
        end_time = QDateTime(start_time).addSecs(60)
        self.axis_x = QDateTimeAxis(self)
        self.axis_x.setRange(start_time, end_time)
        self.axis_x.setFormat("mm:ss")
        _chart.addAxis(self.axis_x, Qt.AlignBottom)

        self.axis_y = QValueAxis(self)
        self.axis_y.setRange(0, 150)
        _chart.addAxis(self.axis_y, Qt.AlignLeft)

        # 创建并装载系列
        for s_name in series_names:
            series = QLineSeries(self)
            series.setName(s_name)
            self.series[s_name] = series
            _chart.addSeries(series)
            _chart.setAxisX(self.axis_x, series)
            _chart.setAxisY(self.axis_y, series)

        self.setChart(_chart)

        for mk in _chart.legend().markers():
            mk.clicked.connect(self._on_marker_clicked)

    def _base_time(self) -> QDateTime:
        return QDateTime.fromMSecsSinceEpoch(0)

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
            self._mark_line = scene_position
            self.scene().update()

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

    def drawForeground(
        self,
        painter: QPainter,
        rect: Union[QRectF, QRect],
    ) -> None:
        painter.save()

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
        for name, series in self.series.items():
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
        text_rect = QRectF(
            p1.x() + 10, p1.y() + 10, area_rect.width(), area_rect.height()
        )

        lines = []
        time = self._base_time().addMSecs(int(value_at_position.x()))
        lines.append(time.toString("mm:ss"))
        for name, point in points.items():
            if not self.series[name].isVisible():
                continue
            format = self.series_value_format.get(name, lambda v: v)
            lines.append(f"{name}: {format(point.y())}")
        text = "\n".join(lines)

        painter.drawText(text_rect, Qt.AlignLeft, text)

        painter.restore()

        return super().drawForeground(painter, rect)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.mark_line = event.pos()
        return super().mouseMoveEvent(event)

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:

        return super().paintEvent(event)

    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent) -> None:
        print("滚轮事件")
        return super().wheelEvent(event)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import (
        QApplication,
        QMainWindow,
        QPushButton,
        QVBoxLayout,
        QHBoxLayout,
        QWidget,
        QSlider,
    )
    from PySide6.QtCore import Qt, QThread, Signal, SignalInstance, QTimer
    from PySide6.QtGui import QPainter
    from PySide6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis
    import random

    app = QApplication(sys.argv)

    chart = MonitorChart(["CPU", "AppCpu"])

    s = chart.series["CPU"]
    chart.series_value_format["CPU"] = lambda v: f"{v}%"
    for i in range(200):
        bt = chart._base_time()
        bt = bt.addSecs(i)
        s.append(bt.toMSecsSinceEpoch(), random.randrange(1, 150))  # 必须用毫秒来做x轴

    s = chart.series["AppCpu"]
    for i in range(200):
        bt = chart._base_time()
        bt = bt.addSecs(i)
        s.append(bt.toMSecsSinceEpoch(), random.randrange(1, 150))  # 必须用毫秒来做x轴

    chart.resize(800, 400)
    chart.show()
    sys.exit(app.exec())
