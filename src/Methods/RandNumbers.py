import random
from Spammer import spammer
import time

def randomnum():
    count = int(input("Enter the number of spam messages you want to send : \n> "))
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in range(count):
        num = random.randint(0,100000000)
        term = str(num)
        spammer(term)