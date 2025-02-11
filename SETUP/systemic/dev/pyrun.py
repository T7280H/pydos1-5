import subprocess
import os

def pyrun_command(file_name):
    """
    اجرای فایل پایتونی
    """
    try:
        if file_name.endswith('.py'):
            if os.path.exists(file_name):
                subprocess.run(['python', file_name])
            else:
                print(f"{file_name} not found.")
        else:
            print("Please provide a valid Python file with .py extension.")
    except Exception as e:
        print(f"An error occurred while running {file_name}: {e}")

if __name__ == "__main__":
    file_name = input("Enter the name of the Python file to run: ")
    pyrun_command(file_name)