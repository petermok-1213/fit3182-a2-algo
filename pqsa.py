import random
import threading
from threadpool import ThreadPool, worker
from threading import Thread

import rand_qs
from rand_qs import rand_partition
import time

'''
    Class representing the master PQSA thread
    Create and Run this thread object to run PQSA
'''
def pqsa(arr: list[int], left: int, right: int):

    if right > left:
        pivot = rand_partition(arr, left, right)     # Choose a random pivot and Partition list
        # Create child thread for sorting left/right partition
        ThreadPool().pool.put(Thread(target=lambda:pqsa(arr, left, pivot)))     # Put threads in threadpool
        ThreadPool().pool.put(Thread(target=lambda:pqsa(arr, pivot+1, right)))  # (block until there is enough space)



if __name__ == '__main__':

    random.seed(31266797)
    data = rand_qs.get_rand_data(100000, 100)
    ThreadPool().pool.put(Thread(target=lambda:pqsa(data, 0, len(data)-1)))
    for _ in range(8):
        threading.Thread(target=worker, daemon=True).start()
    ThreadPool().pool.join()
    print(data == sorted(data))
