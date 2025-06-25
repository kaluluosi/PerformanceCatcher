from perfcat.components.profiler import MonitorCard
from perfcat.services import AndroidProfielerService,RecordService


class MemoryTotalPSSMonitorCard(MonitorCard):
    title = "Memory(APP Total PSS)"
    description = "APP Total PSS内存情况"

    def __init__(self) -> None:
        super().__init__()
        self.create_serie("pss")
        self.create_serie("private_dirty")
        self.create_serie("private_clean")
        self.create_serie("swapped_dirty")
        self.create_serie("heap_size")
        self.create_serie("heap_alloc")
        self.create_serie("heap_free")

        self.update_chart()

    async def sample(self, serialno: str, app: str, process: str):
        device = await AndroidProfielerService.get_device(serialno)
        app_memory_stat = await device.mem.stat(process)

        self._add_point("pss", round(app_memory_stat.pss/1000, 2))
        self._add_point("private_dirty", round(app_memory_stat.private_dirty/1000, 2))
        self._add_point("private_clean", round(app_memory_stat.private_clean/1000, 2))
        self._add_point("swapped_dirty", round(app_memory_stat.swapped_dirty/1000, 2))
        self._add_point("heap_size", round(app_memory_stat.heap_size/1000, 2))
        self._add_point("heap_alloc", round(app_memory_stat.heap_alloc/1000, 2))
        self._add_point("heap_free", round(app_memory_stat.heap_free/1000, 2))
        RecordService.logger.info(
            {"name":self.title,
             "pss": app_memory_stat.pss, 
             "private_dirty": app_memory_stat.private_dirty, 
             "private_clean": app_memory_stat.private_clean, 
             "swapped_dirty": app_memory_stat.swapped_dirty, 
             "heap_size": app_memory_stat.heap_size, 
             "heap_alloc": app_memory_stat.heap_alloc, 
             "heap_free": app_memory_stat.heap_free})
        self.update_chart()