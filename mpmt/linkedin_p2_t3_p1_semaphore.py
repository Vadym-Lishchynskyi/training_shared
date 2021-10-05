import threading
import time
import random

charger = threading.Semaphore(1)    # Our charger switch with 4 elements


def cellphone():
    name = threading.current_thread().getName()
    charger.acquire()
    print(name, 'is charging...')
    time.sleep(random.uniform(1, 2))
    print(name, 'is DONE charging!')
    charger.release()


if __name__ == '__main__':
    for phone in range(10):
        threading.Thread(target=cellphone, name='Phone-'+str(phone)).start()

'''
Result:
Phone-0 is charging...
Phone-1 is charging...
Phone-2 is charging...
Phone-3 is charging...
Phone-1 is DONE charging!
Phone-4 is charging...
Phone-0 is DONE charging!
Phone-5 is charging...
Phone-2 is DONE charging!
Phone-6 is charging...
Phone-3 is DONE charging!
Phone-7 is charging...
Phone-4 is DONE charging!
Phone-8 is charging...
Phone-5 is DONE charging!
Phone-9 is charging...
Phone-6 is DONE charging!
Phone-8 is DONE charging!
Phone-7 is DONE charging!
Phone-9 is DONE charging!

real    0m3,709s
user    0m0,033s
sys     0m0,000s

'''