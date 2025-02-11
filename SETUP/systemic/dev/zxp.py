import zipfile
import os

def zxp_command(source, destination):
    try:
        with zipfile.ZipFile(destination, 'w') as zipf:
            if os.path.isdir(source):
                for root, dirs, files in os.walk(source):
                    for file in files:
                        zipf.write(os.path.join(root, file), 
                                   os.path.relpath(os.path.join(root, file), 
                                                   os.path.join(source, '..')))
                print(f"Directory '{source}' compressed to '{destination}' successfully.")
            elif os.path.isfile(source):
                zipf.write(source, os.path.basename(source))
                print(f"File '{source}' compressed to '{destination}' successfully.")
            else:
                print(f"Error: The source '{source}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    source = input("Enter the source file/directory path: ")
    destination = input("Enter the destination zip file path: ")
    zxp_command(source, destination)