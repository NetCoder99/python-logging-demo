from datetime import datetime
import logging
import sys

now = datetime.now()
#date_time_str = now.strftime("%Y%m%d_%H%M%S")
date_time_str = now.strftime("%Y%m%d_%H")

def config(file_name:str):
    logging_formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)-9s :: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging_formatter)
    logger.addHandler(console_handler)

    #file_handler = logging.FileHandler('logs/file_{}.log'.format(date_time_str))
    file_handler = logging.FileHandler('logs/{}.log'.format(file_name))

    file_handler.setFormatter(logging_formatter)
    logger.addHandler(file_handler)