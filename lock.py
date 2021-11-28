from multiprocessing import Process, Lock, Value
import time

def f(l, i, num):
    l.acquire()
    num.value = num.value+1
    time.sleep(0.2)
    try:
        print('hello world', i, num.value)
    finally:
        num.value = num.value-1
        l.release()

def f2(l, i):
    time.sleep(0.2)

    print('hello world', i)

if __name__ == '__main__':
    lock = Lock()
    number_of_active = Value('i', 0)
    for num in range(10):
        Process(target=f2, args=(lock, num)).start()

    for num in range(10):
        p = Process(target=f2, args=(lock, num))
        p.start()
        p.join()

    for num in range(10):
        Process(target=f, args=(lock, num,number_of_active)).start()
