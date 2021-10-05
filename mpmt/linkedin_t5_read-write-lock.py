import threading
from readerwriterlock import rwlock

"""
    Difference between read-write-lock implementation and general lock implementation
    Time takes the same(may be just a bit less) but 
    
"""
WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0
# lock = threading.Lock()
lock = rwlock.RWLockFair()


def calendar_read(id_number):
    global today
    name = 'Reader ' + str(id_number)
    reader_lock = lock.gen_rlock()
    while today < len(WEEKDAYS) - 1:
        # lock.acquire()
        reader_lock.acquire()
        print(name, 'sees that today is', WEEKDAYS[today], '-read count: ', reader_lock.c_rw_lock.v_read_count)
        reader_lock.release()
        # lock.release()


def calendar_write(id_number):
    global today
    name = 'Writer ' + str(id_number)
    writer_lock = lock.gen_wlock()
    while today < len(WEEKDAYS) - 1:
        writer_lock.acquire()
        # lock.acquire()
        today = (today + 1) % 7
        print(name, 'updated date to ', WEEKDAYS[today])
        writer_lock.release()
        # lock.release()


if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=calendar_read, args=(i, )).start()

    for i in range(2):
        threading.Thread(target=calendar_write, args=(i, )).start()

