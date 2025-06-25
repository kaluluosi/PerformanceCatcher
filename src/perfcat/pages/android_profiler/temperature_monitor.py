from perfcat.components.profiler import MonitorCard
from perfcat.services import AndroidProfielerService,RecordService


class TemperatureMonitorCard(MonitorCard):
    title = "Temperature"
    description = "设备温度情况"

    def __init__(self) -> None:
        super().__init__()
        self.create_serie("CPU温度")
        self.create_serie("GPU温度")
        self.create_serie("体感温度")
        self.create_serie("电池温度")
        self.update_chart()

    async def sample(self, serialno: str, app: str, process: str):
        device = await AndroidProfielerService.get_device(serialno)

        stat = await device.temp.stat()
        self._add_point("CPU温度", round(stat.cpu, 2))
        self._add_point("GPU温度", round(stat.gpu, 2))
        self._add_point("体感温度", round(stat.skin, 2))
        self._add_point("电池温度", round(stat.battery, 2))
        RecordService.logger.info({
            "name": self.title,
            "CPU温度": stat.cpu,
            "GPU温度": stat.gpu,
            "体感温度": stat.skin,
            "电池温度": stat.battery
        })
        self.update_chart()