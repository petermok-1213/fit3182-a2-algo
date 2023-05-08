import copy
import random
import sys
import threading
from rand_qs import get_rand_data, rand_partition, rand_qs
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
    def __init__(self, arr: list[int], left: int, right: int, name=None):
        threading.Thread.__init__(self, name=name)
        self.arr = arr
        self.left = left
        self.right = right


    """
        Override Thread's run method
        Implementation of PQSA
    """
    def run(self):
        if self.right > self.left:
            pivot = rand_partition(self.arr, self.left, self.right)     # Choose a random pivot and Partition list
            l_child_thread = PQSAThread(self.arr, self.left, pivot)     # Create child thread for sorting left partition
            r_child_thread = PQSAThread(self.arr, pivot+1, self.right)  #                                 right partition
            try:
                l_child_thread.start()  # Sort left partition in a new thread
                r_child_thread.start()  #      right partition in a new thread
                l_child_thread.join()   # Wait until left partition is sorted
                r_child_thread.join()   #            right partition is sorted
            except RuntimeError:        # If cant start new threads
                time.sleep(0.1)         # Wait 0.1 second (better than 1s or 0.01s)


if __name__ == '__main__':
    pass
