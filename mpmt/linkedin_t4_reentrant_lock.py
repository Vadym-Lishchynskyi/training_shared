import threading

garlic_count = 0
potato_count = 0
lock = threading.RLock()    # Here is not a regular Lock


def add_garlic():
    global garlic_count
    lock.acquire()
    garlic_count += 1
    # ==========
    add_potato()
    """ This will break all the system and leads to  DeadLock as we need to acquire a lock but it is already
     taken buy ourselves. We need to use Reentrant Lock"""
    lock.release()


def add_potato():
    global potato_count
    lock.acquire()
    potato_count += 1
    lock.release()


def shopper():
    for i in range(10_000):
        add_potato()
        add_garlic()


if __name__ == '__main__':
    thread1_Barron = threading.Thread(target=shopper)
    thread2_Olivia = threading.Thread(target=shopper)
    thread1_Barron.start()
    thread2_Olivia.start()
    thread1_Barron.join()
    thread2_Olivia.join()
    print(f'We should buy {garlic_count} garlic.')
    print(f'We should buy {potato_count} potato.')
