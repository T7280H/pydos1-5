# locas.py
import os

def locas_command(line):
    try:
        current_location = os.getcwd()
        print(f"Current location: {current_location}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    locas_command()