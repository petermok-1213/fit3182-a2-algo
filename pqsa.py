from multiprocessing import Pool
from rand_qs import rand_qs, get_rand_data
import time

def f():
    n = 100
    data = get_rand_data(n,10)
    with Pool(processes=8) as pool:
        start = time.time()
        res = pool.apply_async(rand_qs, (data, 0, n-1))
        end = time.time()
        print("Parallel:", end-start)

    start = time.time()
    rand_qs(get_rand_data(n, 10), 0, n-1)
    end = time.time()
    print("Serial:", end-start)

    print("jobs done")


if __name__ == '__main__':

