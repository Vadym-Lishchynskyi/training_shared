""" Three philosophers, thinking and eating sushi """
import threading
import time
from random import random

lock_1 = threading.Lock()
lock_2 = threading.Lock()
lock_3 = threading.Lock()
sushi_count = 500


def philosopher(name, first_lock, second_lock):
    global sushi_count

    while sushi_count > 0:  # eat sushi until it's all gone
        first_lock.acquire()

        if not second_lock.acquire(blocking=False):
            print(name, 'release the first lock (lock_1)')
            first_lock.release()

            """
                The threads will just constantly acquire() and release() first_lock and 
                will be stack in what is called live-lock. It works but will never end.
                It will be in live-lock unless we make random stop for a thread for some time. 
                
            """

            time.sleep(random()/10)

        else:
            try:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(name, 'took a piece! Sushi remaining:', sushi_count)
            finally:
                second_lock.release()
                first_lock.release()


if __name__ == '__main__':
    threading.Thread(target=philosopher, args=('Barron', lock_1, lock_2)).start()
    threading.Thread(target=philosopher, args=('Olivia', lock_2, lock_3)).start()
    threading.Thread(target=philosopher, args=('Steve', lock_3, lock_1)).start()
    """The order of locks are such that it will be deadlock if we don't change it or provide additional logic"""
