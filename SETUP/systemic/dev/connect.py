import subprocess

def connect_command(new_ip, interface="wlan0"):
    """
    تغییر IP بر روی اینترفیس مشخص شده
    """
    try:
        # دستور برای تغییر IP
        command_ip = f"ifconfig {interface} {new_ip} netmask 255.255.255.0"
        subprocess.run(command_ip, shell=True, check=True)

        # تنظیم دروازه (gateway)
        gateway = '.'.join(new_ip.split('.')[:3]) + '.1'
        command_gateway = f"route add default gw {gateway} {interface}"
        subprocess.run(command_gateway, shell=True, check=True)

        print(f"IP address changed to {new_ip} on interface {interface}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to change IP: {e}")

if __name__ == "__main__":
    new_ip = input("Enter the new IP address: ")
    interface = input("Enter the network interface (default is wlan0): ") or "wlan0"
    connect_command(new_ip, interface)