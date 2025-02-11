import os

def ping_command(host):
    """
    تست پینگ برای بررسی دسترسی به host
    """
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print(f'{host} is up')
    else:
        print(f'{host} is down')

if __name__ == "__main__":
    host = input("Enter the host to ping: ")
    ping_command(host)