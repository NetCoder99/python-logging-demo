import logging
from multiprocessing import Queue

def logger_process(queue: Queue):
    logger = logging.getLogger('app')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    while True:
        message = queue.get()
        if message is None:
            break
        print('message:{}'.format(message))
        logger.handle(message)