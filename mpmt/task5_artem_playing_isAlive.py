"""
How do join method works...

Other threads can call a thread’s join() method.
This blocks the calling thread until the thread whose join() method is called is terminated.


"""

import logging
import threading
import time


def thread_function1(name):
    logging.info(f'Thread {name} starting')
    time.sleep(2)
    logging.info(f'Thread {name} finished')


def thread_function2(name):
    logging.info(f'Thread {name} starting')
    time.sleep(5)
    logging.info(f'Thread {name} finished')


if __name__ == '__main__':
    form = '%(asctime)s: %(message)s'
    logging.basicConfig(format=form, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main:     before creating thread")
    x1 = threading.Thread(name='Thread 1', target=thread_function1, args=(1,))
    x2 = threading.Thread(name='Thread 2', target=thread_function2, args=(2,), daemon=True)

    logging.info("Main:     before running thread 1")
    x1.start()
    logging.info("Main:     before running thread 2")
    x2.start()

    logging.info("Main:     wait for threads to finish")

    x1.join()
    x2.join()

    """
    10:34:25: Main:     before creating thread
    10:34:25: Main:     before running thread 1
    10:34:25: Thread 1 starting
    10:34:25: Main:     before running thread 2
    10:34:25: Thread 2 starting
    10:34:25: Main:     wait for threads to finish
    10:34:27: Thread 1 finished
    10:34:27: Main:     all done
    
    real    0m2,034s
    user    0m0,028s
    sys     0m0,004s
    
    As we have our Thread 2 daemon we don't have to wait until it will be finished - the main thread continuous and 
    stops the program when it is done. It doesn't wait until daemon thread is finished - is just kills it.
    
    Difference: normal thread || normal thread + join || daemon thread || daemon thread + join
    1) Normal thread from main thread:
    Executes main and child thread bu GIL (5ms for each) 
    
    Result:
    11:41:39: Main:     before creating thread
    11:41:39: Main:     before running thread 1
    11:41:39: Thread 1 starting
    11:41:39: Main:     before running thread 2
    11:41:39: Thread 2 starting
    11:41:39: Main:     wait for threads to finish
    11:41:39: Main:     all done
    11:41:41: Thread 1 finished
    11:41:44: Thread 2 finished

    
    2) Normal thread with join() from main thread:
    Executes child thread -> only after - main thread do the work
    
    Result:
    11:33:52: Main:     before creating thread
    11:33:52: Main:     before running thread 1
    11:33:52: Thread 1 starting
    11:33:52: Main:     before running thread 2
    11:33:52: Thread 2 starting
    11:33:52: Main:     wait for threads to finish
    11:33:54: Thread 1 finished
    11:33:57: Thread 2 finished
    11:33:57: Main:     all done
    
    3) Daemon thread from main thread:
    Executes main and child thread bu GIL (5ms for each) but when main is done it kills child doesn't matter what 
    child was doing
    
    Result:
    11:40:56: Main:     before creating thread
    11:40:56: Main:     before running thread 1
    11:40:56: Thread 1 starting
    11:40:56: Main:     before running thread 2
    11:40:56: Thread 2 starting
    11:40:56: Main:     wait for threads to finish
    11:40:58: Thread 1 finished
    11:40:58: Main:     all done

    
    4) Daemon thread with join() from main thread:
    Executes child thread -> only after - main thread do the work. (Works as general thread with .join())
    
    Result:
    11:33:52: Main:     before creating thread
    11:33:52: Main:     before running thread 1
    11:33:52: Thread 1 starting
    11:33:52: Main:     before running thread 2
    11:33:52: Thread 2 starting
    11:33:52: Main:     wait for threads to finish
    11:33:54: Thread 1 finished
    11:33:57: Thread 2 finished
    11:33:57: Main:     all done

    
    Docs:
    Daemon threads are abruptly stopped at shutdown. Their resources (such as open files, database transactions, 
    etc.) may not be released properly. If you want your threads to stop gracefully, make them non-daemonic and use a 
    suitable signalling mechanism such as an Event 
    

    """
    logging.info("Main:     all done")
