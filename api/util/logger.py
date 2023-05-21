import os
import logging
import sys

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')


def setup_logging():
    logger = logging.getLogger()
    for h in logger.handlers:
        logger.removeHandler(h)

    h = logging.StreamHandler(sys.stdout)

    # use whatever format you want here
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    h.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(h)

    if LOG_LEVEL == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    return logger
