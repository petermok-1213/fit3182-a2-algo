import copy
import random
import sys
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
        if self.right > self.left:
            pivot = rand_partition(self.arr, self.left, self.right)
            l_child_thread = PQSAThread(self.arr, self.left, pivot)
            r_child_thread = PQSAThread(self.arr, pivot+1, self.right)
            try:
                l_child_thread.start()
                r_child_thread.start()
                l_child_thread.join()
                r_child_thread.join()
            except RuntimeError as error:
                time.sleep(0.1)


if __name__ == '__main__':

    random.seed(3126679)
    n = 1000000
    sys.setrecursionlimit(n)    # force increase maximum recursion depth to avoid Exception

    data = get_rand_data(n, 100)
    test_data = copy.deepcopy(data)

    main_pqsa_thread = PQSAThread(data, 0, n-1)
    start = time.time()
    main_pqsa_thread.start()
    main_pqsa_thread.join()
    pqsa_time = time.time()-start
    print("Parallel: ", pqsa_time)

    rand_qs_thread = threading.Thread(target=rand_qs, args=(test_data, 0, n-1))
    start = time.time()
    rand_qs_thread.start()
    rand_qs_thread.join()
    print("Serial: ", time.time()-start)
