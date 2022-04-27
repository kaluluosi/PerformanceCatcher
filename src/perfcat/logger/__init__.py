import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(filename)s:%(lineno)d - %(message)s",
    handlers=[
        logging.FileHandler("debug.log", mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
