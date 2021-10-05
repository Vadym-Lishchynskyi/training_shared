import threading
from threading import Thread
import time

# import time
#
#
# def main(i):
#     print(f'Hello from thread {i} that goes to sleep')
#     time.sleep(2)
#     print(f'World from thread {i}')
#
#
# for i in range(10):
#     main(i)
# """Command to measure time in console >>> time python3 task1_artem.py"""

# real    0m20,041s
# user    0m0,021s
# sys     0m0,000s


# ----------------------------------------------------------------
# from threading import Thread
# import time
#
#
# def main(i):
#
#     print(f'Hello from thread {i} that goes to sleep')
#     time.sleep(5)
#     print(f'World from thread {i}')
#
#
# for i in range(10):
#     th = Thread(target=main, args=(i, ))
#     th.start()
# """Command to measure time in console >>> time python3 task1_artem.py"""

# real    0m5,035s
# user    0m0,018s
# sys     0m0,014s

# ----------------------------------------------------------------
"""Threading function in it's module"""
# import time
# import threading
# from threading import Thread

# threading.active_count()      - int amount of the threads in the system running
# threading.current_thread()    - returns the object of thread that now was run
# threading.enumerate()         - returns a list of all threads
# threading.main_thread()       - return objects of main thread
#
# Thread.run()
# Thread.start()
# Thread.join([time])   let the program wait the end of the thread
# Thread.isAlive()      checks weather the thread is active
# Thread.getName()
# Thread.setName()


# def main(number):
#     print(f'Hello from thread {threading.current_thread()} that goes to sleep')
#     time.sleep(5)
#
#     # if threading.current_thread().name == 'Thread-10':
#     #     print()
#     #     for j in threading.enumerate():     # It has strange behaviour but that is the key
#     #         print(f'{j}')
#     #     print()
#     """It actually can print random number of threads - it depends on the number of 10-th thread in order"""
#     # if threading.current_thread().name == 'Thread-10':
#     #     print(threading.enumerate())
#
#     print(f'World from thread {threading.current_thread()}')
# import threading

""" threading.current_thread() - returns us the object of the current thread"""

# for i in range(10):
#     th = Thread(target=main, args=(i, ))
#     th.start()
#     print(f'\tNumber of currently working threads: {threading.active_count()}')

""" threading.active_count() - gives us the amount of currently running threads"""

# Actually we have 11 threads as 10 new that we make and the 11-th parent thread of our
# python application from where all others are acquired.
"""Command to measure time in console >>> time python3 task1_artem.py"""

# ----------------------------------------------------------------
"""We can name our threads at the moment of creation"""


# def main(i):
#     print(f'Hello from thread "{threading.current_thread().name}" that goes to sleep')
#     time.sleep(5)
#     print(f'World from thread {i}')
#
#
# for i in range(10):
#     """within target we provide function to run and arguments to that function """
#     th = Thread(name=f'Our thread {i}', target=main, args=(i,))
#     th.start()
#     print(f'\tNumber of currently working threads: {threading.active_count()}')
"""Command to measure time in console >>> time python3 task1_artem.py"""

# ----------------------------------------------------------------


