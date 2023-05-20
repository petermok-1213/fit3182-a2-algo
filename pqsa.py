import copy
import random
import sys
import threading

import rand_qs
from rand_qs import rand_partition
import time

'''
    Class representing the master PQSA thread
    Create and Run this thread object to run PQSA
'''
class PQSAThread(threading.Thread):

    """
        Thread's Constructor
        Input:
            arr: list to be sorted
            left: sort from this index
            right sort to this index
    """
    def __init__(self, arr: list[int], left: int, right: int, threads: list[threading.Thread], max_thread: int):
        threading.Thread.__init__(self)
        self.arr = arr
        self.left = left
        self.right = right
        self.max_thread = max_thread
        self.threads = threads


    """
        Override Thread's run method
        Implementation of PQSA
    """
    def run(self):

        if self.right > self.left and len(self.threads) < self.max_thread:
            pivot = rand_partition(self.arr, self.left, self.right)     # Choose a random pivot and Partition list
            self.threads.append(PQSAThread(self.arr, self.left, pivot, self.threads, self.max_thread))     # Create child thread for sorting left partition
            self.threads.append(PQSAThread(self.arr, pivot+1, self.right, self.threads, self.max_thread))  #                                 right partition

            if len(self.threads) > 0:           # Do not remove this if statement, IT BROKE EVERYTHING
                l_child = self.threads.pop(0)
                r_child = self.threads.pop(0)
                try:
                    l_child.start()  # Sort left partition in a new thread
                    r_child.start()  #      right partition in a new thread
                    l_child.join()   # Wait until left partition is sorted
                    r_child.join()   #            right partition is sorted
                except RuntimeError:        # If cant start new threads
                    time.sleep(0.1)         # Wait 0.1 second (better than 1s or 0.01s)


if __name__ == '__main__':

    data = rand_qs.get_rand_data(100, 100)
    t = PQSAThread(data, 0, len(data)-1, [], 8)
    t.start()
    t.join()
    print(data == sorted(data))
