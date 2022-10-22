# from multiprocessing import Process
# import random
# from time import sleep

# def print_func(continent='Asia'):
#     sleep(random.randint(1, 9)/1000)
#     print('\nThe name of continent is : {}'.format(continent), end='')

# def multi_demo1():
#     names = ['America', 'Europe', 'Africa', "Rusia", "Japan","China"]
#     procs = []
#     proc = Process(target=print_func)  # instantiating without any argument
#     procs.append(proc)
#     proc.start()

#     # instantiating process with arguments
#     for name in names:
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()

#     # complete the processes
#     for proc in procs:
#         proc.join()