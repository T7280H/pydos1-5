def help_command():
    """
    نمایش لیست دستورات موجود با توضیحات
    """
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
        "zxp": "ZIP a Files", 
        "unzxp": "UNZIP a Files",
        "opz": "Config Setting"
    }

    print("Available commands:")
    for command, description in commands.items():
        print(f"{command}: {description}")

if __name__ == "__main__":
    help_command()