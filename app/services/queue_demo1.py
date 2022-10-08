from multiprocessing import Process
import multiprocessing
import random
import time
import logging
from services.queue_procs import PrintQueueRecord

logger = logging.getLogger("app_logger")
messageQueuePrint  = multiprocessing.Queue()

# ----------------------------------------------------------------------------
# a child process that is run in parallel, need this as pre-req for the 
# parallel processing syntax in python 
# ----------------------------------------------------------------------------
def PrintCountryName(messageQueue: multiprocessing.Queue, continent:str='Asia', sleep_amt = .1):
    #logger.info('From Printer : {:10} : {}'.format(continent, sleep_amt))
    #print('\nFrom Printer : {:10} : {}'.format(continent, sleep_amt), end='')
    logger.info('PrintCountryName : {:10} : {}'.format(continent, sleep_amt))
    time.sleep(sleep_amt)
    messageQueue.put(continent)

# =============================================================================
# this is the 'main' process, iterate over the objects, process in parallel???
# =============================================================================
def queue_demo1():
    logger.info("+++ queue_demo - started")

    names = ['America', 'Europe', 'Africa', "Japan", "China", "Italy"]
    procs = []

    printFunction = Process(target=PrintQueueRecord, args=(messageQueuePrint,))
    printFunction.start()

    # instantiating process with arguments
    print("+++ Instantiating processes")
    for name in names:
        wait_period = random.randint(1, 5)
        proc1 = Process(target=PrintCountryName, args=(messageQueuePrint, name, wait_period))
        procs.append(proc1)

    # start all the threads
    print("+++ Starting processes")
    for proc in procs:
        proc.start()

    # wait for all 'processing' threads to complete
    print("+++ Waiting on processes - started")
    for proc in procs:
        proc.join()
    print(" ")
    print("+++ Waiting on processes - finished")

    # signal the quest handler to quit
    print("+++ Killing message queue processer")
    messageQueuePrint.put(None)

    # wait for the queue handler to finish
    printFunction.join()
    print("+++ All processing complete")
