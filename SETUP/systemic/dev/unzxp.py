import zipfile
import os

def unzxp_command(zip_file, destination):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall(destination)
            print(f"ZIP file '{zip_file}' extracted to '{destination}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    zip_file = input("Enter the zip file path: ")
    destination = input("Enter the destination directory path: ")
    unzxp_command(zip_file, destination)