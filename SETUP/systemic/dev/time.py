import datetime

def time_command():
    """
    نمایش تاریخ و زمان فعلی
    """
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    time_command()