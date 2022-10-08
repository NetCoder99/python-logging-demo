import logging
#from app.logging_utils.logging_handler import get_file_handler, get_db_handler

formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)-9s :: %(message)s', '%Y-%m-%d %H:%M:%S')

def config():
    logging.basicConfig(format='%(asctime)s :: %(name)s :: %(levelname)-9s :: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    #formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s","%Y-%m-%d %H:%M:%S")
    #logging.basicConfig(format=formatter)
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)
#    streamHandler = logging.StreamHandler()
#    streamHandler.setFormatter(formatter)
#    streamHandler.setLevel(logging.DEBUG)
#    logger.addHandler(streamHandler)
#    logger.propagate = False


    #logger
  #streamHandler = logging.StreamHandler()
  #streamHandler.setFormatter(formatter)
  #logger.addHandler(streamHandler)
  #logger.setLevel(logging.DEBUG)

  #logger.addHandler(get_file_handler("debug_handler",    "debug.log",    formatter, logging.DEBUG, file_mode="w"))
  #logger.addHandler(get_file_handler("info_handler",     "info.log",     formatter, logging.INFO, file_mode="w"))
  #logger.addHandler(get_file_handler("warning_handler",  "warning.log",  formatter, logging.WARNING, file_mode="w"))
  #logger.addHandler(get_file_handler("error_handler",    "error.log",    formatter, logging.ERROR, file_mode="w"))
  #logger.addHandler(get_file_handler("critical_handler", "critical.log", formatter, logging.CRITICAL, file_mode="w"))
  #logger.addHandler(logging.StreamHandler())
  #logger.addHandler(get_db_handler("debug_handler",    "debug.log",    formatter, logging.DEBUG, file_mode="w"))
