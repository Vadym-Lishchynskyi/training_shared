""" Without lock"""
# import threading
#
# x = 0
#
#
# def increment():
#     global x
#     x += 1
#
#
# def thread_task():
#     for _ in range(100_000):
#         increment()
#
#
# def main():
#     global x
#     x = 0
#
#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)
#
#     t1.start()
#     t2.start()
#
#     t1.join(timeout=None)
#     t2.join()
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         main()
#         print(f'Iteration {i}: x = {x} ')

""" With lock"""
import threading

x = 0


def increment():
    global x
    x += 1


def thread_task(lock):
    for _ in range(100_000):

        """ми маєм получити лок в головному треді - іначе чото не паше"""
        # lock = threading.Lock()

        lock.acquire()
        increment()
        lock.release()


def main():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock, ))
    t2 = threading.Thread(target=thread_task, args=(lock, ))

    t1.start()
    t2.start()

    t1.join(timeout=None)
    t2.join()


if __name__ == '__main__':
    for i in range(10):
        main()
        print(f'Iteration {i}: x = {x} ')




