import os

NAME = "clear"

def run():
    os.system('cls' if os.name == 'nt' else 'clear')