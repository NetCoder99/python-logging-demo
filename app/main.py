# ----------------------------------------------------------------------------------------
# need this for vs code to find sibling and child directories
# ----------------------------------------------------------------------------------------
import multiprocessing
import sys
import logging
from services.queue_demo1 import queue_demo1
#from services.multi_demo1 import multi_demo1
#from services.logging_demo1 import logging_demo1

sys.path.append("./")

# ----------------------------------------------------------------------------------------
# other misc app related logging imports
# ----------------------------------------------------------------------------------------
from   logging_utils import logging_config
from   database_utils import sqllite_demo

# ----------------------------------------------------------------------------------------
# configure the basic logging handlers, formatting, etc
# ----------------------------------------------------------------------------------------
logging_config.config()
logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

# ----------------------------------------------------------------------------------------
# test the logging handlers 
# ----------------------------------------------------------------------------------------
def test_logging_by_level(msg):
  logger.debug   ("debug    - test:{}".format(msg))
  logger.info    ("info     - test:{}".format(msg))
  logger.warning ("warning  - test:{}".format(msg))
  logger.error   ("error    - test:{}".format(msg))
  logger.critical("critical - test:{}".format(msg))

# ----------------------------------------------------------------------------------------
# main process to execute 
# ----------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        print("Number of cpu : ", multiprocessing.cpu_count())
        queue_demo1()

    except Exception as ex:
        print("Error while executing applicaiton", ex)
        logger.exception("error trapped by main:{}".format(ex))


