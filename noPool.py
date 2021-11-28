from multiprocessing import Pool
import time

def f(x):
    time.sleep(0.2)
    return x*x

if __name__ == '__main__':
    start_time = time.time()

    arguments = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    # arguments = list(range(20))
    result = []
    for arg in arguments:
        result.append(f(arg))

    print(result)
    end_time = time.time()

    print(f"program run for: {end_time-start_time:.2f}s")
