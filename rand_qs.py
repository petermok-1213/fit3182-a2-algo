import copy
import random

'''
    A function for generating a list of random numbers
    Input:
        length: length of the output list
        max_val: maximum value of elements
    Output:
        a list with length == size of random integers with values in the range of 0 to limit-1 inclusively
'''
def get_rand_data(length: int, max_val: int) -> list:
    return [random.randrange(start=0, stop=max_val) for _ in range(length)]


'''
    In-place Partitioning function for quick sort, pivot is randomly chosen
    returns the pivot index
    Input:
        arr: the list to be partitioned
        left: start partitioning from this index
        right: stop partitioning at this index
    Output:
        pivot_index: int
'''
def rand_partition(arr: list[int], left: int, right: int) -> int:
    pivot_index = random.randrange(start=left, stop=right)  # selecting a random index as pivot
    store_index = left
    for i in range(left, right+1):
        if arr[i] < arr[pivot_index] and i != pivot_index:  # if element i is smaller than pivot
            arr[store_index], arr[i] = arr[i], arr[store_index]  # swap elements in i and store_index
            if pivot_index == store_index:  # if element i is swapped with pivot
                pivot_index = i  # pivot_index become i
            store_index += 1

    arr[pivot_index], arr[store_index] = arr[store_index], arr[pivot_index]  # Swap elements of (pivot_index, store_index)
    pivot_index = store_index  # update pivot_index
    return pivot_index

"""
    In-place iterative random quick sort algorithm
    Inputs:
        arr: list to be sorted
        left: sort from this index
        right: sort to this index
"""
def it_rand_qs(arr: list[int], left: int, right: int):
    stack = []                      # stack for index-pair of the array
    stack.insert(0, (left, right))  # initial (partition from, partition to) pair
    while len(stack) > 0:
        left, right = stack.pop(0)  # get index-pair to partition
        pivot = rand_partition(arr, left, right)    # partition arr and get pivot
        if pivot-1 > left:                          # If there are elements left of pivot
            stack.insert(0, (left, pivot-1))
        if pivot+1 < right:
            stack.insert(0, (pivot+1, right))


'''
    In-place recursive random quick sort algorithm
    Input:
        arr: the list to be partitioned
        left: start partitioning from this index
        right: stop partitioning at this index
'''
def rs_rand_qs(arr: list[int], left: int, right: int) -> list[int]:
    if right > left:
        pivot = rand_partition(arr, left, right)
        rs_rand_qs(arr, left, pivot)
        rs_rand_qs(arr, pivot + 1, right)
    return arr

'''
    Function for testing rand_qs()
    Input:
        length: length of the array
        max_val: maximum value of elements
    Output:
        pass: array is sorted
'''
def test_rand_qs(length: int, max_val: int):
    data = get_rand_data(length, max_val)
    test_data = copy.deepcopy(data)
    rs_rand_qs(data, 0, len(data) - 1)
    test_data.sort()
    return data == test_data


if __name__ == "__main__":
    random.seed(31266797)
    n = 100
    data = get_rand_data(n, 100)
    test_data = copy.deepcopy(data)
    test_data.sort()

    it_rand_qs(data, 0, len(data)-1)
    print(data == test_data)
