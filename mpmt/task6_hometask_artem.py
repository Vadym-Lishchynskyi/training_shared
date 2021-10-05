import threading
import random
import time

counter = 0


def thread_job(l):
    global counter

    l.acquire()

    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1

    l.release()

    print(f"{counter}", end='')


lock = threading.Lock()
threads = [threading.Thread(target=thread_job, args=(lock,)) for i in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f'\nfinally counter: {counter}')
