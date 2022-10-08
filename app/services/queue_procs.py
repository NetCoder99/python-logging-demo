import multiprocessing
from   datetime import datetime
import logging


# ----------------------------------------------------------------------------
# executed by import, configure logging options
# ----------------------------------------------------------------------------
#logger = logging.getLogger('root')
logger = logging.getLogger("app_logger")
#logger.setLevel(logging.DEBUG)
#log_formatter    = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#console_handler  = logging.StreamHandler()
#console_handler.setFormatter(log_formatter)
#logger.addHandler(console_handler)

# ----------------------------------------------------------------------------
# this is the thread that reads from the queue and prints the 'queued' messages 
# ----------------------------------------------------------------------------
def PrintQueueRecord(messageQueue: multiprocessing.Queue):
    while True:
        try:
            record = messageQueue.get()
            date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if record is None:  # We send this as a sentinel to tell the listener to quit.
                break
            #print('\nFrom Reader Printer : {:10} : {}'.format(record, date_str), end='')
            #logger.info('\nPrintQueueRecord Logger : {:10} : {}'.format(record, date_str))
            logger.info(record)
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

# ----------------------------------------------------------------------------
# this is the thread that reads from the queue and prints the 'queued' messages 
# ----------------------------------------------------------------------------
#def LogQueueRecord(messageQueue: multiprocessing.Queue):
#    while True:
#        try:
#            record = messageQueue.get()
#            date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#            if record is None:  # We send this as a sentinel to tell the listener to quit.
#                break
#            print('\nFrom Reader  : {:10} : {}'.format(record, date_str), end='')
#        except Exception:
#            import sys, traceback
#            print('Whoops! Problem:', file=sys.stderr)
#            traceback.print_exc(file=sys.stderr)