import socket

def ipconfig_command():
    """
    نمایش نام میزبان و آدرس IP
    """
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f'Hostname: {hostname}')
    print(f'IP Address: {ip_address}')

if __name__ == "__main__":
    ipconfig_command()