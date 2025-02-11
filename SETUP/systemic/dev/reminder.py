# reminder.py
import time
import threading

def reminder_command(message, delay):
    def reminder():
        time.sleep(delay)
        print(f"Reminder: {message}")

    threading.Thread(target=reminder).start()

if __name__ == "__main__":
    message = input("Enter the reminder message: ")
    delay = int(input("Enter the delay in seconds: "))
    reminder_command(message, delay)