import os
import shutil
import subprocess
import time
import curses
from tqdm import tqdm
from colorama import init

init()

def print_center(stdscr, text, delay=0.01):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    x = width // 2 - len(text) // 2
    y = height // 2
    for char in text:
        stdscr.addstr(y, x, char)
        stdscr.refresh()
        time.sleep(delay)
        x += 1
    time.sleep(1)
    stdscr.clear()
    stdscr.refresh()

def print_slow(stdscr, text, delay=0.01):
    height, width = stdscr.getmaxyx()
    lines = []
    for i in range(0, len(text), width - 1):
        lines.append(text[i:i + width - 1])
    for line in lines:
        stdscr.addstr(line + "\n")
        stdscr.refresh()
        time.sleep(delay)
    stdscr.refresh()

def display_setup_banner(stdscr):
    banner = """
.---. .-..-..---.  .--.  .--. 
: .; :: :: :: .  :: ,. :: .--'
:  _.'`.  .': :: :: :: :`. `. 
: :    .' ; : :; :: :; : _`, :
:_;   :_,'  :___.'`.__.'`.__.'
    """
    print_slow(stdscr, banner)

def welcome_message(stdscr):
    # Clear the screen to provide a clean slate
    stdscr.clear()
    stdscr.refresh()
    
    # Display the welcome message with a typing effect
    print_slow(stdscr, "PyDOS is a Python program with a text-based user interface.")
    print_slow(stdscr, "This is version 1.5 beta, updated from version 1.0 alpha.")
    print_slow(stdscr, "To install the system, press the Next button, and to exit, press the Exit button.")
    
    # Pause for 2 seconds before clearing the screen
    time.sleep(2)

def check_files(files, base_path):
    missing_files = []
    for file in files:
        if not os.path.exists(os.path.join(base_path, file)):
            missing_files.append(file)
    return missing_files

def linear_loading(stdscr, message, duration=2):
    for i in tqdm(range(100), desc=message):
        time.sleep(duration / 100)
    stdscr.addstr("\n")
    stdscr.refresh()

def draw_menu(stdscr, selected_row_idx, menu):
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h - 2 - len(menu) + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def select_install_path(stdscr):
    stdscr.clear()
    stdscr.refresh()
    print_slow(stdscr, "Please select the installation path.")
    stdscr.addstr("Enter the installation path (e.g., /storage/emulated/0): ")
    stdscr.refresh()
    curses.echo()
    install_path = stdscr.getstr().decode().strip()
    return install_path

def enter_name_and_company(stdscr):
    stdscr.clear()
    stdscr.refresh()
    print_slow(stdscr, "Please enter your name and company information.")
    stdscr.addstr("Enter your name: ")
    stdscr.refresh()
    curses.echo()
    name = stdscr.getstr().decode().strip()
    stdscr.addstr("Enter your company: ")
    stdscr.refresh()
    company = stdscr.getstr().decode().strip()
    return name, company

def license_agreement(stdscr):
    stdscr.clear()
    stdscr.refresh()
    license_text = """
    PyDOS License Agreement
    ------------------------
    By using this software, you agree to the following terms and conditions:
    1. You may use this software for personal and commercial purposes.
    2. Redistribution of this software is prohibited without prior written consent.
    3. The author is not responsible for any damage caused by the use of this software.
    """
    print_slow(stdscr, license_text)
    menu = ["Yes", "No"]
    current_row = 0
    while True:
        draw_menu(stdscr, current_row, menu)
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                return True
            else:
                return False

def save_user_info(stdscr, name, company, install_path):
    user_info_path = os.path.join(install_path, "usr.txt")
    with open(user_info_path, "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Company: {company}\n")
    print_slow(stdscr, f"User information saved to {user_info_path}")

def check_memory(stdscr):
    print_slow(stdscr, "Checking memory...")
    linear_loading(stdscr, "Checking memory")
    print_slow(stdscr, "Memory check complete.")

def create_directories(stdscr, destination):
    directories = ["dev", "main", "banner", "apps"]
    for directory in directories:
        os.makedirs(os.path.join(destination, directory), exist_ok=True)
    print_slow(stdscr, "Directories created successfully")

def copy_files(stdscr, files, base_path, destination):
    print_slow(stdscr, "Copying files...")
    for file, target_dir in tqdm(files.items(), desc="Copying files"):
        target_path = os.path.join(destination, target_dir)
        try:
            shutil.copy(os.path.join(base_path, file), target_path)
        except FileNotFoundError:
            print_slow(stdscr, f"Error: {file} not found. Skipping...")
    print_slow(stdscr, "Files copied successfully")

def copy_boot_file(stdscr, base_path, install_path):
    print_slow(stdscr, "Copying boot.py...")
    shutil.copy(os.path.join(base_path, "boot.py"), install_path)
    print_slow(stdscr, "boot.py copied successfully")

def install_requirements(stdscr, base_path):
    print_slow(stdscr, "Installing required packages...")
    try:
        subprocess.check_call(["pip", "install", "-r", os.path.join(base_path, "requirements.txt")])
        print_slow(stdscr, "Requirements installed successfully")
    except Exception as e:
        print_slow(stdscr, f"Error installing requirements: {e}")

def setup_complete(stdscr):
    print_slow(stdscr, "Setup is complete. PyDOS is installed, please press Enter to exit Setup")

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.bkgd(' ', curses.color_pair(2))
    current_row = 0

    base_path = "systemic"
    required_files = [
        "dev/__init__.py", "dev/help.py", "dev/echo.py", "dev/rd.py", "dev/connect.py", 'dev/IPconfig.py', "dev/edit.py", 
        "dev/xxcfg.py", "dev/bootinf.py", "dev/dir.py", "dev/reminder.py", "dev/time.py", "dev/date.py", "dev/dash.py", 
        "dev/zxp.py", "dev/unzxp.py", "dev/opz.py", "dev/pyrun.py", "dev/ping.py", "dev/locas.py", "dev/mkdir.py", 
        "dev/cd.py", "dev/xcopy.py", "dev/calc.py", "dev/find.py", "dev/backup.py", "dev/restore.py", "dev/ver.py", 
        "dev/exit.py", "dev/cls.py", "main/pydos.py", "banner/banner.py", "banner/HACKER.py", "banner/logo.py", 
        "banner/PyDOSbanner.py", "banner/__init__.py", "apps/__init__.py", "apps/editor.py", "apps/pybomber.py", "boot.py", 
        "requirements.txt"
    ]

    files = {
        "main/pydos.py": "main", 
        "dev/echo.py": "dev", 
        "dev/dir.py": "dev", 
        "dev/cd.py": "dev", 
        "dev/rd.py": "dev", 
        "dev/xxcfg.py": "dev", 
        "dev/bootinf.py": "dev", 
        "dev/help.py": "dev", 
        "dev/locas.py": "dev", 
        "dev/mkdir.py": "dev", 
        "dev/time.py": "dev", 
        "dev/date.py": "dev", 
        "dev/IPconfig.py": "dev", 
        "dev/connect.py": "dev", 
        "dev/dash.py": "dev", 
        "dev/bootinf.py": "dev", 
        "dev/xcopy.py": "dev", 
        "dev/ping.py": "dev", 
        "dev/pyrun.py": "dev", 
        "dev/find.py": "dev", 
        "dev/calc.py": "dev", 
        "dev/unzxp.py": "dev", 
        "dev/zxp.py": "dev", 
        "dev/opz.py": "dev", 
        "dev/backup.py": "dev", 
        "dev/restore.py": "dev", 
        "dev/reminder.py": "dev", 
        "dev/ver.py": "dev", 
        "dev/exit.py": "dev", 
        "dev/cls.py": "dev", 
        "dev/bomb.py": "dev", 
        "dev/edit.py": "dev", 
        "dev/__init__.py": "dev", 
        "banner/banner.py": "banner", 
        "banner/HACKER.py": "banner", 
        "banner/logo.py": "banner", 
        "banner/PyDOSbanner.py": "banner", 
        "banner/__init__.py": "banner", 
        "apps/editor.py": "apps", 
        "apps/pybomber.py": "apps", 
        "apps/__init__.py": "apps"
    }

    # Stage 1
    print_center(stdscr, "SETUP IS STARTING...")
    print_slow(stdscr, "Checking required files...")
    missing_files = check_files(required_files, base_path)
    if missing_files:
        print_slow(stdscr, "Required files are missing. Setup cannot proceed.")
        print_slow(stdscr, f"Missing files: {', '.join(missing_files)}")
        return
    linear_loading(stdscr, "Checking files")

    # Stage 2
    print_center(stdscr, "Welcome to PyDOS Setup")
    welcome_message(stdscr)

    # Stage 3
    menu = ["Install PyDOS", "Exit"]
    while True:
        draw_menu(stdscr, current_row, menu)
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 1:
                return
            break

    # Stage 4
    print_center(stdscr, "Select Installation Path")
    install_path = select_install_path(stdscr)

    # Stage 5
    while True:
        print_center(stdscr, "Enter Name and Company")
        name, company = enter_name_and_company(stdscr)
        if name and company:
            break
        menu = ["Retry", "Back"]
        current_row = 0
        while True:
            draw_menu(stdscr, current_row, menu)
            key = stdscr.getch()
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 1:
                    return
                break

    # Stage 6
    if not license_agreement(stdscr):
        print_slow(stdscr, "You must accept the license agreement to proceed.")
        return

    # Save user info
    save_user_info(stdscr, name, company, install_path)

    # Stage 7
    print_center(stdscr, "SETUP IS CHECKING YOUR MEMORY...")
    check_memory(stdscr)

    # Create directories
    print_center(stdscr, "SETUP IS CREATING DICTIONARIES...")
    create_directories(stdscr, install_path)

    # Stage 8
    print_center(stdscr, "SETUP IS COPYING SYSTEM FILES...")
    copy_files(stdscr, files, base_path, install_path)

    # Copy boot file
    print_center(stdscr, "SETUP IS COPYING BOOT.PY...")
    copy_boot_file(stdscr, base_path, install_path)

    # Stage 9
    print_center(stdscr, "SETUP IS INSTALLING RQUIREMENTS...")
    install_requirements(stdscr, base_path)

    # Stage 10
    print_center(stdscr, "Setup Complete")
    setup_complete(stdscr)
    menu = ["Exit"]
    current_row = 0
    while True:
        draw_menu(stdscr, current_row, menu)
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                return

if __name__ == "__main__":
    curses.wrapper(main)
