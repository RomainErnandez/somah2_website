import logging
from logging.handlers import RotatingFileHandler

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    # writing debug logs into log file
    file_handler = RotatingFileHandler('logs.log', 'a', 1000000, 1)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # writing debug logs into console
    steam_handler = logging.StreamHandler()
    steam_handler.setLevel(logging.ERROR)
    logger.addHandler(steam_handler)

    return logger