import random
import threading
from rand_qs import get_rand_data, it_rand_qs


"""
    Partition data based on the given number of threads
    Input:
        arr: list to be partitioned
        n: number of threads
    Output:
        partitions: list of partitions each for one thread
"""
def partition_by_threads(arr: list[int], n: int, partitions: list[list[int]]) -> list[list[int]]:
    cur_partition = []
    cur_index = 0
    while len(partitions) < n:
        while (len(cur_partition) < len(arr)/n) and cur_index < len(arr):
            cur_partition.append(arr[cur_index])
            cur_index += 1
        partitions.append(cur_partition)
        cur_partition = []
    return partitions

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
        partitions.append(result)                   # put result at the end of the queue
    return partitions[0]                            # [[result]] -> [result]

"""
    Implementation of Merging Subarrys from Quick Sort Algorithm
    Input:
        arr: list to be sorted
        n: number of threads
"""
def msqsa(arr: list[int], n: int) -> None:

    partitions = []
    partition_thread = threading.Thread(
        target=partition_by_threads,
        args=(arr, n, partitions)
    )
    partition_thread.start()
    partition_thread.join()

    threads = []
    for i in range(n):
        threads.append(threading.Thread(
            target=it_rand_qs,
            args=(partitions[i], 0, len(partitions[i])-1)
        ))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    partitions = merge(partitions)
    print(partitions)

if __name__ == "__main__":

    random.seed(31266797)

    msqsa(get_rand_data(1000, 10), 8)

