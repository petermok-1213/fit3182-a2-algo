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
        arr: list of partitions
        left: merge from this index
        length: length of each sorted section
    Output:
        partitions[0]: the final merged partition
"""
def merge(arr: list[int], left: int, length: int) -> list[int]:
    mid = left + length         # the middle index
    right = left + 2*length -1  # the right most index
    if right >= len(arr):
        right = len(arr)-1
    l_ptr = left                # pointer for the left sorted list
    r_ptr = mid + 1             # pointer for the right sorted list

    while l_ptr < mid and r_ptr < right:
        if arr[l_ptr] < arr[r_ptr]:
            l_ptr += 1
        else:
            arr.insert(l_ptr, arr.pop(r_ptr))
            l_ptr += 1
            r_ptr += 1
            mid += 1


"""
    Implementation of Merging Subarrys from Quick Sort Algorithm
    Input:
        arr: list to be sorted
        n: number of threads
"""
def msqsa(arr: list[int], n: int) -> None:

    # Creates n child threads sorting their corresponding portion
    threads = []
    length = int(len(arr)/n)          # length of each portion
    for i in range(n):
        threads.append(threading.Thread(
            target=it_rand_qs,
            args=(arr, i*length, (i+1)*(length-1))
        ))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Merge-Sort the sorted sub-arrays
    length = int(len(arr)/n)
    left = 0
    while length < len(arr):
        while left + length < len(arr):
            merge(arr, left, length)
            left = left + length
        length = length * 2
        left = 0

    print(arr)

if __name__ == "__main__":

    random.seed(31266797)

    msqsa(get_rand_data(100, 10), 10)

