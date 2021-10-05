import multiprocessing as mp
import time

serving_line = mp.Queue(5)


def cpu_work(work_units):
    x = 0
    for work in range(work_units * 1_000_000):
        x += 1


def soup_producer(serving_line):
    for i in range(20):  # serve 20 bowls of soup
        serving_line.put_nowait('Bowl #' + str(i))
        print('Served Bowl #', str(i), '- remaining capacity:',
              serving_line._maxsize - serving_line.qsize())
        time.sleep(0.2)  # time to serve a bowl of soup
    serving_line.put_nowait('no soup for you!')
    serving_line.put_nowait('no soup for you!')

def soup_consumer(serving_line):
    while True:
        bowl = serving_line.get()
        if bowl == 'no soup for you!':
            break
        print('Ate', bowl)
        # time.sleep(0.3) Works fine cause it doesn't do any actual work and can be very long.
        # Good approach for I/O actions but not parallel execution.
        # The reason for that is shown on the next line where CPU works instead of just waiting
        cpu_work(4)  # Time to eat bowl of soup


if __name__ == '__main__':
    for consumer in range(2):
        mp.Process(target=soup_consumer, args=(serving_line,)).start()
    mp.Process(target=soup_producer, args=(serving_line,)).start()


