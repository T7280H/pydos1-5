import sys
import time

def loading_animation(message):
    """
    نمایش لودینگ چرخشی با پیام مورد نظر
    """
    for _ in range(10):
        for char in "|/-\\":
            sys.stdout.write(f'\r{message} {char}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\rDone!       \n')

def exit_command():
    """
    خروج از PyDOS با تاییدیه کاربر و لودینگ چرخشی
    """
    user_input = input("Are you sure you want to exit PyDOS? (Y to confirm, N to cancel): ").strip().upper()
    if user_input == 'Y':
        loading_animation("Exiting PyDOS")
        print("Goodbye!")
        sys.exit(0)
    elif user_input == 'N':
        print("Exit cancelled.")
    else:
        print("Invalid input. Exit cancelled.")

if __name__ == "__main__":
    exit_command()