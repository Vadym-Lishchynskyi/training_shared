import threading
import time


def target1():
    time.sleep(0.1)
    print("target1 running")
    time.sleep(4)


def target2():
    time.sleep(0.1)
    print("target2 running")
    time.sleep(2)


def launch_thread_with_message(target, message, args=[], kwargs={}):
    """
    Such structure let's us do(print) something as soon as the thread has finished ans was demolished

    Reason: something can be done faster so all program has to wait because it does't know that it was done
    Like we wait from something DB and print calculate smth. Db is more important but how do we know that it is done&
    Actually, that is the answer
     
    Problem: we can't do it from main thread when using thread.join()

    """

    def target_with_msg(*args, **kwargs):
        target(*args, **kwargs)
        print(message)

    thread = threading.Thread(target=target_with_msg, args=args, kwargs=kwargs)
    thread.start()
    return thread


if __name__ == '__main__':
    thread1 = launch_thread_with_message(target1, "finished target1")
    thread2 = launch_thread_with_message(target2, "finished target2")

    print("main: launched all threads")

    thread1.join()
    print('main: Thread 1 done and main prints it')
    thread2.join()
    print('main: Thread 2 done and main prints it')

    print("main: finished all threads")


"""
Join locks only main thread and makes it wait for it. Actually the thread from which another was called (parent thread)
"""