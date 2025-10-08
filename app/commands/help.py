import os
import importlib

NAME = "help"

commands_dir = os.path.join(os.path.dirname(__file__))
commands = {}

def run():
    print("=======Lista de comandos=======")
    for arquivo in os.listdir(commands_dir):
        if arquivo.endswith(".py") and arquivo != "__init__.py":
            nome = arquivo[:-3]
            print(f"{nome}\n")