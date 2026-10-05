#Python Alarm Clock
import time
import datetime
import winsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")
    

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format (24-hour): ")
    set_alarm(alarm_time)