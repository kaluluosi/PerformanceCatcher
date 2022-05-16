import re
import logging
from ppadb.client import Client
from ppadb.device import Device


log = logging.getLogger(__name__)


class FpsSampler:
    SURFACE_PARTTERN = "^{package_name}/com.[\w\.]+#\d$"

    def __init__(self, device: Device, package_name: str) -> None:
        self.device = device
        self._package_name = package_name
        self._surface_name = None

    @property
    def surface_name(self):
        result = self.device.shell(
            f"dumpsys SurfaceFlinger --list|grep ^{self._package_name}.*#"
        )
        # log.debug(f"找surface：{result}")
        return result

    @property
    def data(self) -> dict:
        """
        参考：https://zhuanlan.zhihu.com/p/67056913
        Returns:
            float: 帧率
        """
        data = {"fps": -1, "jank": -1, "big_jank": -1, "frametime": -1}

        if not self.surface_name:
            log.warning("没有找到surface")
            return data

        result: str = self.device.shell(
            f"dumpsys SurfaceFlinger --latency {self.surface_name}"
        )
        refresh_period, data_table = self._parse_data(result)
        if not data_table:
            log.warning(f"{self.surface_name} 没有数据")
            return data

        fps = self._calc_fps(data_table)
        jank, big_jank, frametime = self._calc_jank(data_table, refresh_period)
        return {"fps": fps, "jank": jank, "big_jank": big_jank, "frametime": frametime}

    def _parse_data(self, result: str):
        lines = result.strip().split("\n")
        refresh_period = float(lines[0])

        data = []
        if len(lines) > 1:
            for line in lines[1:]:
                line_data = [float(v) for v in line.split("\t")]
                data.append(line_data)
        data = list(filter(lambda v: sum(v) > 0, data))

        return refresh_period, data

    def _calc_jank(self, data_table, refresh_period):

        b_delta_list = []
        jank_count = 0
        big_jank_count = 0

        for index, data in enumerate(data_table):
            if index == 0:
                b_delta_list.append(0)
                continue

            delta = data_table[index][0] - data_table[index - 1][0]
            b_delta_list.append(delta)

            # 计算前3帧平均耗时
            if index < 3:
                continue

            pre_avg = sum(b_delta_list[index - 3 : index]) / 3
            if delta > pre_avg * 2 or delta > 83.33 * pow(10, 6):
                jank_count += 1

                if delta > 125 * pow(10, 6):
                    big_jank_count += 1

        frame_time = max([delta / pow(10, 6) for delta in b_delta_list])
        return jank_count, big_jank_count, frame_time

    def _calc_fps(self, data_table):
        frame_count = len(data_table)

        if frame_count == 1:
            return 0

        start_time = data_table[0][0]
        end_time = data_table[-1][0]

        duration = end_time - start_time
        # pow(10,9)是 1000000000 ，用来把纳秒转秒

        return frame_count * pow(10, 9) / duration


if __name__ == "__main__":
    adb = Client()
    dev = adb.devices(state="device")[0]
    # sampler = FpsSampler(dev, "com.mhatsh.eu")
    sampler = FpsSampler(dev, "com.xinyuanstu.bee")
    print(sampler.data)
