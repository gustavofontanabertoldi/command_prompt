import os

NAME = "exit"

def run(*args):
    os._exit(int(args))