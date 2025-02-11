# find.py
import os

def find_command(file_name, path="."):
    for root, dirs, files in os.walk(path):
        if file_name in files:
            print(os.path.join(root, file_name))

if __name__ == "__main__":
    file_name = input("Enter the file name to search for: ")
    path = input("Enter the directory path to search in (default is current directory): ") or "."
    find_command(file_name, path)