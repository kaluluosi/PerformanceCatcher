
"""
## 纯QEvent方案（失败）

app实现设备热拔插事件，然后自上而下广播给page。

Qt中，事件是由下而上传递，app.sendEvent 不会往下传递给所有子widget。
反过来子widget.sendEvent只要没被accept就会一直往上传递

因此无法靠自定义QEvent的方式广播 usb设备 热拔插事件给所有pages

## EventFilter+Signal方案 

自定义EventFilter，创建一个单例EventFilter然后安装到app上。
因为EventFilter是个单例，所以所有page都可以引入去connect他的signal。


"""

import sys

if sys.platform == 'win32':
    from .win import WinHotPlugNativeEventFilter as HotPlugNativeEventFilter

elif sys.platform == 'linux':
    from .linux import LinuxHotPlugNatvieEventFilter as HotPlugNativeEventFilter
elif sys.platform == 'darwin':
    from .base import BaseHotPlugNativeEventFilter as HotPlugNativeEventFilter

HotPlugWatcher = HotPlugNativeEventFilter()