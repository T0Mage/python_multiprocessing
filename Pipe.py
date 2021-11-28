from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

def f_read(conn):
    print(conn.recv())
    # print(conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p2 = Process(target=f_read, args=(parent_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']" #blocking operation!
    child_conn.send([42, None, 'hello1'])
    p2.start()
    p2.join()
    p.join()
