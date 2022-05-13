from ppadb.client import Client
from ppadb.device import Device


class TempUtil:

    TEMP_FILE_PATHS = [
        "/sys/devices/system/cpu/cpu0/cpufreq/cpu_temp",
        "/sys/devices/system/cpu/cpu0/cpufreq/FakeShmoo_cpu_temp",
        "/sys/class/thermal/thermal_zone0/temp",
        "/sys/class/i2c-adapter/i2c-4/4-004c/temperature",
        "/sys/devices/platform/tegra-i2c.3/i2c-4/4-004c/temperature",
        "/sys/devices/platform/omap/omap_temp_sensor.0/temperature",
        "/sys/devices/platform/tegra_tmon/temp1_input",
        "/sys/kernel/debug/tegra_thermal/temp_tj",
        "/sys/devices/platform/s5p-tmu/temperature",
        "/sys/class/thermal/thermal_zone1/temp",
        "/sys/class/hwmon/hwmon0/device/temp1_input",
        "/sys/devices/virtual/thermal/thermal_zone1/temp",
        "/sys/devices/virtual/thermal/thermal_zone0/temp",
        "/sys/class/thermal/thermal_zone3/temp",
        "/sys/class/thermal/thermal_zone4/temp",
        "/sys/class/hwmon/hwmonX/temp1_input",
        "/sys/devices/platform/s5p-tmu/curr_temp",
    ]

    def __init__(self, device: Device) -> None:
        self.device = device
        self.cpu_temp_valid_path = None

    def cpu_temp(self):

        if not self.cpu_temp_valid_path:
            for path in self.TEMP_FILE_PATHS:
                temp = self.__try_get_temp(path)
                if temp is None:
                    continue
                else:
                    return temp
        else:
            return self.__try_get_temp(self.cpu_temp_valid_path)

    def __try_get_temp(self, path):
        try:
            print(f"读取 {path}")
            result = self.device.shell(f"cat {path}")
            temp = float(result)
            print(f"{temp} valid {self.is_temp_valid(temp)}")
            print(f"{temp/1000} valid {self.is_temp_valid(temp/1000)}")
            if self.is_temp_valid(temp):
                self.cpu_temp_valid_path = path
                return temp
            elif self.is_temp_valid(temp / 1000):
                self.cpu_temp_valid_path = path
                return temp / 1000
        except Exception as e:
            print(e)
            return None

    def is_temp_valid(self, value):
        return -30 <= value <= 250


if __name__ == "__main__":
    from ppadb.client import Client

    adb = Client()
    dev = adb.devices()[0]

    util = TempUtil(dev)
    print("第一次", util.cpu_temp())
    print("第二次", util.cpu_temp())
