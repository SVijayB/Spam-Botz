from pynput.keyboard import *
import time

keyboard = Controller()
def spammer(message,sleep):
    time.sleep(sleep)
    for unit in message:
        keyboard.press(unit)
        keyboard.release(unit)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)