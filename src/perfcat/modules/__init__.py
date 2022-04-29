# todo: 之后要引入dotenv 根据开发和生产环境切换导入这个控件示例页面
from .widgets import Widgets
from .home import Home

from .profiler import Profiler

register = [Home, Profiler, Widgets]
