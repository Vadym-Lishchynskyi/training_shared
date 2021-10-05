import threading
import datetime


class MyThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self) -> None:
        print('Starting ' + self.name)
        print_date(self.name, self.counter)
        print('Exiting ' + self.name)


def print_date(thread_name, counter):
    today = datetime.datetime.now()
    print(
        "%s[%d]: %s" % (thread_name, counter, today)
    )


thread1 = MyThread('Thread', 1)
thread2 = MyThread('Thread', 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print('Exiting main')
