import logging
import sys

# 配置baseconfig，让logging可以输出到文件，日志不追加，而是覆盖
logging.basicConfig(
	level=logging.WARNING,
	filename='app.log',
	encoding="utf-8"
)

# 捕获未处理异常，输出到日志文件

def handle_exception(exc_type, exc_value, exc_traceback):
	if issubclass(exc_type, KeyboardInterrupt):
		sys.__excepthook__(exc_type, exc_value, exc_traceback)
		return
	logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception

