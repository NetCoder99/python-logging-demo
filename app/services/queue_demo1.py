from multiprocessing import Process
import multiprocessing
import random
import time
import logging
from services.queue_procs import LogQueueRecord

logger = logging.getLogger("app_logger")
loggingQueuePrint  = multiprocessing.Queue()

# ----------------------------------------------------------------------------
# a child process that is run in parallel, need this as pre-req for the 
# parallel processing syntax in python 
# ----------------------------------------------------------------------------
def PrintCountryName(loggingQueue: multiprocessing.Queue, continent:str='Asia', sleep_amt = .1):
    logString='PrintCountryName : {:10} : {}'.format(continent, sleep_amt)
    time.sleep(sleep_amt)
    loggingQueue.put(logString)

# =============================================================================
# this is the 'main' process, iterate over the objects, process in parallel???
# =============================================================================
def queue_demo1():
    
    logger.info  ("--- queue_demo - started")
    logger.debug ("--- queue_demo - started - debug")
    logger.warn  ("--- queue_demo - started - warn")
    logger.error ("--- queue_demo - started - error")

    names = ['America', 'Europe', 'Africa', "Japan", "China", "Italy"]
    procs = []

    # this is singleton thread that executes the logging function 
    logFunction = Process(target=LogQueueRecord, args=(loggingQueuePrint,))
    logFunction.start()

    # instantiating process with arguments
    logger.info("--- Instantiating processes")
    for name in names:
        wait_period = random.randint(1, 3)
        proc1 = Process(target=PrintCountryName, args=(loggingQueuePrint, name, wait_period))
        procs.append(proc1)

    # start all the threads
    logger.info("--- Starting processes")
    for proc in procs:
        proc.start()

    # wait for all 'processing' threads to complete
    logger.info("-----------------------------------------------")
    logger.info("--- Waiting on processes - started")
    logger.info("-----------------------------------------------")
    for proc in procs:
        proc.join()
    logger.info("-----------------------------------------------")
    logger.info("--- Waiting on processes - finished")
    logger.info("-----------------------------------------------")

    # signal the quest handler to quit
    logger.info("--- Killing message queue processer")
    loggingQueuePrint.put(None)

    # wait for the queue handler to finish
    logFunction.join()
    logger.info("--- All processing complete")
