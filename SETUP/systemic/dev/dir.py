# dir.py
import os

def dir_command(path="."):
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dir_command()