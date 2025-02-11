import sys
import time

def animate_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

def bootinf_command():
    animate_text("PyDos Bootable 1.5 Beta")
    animate_text("Created by T7280H")

if __name__ == "__main__":
    bootinf_command()