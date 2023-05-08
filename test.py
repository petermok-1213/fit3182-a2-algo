import sys, time, threading, random, copy
import rand_qs, pqsa, msqsa


def print_sorting_time(sorting_thread: threading.Thread) -> None:
    start_time = time.time()
    sorting_thread.start()
    sorting_thread.join()
    end_time = time.time()
    print(sorting_thread.name + " Time Taken: " + str(end_time-start_time) + " seconds")


if __name__ == "__main__":
    random.seed(3126679)
    n = 1000
    sys.setrecursionlimit(n)  # force increase maximum recursion depth to avoid Exception

    data = rand_qs.get_rand_data(n, 100)

    main_pqsa_thread = pqsa.PQSAThread(copy.deepcopy(data), 0, n - 1, name="PQSA")
    print_sorting_time(main_pqsa_thread)

    rand_qs_thread = threading.Thread(target=rand_qs.rs_rand_qs, args=(copy.deepcopy(data), 0, n - 1), name="Random Quick Sort")
    print_sorting_time(rand_qs_thread)
