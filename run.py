import time
from threading import Thread

from msqsa import msqsa
from pqsa import pqsa
from rand_qs import get_rand_data
from threadpool import ThreadPool


def cmds():
    print(
        "Syntax: algo data_size data_max_val max_thread"
        "\n"
        "Available Algorithms:"
        "  pqsa"
        "  msqsa"
        "  msqsa_mod"
        "\n"
        "data_size: length of the list; int > 0"
        "data_max_val: maximum value of elements in list; int > 0"
        "max_thread: maximum number of threads allocate: int > 0"
    )


if __name__ == "__main__":
    while True:
        cmd = input(
            "enter cmds to see available commands\n"
            "      ctrl+c anytime to quit the program"
            "Awaiting command...\n"
        )
        cmd_parts = cmd.split(" ")

        if cmd_parts[0] == "cmds":
            cmds()
        elif cmd_parts[0] in ["pqsa", "msqsa", "msqsa_mod"]:
            try:
                data_size = int(cmd_parts[1])
                max_val = int(cmd_parts[2])
                max_worker = int(cmd_parts[3])
            except ValueError:
                print("Value Error")
                break
            else:
                data = get_rand_data(data_size, max_val)
                threadpool = ThreadPool(max_worker)

                if cmd_parts[0] == "pqsa":
                    start = time.time()
                    threadpool.pool.put(Thread(target=pqsa, args=(data, 0, len(data)-1)))
                    threadpool.start_worker()
                    threadpool.pool.join()
                    threadpool.stop_worker()
                    end = time.time()
                elif cmd_parts[0] == "msqsa":
                    msqsa(data, max_worker)
                elif cmd_parts[0] == "msqsa_mod":
                    threadpool.pool.put(Thread(target=msqsa, args=(data, max_worker)))

                print(data == sorted(data))
                print(end-start)

        else:
            print("invalid command")
