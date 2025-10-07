import sys
import os


def main():
    while True:
        sys.stdout.write("$ ")

        def help():
            print("=======Lista de comandos=======")
            for cm in commands:
                print(cm)

        commands={
            "exit": lambda exit_code: os._exit(int(exit_code)),
            "echo": lambda *args: print(" ".join(args)),
            "clear": lambda: os.system('cls' if os.name == 'nt' else 'clear'),
            "type": lambda cmd, *_: print(f'{cmd} is a shell builtin') if cmd in commands else print(f"{cmd} is not a shell builtin"),
            "help": help,
        }

        command = input()
        command_list = command.split()
        cmd = command_list[0]
        args = command_list[1:]

        if cmd in commands:
            commands[cmd](*args)



if __name__ == "__main__":
    main()
