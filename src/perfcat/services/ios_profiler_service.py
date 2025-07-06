"""
author:        kaluluosi111 <kaluluosi@gmail.com>
date:          2025-07-06 12:08:50
Copyright © Kaluluosi All rights reserved
"""

from ios_device.util.usbmux import USBMux


class _IOSProfilerService:
    def __init__(self) -> None: ...

    @property
    def devices(self):
        with USBMux() as mux:
            return mux.get_devices()


IOSProfilerService = _IOSProfilerService()
