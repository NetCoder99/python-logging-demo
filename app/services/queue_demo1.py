from multiprocessing import Process
import multiprocessing
import random
import time
#from datetime import datetime

from services.queue_procs import PrintQueueRecord

messageQueueGlbl  = multiprocessing.Queue()

# ----------------------------------------------------------------------------
# a child process that is run in parallel, need this as pre-req for the 
# parallel processing syntax in python 
# ----------------------------------------------------------------------------
def PrintCountryName(messageQueue: multiprocessing.Queue, continent:str='Asia', sleep_amt = .1):
    print('\nFrom Printer : {} : {}'.format(sleep_amt, continent), end='')
    time.sleep(sleep_amt)
    messageQueue.put(continent)

# =============================================================================
# this is the 'main' process, iterate over the objects process parallel???
# =============================================================================
def queue_demo1():
    names = ['America', 'Europe', 'Africa', "Rusia", "Japan", "China", "Italy"]
    procs = []

    printFunction = Process(target=PrintQueueRecord, args=(messageQueueGlbl,))
    printFunction.start()

    # instantiating process with arguments
    print("+++ Instantiating processes")
    for name in names:
        wait_period = random.randint(1, 9)
        proc1 = Process(target=PrintCountryName, args=(messageQueueGlbl, name, wait_period))
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
    messageQueueGlbl.put(None)

    # wait for the queue handler to finish
    printFunction.join()
    print("+++ All processing complete")
