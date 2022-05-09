from ppadb.device import Device
from ppadb.client import Client


def __cpu_max_freq(dev: Device) -> list:
    count = dev.cpu_count()
    freq = []
    for index in range(count):
        cmd_root = f"cat /sys/devices/system/cpu/cpu{index}/cpufreq"
        max = dev.shell(f"{cmd_root}/cpuinfo_max_freq")

        freq.append(int(max))

    return freq


def normalize(device: Device):

    # 合计所有CPU最大频率
    max_freq = __cpu_max_freq(device)
    total_max_freq = sum(max_freq)

    # 找出所有在在线的CPU
    online_cmd = "cat /sys/devices/system/cpu/online"
    online = device.shell(online_cmd)
    count = int(online.strip().split("-")[1])

    # 合计所有在线CPU的当前频率
    cur_freq_sum = 0
    for index in range(count):
        cmd_cur_freq = (
            f"cat /sys/devices/system/cpu/cpu{index}/cpufreq/scaling_cur_freq"
        )
        cur_freq = device.shell(cmd_cur_freq)
        cur_freq_sum += int(cur_freq)

    return cur_freq_sum / total_max_freq


if __name__ == "__main__":
    adb = Client()
    dev: Device = adb.devices()[0]
    print(normalize(0.5, dev))
