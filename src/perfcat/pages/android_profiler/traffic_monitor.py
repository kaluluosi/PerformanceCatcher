"""
author:        kaluluosi111 <kaluluosi@gmail.com>
date:          2025-06-29 20:48:00
Copyright © Kaluluosi All rights reserved
"""

from perfcat.components.profiler import MonitorCard
from perfcat.services import AndroidProfielerService, RecordService


class TrafficMonitorCard(MonitorCard):
    title = "Traffic"
    description = "流量使用情况"

    def __init__(self) -> None:
        super().__init__(y_axis_unit="byte")

        self.create_serie("recivce")
        self.create_serie("send")
        self.update_chart()

    async def sample(self, serialno: str, app: str, process: str):
        dev = await AndroidProfielerService.get_device(serialno)
        stat = await dev.traffic.stat()

        self._add_point("recivce", stat.receive)
        self._add_point("send", stat.send)
        RecordService.logger.info(
            {"name": self.title, "recive": stat.receive, "send": stat.send}
        )
        self.update_chart()
