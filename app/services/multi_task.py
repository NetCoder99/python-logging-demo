# import logging
# from logging.handlers import QueueHandler
# from multiprocessing import current_process, Queue
# from random import random
# from time import sleep

# # task to be executed in child processes
# def multi_task1(queue: Queue):
#     logger = logging.getLogger('app')
#     logger.addHandler(QueueHandler(queue))
#     process = current_process()
#     logging.info(f'Child {process.name} starting.')

#     for i in range(5):
#         # report a message
#         logging.debug(f'Child {process.name} step {i}.')
#         sleep(random())

#     logging.info(f'Child {process.name} done.')