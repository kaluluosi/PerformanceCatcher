#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   logcat_provider.py
@Time    :   2022/05/27 12:48:25
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   emm...
"""

# here put the import lib
import re
import subprocess
import pkg_resources
import logging
import time
from typing import Optional
from shutil import which
from PySide6.QtCore import QThread, QObject, SignalInstance, Signal

log = logging.getLogger(__name__)


class LogProvider(QThread):
    """
    Logcat数据提供者，只负责抓log数据然后解析成行然后发信号出去
    """

    new_log_added: SignalInstance = Signal(list)

    MAX_BUFFER_SIZE = 10000
    TIMEOUT = 1

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)

        self.process = None
        self.serial = None
        self.buffer = []
        self.last_flush_time = time.time()

    @property
    def adb_path(self):
        path = which("adb")
        default_adb_path = pkg_resources.resource_filename("perfcat", "adb/adb.exe")
        return path or default_adb_path

    def run(self) -> None:
        subprocess.call([self.adb_path, "-s", self.serial, "logcat", "-c"], shell=True)
        self.process = subprocess.Popen(
            [self.adb_path, "-s", self.serial, "logcat"],
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
        )

        while self.process.poll() is None:
            try:
                line = self.process.stdout.readline()
                parsed_line = self._parse(line)
                if parsed_line:
                    if len(self.buffer) >= self.MAX_BUFFER_SIZE or self.is_timeout:
                        self.flush()
                    else:
                        self.buffer.append(parsed_line)
            finally:
                continue

        log.debug("停止日志采集")

    def start(
        self, serial: str, priority: QThread.Priority = QThread.Priority.NormalPriority
    ) -> None:
        self.serial = serial
        return super().start(priority)

    def exit(self, retcode: int = 0) -> None:
        if self.process:
            self.process.kill()
        return super().exit(retcode)

    def flush(self):
        if self.buffer:
            self.new_log_added.emit(self.buffer)
            self.buffer.clear()
        self.last_flush_time = time.time()

    @property
    def is_timeout(self):
        return (time.time() - self.last_flush_time) > self.TIMEOUT

    def _parse(self, msg: str):
        try:
            r = re.search("(.*[0-9\s][VISFEWD]\s.*?):\s(.*)", msg)
            try:
                _data_list = r.group(1).split(" ")
            except Exception:
                return ["", "", "", "", "", "", msg]
            while "" in _data_list:
                _data_list.remove("")
            _content = r.group(2)
            _date = _data_list[0]
            _time = _data_list[1]
            _pid = _data_list[2]
            _tid = _data_list[3]
            _priority = _data_list[4]
            try:
                _tag = _data_list[5]
            except Exception:
                _tag = ""
            return [_date, _time, _pid, _tid, _priority, _tag, _content]
        except Exception as e:
            log.exception(msg)
            return None
