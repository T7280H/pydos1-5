import os
import time
import subprocess
import sys
from colorama import init, Fore, Style
from tqdm import tqdm

# لیست فایل‌های ضروری
REQUIRED_FILES = [
    "dev/__init__.py",
    "dev/exit.py",
    "dev/dir.py",
    "dev/ping.py",
    "dev/calc.py",
    "dev/date.py",
    "dev/edit.py",
    "dev/find.py",
    "dev/help.py",
    "dev/mkdir.py",
    "dev/rd.py",
    "dev/time.py",
    "dev/ver.py",
    "dev/restore.py",
    "dev/reminder.py",
    "dev/connect.py",
    "dev/IPconfig.py",
    "dev/xxcfg.py",
    "dev/bomb.py",
    "dev/pyrun.py",
    "dev/cls.py",
    "dev/echo.py",
    "dev/bootinf.py",
    "dev/cd.py",
    "dev/locas.py",
    "dev/backup.py",
    "dev/xcopy.py",
    "dev/zxp.py", 
    "dev/unzxp.py", 
    "banner/__init__.py",
    "banner/banner.py",
    "main/pydos.py"
]

# بررسی فایل‌های ضروری
def check_files():
    all_files_present = True
    for f in REQUIRED_FILES:
        file_path = os.path.join(os.path.dirname(__file__), f)
        if os.path.exists(file_path):
            print(Fore.GREEN + f"Checked: {f} - OK" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Checked: {f} - Missing" + Style.RESET_ALL)
            all_files_present = False

    if not all_files_present:
        print(Fore.RED + "Error: Some required files are missing. Boot process stopped." + Style.RESET_ALL)
        sys.exit(1)
    else:
        print(Fore.GREEN + "All required files are present." + Style.RESET_ALL)

# نمایش انیمیشن لودینگ با tqdm
def display_loading():
    for i in tqdm(range(100), desc="Booting"):
        time.sleep(0.02)  # Simulate boot time

    boot_message = "System is booting up..."
    print(boot_message)
    print(f"Running from: {os.path.abspath(__file__)}")

# اجرای فایل PyDOS.py
def run_pydos():
    time.sleep(2)
    os.system('clear')
    pydos_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main', 'pydos.py'))
    subprocess.run(['python', pydos_path])

# اجرای اصلی
if __name__ == "__main__":
    init(autoreset=True)
    check_files()
    display_loading()
    run_pydos()
