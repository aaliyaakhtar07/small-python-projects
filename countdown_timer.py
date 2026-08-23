#Countdown timer
import time

def countdown(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Example usage
seconds = int(input("Enter the countdown time in seconds: "))
if seconds > 0:
    countdown(seconds)