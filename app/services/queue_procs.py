import multiprocessing
import logging

# ----------------------------------------------------------------------------
# executed by import, configure logging options
# ----------------------------------------------------------------------------
logger = logging.getLogger("app_logger")

# ----------------------------------------------------------------------------
# this is the thread that reads from the queue and logs the 'queued' messages 
# ----------------------------------------------------------------------------
def LogQueueRecord(messageQueue: multiprocessing.Queue):
    while True:
        try:
            record = messageQueue.get()
            if record is None:  # We send this as a sentinel to tell the listener to quit.
                break
            logger.info(record)
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

