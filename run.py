from threading import Thread

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
        elif cmd_parts[0] == "pqsa":
            data_size = int(cmd_parts[1])
            max_val = int(cmd_parts[2])
            data = get_rand_data(data_size, max_val)

            max_worker = int(cmd_parts[3])
            threadpool = ThreadPool(max_worker)
            threadpool.pool.put(Thread(target=pqsa, args=(data, 0, len(data)-1)))
            threadpool.start_worker()
            threadpool.pool.join()
            threadpool.stop_worker()

            print(data == sorted(data))


        elif cmd_parts[0] == "msqsa":
            pass
        elif cmd_parts[0] == "msqsa_mod":
            pass
        else:
            print("invalid command")
