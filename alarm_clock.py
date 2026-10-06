#Python Alarm Clock
import time
import datetime
import winsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")
    sound_file = "alarm_sound.wav"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake up! Alarm ringing!")
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
            is_running = False

        time.sleep(1)  # Wait for 1 second before checking the time again   

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format (24-hour): ")
    set_alarm(alarm_time)