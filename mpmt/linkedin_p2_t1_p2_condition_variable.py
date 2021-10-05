import threading


lock = threading.Lock()
soup_servings = 11
soup_taken = threading.Condition(lock=lock)
''' soup_taken signals after one of the threads has taken soup. If we do not specify the lock,
threading module will create RLock and use it instead of provided one.
'''


def hungry_person(person_id):
    global soup_servings
    while soup_servings > 0:
        with lock:
            while person_id != (soup_servings % 2) and (soup_servings > 0):
                print('Person', person_id, 'checked... then put the ld back.')
                soup_taken.wait()

            if soup_servings > 0:
                soup_servings -= 1
                print('Person', person_id, 'took soup. Servings left:', soup_servings)
                soup_taken.notify()


if __name__ == '__main__':
    for person in range(2):
        threading.Thread(target=hungry_person, args=(person,)).start()


"""
Time spent:

real    0m0,024s
user    0m0,021s
sys     0m0,004s


"""

