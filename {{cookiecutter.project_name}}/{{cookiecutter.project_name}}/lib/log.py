import logging
import sys
from typing import TextIO

FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S %z'

logger = logging.getLogger("{{cookiecutter.project_name}}")
logger.propagate = False


def setup_logger(level: str = None, stream: TextIO = sys.stdout):
    # clear logging default handlers
    logging.getLogger().handlers.clear()
    logger.handlers.clear()
    # add logger format
    formatter = logging.Formatter(FORMAT, TIMESTAMP_FORMAT)
    output_handler = logging.StreamHandler(stream)
    output_handler.setFormatter(formatter)
    logger.addHandler(output_handler)
    # set level
    logger.setLevel(level)
