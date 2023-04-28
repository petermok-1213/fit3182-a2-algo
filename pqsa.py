import random

def gen_rand_data(size: int, max: int) -> list:
    int_list = []
    for _ in range(size):
        int_list.append(random.randrange(start=0, stop=max))
    return int_list

def partition(arr: list[int], pivot_index: int) -> tuple[list[int], int]:
    store_index = 0
    for i in range(len(arr)):
        if arr[i] <= arr[pivot_index] and i != pivot_index:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            if pivot_index == store_index:
                pivot_index = i
            store_index += 1

    arr[pivot_index], arr[store_index] = arr[store_index], arr[pivot_index]
    pivot_index = store_index
    return (arr, pivot_index)

def pqsa(arr: list[int]) -> list[int]:
    if len(arr) > 1:
        pivot = random.randrange(start=0, stop=len(arr)-1)  # selecting a random index as pivot
        x = pqsa(arr[:pivot])
        y = pqsa(arr[pivot+1:])
        print(x)
        print(y)
    else:
        return arr

if __name__ == "__main__":
    random.seed(123123123123)
    data = gen_rand_data(10, 10)
    print(data)
    print(partition(data, 4))
    

