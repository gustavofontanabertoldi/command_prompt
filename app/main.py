import sys
import os


def main():
    while True:
        sys.stdout.write("$ ")

        commands={
            "exit": lambda exit_code: os._exit(int(exit_code)),
            "echo": lambda *args: print(" ".join(args)),
        }
        # Wait for user input
        command = input()
        command_list = command.split()
        args = command_list[1:]

        for i in command_list:
            if i in commands:
                commands[i](*args)



if __name__ == "__main__":
    main()
