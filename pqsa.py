import random


'''
    A function for generating a list of random numbers

    Input:
        size: int
        max: int
    Output:
        a list with length == size of random integers with values in the range of 0 to max-1 inclusively
'''
def gen_rand_data(size: int, max: int) -> list:
    int_list = []
    for _ in range(size):
        int_list.append(random.randrange(start=0, stop=max))
    return int_list


'''
    In-place Partitioning function for quick sort,
    returns the pivot index

    Input:
        arr: list[int]
    Output:
        pivot_index: int
'''
def partition(arr: list[int], left, right) -> int:
    pivot_index = random.randrange(start=left, stop=right)  # selecting a random index as pivot
    store_index = left
    for i in range(left+1, right):
        if arr[i] <= arr[pivot_index] and i != pivot_index:                     # if element i is smaller than pivot
            arr[store_index], arr[i] = arr[i], arr[store_index]                 # swap elements in i and store_index
            if pivot_index == store_index:                                          # if element i is swapped with pivot     
                pivot_index = i                                                     # pivot_index become i
            store_index += 1

    arr[pivot_index], arr[store_index] = arr[store_index], arr[pivot_index]     # Swap elements of (pivot_index, store_index)
    pivot_index = store_index                                                   # update pivot_index 
    return pivot_index

def pqsa(arr: list[int], left, right) -> list[int]:
    if right > left:
        pivot = partition(arr, left, right)
        pqsa(arr, left, pivot)
        pqsa(arr, pivot+1, right)

if __name__ == "__main__":
    random.seed(31266797)
    data = gen_rand_data(15, 10)
    print(data)
    pqsa(data, 0, len(data))
    print(data)
