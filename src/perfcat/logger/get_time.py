from textwrap import wrap
import time
import logging
from functools import wraps
from typing import Callable

log = logging.getLogger(__name__)


def get_time(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s_time = time.time()
        res = func(*args, **kwargs)
        e_time = time.time()
        log.debug(f"{func.__name__} 耗时：{e_time-s_time}")
        return res

    return wrapper
