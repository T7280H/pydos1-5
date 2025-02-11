import os
import curses

accounts = {}

def create_account(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Create an account", curses.color_pair(1))
    stdscr.addstr(1, 0, "Username: ")
    curses.echo()
    username = stdscr.getstr(1, 10).decode('utf-8')
    stdscr.addstr(2, 0, "Password: ")
    password = stdscr.getstr(2, 10).decode('utf-8')
    curses.noecho()
    
    accounts[username] = password
    stdscr.addstr(4, 0, "Account created successfully!")
    stdscr.refresh()
    stdscr.getch()

def login_account(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Login to your account", curses.color_pair(1))
    stdscr.addstr(1, 0, "Username: ")
    curses.echo()
    username = stdscr.getstr(1, 10).decode('utf-8')
    stdscr.addstr(2, 0, "Password: ")
    password = stdscr.getstr(2, 10).decode('utf-8')
    curses.noecho()
    
    if username in accounts and accounts[username] == password:
        stdscr.addstr(4, 0, "Login successful!")
    else:
        stdscr.addstr(4, 0, "Login failed. Incorrect username or password.")
    
    stdscr.refresh()
    stdscr.getch()

def display_message_box(stdscr, message):
    height, width = stdscr.getmaxyx()
    box_height, box_width = 7, 50
    box_y, box_x = (height - box_height) // 2, (width - box_width) // 2

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(box_y, box_x, "+" + "-" * (box_width - 2) + "+")
    for i in range(1, box_height - 1):
        stdscr.addstr(box_y + i, box_x, "|" + " " * (box_width - 2) + "|")
    stdscr.addstr(box_y + box_height - 1, box_x, "+" + "-" * (box_width - 2) + "+")
    stdscr.attroff(curses.color_pair(1))

    stdscr.addstr(box_y + 2, box_x + (box_width - len(message)) // 2, message)
    stdscr.addstr(box_y + 4, box_x + 18, "[ OK ]  [ Cancel ]")

    stdscr.refresh()
    selected_button = 0

    while True:
        stdscr.attron(curses.color_pair(2) if selected_button == 0 else curses.color_pair(1))
        stdscr.addstr(box_y + 4, box_x + 18, "[ OK ]")
        stdscr.attroff(curses.color_pair(2) if selected_button == 0 else curses.color_pair(1))

        stdscr.attron(curses.color_pair(2) if selected_button == 1 else curses.color_pair(1))
        stdscr.addstr(box_y + 4, box_x + 26, "[ Cancel ]")
        stdscr.attroff(curses.color_pair(2) if selected_button == 1 else curses.color_pair(1))

        key = stdscr.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT]:
            selected_button = (selected_button + 1) % 2
        elif key in [10, 13]:  # Enter key
            return selected_button == 0  # OK -> True, Cancel -> False

def change_banner(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Select your banner", curses.color_pair(1))
    
    # استفاده از مسیر مطلق برای پوشه banner
    banner_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banner'))
    banners = [f for f in os.listdir(banner_dir) if os.path.isfile(os.path.join(banner_dir, f)) and f not in ["__init__.py", "current_banner.txt"]]

    selected_idx = 0
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Select your banner", curses.color_pair(1))
        for idx, banner in enumerate(banners):
            if idx == selected_idx:
                stdscr.addstr(idx + 1, 0, f"> {banner}", curses.color_pair(2))
            else:
                stdscr.addstr(idx + 1, 0, f"  {banner}", curses.color_pair(1))

        stdscr.addstr(len(banners) + 2, 0, "<OK> <Cancel>")
        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_idx > 0:
            selected_idx -= 1
        elif key == curses.KEY_DOWN and selected_idx < len(banners) - 1:
            selected_idx += 1
        elif key == 10:  # Enter key
            if display_message_box(stdscr, "Do you want to select this banner?"):
                selected_banner = banners[selected_idx]
                with open(os.path.join(banner_dir, 'current_banner.txt'), 'w') as f:
                    f.write(selected_banner)
                stdscr.addstr(len(banners) + 2, 0, f"Banner '{selected_banner}' selected.", curses.color_pair(1))
                stdscr.refresh()
                stdscr.getch()
                break
        elif key == 27:  # Esc key
            break

    stdscr.refresh()
    stdscr.getch()

def opz_command():
    def main(stdscr):
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

        stdscr.clear()
        stdscr.bkgd(curses.color_pair(1))
        stdscr.addstr(0, 0, "PyDOS Option", curses.color_pair(1))
        stdscr.refresh()

        options = [
            "1) Create an account",
            "2) Login to your account",
            "3) Change your banner from banner folder",
            "4) Back to PyDOS"
        ]

        selected_option = 0
        while True:
            stdscr.clear()
            stdscr.bkgd(curses.color_pair(1))
            stdscr.addstr(0, 0, "PyDOS Option", curses.color_pair(1))
            height, width = stdscr.getmaxyx()

            for i, option in enumerate(options):
                x = width // 2 - len(option) // 2
                y = height // 2 - len(options) // 2 + i + 1  # اضافه کردن 1 به y برای چاپ در خطوط بعد از "PyDOS Option"
                if i == selected_option:
                    stdscr.addstr(y, x, option, curses.color_pair(2))
                else:
                    stdscr.addstr(y, x, option, curses.color_pair(1))

            stdscr.refresh()
            key = stdscr.getch()

            if key == curses.KEY_UP and selected_option > 0:
                selected_option -= 1
            elif key == curses.KEY_DOWN and selected_option < len(options) - 1:
                selected_option += 1
            elif key == 10:  # Enter key
                if selected_option == 0:
                    create_account(stdscr)
                elif selected_option == 1:
                    login_account(stdscr)
                elif selected_option == 2:
                    change_banner(stdscr)
                elif selected_option == 3:
                    break

    curses.wrapper(main)

if __name__ == "__main__":
    opz_command()