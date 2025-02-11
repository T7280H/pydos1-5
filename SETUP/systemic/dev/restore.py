# restore.py
import shutil
import os

def restore_command(backup_path, restore_path):
    try:
        if os.path.isfile(backup_path):
            shutil.copy2(backup_path, restore_path)
            print(f"File '{backup_path}' restored to '{restore_path}' successfully.")
        elif os.path.isdir(backup_path):
            shutil.copytree(backup_path, restore_path)
            print(f"Directory '{backup_path}' restored to '{restore_path}' successfully.")
        else:
            print(f"Error: The backup source '{backup_path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    backup_path = input("Enter the backup file/directory path: ")
    restore_path = input("Enter the restore destination path: ")
    restore_command(backup_path, restore_path)