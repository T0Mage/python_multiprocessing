from multiprocessing import Process, Value, Array

def f(n, a, normal_variable):
    normal_variable.append(1)
    n.value = 123.45
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    normal_variable = [0]
    p = Process(target=f, args=(num, arr, normal_variable))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
    print(normal_variable)

    f(num, arr, normal_variable)
    print(num.value)
    print(arr[:])
    print(normal_variable)
