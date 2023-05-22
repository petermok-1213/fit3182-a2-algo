import time

from threadpool import ThreadPool
from threading import Thread

from rand_qs import rand_partition, get_rand_data

'''
    Class representing the master PQSA thread
    Create and Run this thread object to run PQSA
'''
def pqsa(arr: list[int], left: int, right: int):

    if right > left:
        pivot = rand_partition(arr, left, right)     # Choose a random pivot and Partition list
        # Create child thread for sorting left/right partition
        ThreadPool().pool.put(Thread(target=pqsa, args=(arr, left, pivot)))     # Put threads in threadpool
        ThreadPool().pool.put(Thread(target=pqsa, args=(arr, pivot+1, right)))  # (block until there is enough space)


"""
    PQSA but
    it spawns as much threads as it needs
"""
def unhinged_pqsa(arr, left, right):
    if right > left:
        pivot = rand_partition(arr, left, right)
        l_child = Thread(target=unhinged_pqsa, args=(arr, left, pivot))
        r_child = Thread(target=unhinged_pqsa, args=(arr, pivot+1, right))
        try:
            l_child.start()
            r_child.start()
            l_child.join()
            r_child.join()
        except RuntimeError:
            time.sleep(0.1)


if __name__ == '__main__':

    n = 10000000
    data = get_rand_data(n, 100)
    start = time.time()
    unhinged_pqsa(data, 0, n-1)
    end = time.time()
    print(data == sorted(data))
    print(end-start)
