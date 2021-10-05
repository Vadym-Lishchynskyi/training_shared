import threading
import time
import queue

serving_line = queue.Queue(maxsize=5)


def cpu_waster(unit_of_work):
    x = 0
    for _ in range(unit_of_work * 10_000_000):
        x += 1


def soup_producer():
    for i in range(20):     # Serve 20 bowls of soup in total
        serving_line.put_nowait('Bowl #' + str(i+1))
        print('Served Bowl #', str(i), ' - remaining capacity: ', serving_line.maxsize - serving_line.qsize())
        time.sleep(0.2)     # Time for bowl of soup to be produced
    serving_line.put_nowait('No soup for you!')
    serving_line.put_nowait('No soup for you!')


def soup_consumer():
    while True:
        bowl = serving_line.get()
        if bowl == 'No soup for you!':
            break
        print('Ate', bowl)
        # time.sleep(0.3) Works fine cause it doesn't do any actual work and can be very long.
        # Good approach for I/O actions but not parallel execution. Because of the GIL.
        # The reason for that is shown on the next line where CPU works instead of just waiting
        cpu_waster(4)   # Time to eat bowl of soup


if __name__ == '__main__':
    prod = threading.Thread(target=soup_producer).start()
    for i in range(2):
        cons = threading.Thread(target=soup_consumer).start()



