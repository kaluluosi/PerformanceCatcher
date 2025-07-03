import asyncio
from perfcat.components.profiler import MonitorCard
from perfcat.services import AndroidProfielerService, RecordService


class CPUMonitorCard(MonitorCard):
    title = "CPU"
    description = "CPU使用率"

    def __init__(self) -> None:
        super().__init__(y_axis_unit="%")

        self.create_serie("Total CPU")
        self.create_serie("CPU")
        self.update_chart()

    async def sample(self, serialno: str, app: str, process: str):
        device = await AndroidProfielerService.get_device(serialno)
        app_cpu_usage, total_cpu_usage = await asyncio.gather(
            device.cpu.get_pid_cpu_usage(process), device.cpu.total_cpu_usage
        )
        total_cpu = round(total_cpu_usage.usage, 2)
        app_cpu = round(app_cpu_usage.usage, 2)
        self._add_point("Total CPU", total_cpu)
        self._add_point("CPU", app_cpu)
        RecordService.logger.info(
            {
                "name": self.title,
                "Total CPU": total_cpu_usage.usage,
                "CPU": app_cpu_usage.usage,
            }
        )
        self.update_chart()
