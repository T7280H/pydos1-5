import datetime

def date_command():
    """
    نمایش تاریخ و زمان فعلی
    """
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    date_command()