import threading

lock_1 = threading.Lock()
lock_2 = threading.Lock()
lock_3 = threading.Lock()

number_of_sushi = 500

phil1_eat = 0
phil2_eat = 0
phil3_eat = 0


def philosopher(first_locker, second_locker):
    global number_of_sushi

    while number_of_sushi > 0:
        first_locker.acquire()
        second_locker.acquire()

        if number_of_sushi > 0:
            number_of_sushi -= 1
            print(f'{threading.current_thread().getName()} took a piece. Remained: {number_of_sushi}')

        first_locker.release()
        second_locker.release()


if __name__ == '__main__':
    thread_philosopher_1 = threading.Thread(name='Ivan', target=philosopher, args=(lock_1, lock_2)).start()
    thread_philosopher_2 = threading.Thread(name='Petro', target=philosopher, args=(lock_2, lock_3)).start()
    thread_philosopher_3 = threading.Thread(name='Mykola', target=philosopher, args=(lock_1, lock_3)).start()




