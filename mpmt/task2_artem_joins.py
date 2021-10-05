"""
How do join method works...

Other threads can call a thread’s join() method.
This blocks the calling thread until the thread whose join() method is called is terminated.


"""

import logging
import threading
import time


def thread_function(name):
    logging.info(f'Thread {name} starting')
    time.sleep(2)
    logging.info(f'Thread {name} finished')


if __name__ == '__main__':
    form = '%(asctime)s: %(message)s'
    logging.basicConfig(format=form, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main:     before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main:     before running thread")
    x.start()
    logging.info("Main:     wait for the thread to finish")

    """
    Without x.join()
    
    The problem here is that we got phrase 'all done' before actually doing everything
    The result looks like that:
    
    22:40:10: Main:     before creating thread      
    22:40:10: Main:     before running thread
    22:40:10: Thread 1 starting
    22:40:10: Main:     wait for the thread to finish
    22:40:10: Main:     all done                        'all done' should go after Thread 1 finished <-| 
    22:40:12: Thread 1 finished                                                                      <-|


    Using the x.join() method we establish main thread to wait for the thread x to be 
    finished and only after - continue (print 'all done')
    
    """
    # x.join()
    """
    With x.join() main threads stops at the point of x.join() -> let it do all the work -> continue the process
     
    22:46:44: Main:     before creating thread
    22:46:44: Main:     before running thread
    22:46:44: Thread 1 starting
    22:46:44: Main:     wait for the thread to finish
    22:46:46: Thread 1 finished
    22:46:46: Main:     all done

    """
    logging.info("Main:     all done")
