from perfcat.components.profiler import MonitorCard
from perfcat.services import AndroidProfielerService,RecordService





class FPSMonitorCard(MonitorCard):
    title = "FPS"
    description = "帧率"

    def __init__(self) -> None:
        super().__init__()

        self.create_serie("FPS")
        self.create_serie("Jank")
        self.create_serie("Big-Jank")
        self.update_chart()

    async def sample(self, serialno: str, app: str, process: str):
        device = await AndroidProfielerService.get_device(serialno)
        stat = await device.fps.stat(process)
        self._add_point("FPS", round(stat.fps,2))
        self._add_point("Jank", stat.jank,type="bar")
        self._add_point("Big-Jank", stat.big_jank,type="bar")
        RecordService.logger.info({"name": self.title, "FPS": stat.fps, "Jank": stat.jank, "Big-Jank": stat.big_jank})
        self.update_chart()