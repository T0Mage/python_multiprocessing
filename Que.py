import multiprocessing as mp
import time
def foo(q):
    time.sleep(0.2)
    q.put(['hello'])
def foo_nowait(q):
    time.sleep(0.2)
    q.put_nowait('hello')

def boo(q):
    print(q.get())
def boo_nowait(q):
    print(q.get_nowait())

if __name__ == '__main__':
    # mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p2 = mp.Process(target=boo, args=(q,))
    p3 = mp.Process(target=boo, args=(q,))
    # q.put(obj,block,timeout)
    p.start()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    # print("not rechable")
    p.join()
