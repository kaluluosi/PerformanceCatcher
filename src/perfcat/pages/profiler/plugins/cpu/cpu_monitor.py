from typing import Optional
from PySide6.QtWidgets import QWidget
from PySide6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis
from PySide6.QtCore import Qt

from ..base import Monitor
from .ui_cpu_monitor import Ui_CPUMonitor


class CPUMonitor(Monitor, Ui_CPUMonitor):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.chart_view = QChartView(self)

        self.frame.layout().addWidget(self.chart_view)

        self.chart = QChart()
        self.chart.setTitle("CPU")
        self.chart_view.setChart(self.chart)

        self.axisX = QValueAxis()
        self.axisX.setRange(200, 500)  # 设置坐标轴范围
        self.axisX.setLabelFormat("%d")  # 标签格式
        self.axisX.setTickCount(5)  # 主分隔个数
        # axisX.setMinorTickCount(4)
        self.axisX.setTitleText("x")  # 标题
        # axisX.setGridLineVisible(True)
        self.axisX.setMinorGridLineVisible(False)

        self.axisY = QValueAxis()
        self.axisY.setRange(50, 200)
        self.axisY.setLabelFormat("%d")  # 标签格式
        self.axisY.setTickCount(4)
        # axisY.setMinorTickCount(4)
        self.axisY.setTitleText("y")
        # axisY.setGridLineVisible(True)
        self.axisY.setMinorGridLineVisible(False)

        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)

        self.series = QLineSeries(self)
        self.series.setName("CPU")

        self.chart.addSeries(self.series)

        self.chart.setAxisX(self.axisX, self.series)
        self.chart.setAxisY(self.axisY, self.series)

        t = 250
        for i in range(1100):
            y = 0.2 * t + 12
            self.series.append(t, y)
            t += 20
