import random
import time
from threading import Thread

from msqsa import msqsa, msqsa_mod
from pqsa import pqsa
from rand_qs import get_rand_data
from threadpool import ThreadPool, create_worker_threads


def cmds():
    print(
        "Syntax: algo data_size data_max_val max_thread\n"
        "\n"
        "Available Algorithms:\n"
        "  pqsa\n"
        "  msqsa\n"
        "  msqsa_mod\n"
        "\n"
        "data_size: length of the list; int > 0\n"
        "data_max_val: maximum value of elements in list; int > 0\n"
        "max_thread: maximum number of threads allocate: int > 0\n"
    )


if __name__ == "__main__":
    random.seed(31266797)

    while True:

        cmd_parts = input(
            "enter cmds to see available commands\n"
            "Awaiting command...\n"
        ).split(" ")

        if cmd_parts[0] == "cmds":
            cmds()
        elif cmd_parts[0] in ["pqsa", "msqsa", "msqsa_mod"]:
            try:
                data_size = int(cmd_parts[1])
                max_val = int(cmd_parts[2])
                max_thread = int(cmd_parts[3])
            except ValueError:
                print("Invalid value for parameters data_size/data_max_val/max_thread")
            else:
                print("Generating data...")
                data = get_rand_data(data_size, max_val)
                create_worker_threads(max_thread)


                if cmd_parts[0] == "pqsa":
                    ThreadPool().pool.put(Thread(target=lambda:pqsa(data, 0, len(data)-1)))
                elif cmd_parts[0] == "msqsa":
                    ThreadPool().pool.put(Thread(target=lambda:msqsa(data, 0, len(data)-1)))
                else:
                    ThreadPool().pool.put(Thread(target=lambda:msqsa_mod(data, 0, len(data)-1)))

                print("Sorting...")
                start = time.time()

                ThreadPool().pool.join()
                end = time.time()
                print("List sorted: " + str(data == sorted(data)))
                print("Time taken: " + str(end - start) + "\n")

        else:
            print("invalid command\n")
