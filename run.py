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
            pass
        elif cmd_parts[0] == "msqsa":
            pass
        elif cmd_parts[0] == "msqsa_mod":
            pass
        else:
            print("invalid command")
