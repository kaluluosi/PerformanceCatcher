import logging
import os
import shutil
from .android_profiler_service import AndroidProfielerService

class _RecordService:
    def __init__(self):
        self._logger = logging.getLogger("RecordService")
        self._logger.setLevel(logging.INFO)

    @property
    def logger(self):
        return self._logger

    async def init_logger(self,serialno:str, app:str, process:str):
        device = await AndroidProfielerService.get_device(serialno)
        model_name = await device.prop.get("ro.product.model")

        self.filehandler = logging.FileHandler("record.log", mode='a', encoding='utf-8')
        self.filehandler.addFilter(lambda record: record.name == "RecordService")
        self._logger.addHandler(self.filehandler)

        self._logger.info({
             "name":"info",
             "model":model_name,
             "app":app,
             "process":process
             })

    async def save_record(self,filename:str):
        # Placeholder for backup logic
        if os.path.exists("record.log"):
            self.filehandler.close()
            self._logger.removeHandler(self.filehandler)
            if not os.path.exists("records"):
                os.makedirs("records")
            shutil.move("record.log", f"records/{filename}.log")



RecordService = _RecordService()

