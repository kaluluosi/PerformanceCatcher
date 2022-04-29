import logging
import sys
import traceback


def log_unhandled_exception(*exc_info):
    text = "".join(traceback.format_exception(*exc_info))
    logging.exception("未捕获的异常: {0}".format(text))


sys.excepthook = log_unhandled_exception

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(filename)s:%(lineno)d - %(message)s",
    handlers=[
        logging.FileHandler("debug.log", mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
