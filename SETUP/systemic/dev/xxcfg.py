import os
import shutil

def xxcfg_command(switch, app_name):
    """
    دستور xxcfg برای مدیریت برنامه‌های پایتونی
    """
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'installation')
    info_path = os.path.join(app_dir, 'info.txt')
    install_path = os.path.join(app_dir, app_name)
    apps_dir = os.path.join(current_dir, 'systemic', 'apps', app_name)

    # بررسی کنید که پوشه apps وجود دارد
    if not os.path.exists(apps_dir):
        print(f"Directory {apps_dir} does not exist.")
        return
    
    if switch == '-v':
        # نصب برنامه در فولدر apps
        if os.path.exists(install_path):
            if os.path.exists(info_path):
                with open(info_path, 'r') as info_file:
                    print(f"App Information for {app_name}:\n")
                    print(info_file.read())
                
                user_input = input("Do you want to install this app? (N to install, E to exit): ").strip().upper()
                if user_input == 'N':
                    shutil.copy(install_path, apps_dir)
                    print(f"App {app_name} installed in apps directory.")
                elif user_input == 'E':
                    print("Installation cancelled.")
                else:
                    print("Invalid input. Installation cancelled.")
            else:
                print(f"Info file for {app_name} not found.")
        else:
            print(f"Install file for {app_name} not found.")
    
    elif switch == '-t':
        # نمایش اطلاعات برنامه
        if os.path.exists(info_path):
            with open(info_path, 'r') as info_file:
                print(f"App Information for {app_name}:\n")
                print(info_file.read())
        else:
            print(f"Info file for {app_name} not found.")
    
    elif switch == '-d':
        # حذف برنامه از فولدر apps
        if os.path.exists(apps_dir):
            try:
                shutil.rmtree(apps_dir)
                print(f'App {app_name} removed from apps directory.')
            except Exception as e:
                print(f"Failed to remove {app_name}: {e}")
        else:
            print(f'App {app_name} not found in apps directory.')
    
    else:
        print(f'Invalid switch: {switch}')

if __name__ == "__main__":
    switch = input("Enter the switch (-v, -t, -d): ")
    app_name = input("Enter the app name: ")
    xxcfg_command(switch, app_name)