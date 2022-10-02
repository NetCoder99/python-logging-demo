import multiprocessing
from   datetime import datetime

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
            print('\nFrom Reader  : {:16} : {}'.format(record, date_str), end='')
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)