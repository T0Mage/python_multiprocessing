from multiprocessing import Process, Lock, Value
import time

def f(l, i, num):
    l.acquire()
    num.value = num.value+1
    time.sleep(0.2)
    try:
        print(f'called : {i}, number of functions at same time:{num.value}')
    finally:
        num.value = num.value-1
        l.release()

def f2(lock,i,num):
    num.value = num.value+1
    time.sleep(0.2)
    print(f'called : {i}, number of functions at same time:{num.value}')
    num.value = num.value-1

if __name__ == '__main__':
    lock = Lock()
    num = Value('i', 0)
    print("concurently:")
    processes=[]
    for i in range(10):
        processes.append(Process(target=f2, args=(lock, i, num)))
        processes[i].start()
    for i in range(10):
        processes[i].join()
    print("sequential:")
    for i in range(10):
        p = Process(target=f2, args=(lock, i, num))
        p.start()
        p.join()
    print("using lock:")
    for i in range(10):
        Process(target=f, args=(lock, i, num)).start()
