import multiprocessing as mp
import time
def f(q):
    q.put(['hello'])
def f_nowait(q):
    q.put_nowait('hello') 

def f_read(q):
    print(q.get())
def f_read_nowait(q):
    print(q.get_nowait())

if __name__ == '__main__':
    q = mp.Queue()
    p = mp.Process(target=f, args=(q,))
    p2 = mp.Process(target=f_read, args=(q,))
    p3 = mp.Process(target=f_read, args=(q,))
    # q.put(obj,block,timeout)
    p.start()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    p.join()
