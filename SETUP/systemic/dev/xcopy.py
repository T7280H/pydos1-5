import shutil
import os

def xcopy_command(source, destination):
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
            print(f"Directory '{source}' copied to '{destination}' successfully.")
        elif os.path.isfile(source):
            shutil.copy2(source, destination)
            print(f"File '{source}' copied to '{destination}' successfully.")
        else:
            print(f"Error: The source '{source}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    source = input("Enter the source file/directory path: ")
    destination = input("Enter the destination path: ")
    xcopy_command(source, destination)