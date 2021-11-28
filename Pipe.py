from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'helloFromProcess'])

def f_read(conn):
    print("other pocess recv: ",conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p2 = Process(target=f_read, args=(parent_conn,))

    p.start()
    p2.start()
    p2.join()
    p.join() 