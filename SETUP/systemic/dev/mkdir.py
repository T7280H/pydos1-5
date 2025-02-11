# mkdir.py
import os

def mkdir_command(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    mkdir_command("new_directory")  # You can change "new_directory" to the name you want.