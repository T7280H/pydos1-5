import subprocess
import os

def bomb_command():
    # مسیر فایل pybomb.py در فولدر apps
    pybomb_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'apps', 'pybomb.py'))
    
    if os.path.exists(pybomb_path):
        # اجرای فایل pybomb.py
        subprocess.run(['python', pybomb_path])
    else:
        print(f"File not found: {pybomb_path}")

if __name__ == "__main__":
    bomb_command()