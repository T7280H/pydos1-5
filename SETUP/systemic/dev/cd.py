# cd.py
import os

def cd_command(directory):
    try:
        os.chdir(directory)
        print(f"Changed directory to {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{directory}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    cd_command(directory)