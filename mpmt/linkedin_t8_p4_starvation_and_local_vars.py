import threading

lock_1 = threading.Lock()
lock_2 = threading.Lock()
lock_3 = threading.Lock()

number_of_sushi = 5000

phil1_eat = 0
phil2_eat = 0
phil3_eat = 0


def philosopher(first_locker, second_locker):
    global number_of_sushi
    sushi_eaten_at_the_end = 0

    name = threading.current_thread().getName()

    while number_of_sushi > 0:

        with first_locker:
            with second_locker:

                if number_of_sushi > 0:
                    number_of_sushi -= 1
                    sushi_eaten_at_the_end += 1
                    print(f'{name} took a piece. Remained: {number_of_sushi}')

                # if number_of_sushi == 300:
                #     print(1/0)      # Crashes the program at the right moment

    print(f'{name} eat: {sushi_eaten_at_the_end}')
    return sushi_eaten_at_the_end


if __name__ == '__main__':
    # for i in range(10):
    thread_philosopher_1 = threading.Thread(name='Ivan', target=philosopher, args=(lock_1, lock_2)).start()
    thread_philosopher_2 = threading.Thread(name='Petro', target=philosopher, args=(lock_2, lock_3)).start()
    thread_philosopher_3 = threading.Thread(name='Mykola', target=philosopher, args=(lock_1, lock_3)).start()

    #  Нічого не повертає
    # print(f'Finally Ivan eat: {thread_philosopher_1}')
    # print(f'Finally Ivan eat: {thread_philosopher_2}')
    # print(f'Finally Ivan eat: {thread_philosopher_3}')

    """
    !!!Starvation is NOT FAIR DISTRIBUTION!!!
    
_________________________________________________________________________________________________________________
    Real result(rare case): (good example of starvation)
    
    Ivan eat: 264
    Petro eat: 236
    Mykola eat: 0
    
_________________________________________________________________________________________________________________
    Real and most possible result:
    
    Distribution:
      thread_philosopher_1 = threading.Thread(name='Ivan', target=philosopher, args=(lock_1, lock_2)).start()
      thread_philosopher_2 = threading.Thread(name='Petro', target=philosopher, args=(lock_2, lock_3)).start()
      thread_philosopher_3 = threading.Thread(name='Mykola', target=philosopher, args=(lock_1, lock_3)).start()
    
    Result:
      Mykola eat: 151
      Petro eat: 312
      Ivan eat: 37
    
    Comments:
      The reason for that is: both Mykola and Ivan compete for the lock_1 at first but Petro acquires lock_2
      without any obstacles so he has chances to get 2x more resources as compete only for lock_3 after lock_2.
      
_________________________________________________________________________________________________________________
    NOTE: We now can see that distribution totally depends on the order of locks we have to acquire to get resources
     
_________________________________________________________________________________________________________________
    Distribution:
      thread_philosopher_1 = threading.Thread(name='Ivan', target=philosopher, args=(lock_1, lock_2)).start()
      thread_philosopher_2 = threading.Thread(name='Petro', target=philosopher, args=(lock_1, lock_3)).start()
      thread_philosopher_3 = threading.Thread(name='Mykola', target=philosopher, args=(lock_1, lock_3)).start()
    
    Result:
      Mykola eat: 1610
      Petro eat: 1268
      Ivan eat: 2122

    Comments:
      In such case Ivan has benefit from such distribution because he compete only for the first lock (lock_1) while 
      Mykola and Petro compete for both locks (lock_1, lock_3)
      
_________________________________________________________________________________________________________________
    """




