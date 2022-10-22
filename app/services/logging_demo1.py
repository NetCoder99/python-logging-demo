# from datetime import date, datetime
# import logging
# import logging.handlers
# import multiprocessing

# # Next two import lines for this demo only
# from random import choice, random
# import time

# # -----------------------------------------------------------------------------------
# def listener_configurer():
#     print('{} :started  :  {} \n'.format('listener_configurer',  str(time.time())))

#     root = logging.getLogger()
#     hndlr = logging.handlers.RotatingFileHandler('logs/mptest.log', 'a', 300, 10)
#     frmtr = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
#     hndlr.setFormatter(frmtr)
#     root.addHandler(hndlr)

# # -----------------------------------------------------------------------------------
# def listener_process(queue, configurer):
#     print('{} :started  :  {} \n'.format('listener_process',  str(time.time())))

#     configurer()
#     while True:
#         try:
#             record = queue.get()
#             print('record: {}'.format(record))
#             if record is None:  # We send this as a sentinel to tell the listener to quit.
#                 break
#             logger = logging.getLogger('root')
#             logger.handle(record)  # No level or filter logic applied - just do it!
#         except Exception:
#             import sys, traceback
#             print('Whoops! Problem:', file=sys.stderr)
#             traceback.print_exc(file=sys.stderr)


# # -----------------------------------------------------------------------------------
# #def worker_configurer(queue):
# #    print('worker_configurer:')
# #    hndlr = logging.handlers.QueueHandler(queue)  # Just the one handler needed
# #    root  = logging.getLogger('root')
# #    root.addHandler(hndlr)
# #    # send all messages, for demo; no other level or filter logic applied.
# #    root.setLevel(logging.DEBUG)            


# # -----------------------------------------------------------------------------------
# LEVELS = [logging.DEBUG, logging.INFO, logging.WARNING,
#           logging.ERROR, logging.CRITICAL]

# #LOGGERS = ['root', 'd.e.f']
# #LOGGERS = ['root']

# MESSAGES = [
#     'Random message #1',
#     'Random message #2',
#     'Random message #3',
# ]

# # -----------------------------------------------------------------------------------
# def worker_process(queue):
#     #configurer(queue)
#     name = multiprocessing.current_process().name
#     print('{} :started  :  {} \n'.format(name,  str(time.time())))

#     logger  = logging.getLogger('root')
#     logger.info('{} :processing  :  {} \n'.format(name,  str(time.time())))

#     #for i in range(5):
#     #    time.sleep(random())
#     #    logger  = logging.getLogger('root')
#     #    print('logger.name:{}'.format(logger.name))
#     #    level   = choice(LEVELS)
#     #    message = choice(MESSAGES)
#     #    logger.log(level, message)
    
#     print('{} :finished :  {} \n'.format(name,  str(time.time())))

# # -----------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------
# def logging_demo1():
#     queue    = multiprocessing.Queue(-1)
#     listener = multiprocessing.Process(target=listener_process,
#                                        args=(queue, listener_configurer))
#     listener.start()
#     listener.is_alive()
#     workers = []

#     for i in range(5):
#         worker = multiprocessing.Process(target=worker_process,
#                                          args=(queue, None))
#         workers.append(worker)
#         worker.start()

#     for w in workers:
#         w.join()

#     queue.put_nowait(None)

#     listener.join()    