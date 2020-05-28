import random
from Spammer import spammer
import time

def randomnum():
    count = int(input("Enter the number of spam messages you want to send : "))
    print("Open Your Social Media Platform and select your text box")
    time.sleep(5)
    for x in range(count):
        num = random.randint(0,100000000)
        term = str(num)
        spammer(term)