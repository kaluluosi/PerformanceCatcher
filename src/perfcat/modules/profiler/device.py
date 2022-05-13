import re
from ppadb.client import Client as adb
from ppadb.device import Device


def device_info(dev: Device) -> dict:
    prop = dev.get_properties()
    info = {}
    info["品牌"] = prop["ro.product.brand"]  # 品牌
    info["制造商"] = prop["ro.product.manufacturer"]  # 制造商
    info["型号"] = prop["ro.product.model"]  # 型号
    info["名称"] = prop["ro.product.name"]  # 名称
    info["系统版本"] = prop["ro.build.version.release"]  # 系统版本
    info["SDK版本"] = prop["ro.build.version.sdk"]  # SDK版本
    info["首选SDK版本"] = prop["ro.product.first_api_level"]  # 首选SDK版本

    info["主板平台"] = prop["ro.board.platform"]

    info["CPU名称"] = __cpu_name(dev)
    info["CPU架构"] = prop["ro.product.cpu.abi"]  # CPU架构
    info["CPU核心"] = str(dev.cpu_count())
    freq = cpu_freq(dev)[0]
    info["CPU频率"] = f"{freq['min']/1000}MHZ - {freq['max']/1000}MHZ"

    gpu_info = __gpu_info(dev)
    info["GPU型号"] = f"{gpu_info['manufactor']} {gpu_info['name']}"
    info["OpenGL"] = gpu_info["opengl"]

    ram_info = __ram_info(dev)
    info["RAM"] = f"{ram_info['mem_total']/1024/1024:.2f}GB"
    info["SWAP"] = f"{ram_info['swap_total']/1024/1024:.2f}GB"

    info["ROOT"] = str(not dev.shell("su"))

    info["Serial"] = f"{dev.serial}"

    return info


def __ram_info(dev: Device) -> float:
    mem_total_str = dev.shell("cat /proc/meminfo|grep MemTotal")
    swap_total_str = dev.shell("cat /proc/meminfo|grep SwapTotal")

    mem_total = re.search("\d+", mem_total_str)
    swap_total = re.search("\d+", swap_total_str)

    return {"mem_total": int(mem_total.group()), "swap_total": int(swap_total.group())}


def __cpu_name(dev: Device) -> str:
    text: str = dev.shell("cat /proc/cpuinfo|grep Hardware")
    name = text.split(":")[1].lstrip()
    return name


def __gpu_info(dev: Device) -> dict:
    text: str = dev.shell("dumpsys SurfaceFlinger |grep GLES")
    text = text.split(":")[1]
    manufactor, name, opengl = text.split(",")[:3]
    return {
        "manufactor": manufactor.strip(),
        "name": name.strip(),
        "opengl": opengl.strip(),
    }


def cpu_freq(dev: Device) -> list:
    count = dev.cpu_count()
    freq = []
    for index in range(count):
        cmd_root = f"cat /sys/devices/system/cpu/cpu{index}/cpufreq"
        min = dev.shell(f"{cmd_root}/cpuinfo_min_freq")
        cur = dev.shell(f"{cmd_root}/scaling_cur_freq")
        max = dev.shell(f"{cmd_root}/cpuinfo_max_freq")

        freq.append({"min": int(min), "max": int(max), "cur": int(cur)})

    return freq
