import socket
import platform
import psutil

def dash_command():
    """
    نمایش داشبورد با اطلاعات دستگاه و دستورات موجود
    """
    # اطلاعات دستگاه
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_info = platform.system() + " " + platform.release()
    cpu_info = platform.processor()
    ram_info = str(round(psutil.virtual_memory().total / (1024.0 **3))) + " GB"
    
    # چاپ اطلاعات دستگاه
    print("=== Device Information ===")
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"Operating System: {os_info}")
    print(f"Processor: {cpu_info}")
    print(f"RAM: {ram_info}")
    
    # لیست دستورات با توضیحات
    commands = {
        "dir": "List directories",
        "cd": "Change directory",
        "rd": "Remove file or directory",
        "connect": "Change IP",
        "dash": "Dashboard",
        "locas": "Show current directory path",
        "mkdir": "Create directory",
        "xxcfg": "Manage Python applications with switches",
        "exit": "Exit PyDOS",
        "help": "Display command help",
        "ipconfig": "Show IP address",
        "pyrun": "Run Python applications",
        "bomb": "Run SMS bomber pybomb.py in the apps folder",
        "calc": "Calculator",
        "reminder": "Reminder",
        "edit": "Text editor",
        "date": "Show date",
        "bootinf": "Show boot version",
        "backup": "Backup all files",
        "restore": "Restore all files",
        "ping": "Ping test",
        "echo": "Print a message",
        "cls": "Clear the screen",
        "time": "Show Time", 
        "xcopy": "Copy the files", 
        "zxp": "ZIP a files", 
        "unzxp": "UNZIP a files", 
        "opz": "Config Setting"
    }
    
    print("\n=== Available Commands ===")
    for command, description in commands.items():
        print(f"{command}: {description}")

if __name__ == "__main__":
    dash_command()