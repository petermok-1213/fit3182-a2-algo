import random
import threading
import time
from rand_qs import get_rand_data, it_rand_qs


"""
    Partition data based on the given number of threads
    Input:
        arr: list to be partitioned
        n: number of threads
    Output:
        partitions: list of partitions each for one thread
"""
def partition_by_threads(arr: list[int], thread_num: int, partitions: list[list[int]]) -> list[list[int]]:
    cur_partition = []
    cur_index = 0
    while (len(cur_partition) < len(arr)/n) and cur_index < len(arr):
        cur_partition.append(arr[cur_index])
        cur_index += 1
    partitions.append(cur_partition)
    cur_partition = []


"""
    Iterative 2-way merge sort
    Input:
        partitions: list of partitions to be merged into 1
    Output:
        partitions[0]: the final merged partition
"""
def merge(partitions: list[list[int]]) -> list[int]:
    while len(partitions) > 1:                      # while there are multiple partitions
        left = partitions.pop(0)                    # pop top 2 partitions
        right = partitions.pop(0)                   # --
        result = []                                 # init placeholder for the sub-result

        while len(left) > 0 and len(right) > 0:     # while they are not empty
            if left[0] < right[0]:                  ###
                result.append(left.pop(0))          # pop the smaller element to the end
            else:                                   # of result
                result.append(right.pop(0))         ###

        while len(left) > 0:                        # while there are elements remain in left or right
            result.append(left.pop(0))              # push the remaining elements in result
        while len(right) > 0:                       #
            result.append(right.pop(0))             #

        partitions.append(result)                   # put result at the end of the queue

    return partitions[0]                            # [result] -> result


def msqsa():
    pass

"""
    Implementation of Merging Subarrys from Quick Sort Algorithm
    Input:
        arr: list to be sorted
        n: number of threads
"""
def msqsa_mod(arr: list[int], n: int) -> list[int]:

    partitions = []     # for storing partitions of arr as partition_by_threads is in-place
    partition_thread = threading.Thread(    # instantiate threads for partitioning data
        target=partition_by_threads,
        args=(arr, n, partitions)
    )
    partition_thread.start()                # run thread
    partition_thread.join()                 # until arr is partitioned

    threads = []                            # local thread pool
    for i in range(n):                      # pushing threads for sorting into thread pool
        threads.append(threading.Thread(
            target=it_rand_qs,
            args=(partitions[i], 0, len(partitions[i])-1)
        ))
    for thread in threads:                  # run all threads
        thread.start()
    for thread in threads:                  # until threads are done running
        thread.join()

    return merge(partitions)
