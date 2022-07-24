# ----------------------------------------------------------------------------------------
# need this for vs code to find sibling and child directories
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# need this for vs code to find sibling and child directories
# ----------------------------------------------------------------------------------------
import sys
sys.path.append("./")

# ----------------------------------------------------------------------------------------
# other misc app related logging imports
# ----------------------------------------------------------------------------------------
import logging
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
try:
  
  test_logging_by_level("hello")

  logger.info(sqllite_demo.get_db_version())


except Exception as ex:
    print("Error while executing applicaiton", ex)
    logger.exception("error trapped by main:{}".format(ex))


