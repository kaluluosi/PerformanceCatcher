from typing import Optional
from ppadb.device import Device

UNIT_MAP = {"G": 1024, "M": 1}
PID = 0
USER = 1
PR = 2
NI = 3
VIRT = 4
RES = 5
SHR = 6
S = 7
CPU = 8
MEM = 9
TIME = 10
CMD = 11


def mem_str_to_num(value: str):
    unit = value[-1]
    if unit.isdigit():
        return float(value)

    unit_scale = UNIT_MAP.get(unit, 1)
    value = float(value[:-1]) * unit_scale
    return value


def top_to_dict(device: Device, pid: Optional[int] = None):
    cmd = "top -n 1 -m 100"
    if pid:
        cmd = f"top -n 1 -p {pid}"
    data = device.shell(cmd)
    lines = data.split("\n")

    result = {}

    def parse_line(result: dict, name: str, line: str):
        line = line.split(":")[1]
        result[name] = {}
        line_items = line.split(",")
        for item in line_items:
            value, field_name = item.split()
            if value[-1].isdigit():
                value = float(value)
            else:
                value = mem_str_to_num(value)

            result[name][field_name] = value

    def parse_cpu(result: dict, name: str, line: str):
        cpu_stat = {}
        line_items = line.split()
        for item in line_items:
            value, field_name = item.split("%")
            value = float(value)

            cpu_stat[field_name] = value

        cpu_stat["total"] = cpu_stat["cpu"] - cpu_stat["idle"]
        result[name] = cpu_stat

    parse_line(result, "tasks", lines[0])
    parse_line(result, "mem", lines[1])
    parse_line(result, "swap", lines[2])
    parse_cpu(result, "cpu", lines[3])

    # 处理进程
    processes = {}
    for line in lines[5:]:
        items = line.split()
        if not items[PID].isdigit():
            continue
        process = {
            "pid": int(items[PID]),
            "user": items[USER],
            "pr": items[PR],
            "ni": items[NI],
            "virt": mem_str_to_num(items[VIRT]),
            "res": mem_str_to_num(items[RES]),
            "shr": mem_str_to_num(items[SHR]),
            "s": items[S],
            "cpu": float(items[CPU]),
            "mem": float(items[MEM]),
            "time": items[TIME],
            "command": items[CMD],
        }

        processes[process["pid"]] = process
    result["processes"] = processes

    return result


if __name__ == "__main__":

    from ppadb.client import Client

    adb = Client()
    dev: Device = adb.devices()[0]

    a = top_to_dict(dev, 17210)
