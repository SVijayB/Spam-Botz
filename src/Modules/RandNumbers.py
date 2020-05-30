import random
from Modules.Spammer import *
import time
import sys

def randomnum():
    try:
        count = int(input("Enter the number of spam messages you want to send : \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message : \n> "))
    except:
        print("ERROR : Enter Only Numbers")
        input("Press any key to exit ")
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in range(count):
        num = random.randint(0,100000000)
        term = str(num)
        spammer(term,sleep)