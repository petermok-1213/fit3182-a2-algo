import copy
import random
import threading
from rand_qs import get_rand_data, rand_partition, rand_qs
import time

class PQSAThread(threading.Thread):

    def __init__(self, arr: list[int], left: int, right: int):
        threading.Thread.__init__(self)
        self.arr = arr
        self.left = left
        self.right = right

    def run(self):
        print("Starting Thread ", threading.get_ident(), "\n")
        if self.right > self.left:
            pivot = rand_partition(self.arr, self.left, self.right)
            l_child_thread = PQSAThread(self.arr, self.left, pivot)
            r_child_thread = PQSAThread(self.arr, pivot+1, self.right)
            l_child_thread.start()
            r_child_thread.start()
            if not l_child_thread.is_alive() and not r_child_thread.is_alive():
                print("Ending Thread", threading.get_ident(), "\n")

def pqsa(arr, left, right):
    if right > left:
        pivot = rand_partition(arr, left, right)
        pqsa(arr, left, pivot)
        pqsa(arr, pivot+1, right)
    return arr


if __name__ == '__main__':

    random.seed(31266797)
    n = 50
    data = get_rand_data(n, 10)
    main_pqsa_thread = PQSAThread(data, 0, n-1)
    main_pqsa_thread.start()
