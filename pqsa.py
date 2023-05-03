import random

'''
    A function for generating a list of random numbers
    Input:
        size: length of the output list
        limit: maximum value of elements
    Output:
        a list with length == size of random integers with values in the range of 0 to limit-1 inclusively
'''
def get_rand_data(size: int, limit: int) -> list:
    int_list = []
    for _ in range(size):
        int_list.append(random.randrange(start=0, stop=limit))
    return int_list


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


'''
    In-place random quick sort algorithm
    Input:
        arr: the list to be partitioned
        left: start partitioning from this index
        right: stop partitioning at this index
'''
def rand_qs(arr: list[int], left: int, right: int) -> None:
    if right > left:
        pivot = rand_partition(arr, left, right)
        rand_qs(arr, left, pivot)
        rand_qs(arr, pivot+1, right)


if __name__ == "__main__":
    random.seed(31266797)
    size = 20
    limit = 20
    data = get_rand_data(size, limit)
    print(data)
    rand_qs(data, 0, len(data)-1)
    print(data)
