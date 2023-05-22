import random
import threading
from threadpool import ThreadPool
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
        ThreadPool().pool.put(Thread(target=pqsa, args=(arr, left, pivot)))     # Put threads in threadpool
        ThreadPool().pool.put(Thread(target=pqsa, args=(arr, pivot+1, right)))  # (block until there is enough space)



if __name__ == '__main__':

    pass
