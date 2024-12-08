import logging
import os


def log_config() -> None:
    logging.basicConfig(
        level=os.getenv("LOGLEVEL", "INFO"),
        format="[%(asctime)s %(levelname)s %(filename)s:%(funcName)s:%(lineno)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S%z",
    )
