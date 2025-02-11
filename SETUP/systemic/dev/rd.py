# rd.py
import os
import shutil

def rd_command(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Directory '{path}' deleted successfully.")
        else:
            print(f"Path '{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    rd_command("path_to_delete")  # You can change "path_to_delete" to the path you want to delete.