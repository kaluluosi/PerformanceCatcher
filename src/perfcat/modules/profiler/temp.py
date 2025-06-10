import logging
import re
from typing import List
from ppadb.client import Client
from ppadb.device import Device

log = logging.getLogger(__name__)


class MarkTempSampler:

    def __init__(self, device: Device) -> None:
        self.device = device

    def get_temp(self):
        
        output:str = self.device.shell("dumpsys hardware_properties")
        # 正则表达式匹配 CPU temperatures: [33.042] 中的 33.042 
        r_cpu_temp = re.findall(r"CPU temperatures: \[(.*?)\]", output) 
        # 正则表达式匹配 GPU temperature: [33.042] 中的 33.042
        r_gpu_temp = re.findall(r"GPU temperatures: \[(.*?)\]", output) 
        # 正则表达式匹配 Battery temperature: [33.042] 中的 33.042
        r_battery_temp = re.findall(r"Battery temperatures: \[(.*?)\]", output) 
        # 正则表达式匹配 Skin temperature: [33.042] 中的 33.042
        r_skin_temp = re.findall(r"Skin temperatures: \[(.*?)\]", output) 

        if not r_cpu_temp:
            cpu_temp = 0
        else:
            if not r_cpu_temp[0]:
                cpu_temp = 0
            else:
                cpu_temp = float(r_cpu_temp[0])

        if not r_gpu_temp:
            gpu_temp = 0
        else:
            if not r_gpu_temp[0]:
                gpu_temp = 0
            else:
                gpu_temp = float(r_gpu_temp[0])

        if not r_battery_temp:
            battery_temp = 0
        else:
            if not r_battery_temp[0]:
                battery_temp = 0
            else:
                battery_temp = float(r_battery_temp[0])

        if not r_skin_temp:
            skin_temp = 0
        else:
            if not r_skin_temp[0]:
                skin_temp = 0
            else:
                skin_temp = float(r_skin_temp[0])

        return {
            "cpu": cpu_temp,
            "gpu": gpu_temp,
            "skin": skin_temp,
            "battery": battery_temp,
        }

if __name__ == "__main__":
    from ppadb.client import Client

    adb = Client()
    dev = adb.devices()[0]
    print(dev.serial)

    util = MarkTempSampler(dev)
    print(util.get_temp())
    print("all", util.get_temp())
