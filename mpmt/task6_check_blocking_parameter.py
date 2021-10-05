"""
The idea behind the blocking is like the toilet in a popular place
Tou go there try to door to open
if closed - go do you stuff and return when you will be free
otherwise - go to the toilet

the same for lots of threads they ask and if it was successful - do smth with lock

"""

import threading
import time
import logging
import random

counter = 0


def some_func(lock, number):
    global counter
    logging.info(f'Thread {number}: start')
    time.sleep(1)

    a = number * 2
    logging.info(f'Thread {number}: do personal work a:{a}')

    # ------

    lock.acquire(blocking=False)
    time.sleep(2)
    counter += random.randint(0, 3)
    logging.info(f'Thread {number}: did common work counter:{counter}')
    lock.release()

    time.sleep(4)
    a = number * 2
    logging.info(f'Thread {number}: do personal work a:{a}')

    # d1 = True
    # d2 = True
    #
    # while d1:
    #     if d1 and lock.acquire(blocking=False):       # | delete if and parameter
    #         d1 = False
    #         time.sleep(2)
    #         counter += random.randint(0, 3)
    #         logging.info(f'Thread {number}: did common work counter:{counter}')
    #         lock.release()
    #
    #     if d2:
    #         d2 = False
    #         time.sleep(1)
    #         a = number * 2
    #         logging.info(f'Thread {number}: do personal work a:{a}')


if __name__ == '__main__':
    form = '%(asctime)s: %(message)s'
    logging.basicConfig(format=form, level=logging.INFO, datefmt="%H:%M:%S")

    locker = threading.Lock()

    threads = [threading.Thread(target=some_func, args=(locker, i)) for i in range(3)]

    logging.info("Main:     start the threads")

    for thread in threads:
        thread.start()

    logging.info("Main:     wait for the thread to finish")

    for thread in threads:
        thread.join()

    logging.info("Main:     All the work is done")

"""
The difference is that we check if some of other threads work with the common data
if yes -> skip the task and continue 
else   -> do the tasks

but we should do it in a circle so to return and wait as it will be free

In this example it saves us only 1 second but it is 12.5% of all time. On nonblocking.py it saves 6 of 8 sec;


NOTE!!! If we work with blocking lock - it will lock only the data from .acquire() to .release() for 
"""