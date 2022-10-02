import sys
sys.path.append("./")
import logging

from app.logging_utils.logging_handler import get_file_handler, get_db_handler

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-9s - %(message)s')

def config():
  logger = logging.getLogger("app_logger")

  consoleHandler = logging.StreamHandler()
  consoleHandler.setFormatter(formatter)
  logger.addHandler(consoleHandler)

  logger.addHandler(get_file_handler("debug_handler",    "debug.log",    formatter, logging.DEBUG, file_mode="w"))
  logger.addHandler(get_file_handler("info_handler",     "info.log",     formatter, logging.INFO, file_mode="w"))
  logger.addHandler(get_file_handler("warning_handler",  "warning.log",  formatter, logging.WARNING, file_mode="w"))
  logger.addHandler(get_file_handler("error_handler",    "error.log",    formatter, logging.ERROR, file_mode="w"))
  logger.addHandler(get_file_handler("critical_handler", "critical.log", formatter, logging.CRITICAL, file_mode="w"))


  logger.addHandler(logging.StreamHandler())
  
  #logger.addHandler(get_db_handler("debug_handler",    "debug.log",    formatter, logging.DEBUG, file_mode="w"))
