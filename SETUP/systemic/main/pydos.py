import sys
import os
import subprocess
import colorama
from colorama import Fore, Style, Back
from cmd import Cmd

# افزودن مسیر پوشه dev
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ایمپورت دستورات از پوشه dev
from dev.exit import exit_command
from dev.dir import dir_command
from dev.ping import ping_command
from dev.calc import calc_command
from dev.date import date_command
from dev.edit import edit_command
from dev.find import find_command
from dev.help import help_command
from dev.mkdir import mkdir_command
from dev.rd import rd_command
from dev.time import time_command
from dev.ver import ver_command
from dev.backup import backup_command
from dev.restore import restore_command
from dev.reminder import reminder_command
from dev.connect import connect_command
from dev.IPconfig import ipconfig_command
from dev.xxcfg import xxcfg_command
from dev.bomb import bomb_command
from dev.pyrun import pyrun_command
from dev.cls import cls_command
from dev.echo import echo_command
from dev.bootinf import bootinf_command
from dev.locas import locas_command
from dev.cd import cd_command
from dev.dash import dash_command
from dev.xcopy import xcopy_command
from dev.zxp import zxp_command
from dev.unzxp import unzxp_command
from dev.opz import opz_command

def load_banner():
    try:
        # خواندن فایل current_banner.txt از پوشه banner
        banner_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banner'))
        current_banner_path = os.path.join(banner_dir, 'current_banner.txt')

        with open(current_banner_path, 'r') as f:
            banner_file = f.read().strip()
        banner_path = os.path.join(banner_dir, banner_file)
        
        # اجرای فایل بنر و نمایش فقط خروجی
        with open(banner_path, 'r') as f:
            banner_code = f.read()
        exec(banner_code, {'__name__': '__main__'})
        
    except FileNotFoundError:
        print("No banner selected. Default banner will be used.")
    except Exception as e:
        print(f"Error loading banner: {e}")

class PyDOSCmd(Cmd):
    prompt = Back.RED + Fore.BLACK + 'PyDOS> ' + Style.RESET_ALL
    intro = Fore.GREEN + "PyDOS 1.5 BETA DEVELOPED BY T7280H TO SEE COMMANDS TYPE (HELP)" + Style.RESET_ALL

    def preloop(self):
        load_banner()

    def do_exit(self, line):
        exit_command()
        return True

    def do_dir(self, line):
        print(Fore.CYAN, end="")
        dir_command()
        print(Style.RESET_ALL, end="")

    def do_ping(self, line):
        print(Fore.YELLOW, end="")
        ping_command(line)
        print(Style.RESET_ALL, end="")

    def do_calc(self, line):
        print(Fore.GREEN, end="")
        calc_command(line)
        print(Style.RESET_ALL, end="")

    def do_date(self, line):
        print(Fore.BLUE, end="")
        date_command()
        print(Style.RESET_ALL, end="")

    def do_edit(self, line):
        print(Fore.MAGENTA, end="")
        edit_command(line)
        print(Style.RESET_ALL, end="")

    def do_find(self, line):
        print(Fore.GREEN, end="")
        find_command(line)
        print(Style.RESET_ALL, end="")

    def do_help(self, line):
        print(Fore.YELLOW, end="")
        help_command()
        print(Style.RESET_ALL, end="")

    def do_mkdir(self, line):
        print(Fore.BLUE, end="")
        mkdir_command(line)
        print(Style.RESET_ALL, end="")

    def do_rd(self, line):
        print(Fore.RED, end="")
        rd_command(line)
        print(Style.RESET_ALL, end="")

    def do_time(self, line):
        print(Fore.GREEN, end="")
        time_command()
        print(Style.RESET_ALL, end="")

    def do_ver(self, line):
        print(Fore.MAGENTA, end="")
        ver_command()
        print(Style.RESET_ALL, end="")

    def do_restore(self, line):
        args = line.split()
        if len(args) < 1:
            print("Usage: restore <restore_path>")
            return
        restore_path = args[0]
        restore_command(restore_path)

    def do_reminder(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: reminder <message> <delay>")
            return
        message = args[0]
        delay = int(args[1])
        reminder_command(message, delay)

    def do_connect(self, line):
        print(Fore.GREEN, end="")
        connect_command(line)
        print(Style.RESET_ALL, end="")

    def do_ipconfig(self, line):
        print(Fore.BLUE, end="")
        ipconfig_command()
        print(Style.RESET_ALL, end="")

    def do_xxcfg(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: xxcfg <switch> <appname>")
            return
        switch = args[0]
        app_name = args[1]
        print(Fore.CYAN, end="")
        xxcfg_command(switch, app_name)
        print(Style.RESET_ALL, end="")

    def do_bomb(self, line):
        print(Fore.RED, end="")
        bomb_command()
        print(Style.RESET_ALL, end="")

    def do_pyrun(self, line):
        print(Fore.GREEN, end="")
        pyrun_command(line)
        print(Style.RESET_ALL, end="")

    def do_cls(self, line):
        cls_command()

    def do_echo(self, line):
        echo_command(line)

    def do_bootinf(self, line):
        bootinf_command()
    
    def do_cd(self, line):
        cd_command(line)
    	
    def do_locas(self, line):
        locas_command(line)
    
    def do_dash(self, line):
        dash_command()
    
    def do_backup(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: backup <source> <destination>")
            return
        source = args[0]
        destination = args[1]
        backup_command(source, destination)
    
    def do_xcopy(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: xcopy <source> <destination>")
            return
        source = args[0]
        destination = args[1]
        xcopy_command(source, destination)
    	
    def do_zxp(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: zxp <source> <destination>")
            return
        source = args[0]
        destination = args[1]
        zxp_command(source, destination)
    	
    def do_unzxp(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: unzxp <zip_file> <destination>")
            return
        zip_file = args[0]
        destination = args[1]
        unzxp_command(zip_file, destination)
    	
    def do_opz(self, line):
        opz_command()

if __name__ == '__main__':
    colorama.init()
    PyDOSCmd().cmdloop()
    colorama.deinit()
