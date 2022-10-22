# ----------------------------------------------------------------------------------------
# need this for vs code to find sibling and child directories
# ----------------------------------------------------------------------------------------
import multiprocessing
import logging
from   datetime import datetime

# ----------------------------------------------------------------------------------------
# other misc app related logging imports
# ----------------------------------------------------------------------------------------
from services.queue_demo1 import queue_demo1
from logging_utils        import logging_config

# ----------------------------------------------------------------------------------------
# configure the basic logging handlers, formatting, etc
# ----------------------------------------------------------------------------------------
now = datetime.now()
#fileName = "log_{}".format(now.strftime("%Y%m%d_%H%M"))
fileName = "log_{}".format(now.strftime("%Y%m%d"))
logging_config.config(fileName, logging.DEBUG)
logger = logging.getLogger("app_logger")

# ----------------------------------------------------------------------------------------
# main process to execute 
# ----------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        now = datetime.now()
        date_time_str = now.strftime("%Y%m%d_%H%M%S")
        logger.info("===============================================")

        logger.info("+++ main: started  +++")
        logger.info("+++ Number of cpu: {}".format(multiprocessing.cpu_count()))
        queue_demo1()
        logger.info("+++ main: finished +++")
        logger.info("===============================================")

    except Exception as ex:
        print("Error while executing applicaiton", ex)
        logger.exception("error trapped by main:{}".format(ex))


