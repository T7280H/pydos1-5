# cls.py
import os

def cls_command():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    cls_command()