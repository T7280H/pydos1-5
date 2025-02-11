import shutil
import os

def backup_command(source, destination):
    try:
        if os.path.isfile(source):
            shutil.copy2(source, destination)
            print(f"File '{source}' backed up to '{destination}' successfully.")
        elif os.path.isdir(source):
            shutil.copytree(source, destination)
            print(f"Directory '{source}' backed up to '{destination}' successfully.")
        else:
            print(f"Error: The source '{source}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    source = input("Enter the source file/directory path: ")
    destination = input("Enter the destination path: ")
    backup_command(source, destination)