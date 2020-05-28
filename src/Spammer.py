from pynput.keyboard import *
import time

keyboard = Controller()
message = input("Enter your message : ")
count = int(input("Enter the number of times you want to spam the message : "))
print("Open Your Social Media Platform and select your text box")
time.sleep(5)
for i in range(count):
    for unit in message:
        keyboard.press(unit)
        keyboard.release(unit)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)