#!/usr/bin/env python3
""" Threads that waste CPU cycles """

import os
import multiprocessing as mp
import threading


# a simple function that wastes CPU cycles forever
def cpu_waster():
    while True:
        pass


print('Hi, my name is ', __name__)

# If we do not provide if statement - the mp module will execute line with mp.Process().start() many time
# and creating processes will never stop!
if __name__ == "__main__":
    # display information about this process
    print('\n  Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)

    print('\nStarting 12 CPU Wasters...')
    for i in range(6):
        mp.Process(target=cpu_waster).start()

    # display information about this process
    print('\n  Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)