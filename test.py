import sys, time, threading, random, copy
import rand_qs, pqsa, msqsa

if __name__ == "__main__":
    random.seed(3126679)
    n = 100000
    sys.setrecursionlimit(n)  # force increase maximum recursion depth to avoid Exception

    data = rand_qs.get_rand_data(n, 100)
    test_data = copy.deepcopy(data)

    main_pqsa_thread = pqsa.PQSAThread(data, 0, n - 1)
    start = time.time()
    main_pqsa_thread.start()
    main_pqsa_thread.join()
    pqsa_time = time.time() - start
    print("Parallel: ", pqsa_time)

    rand_qs_thread = threading.Thread(target=rand_qs.rand_qs, args=(test_data, 0, n - 1))
    start = time.time()
    rand_qs_thread.start()
    rand_qs_thread.join()
    print("Serial: ", time.time() - start)
