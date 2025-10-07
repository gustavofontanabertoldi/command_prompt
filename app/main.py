import sys
import os
import importlib

commands_dir = os.path.join(os.path.dirname(__file__), "commands")
commands={}

for arquivo in os.listdir(commands_dir):
    if arquivo.endswith(".py") and arquivo != "__init__.py":
        name = arquivo[:-3]
        module = importlib.import_module(f"commands.{name}")
        commands[name] = module

def main():
    while True:
        # sys.stdout.write("$ ")

        # command = input()
        # command_list = command.split()
        # cmd = command_list[0]
        # args = command_list[1:]

        # if cmd in commands:
        #     commands[cmd](*args)
        # else:
        #     print(f'invalid command')
        ...
        

if __name__ == "__main__":
    main()
