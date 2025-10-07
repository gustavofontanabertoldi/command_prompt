import commands
import os
import importlib

NAME = "help"

def run():
    print("=======Lista de comandos=======")
    for arquivo in os.listdir("commands"):
        if arquivo.endswith(".py"):
            nome = arquivo[:-3]
            print(f"{nome}\n")