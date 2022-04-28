__version__ = "0.1.0"

import sys

# 把asset/放到搜索目录里，这样.ui文件里 import asset_rc 才能正常导入asset_rc
import pkg_resources

asset_dir = pkg_resources.resource_filename(__package__, "assets")
sys.path.append(asset_dir)


# 初始化模块
from .views import home, android_profiler
